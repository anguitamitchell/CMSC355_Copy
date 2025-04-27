/**
 * Medical Adherence System
 * Sprint 3
 * CMSC 355 - Fundamentals of Software Engineering
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//Represents a medication reminder for a user.
public class Reminder {
    private String username;
    private String medication;
    private boolean acknowledged;


    // Constructs a Reminder for a specific user and medication.
    public Reminder(String username, String medication) {
        this.username = username;
        this.medication = medication;
        this.acknowledged = false;
    }

    // Returns the username associated with this reminder.
    public String getUsername() {
        return username;
    }

    //Returns the medication associated with this reminder
    public String getMedication() {
        return medication;
    }

    //Returns true if the reminder has been acknowledged.
    public boolean isAcknowledged() {
        return acknowledged;
    }

    //Marks the reminder as acknowledged.
    public void acknowledge() {
        this.acknowledged = true;
    }
}

//Handles storing, sending, and processing reminders for users.
class ReminderService {
    private List<Reminder> reminders = new ArrayList<>();

    //Adds a new reminder for a given user and medication.
    public void addReminder(String username, String medication) {
        reminders.add(new Reminder(username, medication));
    }

    //Sends reminders to users and prompts for acknowledgment.
    public void sendReminders(Scanner scanner) {
        for (Reminder reminder : reminders) {
            if (!reminder.isAcknowledged()) {
                processReminder(reminder, scanner);
            }
        }
    }

    //Processes a single reminder by prompting the user for a response.
    public void processReminder(Reminder reminder, Scanner scanner) {
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

    //Returns the list of reminders.
    public List<Reminder> getReminders() {
        return reminders;
    }

    //Handles a missed reminder by alerting the caregiver or logging it.
    private void handleMissedReminder(Reminder reminder) {
        System.out.println("ALERT: User " + reminder.getUsername() + " missed their medication (" + reminder.getMedication() + ").");
    }
}