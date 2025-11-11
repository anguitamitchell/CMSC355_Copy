import re
import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

#Simulated Doctor-Approved Database 
APPROVED_MEDICATIONS = {
    "Amoxicillin": True,
    "Ibuprofen": True,
    "Metformin": True,
    "Lisinopril": True,
    "Amlodipine": True,
}

#Data Model
class Medication:
    def __init__(self, name, dosage, frequency, end_date):
        self.name = name
        self.dosage = dosage
        self.frequency = frequency
        self.end_date = end_date
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "name": self.name,
            "dosage": self.dosage,
            "frequency": self.frequency,
            "end_date": self.end_date,
            "created_at": self.created_at
        }

#File Storage
def get_data_file():
    """
    Save medications in 'Sprint 1.json' located in the same directory as this file.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(base_dir, "Sprint 1.json")
    return filename

def load_medications():
    filename = get_data_file()
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_medications(data):
    filename = get_data_file()
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def save_medication(medication):
    data = load_medications()
    data.append(medication.to_dict())
    save_medications(data)

def remove_medication(name):
    """Removes medication by name after confirmation (TC02)."""
    data = load_medications()
    updated = [m for m in data if m["name"].lower() != name.lower()]

    if len(updated) == len(data):
        messagebox.showinfo("Info", f"No record found for '{name}'.")
        return

    confirm = messagebox.askyesno("Confirm", f"Are you sure you want to remove '{name}'?")
    if confirm:
        save_medications(updated)
        messagebox.showinfo("Success", "Medication is successfully removed")
    else:
        messagebox.showinfo("Cancelled", "Removal cancelled.")

#GUI
def submit_medication():
    name = entry_name.get().strip().capitalize()
    dosage = entry_dosage.get().strip().lower()
    frequency = entry_frequency.get().strip()
    end_date = entry_end_date.get().strip()

    #TC04: Verify medication exists and has doctor approval
    if name not in APPROVED_MEDICATIONS or not APPROVED_MEDICATIONS[name]:
        messagebox.showerror("Error", "Medication not found or waiting doctor approval")
        return

    #Validate dosage
    if not re.match(r"^\d+\s?mg$", dosage):
        messagebox.showerror("Error", "Invalid dosage, please input a valid format (Ex. 500mg)")
        return

    #Validate frequency
    try:
        frequency = int(frequency)
        if not (1 <= frequency <= 24):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Frequency must be an integer between 1 and 24")
        return

    #Successfully add new medication
    new_med = Medication(name, dosage, frequency, end_date)
    save_medication(new_med)
    messagebox.showinfo("Success", "Medication successfully added")

    # Clear fields
    entry_name.delete(0, tk.END)
    entry_dosage.delete(0, tk.END)
    entry_frequency.delete(0, tk.END)
    entry_end_date.delete(0, tk.END)

def open_remove_window():
    """Small pop-up to handle removal (for TC02)."""
    def confirm_remove():
        med_name = remove_entry.get().strip()
        if med_name:
            remove_medication(med_name)
            remove_window.destroy()

    remove_window = tk.Toplevel(root)
    remove_window.title("Remove Medication")
    remove_window.geometry("300x150")

    tk.Label(remove_window, text="Enter Medication Name to Remove:").pack(pady=(20,5))
    remove_entry = tk.Entry(remove_window, width=25)
    remove_entry.pack()
    tk.Button(remove_window, text="Confirm Removal", command=confirm_remove).pack(pady=10)

#Main Window
root = tk.Tk()
root.title("Medication Management - Sprint 1")
root.geometry("400x350")

# Labels and Input Fields
tk.Label(root, text="Medication Name:").pack(pady=(20,0))
entry_name = tk.Entry(root, width=30)
entry_name.pack()

tk.Label(root, text="Dosage (e.g., 500mg):").pack(pady=(10,0))
entry_dosage = tk.Entry(root, width=30)
entry_dosage.pack()

tk.Label(root, text="Frequency (hours):").pack(pady=(10,0))
entry_frequency = tk.Entry(root, width=30)
entry_frequency.pack()

tk.Label(root, text="End Date (YYYY-MM-DD):").pack(pady=(10,0))
entry_end_date = tk.Entry(root, width=30)
entry_end_date.pack()

# Buttons
tk.Button(root, text="Add Medication", command=submit_medication).pack(pady=15)
tk.Button(root, text="Remove Medication", command=open_remove_window).pack(pady=5)

if __name__ == "__main__":
    root.mainloop()
