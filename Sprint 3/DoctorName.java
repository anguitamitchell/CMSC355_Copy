import java.util.*;

public class DoctorName {

    // Static map to store doctor names and their associated medications
    public static Map<User, String> doctorMedications = new HashMap<>();

    /**
     * Lets users look up a doctor and either view their meds or add a new Rx number
     */
    public static void addDoctorInfo(User givenUser, String givenDoc) {

        User user = givenUser;
        String fullName = givenDoc;
        doctorMedications.put(user, fullName);

        // Check if the doctor exists in the system
        //if (doctorMedications.containsKey(fullName)) {
        //}
        // Check if doctor exists in the system
        // Show the list of medications this doctor prescribes
        // Allow user to \"add\" a new Rx number (this is just a placeholder message for now)
    }
}








