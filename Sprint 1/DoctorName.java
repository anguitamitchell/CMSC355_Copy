import java.util.*;

public class DoctorName {
    private static Map<String, List<String>> doctorMedications = new HashMap<>();
    
    public static void main(String[] args) {
        // test data
        doctorMedications.put("John Smith", Arrays.asList("Aspirin", "Ibuprofen"));
        doctorMedications.put("Jane Doe", Arrays.asList("Paracetamol"));
        
        Scanner scanner = new Scanner(System.in);
        
        // Get doctor name from user
        System.out.print("Enter doctor's first name: ");
        String firstName = scanner.nextLine().trim();
        
        System.out.print("Enter doctor's last name: ");
        String lastName = scanner.nextLine().trim();
        
        String fullName = firstName + " " + lastName;
        
        if (doctorMedications.containsKey(fullName)) {
            System.out.println("Doctor found: " + fullName);
            System.out.println("Menu Options:");
            System.out.println("1. View Medications");
            System.out.println("2. Enter a new Rx number");
            
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); //newline
            
            switch (choice) {
                case 1:
                    System.out.println("Medications: " + doctorMedications.get(fullName));
                    break;
                case 2:
                    System.out.print("Enter new Rx number: ");
                    String rxNumber = scanner.nextLine();
                    System.out.println("Rx number " + rxNumber + " has been added.");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        } else {
            System.out.println("Doctor not found in the system.");
        }
        
        scanner.close();
    }
}