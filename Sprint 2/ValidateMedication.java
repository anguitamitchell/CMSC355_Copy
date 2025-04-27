/** 
* Medication Vaildation System 
* 
* 3.1 and 3.2 */
import java.util.ArrayList;
import java.util.Scanner;
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
private ArrayList<ValidatingMedication> medications;
private ArrayList<String> userLogs;
private ArrayList<Integer> TimeInMinutes;


public MedicationLogging(){
    medications = new ArrayList<>();
    userLogs = new ArrayList<>();
    TimeInMinutes = new ArrayList<>();

    medications.add(new ValidatingMedication("Tylenol"));
    medications.add(new ValidatingMedication("Ibuprofen"));
    medications.add(new ValidatingMedication("Clartin"));
}
public void logMedication(){
    Scanner scan = new Scanner(System.in);
    System.out.println("Enter the name of the medication that was taken:");
    String medInput = scan.nextLine();
    boolean valid = false;
    for(ValidatingMedication med : medications){
        if(med.getNameofMedication().equalsIgnoreCase(medInput)){
            valid = true;
            System.out.println("Medicine Logged!");
            break;
        }
    }
    if (valid){
        System.out.println("Please enter the time the medicine was taken. Please enter the hour, minutes, then AM or PM. (Ex. 8:30)");
        int hour = scan.nextInt();
        String semicolon = scan.nextLine();
        int minute = scan.nextInt();
        String ending = scan.nextLine();
        int total = 0;
        if ((hour <= 12 && hour >= 1 && minute <= 59 && minute >= 0 && semicolon.equalsIgnoreCase(":")) && (ending.equalsIgnoreCase("AM")||ending.equalsIgnoreCase("PM"))){
            total = ConvertToMinutes(hour, minute, ending);
            TimeInMinutes.add(total);
            String TimeFormat = ConvertToTimeFormat(hour, minute, ending);
            ComplianceCheck(total);
            userLogs.add(TimeFormat);
            }
            else{
                System.out.println("Invaild time input.Please enter the correct time format.");
            }
        }
    }
    public int ConvertToMinutes(int hour, int minute, String ending){
        if (ending.equalsIgnoreCase("PM") && hour != 12 ){
        hour = hour + 12;
        }
        if (ending.equalsIgnoreCase("AM") && hour == 12 ){
            hour = 0;
            }
            return (hour * 60) + minute;
        }
        public String ConvertToTimeFormat(int hour, int mintue, String ending){
            String hourF = String.valueOf(hour);
            String minuteF = String.valueOf(mintue);
            return hourF + ":"+ minuteF + ending;
        }
        public void ComplianceCheck(int check){
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
        public static void main(String[] args){
            MedicationLogging app = new MedicationLogging();
            Scanner scan = new Scanner(System.in);
            app.logMedication();
            app.ShowHistory();
            System.out.println("Goodbye!");
        }  
}


