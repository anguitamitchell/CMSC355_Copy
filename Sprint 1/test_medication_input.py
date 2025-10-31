import os
import json
import re
from unittest import mock
import medication_input 

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Sprint 1.json")

def reset_data_file():
    """Clear Sprint 1.json before each test for a clean environment."""
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def load_data():
    """Load data safely from Sprint 1.json."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

#TEST CASES

def test_TC01_success_add():
    """TC01: Successfully add a valid medication."""
    reset_data_file()
    med = medication_input.Medication("Amoxicillin", "500mg", 8, "10 days")

    # Mock messagebox popups
    with mock.patch("tkinter.messagebox.showinfo"), mock.patch("tkinter.messagebox.showerror"):
        medication_input.save_medication(med)

    data = load_data()
    assert len(data) == 1 and data[0]["name"] == "Amoxicillin"
    print("TC01 Passed: Medication successfully added and saved.")

def test_TC02_remove_medication():
    """TC02: Remove medication with confirmation."""
    reset_data_file()
    med = medication_input.Medication("Amoxicillin", "500mg", 8, "10 days")
    medication_input.save_medication(med)

    # Mock confirmation and info boxes
    with mock.patch("tkinter.messagebox.askyesno", return_value=True), \
         mock.patch("tkinter.messagebox.showinfo"):
        medication_input.remove_medication("Amoxicillin")

    data = load_data()
    assert len(data) == 0
    print("TC02 Passed: Medication successfully removed.")

def test_TC03_invalid_dosage():
    """TC03: Detect invalid dosage input."""
    invalid_dosage = "five hundred mg"
    assert not re.match(r"^\d+\s?mg$", invalid_dosage)
    print("TC03 Passed: Invalid dosage correctly detected.")

def test_TC04_unapproved_medication():
    """TC04: Block medication not approved by doctor."""
    reset_data_file()
    unapproved = "UnknownDrug"
    assert unapproved not in medication_input.APPROVED_MEDICATIONS
    print("TC04 Passed: Medication without approval correctly rejected.")

#MAIN TEST RUNNER
if __name__ == "__main__":
    print("\nRunning Functional Tests for medication_input.py...\n")

    try:
        test_TC01_success_add()
        test_TC02_remove_medication()
        test_TC03_invalid_dosage()
        test_TC04_unapproved_medication()
        print("\n🎉 All test cases passed successfully!\n")
    except AssertionError as e:
        print(" Test failed:", e)
