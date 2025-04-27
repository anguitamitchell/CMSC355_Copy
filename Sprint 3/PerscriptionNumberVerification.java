import java.util.*;

class PrescriptionNumberVerification {

    // Stores prescriptions using Rx number as key
    private static Map<String, Prescription> rxStore = new HashMap<>();

    /**hod to manage adding and retrieving prescriptions
     */
    public static void addPrescriptions(String rxNumber,Prescription givenRx) {

        // Add a new prescription to the system
        rxStore.put(rxNumber,givenRx);
    }

    // Look up a prescription by Rx number
    public static String retrievePrescription(String givenRxNumber) {

        if (rxStore.containsKey(givenRxNumber)) {
            Prescription prescription = rxStore.get(givenRxNumber);
            return prescription.getMedicationName() + prescription.getTimes();
        } else {
            return "Rx number not found.";
        }
    }
}

/**
 * Prescription class to store detail of a medication prescription
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