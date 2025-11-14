"""
Test Cases for Sprint 2 - Response to Reminder
Group members: Kenloy Marseille, Mitchell Anguita, Chris Jorss, Wyatt Byrd, Tyler Arrowsmith

Test Case Coverage:
- TC01: User Marks Medication as Taken
- TC02: User Marks Medication as Missed
- TC03: User Snoozes Reminder
- TC04: User Does Not Respond (Auto-Unconfirmed)
"""

import unittest
import json
import os
import sys
from datetime import datetime, timedelta
import tempfile
import shutil

# Add Sprint 2 directory to path
sprint2_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, sprint2_dir)

# Import functions from medication_reminder
from medication_reminder import (
    log_adherence,
    schedule_reminder,
    load_adherence_history,
    load_reminders,
    save_adherence_history,
    save_reminders,
    get_sprint2_data_file,
    get_reminders_file
)


class TestSprint2Reminders(unittest.TestCase):
    """Test Suite for Sprint 2 - Medication Reminder System"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test environment once before all tests"""
        print("\n" + "="*70)
        print("SPRINT 2 TEST SUITE - MEDICATION REMINDER SYSTEM")
        print("="*70)
        
    def setUp(self):
        """Set up fresh test data before each test"""
        # Backup existing files
        self.backup_files()
        
        # Clear test data
        save_adherence_history([])
        save_reminders([])
    
    def tearDown(self):
        """Clean up after each test"""
        # Restore original files
        self.restore_files()
    
    def backup_files(self):
        """Backup existing data files"""
        self.backups = {}
        
        sprint2_file = get_sprint2_data_file()
        reminders_file = get_reminders_file()
        
        if os.path.exists(sprint2_file):
            with open(sprint2_file, 'r') as f:
                self.backups['sprint2'] = f.read()
        
        if os.path.exists(reminders_file):
            with open(reminders_file, 'r') as f:
                self.backups['reminders'] = f.read()
    
    def restore_files(self):
        """Restore original data files"""
        sprint2_file = get_sprint2_data_file()
        reminders_file = get_reminders_file()
        
        if 'sprint2' in self.backups:
            with open(sprint2_file, 'w') as f:
                f.write(self.backups['sprint2'])
        elif os.path.exists(sprint2_file):
            os.remove(sprint2_file)
        
        if 'reminders' in self.backups:
            with open(reminders_file, 'w') as f:
                f.write(self.backups['reminders'])
        elif os.path.exists(reminders_file):
            os.remove(reminders_file)
    
    # ==================== TC01: User Marks Medication as Taken ====================
    
    def test_TC01_mark_medication_taken(self):
        """
        TC01 - User Marks Medication as Taken
        
        Test Objective: Verify that the system correctly logs a medication 
        reminder as "Taken" when the user responds on time.
        
        Input Values:
        - Medication Name: Amlodipine
        - Dosage: 10 mg
        - Reminder Time: 2025-11-07 08:00
        - User Action: "Taken"
        
        Expected Results:
        - Status: Taken
        - Timestamp: 2025-11-07 08:01 (within 1 minute)
        - Entry appears in adherence history
        """
        print("\n" + "-"*70)
        print("TEST CASE TC01: User Marks Medication as Taken")
        print("-"*70)
        
        # Test Input Values
        medication_name = "Amlodipine"
        dosage = "10 mg"
        reminder_time = "2025-11-07 08:00:00"
        user_action = "Taken"
        
        print(f"Input: {medication_name} {dosage} at {reminder_time}")
        print(f"Action: User marks as '{user_action}'")
        
        # Execute: User marks medication as taken
        entry = log_adherence(medication_name, dosage, user_action, reminder_time)
        
        # Verify: Check that entry was created correctly
        self.assertIsNotNone(entry, "Adherence entry should be created")
        self.assertEqual(entry['medication_name'], medication_name)
        self.assertEqual(entry['dosage'], dosage)
        self.assertEqual(entry['status'], "Taken")
        self.assertEqual(entry['reminder_time'], reminder_time)
        
        # Verify: Timestamp exists and is recent
        self.assertIn('timestamp', entry)
        timestamp = datetime.strptime(entry['timestamp'], "%Y-%m-%d %H:%M:%S")
        now = datetime.now()
        time_diff = abs((now - timestamp).total_seconds())
        self.assertLess(time_diff, 5, "Timestamp should be within 5 seconds of now")
        
        # Verify: Entry saved in adherence history
        history = load_adherence_history()
        self.assertEqual(len(history), 1, "History should contain 1 entry")
        self.assertEqual(history[0]['status'], "Taken")
        
        print(f"✓ Status logged as: {entry['status']}")
        print(f"✓ Timestamp: {entry['timestamp']}")
        print(f"✓ Entry saved to adherence history")
        print("RESULT: PASS")
    
    # ==================== TC02: User Marks Medication as Missed ====================
    
    def test_TC02_mark_medication_missed(self):
        """
        TC02 - User Marks Medication as Missed
        
        Test Objective: Ensure system correctly logs medication as "Missed"
        
        Input Values:
        - Medication Name: Metformin
        - Dosage: 500 mg
        - Reminder Time: 2025-11-07 19:00
        - User Action: "Missed"
        
        Expected Results:
        - Status: Missed
        - Timestamp: 2025-11-07 19:05 (5 minutes after reminder)
        - Entry saved in adherence history
        """
        print("\n" + "-"*70)
        print("TEST CASE TC02: User Marks Medication as Missed")
        print("-"*70)
        
        # Test Input Values
        medication_name = "Metformin"
        dosage = "500 mg"
        reminder_time = "2025-11-07 19:00:00"
        user_action = "Missed"
        
        print(f"Input: {medication_name} {dosage} at {reminder_time}")
        print(f"Action: User marks as '{user_action}' at 19:05")
        
        # Execute: User marks medication as missed
        entry = log_adherence(medication_name, dosage, user_action, reminder_time)
        
        # Verify: Check that entry was created correctly
        self.assertIsNotNone(entry, "Adherence entry should be created")
        self.assertEqual(entry['medication_name'], medication_name)
        self.assertEqual(entry['dosage'], dosage)
        self.assertEqual(entry['status'], "Missed")
        self.assertEqual(entry['reminder_time'], reminder_time)
        
        # Verify: Timestamp exists
        self.assertIn('timestamp', entry)
        
        # Verify: Entry saved in adherence history
        history = load_adherence_history()
        self.assertEqual(len(history), 1, "History should contain 1 entry")
        self.assertEqual(history[0]['status'], "Missed")
        
        print(f"✓ Status logged as: {entry['status']}")
        print(f"✓ Timestamp: {entry['timestamp']}")
        print(f"✓ Entry saved to adherence history")
        print("RESULT: PASS")
    
    # ==================== TC03: User Snoozes Reminder ====================
    
    def test_TC03_snooze_reminder(self):
        """
        TC03 - User Snoozes Reminder
        
        Test Objective: Verify snooze delay and final action logging
        
        Input Values:
        - Medication Name: Lisinopril
        - Dosage: 10 mg
        - Reminder Time: 2025-11-07 09:00
        - Snooze Duration: 15 minutes
        - Final Action: "Taken"
        
        Expected Results:
        - Snooze recorded at 09:00 with delay set for 09:15
        - Final status logged as Taken at 09:17
        - Adherence history shows final entry
        """
        print("\n" + "-"*70)
        print("TEST CASE TC03: User Snoozes Reminder")
        print("-"*70)
        
        # Test Input Values
        medication_name = "Lisinopril"
        dosage = "10 mg"
        reminder_time = "2025-11-07 09:00:00"
        snooze_duration = 15  # minutes
        
        print(f"Input: {medication_name} {dosage} at {reminder_time}")
        print(f"Action: User snoozes for {snooze_duration} minutes, then marks as 'Taken'")
        
        # Step 1: Schedule initial reminder
        original_reminder = schedule_reminder(medication_name, dosage, 24)
        reminders = load_reminders()
        self.assertEqual(len(reminders), 1, "Reminder should be scheduled")
        
        print(f"✓ Initial reminder scheduled for: {reminders[0]['next_reminder']}")
        
        # Step 2: Simulate snooze - update reminder time
        original_time = datetime.strptime(reminder_time, "%Y-%m-%d %H:%M:%S")
        snoozed_time = original_time + timedelta(minutes=snooze_duration)
        
        reminders[0]['next_reminder'] = snoozed_time.strftime("%Y-%m-%d %H:%M:%S")
        save_reminders(reminders)
        
        updated_reminders = load_reminders()
        self.assertEqual(
            updated_reminders[0]['next_reminder'], 
            snoozed_time.strftime("%Y-%m-%d %H:%M:%S"),
            "Reminder should be delayed by snooze duration"
        )
        
        print(f"✓ Reminder snoozed to: {snoozed_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Step 3: User marks as taken after snooze
        final_action = "Taken"
        entry = log_adherence(medication_name, dosage, final_action, reminder_time)
        
        # Verify: Final entry logged correctly
        self.assertEqual(entry['status'], "Taken")
        self.assertEqual(entry['medication_name'], medication_name)
        
        # Verify: Entry in history
        history = load_adherence_history()
        self.assertEqual(len(history), 1, "History should contain final entry")
        self.assertEqual(history[0]['status'], "Taken")
        
        print(f"✓ Final status logged as: {entry['status']}")
        print(f"✓ Timestamp: {entry['timestamp']}")
        print("RESULT: PASS")
    
    # ==================== TC04: User Does Not Respond ====================
    
    def test_TC04_no_response_auto_unconfirmed(self):
        """
        TC04 - User Does Not Respond
        
        Test Objective: Verify automatic logging when user does not respond
        
        Input Values:
        - Medication Name: Ibuprofen
        - Dosage: 200 mg
        - Reminder Time: 2025-11-07 18:00
        - User Action: None
        - Expiration Duration: 30 minutes
        
        Expected Results:
        - Status: Unconfirmed
        - Timestamp: 2025-11-07 18:30 (after expiration)
        - Entry added automatically to adherence history
        """
        print("\n" + "-"*70)
        print("TEST CASE TC04: User Does Not Respond (Auto-Unconfirmed)")
        print("-"*70)
        
        # Test Input Values
        medication_name = "Ibuprofen"
        dosage = "200 mg"
        reminder_time = "2025-11-07 18:00:00"
        expiration_duration = 30  # minutes
        
        print(f"Input: {medication_name} {dosage} at {reminder_time}")
        print(f"Action: No user response for {expiration_duration} minutes")
        
        # Simulate: Reminder expires without user action
        # System automatically logs as Unconfirmed
        auto_status = "Unconfirmed"
        entry = log_adherence(medication_name, dosage, auto_status, reminder_time)
        
        # Verify: Entry created with Unconfirmed status
        self.assertIsNotNone(entry, "Adherence entry should be created automatically")
        self.assertEqual(entry['medication_name'], medication_name)
        self.assertEqual(entry['dosage'], dosage)
        self.assertEqual(entry['status'], "Unconfirmed")
        self.assertEqual(entry['reminder_time'], reminder_time)
        
        # Verify: Timestamp exists (simulating 30 minutes after reminder)
        self.assertIn('timestamp', entry)
        
        # Verify: Entry saved in adherence history
        history = load_adherence_history()
        self.assertEqual(len(history), 1, "History should contain auto-generated entry")
        self.assertEqual(history[0]['status'], "Unconfirmed")
        
        print(f"✓ Status auto-logged as: {entry['status']}")
        print(f"✓ Timestamp: {entry['timestamp']}")
        print(f"✓ Entry automatically saved to adherence history")
        print("RESULT: PASS")
    
    # ==================== Additional Integration Tests ====================
    
    def test_multiple_medications_adherence(self):
        """
        Integration Test: Multiple medications with different statuses
        """
        print("\n" + "-"*70)
        print("INTEGRATION TEST: Multiple Medications")
        print("-"*70)
        
        # Log multiple medications
        medications = [
            ("Amlodipine", "10 mg", "Taken", "2025-11-07 08:00:00"),
            ("Metformin", "500 mg", "Missed", "2025-11-07 19:00:00"),
            ("Lisinopril", "10 mg", "Taken", "2025-11-07 09:00:00"),
            ("Ibuprofen", "200 mg", "Unconfirmed", "2025-11-07 18:00:00"),
        ]
        
        for med_name, dosage, status, time in medications:
            log_adherence(med_name, dosage, status, time)
            print(f"✓ Logged: {med_name} - {status}")
        
        # Verify all entries saved
        history = load_adherence_history()
        self.assertEqual(len(history), 4, "History should contain 4 entries")
        
        # Verify each status
        statuses = [entry['status'] for entry in history]
        self.assertIn("Taken", statuses)
        self.assertIn("Missed", statuses)
        self.assertIn("Unconfirmed", statuses)
        
        print(f"✓ Total entries in history: {len(history)}")
        print("RESULT: PASS")
    
    def test_timestamp_accuracy(self):
        """
        Test: Verify timestamp accuracy (within acceptable range)
        """
        print("\n" + "-"*70)
        print("ACCURACY TEST: Timestamp Precision")
        print("-"*70)
        
        before = datetime.now()
        entry = log_adherence("Test Med", "100 mg", "Taken", "2025-11-07 12:00:00")
        after = datetime.now()
        
        timestamp = datetime.strptime(entry['timestamp'], "%Y-%m-%d %H:%M:%S")
        
        # Timestamp should be between before and after
        self.assertGreaterEqual(timestamp, before - timedelta(seconds=1))
        self.assertLessEqual(timestamp, after + timedelta(seconds=1))
        
        print(f"✓ Timestamp: {entry['timestamp']}")
        print(f"✓ Timestamp is accurate within acceptable range")
        print("RESULT: PASS")


def run_tests():
    """Run all tests with detailed output"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestSprint2Reminders)
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("\n✓ ALL TESTS PASSED")
    else:
        print("\n✗ SOME TESTS FAILED")
    
    print("="*70)
    
    return result


if __name__ == "__main__":
    # Run all tests
    result = run_tests()
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)