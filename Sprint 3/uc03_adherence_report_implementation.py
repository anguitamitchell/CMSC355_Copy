"""
Use Case 3: Generation of Adherence Report - Implementation
Sprint 3 - Medication Reminder System

This module contains the production code for adherence report generation.
"""

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Optional, Any


class ResponseStatus(Enum):
    """Enum for medication response statuses"""
    TAKEN = "Taken"
    MISSED = "Missed"
    LATE_TAKEN = "Late Taken"
    LATE_MISSED = "Late Missed"
    UNCONFIRMED = "Unconfirmed"


class AdherenceEntry:
    """Represents a single adherence record entry"""
    
    def __init__(self, medication_name: str, status: ResponseStatus, 
                 timestamp: datetime, scheduled_time: Optional[datetime] = None):
        """
        Initialize an adherence entry.
        
        Args:
            medication_name: Name of the medication
            status: ResponseStatus enum value
            timestamp: When the response was recorded
            scheduled_time: When the dose was scheduled (defaults to timestamp)
        """
        self.medication_name = medication_name
        self.status = status
        self.timestamp = timestamp
        self.scheduled_time = scheduled_time or timestamp
        self.delay_minutes = self._calculate_delay()
    
    def _calculate_delay(self) -> float:
        """Calculate delay in minutes from scheduled time"""
        if self.scheduled_time:
            delta = self.timestamp - self.scheduled_time
            return delta.total_seconds() / 60
        return 0.0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert entry to dictionary for serialization"""
        return {
            'medication_name': self.medication_name,
            'status': self.status.value,
            'timestamp': self.timestamp.isoformat(),
            'scheduled_time': self.scheduled_time.isoformat(),
            'delay_minutes': round(self.delay_minutes, 2)
        }
    
    def __repr__(self):
        return (f"AdherenceEntry(medication={self.medication_name}, "
                f"status={self.status.value}, timestamp={self.timestamp})")


class DatabaseConnection:
    """Mock database connection for adherence records"""
    
    def __init__(self):
        """Initialize database connection"""
        self.connected = True
        self.storage = []
        self.fail_next_operation = False
    
    def save_record(self, entry: Dict) -> bool:
        """
        Save a record to the database.
        
        Args:
            entry: Dictionary containing adherence entry data
            
        Returns:
            bool: True if save successful, False otherwise
        """
        if self.fail_next_operation:
            self.fail_next_operation = False
            return False
        
        if not self.connected:
            return False
        
        self.storage.append(entry)
        return True
    
    def get_all_records(self) -> List[Dict]:
        """
        Retrieve all records from database.
        
        Returns:
            list: All stored adherence records
        """
        return self.storage.copy()
    
    def simulate_error(self):
        """Simulate a database error on next operation"""
        self.fail_next_operation = True
    
    def disconnect(self):
        """Simulate database disconnection"""
        self.connected = False
    
    def reconnect(self):
        """Reconnect to database"""
        self.connected = True


class AdherenceReport:
    """
    Manages medication adherence tracking and reporting.
    
    This class handles:
    - Recording medication responses (taken/missed)
    - Tracking late responses
    - Logging unconfirmed doses
    - Calculating adherence statistics
    - Generating adherence reports
    """
    
    def __init__(self, database: Optional[DatabaseConnection] = None):
        """
        Initialize adherence report system.
        
        Args:
            database: Database connection (creates new if None)
        """
        self.database = database or DatabaseConnection()
        self.entries: List[AdherenceEntry] = []
        self._load_from_database()
    
    def _load_from_database(self):
        """Load existing records from database"""
        records = self.database.get_all_records()
        for record in records:
            entry = AdherenceEntry(
                medication_name=record['medication_name'],
                status=ResponseStatus(record['status']),
                timestamp=datetime.fromisoformat(record['timestamp']),
                scheduled_time=datetime.fromisoformat(record['scheduled_time'])
            )
            self.entries.append(entry)
    
    def log_response(self, medication_name: str, status: ResponseStatus,
                    timestamp: Optional[datetime] = None,
                    scheduled_time: Optional[datetime] = None) -> Dict[str, Any]:
        """
        Log a medication response and update the adherence report.
        
        Args:
            medication_name: Name of the medication
            status: Response status (Taken, Missed, etc.)
            timestamp: When the response occurred (defaults to now)
            scheduled_time: When the dose was scheduled
        
        Returns:
            dict: Confirmation with entry details and updated adherence
        
        Raises:
            Exception: If database operation fails
        """
        if timestamp is None:
            timestamp = datetime.now()
        
        if scheduled_time is None:
            scheduled_time = timestamp
        
        # Create adherence entry
        entry = AdherenceEntry(medication_name, status, timestamp, scheduled_time)
        
        # Attempt to save to database
        if not self.database.save_record(entry.to_dict()):
            raise Exception("Unable to record response. Please try again.")
        
        # Add to in-memory records
        self.entries.append(entry)
        
        # Calculate updated statistics
        stats = self.get_statistics()
        
        return {
            'success': True,
            'message': 'Response recorded successfully.',
            'entry': entry.to_dict(),
            'adherence_percentage': stats['adherence_percentage'],
            'total_doses': stats['total_doses'],
            'taken_doses': stats['taken_doses']
        }
    
    def log_no_response(self, medication_name: str, 
                       scheduled_time: Optional[datetime] = None) -> Dict[str, Any]:
        """
        Log when user doesn't respond to a reminder.
        
        Args:
            medication_name: Name of the medication
            scheduled_time: When the dose was scheduled
        
        Returns:
            dict: Confirmation with entry details
        """
        timestamp = datetime.now()
        
        if scheduled_time is None:
            scheduled_time = timestamp
        
        return self.log_response(
            medication_name=medication_name,
            status=ResponseStatus.UNCONFIRMED,
            timestamp=timestamp,
            scheduled_time=scheduled_time
        )
    
    def log_late_response(self, medication_name: str, scheduled_time: datetime,
                         response_time: datetime, was_taken: bool = True) -> Dict[str, Any]:
        """
        Log a late response to a medication reminder.
        
        Args:
            medication_name: Name of the medication
            scheduled_time: When the dose was originally scheduled
            response_time: When the user actually responded
            was_taken: Whether the medication was taken
        
        Returns:
            dict: Confirmation with entry details
        """
        delay_minutes = (response_time - scheduled_time).total_seconds() / 60
        
        if delay_minutes > 30:  # Beyond 30-minute grace period
            status = ResponseStatus.LATE_TAKEN if was_taken else ResponseStatus.LATE_MISSED
        else:
            status = ResponseStatus.TAKEN if was_taken else ResponseStatus.MISSED
        
        return self.log_response(
            medication_name=medication_name,
            status=status,
            timestamp=response_time,
            scheduled_time=scheduled_time
        )
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Calculate adherence statistics.
        
        Returns:
            dict: Statistics including adherence percentage, dose counts
        """
        total_doses = len(self.entries)
        
        if total_doses == 0:
            return {
                'total_doses': 0,
                'taken_doses': 0,
                'missed_doses': 0,
                'unconfirmed_doses': 0,
                'late_doses': 0,
                'adherence_percentage': 0.0
            }
        
        taken_doses = sum(1 for e in self.entries 
                         if e.status in [ResponseStatus.TAKEN, ResponseStatus.LATE_TAKEN])
        missed_doses = sum(1 for e in self.entries 
                          if e.status in [ResponseStatus.MISSED, ResponseStatus.LATE_MISSED])
        unconfirmed_doses = sum(1 for e in self.entries 
                               if e.status == ResponseStatus.UNCONFIRMED)
        late_doses = sum(1 for e in self.entries 
                        if e.status in [ResponseStatus.LATE_TAKEN, ResponseStatus.LATE_MISSED])
        
        adherence_percentage = round((taken_doses / total_doses) * 100, 2)
        
        return {
            'total_doses': total_doses,
            'taken_doses': taken_doses,
            'missed_doses': missed_doses,
            'unconfirmed_doses': unconfirmed_doses,
            'late_doses': late_doses,
            'adherence_percentage': adherence_percentage
        }
    
    def get_report(self, start_date: Optional[datetime] = None,
                   end_date: Optional[datetime] = None) -> Dict[str, Any]:
        """
        Generate a comprehensive adherence report.
        
        Args:
            start_date: Filter records from this date (inclusive)
            end_date: Filter records to this date (inclusive)
        
        Returns:
            dict: Complete adherence report with entries and statistics
        """
        # Filter entries by date range if specified
        filtered_entries = self.entries
        
        if start_date:
            filtered_entries = [e for e in filtered_entries 
                              if e.timestamp >= start_date]
        
        if end_date:
            filtered_entries = [e for e in filtered_entries 
                              if e.timestamp <= end_date]
        
        # Calculate statistics for filtered entries
        temp_report = AdherenceReport(self.database)
        temp_report.entries = filtered_entries
        stats = temp_report.get_statistics()
        
        return {
            'report_generated': datetime.now().isoformat(),
            'date_range': {
                'start': start_date.isoformat() if start_date else None,
                'end': end_date.isoformat() if end_date else None
            },
            'statistics': stats,
            'entries': [e.to_dict() for e in filtered_entries]
        }
    
    def get_medication_report(self, medication_name: str) -> Dict[str, Any]:
        """
        Generate adherence report for a specific medication.
        
        Args:
            medication_name: Name of the medication
        
        Returns:
            dict: Adherence report for specific medication
        """
        med_entries = [e for e in self.entries 
                      if e.medication_name == medication_name]
        
        temp_report = AdherenceReport(self.database)
        temp_report.entries = med_entries
        stats = temp_report.get_statistics()
        
        return {
            'medication_name': medication_name,
            'statistics': stats,
            'entries': [e.to_dict() for e in med_entries]
        }


