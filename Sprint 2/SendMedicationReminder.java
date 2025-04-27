/**
 * Medical Adherence System
 * Sprint 2
 * CMSC 355 - Fundamentals of Software Engineering
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Reminder object
public class Reminder {
    private String username;
    private String medication;
    private boolean acknowledged;

    public Reminder(String username, String medication) {
        this.username = username;
        this.medication = medication;
        this.acknowledged = false;
    }

    public String getUsername() {
        return username;
    }

    public String getMedication() {
        return medication;
    }

    public boolean isAcknowledged() {
        return acknowledged;
    }

    public void acknowledge() {
        this.acknowledged = true;
    }
}

// Handles storing and sending reminders
class ReminderService {
    private List<Reminder> reminders = new ArrayList<>();

    public void addReminder(String username, String medication) {
        reminders.add(new Reminder(username, medication));
    }

    public void sendReminders(Scanner scanner) {
        for (Reminder reminder : reminders) {
            if (!reminder.isAcknowledged()) {
                System.out.println("Reminder for " + reminder.getUsername() + ": Take " + reminder.getMedication());
                System.out.println("Did the user acknowledge the reminder? (yes/no)");
                String response = scanner.nextLine();

                if (response.equalsIgnoreCase("yes")) {
                    reminder.acknowledge();
                    System.out.println("Reminder acknowledged.");
                } else {
                    System.out.println("Reminder missed. Logging missed reminder.");
                    handleMissedReminder(reminder);
                }
            }
        }
    }

    public List<Reminder> getReminders() {
        return reminders;
    }

    private void handleMissedReminder(Reminder reminder) {
        System.out.println("User " + reminder.getUsername() + " missed their medication. Alerting caregiver if necessary.");
    }
}
