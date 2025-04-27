/**
 * Medical Adherence System
 * Sprint 2
 * CMSC 355 - Fundamentals of Software Engineering
 */

import java.util.Scanner;

public class TrackReminderResponse {
    private ReminderService reminderService;

    public TrackReminderResponse(ReminderService reminderService) {
        this.reminderService = reminderService;
    }

    public void run() {
        Scanner scanner = new Scanner(System.in);

        for (Reminder reminder : reminderService.getReminders()) {
            if (!reminder.isAcknowledged()) {
                System.out.println("Reminder for user: " + reminder.getUsername() + " - Medication: " + reminder.getMedication());
                System.out.println("Has the user responded? (yes/no)");

                String response = scanner.nextLine();

                if (response.equalsIgnoreCase("yes")) {
                    reminder.acknowledge();
                    System.out.println("Marked as acknowledged.");
                } else {
                    System.out.println("No response received. Logging as missed.");
                    handleMissedResponse(reminder);
                }
            }
        }
    }

    private void handleMissedResponse(Reminder reminder) {
        System.out.println("ALERT: User " + reminder.getUsername() + " missed their medication (" + reminder.getMedication() + ").");
    }
}
