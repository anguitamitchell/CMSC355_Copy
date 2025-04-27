/**
 * Medical Adherence System
 * Sprint 3
 * CMSC 355 - Fundamentals of Software Engineering
 */

import java.util.Scanner;

//TrackReminderResponse handles tracking user responses to reminders.
public class TrackReminderResponse {
    private ReminderService reminderService;

    //Constructor initializes with a given ReminderService.
    public TrackReminderResponse(ReminderService reminderService) {
        this.reminderService = reminderService;
    }

    //Runs the reminder response tracking process.
    public void run() {
        Scanner scanner = new Scanner(System.in);

        for (Reminder reminder : reminderService.getReminders()) {
            if (!reminder.isAcknowledged()) {
                reminderService.processReminder(reminder, scanner);
            }
        }
    }
}