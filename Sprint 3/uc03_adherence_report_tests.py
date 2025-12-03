"""
Use Case 3: Generation of Adherence Report - Test Suite
Sprint 3 - Medication Reminder System

This module contains all test cases for UC03.
"""

import unittest
from datetime import datetime, timedelta
import sys
import os

# Import the implementation module
from uc03_adherence_report_implementation import (
    AdherenceReport,
    ReminderSystem,
    DatabaseConnection,
    ResponseStatus
)


class TestTC01_SuccessfulLoggingAndReportUpdate(unittest.TestCase):
    """
    TC01 - Successful logging and report update
    
    Test Objective:
    Verify that the system correctly records a valid user response 
    and updates the adherence report.
    """
    
    def setUp(self):
        """Set up test fixtures"""
        self.database = DatabaseConnection()
        self.adherence_report = AdherenceReport(self.database)
        self.reminder_system = ReminderSystem(self.adherence_report)
        
    def test_taken_response_recorded(self):
        """
        Test that 'Taken' response is correctly recorded
        
        Expected: Entry is created with correct medication name,
        status, and timestamp
        """
        # Arrange
        medication_name = "Amoxicillin"
        
        # Act
        result = self.reminder_system.process_response(medication_name, taken=True)
        
        # Assert
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], 'Response recorded successfully.')
        self.assertEqual(result['entry']['medication_name'], medication_name)
        self.assertEqual(result['entry']['status'], 'Taken')
        self.assertIsNotNone(result['entry']['timestamp'])
        
    def test_adherence_report_updated(self):
        """
        Test that adherence report is updated correctly
        
        Expected: Report shows 1 total dose, 1 taken dose, 100% adherence
        """
        # Arrange
        medication_name = "Amoxicillin"
        
        # Act
        result = self.reminder_system.process_response(medication_name, taken=True)
        stats = self.adherence_report.get_statistics()
        
        # Assert
        self.assertEqual(stats['total_doses'], 1)
        self.assertEqual(stats['taken_doses'], 1)
        self.assertEqual(stats['adherence_percentage'], 100.0)
        
    def test_timestamp_accuracy(self):
        """
        Test that timestamp is accurately recorded
        
        Expected: Timestamp is within the time window of test execution
        """
        # Arrange
        medication_name = "Amoxicillin"
        before_time = datetime.now()
        
        # Act
        result = self.reminder_system.process_response(medication_name, taken=True)
        after_time = datetime.now()
        
        # Assert
        timestamp = datetime.fromisoformat(result['entry']['timestamp'])
        self.assertGreaterEqual(timestamp, before_time)
        self.assertLessEqual(timestamp, after_time)
        
    def test_multiple_responses_adherence_calculation(self):
        """
        Test adherence percentage with multiple responses
        
        Expected: With 2 taken and 1 missed, adherence should be 66.67%
        """
        # Arrange & Act
        self.reminder_system.process_response("Amoxicillin", taken=True)
        self.reminder_system.process_response("Ibuprofen", taken=True)
        result = self.reminder_system.process_response("Metformin", taken=False)
        
        # Assert
        self.assertEqual(result['adherence_percentage'], 66.67)
        
    def test_confirmation_message_displayed(self):
        """
        Test that confirmation message is displayed
        
        Expected: Result contains success message
        """
        # Arrange
        medication_name = "Amoxicillin"
        
        # Act
        result = self.reminder_system.process_response(medication_name, taken=True)
        
        # Assert
        self.assertIn('message', result)
        self.assertEqual(result['message'], 'Response recorded successfully.')


