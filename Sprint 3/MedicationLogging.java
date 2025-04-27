/**
* Medication Vaildation System 
* 
* 3.1 and 3.2 */

import java.util.ArrayList;

class ValidatingMedication {
    private String nameOfMedication;

    public ValidatingMedication(String name) {
        this.nameOfMedication = name;
    }

    public String getNameofMedication() {
        return nameOfMedication;
    }
}
public class MedicationLogging{
public static ArrayList<ValidatingMedication> medications;
private static ArrayList<String> userLogs;
private static ArrayList<Integer> TimeInMinutes;

    public MedicationLogging(){
    medications = new ArrayList<>();
    userLogs = new ArrayList<>();
    TimeInMinutes = new ArrayList<>();
}
    public static void logMedication(String medInput, int hour, int minute, String ending) {
        boolean valid = false;
        for (ValidatingMedication med : medications) {
            if (med.getNameofMedication().equalsIgnoreCase(medInput)) {
                valid = true;
                System.out.println("Medicine Logged!");
                break;
            }
        }

        if (valid) {
            int total = 0;
            if ((hour <= 12 && hour >= 1 && minute <= 59 && minute >= 0) && (ending.equalsIgnoreCase("AM") || ending.equalsIgnoreCase("PM"))) {
                total = ConvertToMinutes(hour, minute, ending);
                TimeInMinutes.add(total);
                String TimeFormat = ConvertToTimeFormat(hour, minute, ending);
                ComplianceCheck(total);
                userLogs.add(TimeFormat);
            } else {
                System.out.println("Invalid time input. Please enter the correct time format.");
            }
        } else {
            System.out.println("Medication name not recognized.");
        }
    }

    public static int ConvertToMinutes(int hour, int minute, String ending){
        if (ending.equalsIgnoreCase("PM") && hour != 12 ){
        hour = hour + 12;
        }
        if (ending.equalsIgnoreCase("AM") && hour == 12 ){
            hour = 0;
            }
            return (hour * 60) + minute;
        }
        public static String ConvertToTimeFormat(int hour, int mintue, String ending){
            String hourF = String.valueOf(hour);
            String minuteF = String.valueOf(mintue);
            return hourF + ":"+ minuteF + ending;
        }
        public static void ComplianceCheck(int check){
            if(!TimeInMinutes.isEmpty()){
                int previous = TimeInMinutes.get(TimeInMinutes.size()-1);
                int difference = Math.abs(check - previous);
                if (difference > 30){
                    System.out.println("Not Compliant: Medication was not taken on time your doctor will be notified.");
                } else {
                    System.out.println("Compliant: Medication taken on time. ");
                }
            }
            
        }
        public void ShowHistory(){
            if (userLogs.isEmpty()){
                System.out.println("No times have not been logged yet.");
            }else{
                System.out.println("Times that are logged:");
                for (String timestamps : userLogs){
                    System.out.println(timestamps);
                }
            }
        }
}



