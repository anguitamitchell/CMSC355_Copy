import java.util.*;

public class DoctorName {

    // Static map to store doctor names and their associated medications
    private static Map<String, List<String>> doctorMedications = new HashMap<>();

    // Initialize with some sample doctor data (can later be replaced with real input)
    static {
        doctorMedications.put("John Smith", Arrays.asList("Aspirin", "Ibuprofen"));
        doctorMedications.put("Jane Doe", Arrays.asList("Paracetamol"));
    }

    /**
     * Adds doctor info or lets users view existing doctor prescriptions
     */
    public static void addDoctorInfo() {
        Scanner scanner = new Scanner(System.in);

        // Get doctor's full name from user
        System.out.print("Enter doctor's first name: ");
        String firstName = scanner.nextLine().trim();

        System.out.print("Enter doctor's last name: ");
        String lastName = scanner.nextLine().trim();

        String fullName = firstName + " " + lastName;

        // Check if the doctor exists in the system
        if (doctorMedications.containsKey(fullName)) {
            System.out.println("Doctor found: " + fullName);
            System.out.println("Menu Options:");
            System.out.println("1. View Medications");
            System.out.println("2. Enter a new Rx number");

            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Clear newline character

            switch (choice) {
                case 1:
                    // Show medications assigned to this doctor
                    System.out.println("Medications: " + doctorMedications.get(fullName));
                    break;

                case 2:
                    // Allow adding a new Rx number (future feature: link to Prescription module)
                    System.out.print("Enter new Rx number: ");
                    String rxNumber = scanner.nextLine();
                    System.out.println("Rx number " + rxNumber + " has been added."); // No storage yet
                    break;

                default:
                    System.out.println("Invalid choice.");
            }
        } else {
            System.out.println("Doctor not found in the system.");
        }
    }
}