class ReminderSystem:
    """
    Medication reminder system that integrates with adherence tracking.
    
    Handles:
    - Processing user responses to reminders
    - Managing reminder expiration
    - Tracking late responses
    """
    
    def __init__(self, adherence_report: AdherenceReport):
        """
        Initialize reminder system.
        
        Args:
            adherence_report: AdherenceReport instance to log responses
        """
        self.adherence_report = adherence_report
        self.reminder_window_minutes = 30
        self.active_reminders: Dict[str, datetime] = {}
    
    def send_reminder(self, medication_name: str, scheduled_time: datetime):
        """
        Send a medication reminder.
        
        Args:
            medication_name: Name of the medication
            scheduled_time: When the dose should be taken
        """
        self.active_reminders[medication_name] = scheduled_time
        print(f"Reminder sent: {medication_name} at {scheduled_time.strftime('%H:%M')}")
    
    def process_response(self, medication_name: str, taken: bool,
                        response_time: Optional[datetime] = None) -> Dict[str, Any]:
        """
        Process user response to a reminder.
        
        Args:
            medication_name: Name of the medication
            taken: Whether the medication was taken
            response_time: When the user responded (defaults to now)
        
        Returns:
            dict: Result of logging the response
        """
        if response_time is None:
            response_time = datetime.now()
        
        scheduled_time = self.active_reminders.get(medication_name, response_time)
        
        # Check if response is late
        delay = (response_time - scheduled_time).total_seconds() / 60
        
        if delay > self.reminder_window_minutes:
            result = self.adherence_report.log_late_response(
                medication_name, scheduled_time, response_time, taken
            )
        else:
            status = ResponseStatus.TAKEN if taken else ResponseStatus.MISSED
            result = self.adherence_report.log_response(
                medication_name, status, response_time, scheduled_time
            )
        
        # Remove from active reminders
        if medication_name in self.active_reminders:
            del self.active_reminders[medication_name]
        
        return result
    
    def check_expired_reminders(self):
        """
        Check for expired reminders and log them as unconfirmed.
        
        Returns:
            list: Results of logging expired reminders
        """
        current_time = datetime.now()
        expired = []
        
        for med_name, scheduled_time in list(self.active_reminders.items()):
            expiration_time = scheduled_time + timedelta(minutes=self.reminder_window_minutes)
            
            if current_time > expiration_time:
                result = self.adherence_report.log_no_response(med_name, scheduled_time)
                expired.append(result)
                del self.active_reminders[med_name]
        
        return expired


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