class TestTC02_NoResponseFromUser(unittest.TestCase):
    """
    TC02 - No response from user
    
    Test Objective:
    Ensure the system correctly logs missed/unconfirmed doses when 
    the user does not respond.
    """
    
    def setUp(self):
        """Set up test fixtures"""
        self.database = DatabaseConnection()
        self.adherence_report = AdherenceReport(self.database)
        self.reminder_system = ReminderSystem(self.adherence_report)
        
    def test_expired_reminder_logged_as_unconfirmed(self):
        """
        Test that expired reminder is logged as Unconfirmed
        
        Expected: Entry is created with status 'Unconfirmed'
        """
        # Arrange
        medication_name = "Ibuprofen"
        scheduled_time = datetime.now() - timedelta(hours=1)
        
        # Act
        self.reminder_system.send_reminder(medication_name, scheduled_time)
        expired = self.reminder_system.check_expired_reminders()
        
        # Assert
        self.assertEqual(len(expired), 1)
        self.assertEqual(expired[0]['entry']['medication_name'], medication_name)
        self.assertEqual(expired[0]['entry']['status'], 'Unconfirmed')
        
    def test_unconfirmed_affects_adherence(self):
        """
        Test that unconfirmed status affects adherence percentage
        
        Expected: With 1 taken and 1 unconfirmed, adherence should be 50%
        """
        # Arrange
        self.reminder_system.process_response("Amoxicillin", taken=True)
        
        # Act
        medication_name = "Ibuprofen"
        scheduled_time = datetime.now() - timedelta(hours=1)
        self.reminder_system.send_reminder(medication_name, scheduled_time)
        self.reminder_system.check_expired_reminders()
        
        # Assert
        stats = self.adherence_report.get_statistics()
        self.assertEqual(stats['total_doses'], 2)
        self.assertEqual(stats['taken_doses'], 1)
        self.assertEqual(stats['adherence_percentage'], 50.0)
        
    def test_no_user_input_required(self):
        """
        Test that system logs without requiring user input
        
        Expected: Entry is automatically created when reminder expires
        """
        # Arrange
        medication_name = "Ibuprofen"
        scheduled_time = datetime.now() - timedelta(hours=1)
        
        # Act
        self.reminder_system.send_reminder(medication_name, scheduled_time)
        expired = self.reminder_system.check_expired_reminders()
        
        # Assert
        self.assertEqual(len(expired), 1)
        self.assertEqual(expired[0]['entry']['status'], 'Unconfirmed')
        
    def test_timestamp_generated_automatically(self):
        """
        Test that timestamp is generated automatically
        
        Expected: Timestamp is current time when reminder expires
        """
        # Arrange
        medication_name = "Ibuprofen"
        scheduled_time = datetime.now() - timedelta(hours=1)
        before_time = datetime.now()
        
        # Act
        self.reminder_system.send_reminder(medication_name, scheduled_time)
        expired = self.reminder_system.check_expired_reminders()
        after_time = datetime.now()
        
        # Assert
        timestamp = datetime.fromisoformat(expired[0]['entry']['timestamp'])
        self.assertGreaterEqual(timestamp, before_time)
        self.assertLessEqual(timestamp, after_time)


class TestTC03_LateResponse(unittest.TestCase):
    """
    TC03 - Late response
    
    Test Objective:
    Verify the system correctly handles a late response and applies 
    the proper status.
    """
    
    def setUp(self):
        """Set up test fixtures"""
        self.database = DatabaseConnection()
        self.adherence_report = AdherenceReport(self.database)
        self.reminder_system = ReminderSystem(self.adherence_report)
        
    def test_late_response_marked_correctly(self):
        """
        Test that late response is marked as 'Late Taken'
        
        Expected: Response 2 hours late is marked as 'Late Taken'
        """
        # Arrange
        medication_name = "Metformin"
        scheduled_time = datetime.now() - timedelta(hours=2)
        response_time = datetime.now()
        
        # Act
        self.reminder_system.send_reminder(medication_name, scheduled_time)
        result = self.reminder_system.process_response(
            medication_name, taken=True, response_time=response_time
        )
        
        # Assert
        self.assertEqual(result['entry']['status'], 'Late Taken')
        self.assertEqual(result['entry']['medication_name'], medication_name)
        
    def test_late_response_within_window(self):
        """
        Test response within window is marked as 'Taken'
        
        Expected: Response 15 minutes late is marked as 'Taken' (within 30-min window)
        """
        # Arrange
        medication_name = "Metformin"
        scheduled_time = datetime.now() - timedelta(minutes=15)
        response_time = datetime.now()
        
        # Act
        self.reminder_system.send_reminder(medication_name, scheduled_time)
        result = self.reminder_system.process_response(
            medication_name, taken=True, response_time=response_time
        )
        
        # Assert
        self.assertEqual(result['entry']['status'], 'Taken')
        
    def test_late_response_affects_adherence(self):
        """
        Test that late response counts toward adherence
        
        Expected: Late taken still counts as taken, 100% adherence
        """
        # Arrange
        medication_name = "Metformin"
        scheduled_time = datetime.now() - timedelta(hours=2)
        response_time = datetime.now()
        
        # Act
        self.reminder_system.send_reminder(medication_name, scheduled_time)
        self.reminder_system.process_response(
            medication_name, taken=True, response_time=response_time
        )
        
        # Assert
        stats = self.adherence_report.get_statistics()
        self.assertEqual(stats['taken_doses'], 1)
        self.assertEqual(stats['adherence_percentage'], 100.0)
        
    def test_late_timestamp_accuracy(self):
        """
        Test that late timestamp is stored accurately
        
        Expected: Stored timestamp matches response time
        """
        # Arrange
        medication_name = "Metformin"
        scheduled_time = datetime.now() - timedelta(hours=2)
        response_time = datetime.now()
        
        # Act
        self.reminder_system.send_reminder(medication_name, scheduled_time)
        result = self.reminder_system.process_response(
            medication_name, taken=True, response_time=response_time
        )
        
        # Assert
        stored_timestamp = datetime.fromisoformat(result['entry']['timestamp'])
        self.assertEqual(stored_timestamp.replace(microsecond=0), 
                        response_time.replace(microsecond=0))
        
    def test_confirmation_message_for_late_response(self):
        """
        Test that confirmation message appears for late response
        
        Expected: Success message is returned
        """
        # Arrange
        medication_name = "Metformin"
        scheduled_time = datetime.now() - timedelta(hours=2)
        response_time = datetime.now()
        
        # Act
        self.reminder_system.send_reminder(medication_name, scheduled_time)
        result = self.reminder_system.process_response(
            medication_name, taken=True, response_time=response_time
        )
        
        # Assert
        self.assertIn('message', result)
        self.assertEqual(result['message'], 'Response recorded successfully.')


