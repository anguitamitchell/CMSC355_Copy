import javax.swing.*;
import java.awt.*;
import java.util.*;
import java.util.List;

// Represents a medicine entry
class Medicine {
    String name;
    String schedule;
    String adherence;
    String sideEffects;

    public Medicine(String name, String schedule, String adherence, String sideEffects) {
        this.name = name;
        this.schedule = schedule;
        this.adherence = adherence;
        this.sideEffects = sideEffects;
    }

    public void printDetails() {
        System.out.println("Medication: " + name);
        System.out.println("  Schedule: " + schedule);
        System.out.println("  Adherence: " + adherence);
        System.out.println("  Side Effects: " + sideEffects);
    }
}

// System that manages the medication report
class ReportSystem {
    static List<Medicine> medicationList = new ArrayList<>();
    MedicationLogging medicationLogging;

    public ReportSystem(MedicationLogging medicationLogging) {
        this.medicationLogging = medicationLogging;
        retrieveMedicationData();
    }

    public void retrieveMedicationData() {
        for (ValidatingMedication med : medicationLogging.medications) {
            medicationList.add(new Medicine(
                    med.getNameofMedication(),
                    "Unknown Schedule",
                    "Unknown",
                    "None"
            ));
        }
    }

    public static void generateReport(User user, JTextArea outputArea) {
        /*
        if (!user.isAuthenticated) {
            outputArea.setText("Access denied. Please log in.\n");
            return;
        }

        if (medicationList.isEmpty()) {
            outputArea.setText("No medication data available.\n");
            return;
        }

         */

        StringBuilder report = new StringBuilder();
        report.append("=== Medication Adherence Report ===\n");

        for (Medicine med : medicationList) {
            report.append("Medication: ").append(med.name).append("\n")
                    .append("  Schedule: ").append(med.schedule).append("\n")
                    .append("  Adherence: ").append(med.adherence).append("\n")
                    .append("  Side Effects: ").append(med.sideEffects).append("\n")
                    .append("-----------------------------------\n");
        }

        /*
        if (user.isDoctor()) {
            report.append("Doctor Recommendations:\n")
                    .append(" - Continue medications as prescribed\n")
                    .append(" - Adjust based on side effects\n\n");
        }

         */

        outputArea.setText(report.toString());
    }

    public static void addMedicine(String name, String schedule, String adherence, String sideEffects) {
        medicationList.add(new Medicine(name, schedule, adherence, sideEffects));
    }

    public static void removeMedicine(String name) {
        medicationList.removeIf(med -> med.name.equalsIgnoreCase(name));
    }
}
