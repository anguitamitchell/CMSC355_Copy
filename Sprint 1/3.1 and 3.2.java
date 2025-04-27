/* Medication Vaildation System 3.1 and 3.2 */
import java.util;
import java.util.HashMap;
import java.util.Scanner;

public class ValidateMedication {
    private static final HashMap<String, Boolean> vaildMeds = new HashMap<>();
static {
    validMeds.put("Tyelnol", true);
}
public class TimeMedsTaken{
    private static final HashMap<String, Boolean> TimeVal = new HashMap<>();

static {
    TimeVal.put("2:00 PM", true);
}
}
}

public static void main(String[] args) {
Scanner scan = new Scanner(System.in);
System.out.println("Enter Medication name");
String input = scan.nextLine();
if (validMeds(input)){
    System.out.println("Medication Logged: Confirmed");
    System.out.println("Enter the time the medication was taken");
    String inputtime = scan.nextLine();
    if (TimeVal(inputtime)){
        System.out.println("Medication Time Logged: Confirm Positive Status");
    } else{
        System.out.println("Medication Time Logged: Confirm Negative Status");
    }
} else {
    System.out.println("Input was incorrect. Please Try Again");
}

}