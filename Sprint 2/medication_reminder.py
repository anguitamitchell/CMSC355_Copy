import json
import os
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox, ttk
import threading
import time

# File paths
def get_sprint1_data_file():
    """Load medications from Sprint 1 directory"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)
    sprint1_dir = os.path.join(parent_dir, "Sprint 1")
    return os.path.join(sprint1_dir, "Sprint 1.json")

def get_sprint2_data_file():
    """Save adherence history in Sprint 2 directory"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "Sprint 2.json")

def get_reminders_file():
    """Store scheduled reminders"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "reminders.json")

# Data Loading Functions
def load_medications():
    """Load medications from Sprint 1"""
    filename = get_sprint1_data_file()
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def load_adherence_history():
    """Load adherence history from Sprint 2"""
    filename = get_sprint2_data_file()
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_adherence_history(data):
    """Save adherence history to Sprint 2"""
    filename = get_sprint2_data_file()
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_reminders():
    """Load scheduled reminders"""
    filename = get_reminders_file()
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_reminders(data):
    """Save scheduled reminders"""
    filename = get_reminders_file()
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Adherence Logging
def log_adherence(medication_name, dosage, status, reminder_time):
    """
    Log medication adherence with timestamp
    Status: Taken, Missed, or Unconfirmed
    """
    history = load_adherence_history()
    
    entry = {
        "medication_name": medication_name,
        "dosage": dosage,
        "reminder_time": reminder_time,
        "status": status,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    history.append(entry)
    save_adherence_history(history)
    return entry

# Reminder Scheduling
def schedule_reminder(medication_name, dosage, frequency):
    """
    Schedule a reminder for a medication
    Frequency is in hours
    """
    reminders = load_reminders()
    
    # Calculate next reminder time
    now = datetime.now()
    next_reminder = now + timedelta(hours=int(frequency))
    
    reminder = {
        "medication_name": medication_name,
        "dosage": dosage,
        "frequency": frequency,
        "next_reminder": next_reminder.strftime("%Y-%m-%d %H:%M:%S"),
        "active": True
    }
    
    reminders.append(reminder)
    save_reminders(reminders)
    return reminder

# GUI Application
class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medication Reminder System - Sprint 2")
        self.root.geometry("600x500")
        
        self.active_reminders = []
        self.check_interval = 60  # Check every 60 seconds (NFR01)
        
        self.create_widgets()
        self.load_active_medications()
        
        # Start reminder checker thread
        self.running = True
        self.reminder_thread = threading.Thread(target=self.check_reminders_loop, daemon=True)
        self.reminder_thread.start()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Medication Reminder System", 
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Active Medications Frame
        meds_frame = tk.LabelFrame(self.root, text="Active Medications", 
                                   font=("Arial", 12))
        meds_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        # Treeview for medications
        columns = ("Name", "Dosage", "Frequency", "Next Reminder")
        self.meds_tree = ttk.Treeview(meds_frame, columns=columns, show="headings", height=8)
        
        for col in columns:
            self.meds_tree.heading(col, text=col)
            self.meds_tree.column(col, width=130)
        
        self.meds_tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Buttons Frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=10)
        
        tk.Button(buttons_frame, text="Schedule New Reminder", 
                 command=self.open_schedule_window, width=20).pack(side=tk.LEFT, padx=5)
        tk.Button(buttons_frame, text="View Adherence History", 
                 command=self.view_history, width=20).pack(side=tk.LEFT, padx=5)
        tk.Button(buttons_frame, text="Refresh", 
                 command=self.refresh_display, width=15).pack(side=tk.LEFT, padx=5)
        
        # Status Label
        self.status_label = tk.Label(self.root, text="System Active - Checking for reminders...", 
                                     fg="green")
        self.status_label.pack(pady=5)
    
    def load_active_medications(self):
        """Load medications from Sprint 1 that can be scheduled"""
        medications = load_medications()
        reminders = load_reminders()
        
        # Clear treeview
        for item in self.meds_tree.get_children():
            self.meds_tree.delete(item)
        
        # Display active reminders
        for reminder in reminders:
            if reminder.get("active", True):
                self.meds_tree.insert("", tk.END, values=(
                    reminder["medication_name"],
                    reminder["dosage"],
                    f"Every {reminder['frequency']} hours",
                    reminder["next_reminder"]
                ))
    
    def refresh_display(self):
        """Refresh the medication display"""
        self.load_active_medications()
        messagebox.showinfo("Refreshed", "Medication list updated")
    
    def open_schedule_window(self):
        """Open window to schedule a new reminder"""
        schedule_window = tk.Toplevel(self.root)
        schedule_window.title("Schedule New Reminder")
        schedule_window.geometry("400x300")
        
        medications = load_medications()
        
        if not medications:
            messagebox.showwarning("No Medications", 
                                 "No medications found. Please add medications in Sprint 1 first.")
            schedule_window.destroy()
            return
        
        tk.Label(schedule_window, text="Select Medication:", font=("Arial", 10)).pack(pady=(20,5))
        
        med_var = tk.StringVar()
        med_dropdown = ttk.Combobox(schedule_window, textvariable=med_var, 
                                    values=[f"{m['name']} - {m['dosage']}" for m in medications],
                                    width=30, state="readonly")
        med_dropdown.pack()
        
        tk.Label(schedule_window, text="Reminder Time (HH:MM):", font=("Arial", 10)).pack(pady=(20,5))
        time_entry = tk.Entry(schedule_window, width=20)
        time_entry.pack()
        time_entry.insert(0, "09:00")
        
        def confirm_schedule():
            selected = med_var.get()
            time_str = time_entry.get().strip()
            
            if not selected:
                messagebox.showerror("Error", "Please select a medication")
                return
            
            # Validate time format
            try:
                datetime.strptime(time_str, "%H:%M")
            except ValueError:
                messagebox.showerror("Error", "Invalid time format. Use HH:MM (e.g., 09:00)")
                return
            
            # Extract medication info
            med_name = selected.split(" - ")[0]
            med = next((m for m in medications if m['name'] == med_name), None)
            
            if med:
                schedule_reminder(med['name'], med['dosage'], med['frequency'])
                messagebox.showinfo("Success", f"Reminder scheduled for {med['name']}")
                self.refresh_display()
                schedule_window.destroy()
        
        tk.Button(schedule_window, text="Confirm", command=confirm_schedule, 
                 width=15).pack(pady=20)
    
    def check_reminders_loop(self):
        """Background thread to check for due reminders"""
        while self.running:
            self.check_due_reminders()
            time.sleep(self.check_interval)
    
    def check_due_reminders(self):
        """Check if any reminders are due and trigger notifications"""
        reminders = load_reminders()
        now = datetime.now()
        
        for i, reminder in enumerate(reminders):
            if not reminder.get("active", True):
                continue
            
            reminder_time = datetime.strptime(reminder["next_reminder"], "%Y-%m-%d %H:%M:%S")
            
            # If reminder time has passed (within 60 seconds - NFR01)
            if now >= reminder_time:
                # Trigger reminder notification
                self.root.after(0, self.show_reminder_notification, reminder, i)
    
    def show_reminder_notification(self, reminder, reminder_index):
        """Show reminder notification popup"""
        notification = tk.Toplevel(self.root)
        notification.title("⏰ Medication Reminder")
        notification.geometry("400x250")
        notification.attributes('-topmost', True)
        
        tk.Label(notification, text="🔔 Time to Take Your Medication!", 
                font=("Arial", 14, "bold"), fg="blue").pack(pady=20)
        
        tk.Label(notification, text=f"Medication: {reminder['medication_name']}", 
                font=("Arial", 11)).pack(pady=5)
        tk.Label(notification, text=f"Dosage: {reminder['dosage']}", 
                font=("Arial", 11)).pack(pady=5)
        
        # Response buttons
        button_frame = tk.Frame(notification)
        button_frame.pack(pady=20)
        
        def mark_taken():
            log_adherence(reminder['medication_name'], reminder['dosage'], 
                         "Taken", reminder['next_reminder'])
            self.reschedule_reminder(reminder_index, reminder)
            messagebox.showinfo("Confirmed", "Medication marked as Taken")
            notification.destroy()
        
        def mark_missed():
            log_adherence(reminder['medication_name'], reminder['dosage'], 
                         "Missed", reminder['next_reminder'])
            self.reschedule_reminder(reminder_index, reminder)
            messagebox.showinfo("Confirmed", "Medication marked as Missed")
            notification.destroy()
        
        def snooze():
            # Snooze for 15 minutes
            reminders = load_reminders()
            next_time = datetime.now() + timedelta(minutes=15)
            reminders[reminder_index]['next_reminder'] = next_time.strftime("%Y-%m-%d %H:%M:%S")
            save_reminders(reminders)
            messagebox.showinfo("Snoozed", "Reminder snoozed for 15 minutes")
            notification.destroy()
        
        tk.Button(button_frame, text="✓ Taken", command=mark_taken, 
                 width=12, bg="green", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="✗ Missed", command=mark_missed, 
                 width=12, bg="red", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="⏰ Snooze", command=snooze, 
                 width=12, bg="orange", fg="white").pack(side=tk.LEFT, padx=5)
        
        # Auto-mark as Unconfirmed after 5 minutes (E01)
        def auto_mark_unconfirmed():
            if notification.winfo_exists():
                log_adherence(reminder['medication_name'], reminder['dosage'], 
                             "Unconfirmed", reminder['next_reminder'])
                self.reschedule_reminder(reminder_index, reminder)
                notification.destroy()
        
        notification.after(300000, auto_mark_unconfirmed)  # 5 minutes
    
    def reschedule_reminder(self, index, reminder):
        """Reschedule reminder for next dose (BR02)"""
        reminders = load_reminders()
        next_time = datetime.now() + timedelta(hours=int(reminder['frequency']))
        reminders[index]['next_reminder'] = next_time.strftime("%Y-%m-%d %H:%M:%S")
        save_reminders(reminders)
        self.refresh_display()
    
    def view_history(self):
        """View adherence history"""
        history = load_adherence_history()
        
        if not history:
            messagebox.showinfo("Adherence History", "No adherence history yet")
            return
        
        history_window = tk.Toplevel(self.root)
        history_window.title("Adherence History")
        history_window.geometry("700x400")
        
        # Treeview for history
        columns = ("Medication", "Dosage", "Reminder Time", "Status", "Timestamp")
        history_tree = ttk.Treeview(history_window, columns=columns, show="headings")
        
        for col in columns:
            history_tree.heading(col, text=col)
            history_tree.column(col, width=130)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(history_window, orient=tk.VERTICAL, command=history_tree.yview)
        history_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        history_tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Populate history (most recent first)
        for entry in reversed(history):
            # Color code by status
            tag = entry['status'].lower()
            history_tree.insert("", tk.END, values=(
                entry['medication_name'],
                entry['dosage'],
                entry['reminder_time'],
                entry['status'],
                entry['timestamp']
            ), tags=(tag,))
        
        # Configure tags for colors
        history_tree.tag_configure('taken', background='lightgreen')
        history_tree.tag_configure('missed', background='lightcoral')
        history_tree.tag_configure('unconfirmed', background='lightyellow')
    
    def on_closing(self):
        """Clean shutdown"""
        self.running = False
        self.root.destroy()

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()