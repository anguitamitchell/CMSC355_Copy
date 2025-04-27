// MedicineReport.java

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

    public void printReport() {
        System.out.println("Medication: " + name);
        System.out.println("Schedule: " + schedule);
        System.out.println("Adherence: " + adherence);
        System.out.println("Side Effects: " + sideEffects);
    }
}

public class MedicineReport {
    public static void main(String[] args) {
        System.out.println("Generating medicine report...");

        Medicine med = new Medicine("Aspirin", "Twice a day", "90%", "None");
        med.printReport();

        System.out.println("Report ready to view or download.");
    }
}
