/**
 * Medical Adherence System
 * Sprint 1
 * CMSC 355 - Fundamentals of Software Engineering
 *
 */
import java.util.ArrayList;
import java.util.Scanner;
import java.util.List;
class Reminder {
    private String username;
    private String medication;
    private boolean acknowledged;

    public Reminder(String username, String medication) {
        this.username = username;
        this medication = medication;
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

class ReminderService {
    private List<Reminder> reminders = new ArrayList<>();

    public void addReminder(String username, String medication) {
        reminders.add(new Reminder(username, medication));
        System.out.println("Reminder added for " + username + ": " + medication);
    }

    public void sendReminders() {
        Scanner scanner = new Scanner(System.in);
        for (Reminder reminder : reminders) {
            if (!reminder.isAcknowledged()) {
                System.out.println("Sending reminder to " + reminder.getUsername() + " for " + reminder.getMedication());
                System.out.printlm("Did the user acknowledge the reminder? (yes/no)");
                String response = scanner.nextLine();

                if (response.equalsIgnoreCase("yes")) {
                    reminder.acknowledge();
                    System.out.println("Reminder acknowledged.");
                }
                else {
                    System.out.println("Reminder missed. Logging missed reminder.");
                    handleMissedReminder(reminder);
                }
            }
        }
    }
    private void handleMissedReminder(Reminder reminder) {
        System.out.println("User " + reminder.getUsername() + " missed their medication. Alerting caregiver if necessary.");
    }
}
