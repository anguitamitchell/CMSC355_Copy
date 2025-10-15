import re
import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# ---------- Data Model ----------
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

# ---------- File Storage ----------
def save_medication(medication):
    filename = "data/medications.json"
    os.makedirs("data", exist_ok=True)

    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(medication.to_dict())

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# ---------- GUI ----------
def submit_medication():
    name = entry_name.get().strip()
    dosage = entry_dosage.get().strip().lower()
    frequency = entry_frequency.get().strip()
    end_date = entry_end_date.get().strip()

    # Validate dosage
    if not re.match(r"^\d+\s?mg$", dosage):
        messagebox.showerror("Error", "Dosage must be a number followed by 'mg' (e.g., 10 mg)")
        return

    # Validate frequency
    try:
        frequency = int(frequency)
        if not (1 <= frequency <= 24):
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Frequency must be an integer between 1 and 24")
        return

    # Optionally, you could validate date format here

    # Create medication and save
    new_med = Medication(name, dosage, frequency, end_date)
    save_medication(new_med)
    messagebox.showinfo("Success", f"Medication '{name}' added successfully!")

    # Clear fields
    entry_name.delete(0, tk.END)
    entry_dosage.delete(0, tk.END)
    entry_frequency.delete(0, tk.END)
    entry_end_date.delete(0, tk.END)

# ---------- Main Window ----------
root = tk.Tk()
root.title("Add New Medication")
root.geometry("400x300")

# Labels
tk.Label(root, text="Medication Name:").pack(pady=(20,0))
entry_name = tk.Entry(root, width=30)
entry_name.pack()

tk.Label(root, text="Dosage (e.g., 10 mg):").pack(pady=(10,0))
entry_dosage = tk.Entry(root, width=30)
entry_dosage.pack()

tk.Label(root, text="Frequency (hours):").pack(pady=(10,0))
entry_frequency = tk.Entry(root, width=30)
entry_frequency.pack()

tk.Label(root, text="End Date (YYYY-MM-DD):").pack(pady=(10,0))
entry_end_date = tk.Entry(root, width=30)
entry_end_date.pack()

# Submit Button
tk.Button(root, text="Add Medication", command=submit_medication).pack(pady=20)

root.mainloop()