class TestTC04_SystemErrorWhileSavingRecord(unittest.TestCase):
    """
    TC04 - System error while saving record
    
    Test Objective:
    Verify system behavior when an error prevents storing the response.
    """
    
    def setUp(self):
        """Set up test fixtures"""
        self.database = DatabaseConnection()
        self.adherence_report = AdherenceReport(self.database)
        self.reminder_system = ReminderSystem(self.adherence_report)
        
    def test_database_error_handling(self):
        """
        Test that database errors are handled properly
        
        Expected: Exception is raised with appropriate message
        """
        # Arrange
        medication_name = "Lisinopril"
        
        # Act
        self.database.simulate_error()
        
        # Assert
        with self.assertRaises(Exception) as context:
            self.reminder_system.process_response(medication_name, taken=True)
        
        self.assertIn("Unable to record response", str(context.exception))
        
    def test_error_message_displayed(self):
        """
        Test that appropriate error message is displayed
        
        Expected: Error message includes "Please try again"
        """
        # Arrange
        medication_name = "Lisinopril"
        
        # Act
        self.database.simulate_error()
        
        try:
            self.reminder_system.process_response(medication_name, taken=True)
            error_occurred = False
        except Exception as e:
            error_occurred = True
            error_message = str(e)
        
        # Assert
        self.assertTrue(error_occurred)
        self.assertIn("Please try again", error_message)
        
    def test_no_partial_data_on_error(self):
        """
        Test that no partial data is added on error
        
        Expected: No entries are added when database save fails
        """
        # Arrange
        medication_name = "Lisinopril"
        initial_count = len(self.adherence_report.entries)
        
        # Act
        self.database.simulate_error()
        
        try:
            self.reminder_system.process_response(medication_name, taken=True)
        except Exception:
            pass
        
        # Assert
        self.assertEqual(len(self.adherence_report.entries), initial_count)
        
    def test_system_state_stable_after_error(self):
        """
        Test that system remains in stable state after error
        
        Expected: System can successfully process next request after error
        """
        # Arrange
        medication_name = "Lisinopril"
        
        # Act - First attempt fails
        self.database.simulate_error()
        
        try:
            self.reminder_system.process_response(medication_name, taken=True)
        except Exception:
            pass
        
        # Act - Retry should work
        result = self.reminder_system.process_response(medication_name, taken=True)
        
        # Assert
        self.assertTrue(result['success'])
        self.assertEqual(len(self.adherence_report.entries), 1)
        
    def test_retry_option_available(self):
        """
        Test that retry is possible after error
        
        Expected: Second attempt succeeds after first fails
        """
        # Arrange
        medication_name = "Lisinopril"
        
        # Act - First attempt
        self.database.simulate_error()
        
        try:
            self.reminder_system.process_response(medication_name, taken=True)
        except Exception:
            pass
        
        # Act - Retry
        result = self.reminder_system.process_response(medication_name, taken=True)
        
        # Assert
        self.assertTrue(result['success'])


# ============================================================================
# TEST RUNNER
# ============================================================================

def run_test_suite():
    """Run the complete test suite with detailed reporting"""
    
    print("="*70)
    print("USE CASE 3: GENERATION OF ADHERENCE REPORT - TEST SUITE")
    print("="*70)
    print()
    
    # Create test suite
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        TestTC01_SuccessfulLoggingAndReportUpdate))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        TestTC02_NoResponseFromUser))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        TestTC03_LateResponse))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        TestTC04_SystemErrorWhileSavingRecord))
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Total Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("\n✓ All tests passed successfully!")
    else:
        print("\n✗ Some tests failed. Please review the output above.")
    
    print("="*70)
    
    return result


if __name__ == '__main__':
    run_test_suite()