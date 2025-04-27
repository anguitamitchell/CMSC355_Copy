import java.util.*;

public class PrescriptionNumberVerification {

    // Stores prescriptions using Rx number as key
    private static Map<String, Prescription> rxStore = new HashMap<>();

    /**hod to manage adding and retrieving prescriptions
     */
    public static void managePrescriptions() {
        Scanner scann
     * Meter = new Scanner(System.in);

        System.out.println("Menu Options:");
        System.out.println("1. Add a new prescription");
        System.out.println("2. Retrieve medication details");
        System.out.println("3. Go back");

        System.out.print("Enter your choice: ");
        int choice = scanner.nextInt();
        scanner.nextLine(); // Consume newline character

        switch (choice) {
            case 1:
                // Add a new prescription to the system
                System.out.print("Enter Rx number: ");
                String rxNumber = scanner.nextLine().trim();

                System.out.print("Enter medication name: ");
                String medicationName = scanner.nextLine().trim();

                System.out.print("Enter times to take the medication: ");
                String times = scanner.nextLine().trim();

                rxStore.put(rxNumber, new Prescription(rxNumber, medicationName, times));
                System.out.println("Prescription added successfully.");
                break;

            case 2:
                // Look up a prescription by Rx number
                System.out.print("Enter Rx number: ");
                String searchRxNumber = scanner.nextLine().trim();

                if (rxStore.containsKey(searchRxNumber)) {
                    Prescription prescription = rxStore.get(searchRxNumber);
                    System.out.println("Medication: " + prescription.getMedicationName());
                    System.out.println("Times: " + prescription.getTimes());
                } else {
                    System.out.println("Rx number not found.");
                }
                break;

            case 3:
                // Return to previous menu (Main.home)
                System.out.println("Returning to main menu.");
                break;

            default:
                System.out.println("Invalid choice. Please try again.");
        }
    }
}

/**
 * Prescription class to store detailof a medication prescription
 */
class Prescription {
    private String rxNumber;
    private String medicationName;
    private String times;

    public Prescription(String rxNumber, String medicationName, String times) {
        this.rxNumber = rxNumber;
        this.medicationName = medicationName;
        this.times = times;
    }

    public String getRxNumber() {
        return rxNumber;
    }

    public String getMedicationName() {
        return medicationName;
    }

    public String getTimes() {
        return times;
    }
}
