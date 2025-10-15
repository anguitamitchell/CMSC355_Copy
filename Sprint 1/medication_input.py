import re
from datetime import datetime
import json
import os

# ---------- Data Model ----------
class Medication:
    def __init__(self, name, dosage, frequency, end_date):
        self.name = name
        self.dosage = dosage
        self.frequency = frequency  # in hours
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

# ---------- Core Functionality ----------
def input_new_medication():
    """Handles user input for a new medication record with dosage validation"""
    print("\n--- Add a New Medication ---")

    # Medication name
    name = input("Enter medication name: ").strip()

    # Dosage validation: must be number followed by 'mg'
    dosage_pattern = r"^\d+\s?mg$"
    while True:
        dosage = input("Enter dosage (e.g., '10 mg'): ").strip().lower()
        if re.match(dosage_pattern, dosage):
            break
        else:
            print("Invalid format! Dosage must be a number followed by 'mg' (e.g., 10 mg)")

    # Frequency validation
    while True:
        try:
            frequency = int(input("Enter frequency (hours between doses, 1–24): "))
            if 1 <= frequency <= 24:
                break
            else:
                print("Frequency must be between 1 and 24 hours.")
        except ValueError:
            print("Please enter a valid number for frequency.")

    # End date
    end_date = input("Enter end date (YYYY-MM-DD): ").strip()

    # Confirm or cancel
    confirm = input("Confirm adding this medication? (Y/N): ").strip().lower()
    if confirm != "y":
        print("Medication entry canceled.")
        return None

    # Create and save the record
    new_med = Medication(name, dosage, frequency, end_date)
    save_medication(new_med)
    print(f"Medication '{new_med.name}' successfully added!\n")

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

    print(f"Saved to {filename}")

# ---------- Main ----------
if __name__ == "__main__":
    input_new_medication()