def demonstrate_use_case_3():
    """Demonstrate Use Case 3 functionality"""
    
    print("="*70)
    print("USE CASE 3: GENERATION OF ADHERENCE REPORT - DEMONSTRATION")
    print("="*70)
    print()
    
    # Initialize system
    database = DatabaseConnection()
    adherence_report = AdherenceReport(database)
    reminder_system = ReminderSystem(adherence_report)
    
    # Scenario 1: Successful response
    print("Scenario 1: User responds 'Taken' to reminder")
    print("-" * 70)
    result = reminder_system.process_response("Amoxicillin", taken=True)
    print(f"Status: {result['message']}")
    print(f"Adherence: {result['adherence_percentage']}%")
    print()
    
    # Scenario 2: Missed dose
    print("Scenario 2: User responds 'Missed' to reminder")
    print("-" * 70)
    result = reminder_system.process_response("Ibuprofen", taken=False)
    print(f"Status: {result['message']}")
    print(f"Adherence: {result['adherence_percentage']}%")
    print()
    
    # Scenario 3: Late response
    print("Scenario 3: User responds late (2 hours)")
    print("-" * 70)
    scheduled = datetime.now() - timedelta(hours=2)
    reminder_system.send_reminder("Metformin", scheduled)
    result = reminder_system.process_response("Metformin", taken=True)
    print(f"Status: {result['entry']['status']}")
    print(f"Delay: {result['entry']['delay_minutes']} minutes")
    print(f"Adherence: {result['adherence_percentage']}%")
    print()
    
    # Scenario 4: No response (expired)
    print("Scenario 4: Reminder expires without response")
    print("-" * 70)
    old_scheduled = datetime.now() - timedelta(hours=1)
    reminder_system.send_reminder("Lisinopril", old_scheduled)
    expired = reminder_system.check_expired_reminders()
    print(f"Expired reminders: {len(expired)}")
    print(f"Status: {expired[0]['entry']['status']}")
    stats = adherence_report.get_statistics()
    print(f"Adherence: {stats['adherence_percentage']}%")
    print()
    
    # Generate comprehensive report
    print("Comprehensive Adherence Report")
    print("-" * 70)
    report = adherence_report.get_report()
    print(f"Total Doses: {report['statistics']['total_doses']}")
    print(f"Taken: {report['statistics']['taken_doses']}")
    print(f"Missed: {report['statistics']['missed_doses']}")
    print(f"Unconfirmed: {report['statistics']['unconfirmed_doses']}")
    print(f"Late: {report['statistics']['late_doses']}")
    print(f"Overall Adherence: {report['statistics']['adherence_percentage']}%")
    print()
    
    print("Detailed Entries:")
    for entry in report['entries']:
        print(f"  - {entry['medication_name']}: {entry['status']} "
              f"at {entry['timestamp'][:19]}")
    
    print()
    print("="*70)


if __name__ == '__main__':
    demonstrate_use_case_3()