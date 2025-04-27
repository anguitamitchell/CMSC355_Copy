/**
 * Medical Adherence System
 * Sprint 1
 * CMSC 355 - Fundamentals of Software Engineering
 *
 */
import java.util.Scanner;

class ResponseTracker {
    private ReminderService reminderService;

    public ResponseTracker(ReminderService reminderService) {
        this.reminderService = reminderService;
    }

    public void trackResponse() {
        Scanner scanner = new Scanner(System.in);

        for (Reminder reminder : reminderService.getReminders()) {
            if (!reminder.isAcknowledged()) {
                System.out.println("Checking response for " + reminder.getUsername() + " - Medication: " + reminder.getMedication());

                System.out.println("Did the user acknowledge the reminder? (yes/no)");
                String response = scanner.nextLine();

                if (response.equalsIgnoreCase("yes")) {
                    reminder.acknowledge();
                    System.out.println("Response recorded: User took medication.");
                } else {
                    System.out.println("Response not received. Logging as a missed dose.");
                    handleMissedResponse(reminder);
                }
            }
        }
    }
}
