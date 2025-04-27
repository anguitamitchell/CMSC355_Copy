/**
 * Medical Adherence System
 * Sprint 1
 * CMSC 355 - Fundamentals of Software Engineering
 *
 */
import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        login(); //call in the login function
    }

    public static void login() {

        Authentication authentication = new Authentication();
        Scanner scr = new Scanner(System.in);

        while (true){
            System.out.println("\n1. Register\n2. Login\n3. Exit");
            System.out.println("Choose an option: ");
            String choice = scr.nextLine();

            if (choice.equals("1")){ //Register
                System.out.println("Enter username: ");
                String username = scr.nextLine();

                if (authentication.usernameAvail(username)) {
                    System.out.println("Enter password: ");
                    String password = scr.nextLine();
                    authentication.register(username, password);
                }
            }
            else if (choice.equals("2")){ //Login
                System.out.println("Enter username: ");
                String username = scr.nextLine();

                System.out.println("Enter password: ");
                String password = scr.nextLine();

                if (authentication.login(username,password)){
                    home();
                }
            }
            else { //Exit
                System.out.println("Goodbye!");
                break;
            }
        }
        scr.close();
    }

    /**
     * serves as home page
     */
    public static void home() {
        Scanner scr = new Scanner(System.in);

        while (true){
            System.out.println("\n1. Add Doctor Info \n2. Add Rx Info \n3. Log Medicine \n4. Pull Medicine Adherence Report \n5. Reminders \n6. Exit");
            System.out.println("Choose an option: ");
            String choice = scr.nextLine();

            if (choice.equals("1")){ //Add Doctor Info
                DoctorName.main(new String[]{});
            }
            else if (choice.equals("2")){ //Add Rx Info
                PrescriptionNumberVerification.main(new String[]{});
            }
            else if (choice.equals("3")){ //Log Medicine
                ValidateMedication.main(new String[] {});
            }
            else if (choice.equals("4")){ //Pull Med report
                MedicineReport.main(new String[]{});
            }
            else if (choice.equals("5")){ //Reminders
                ResponseTracker.trackResponse();
            }
            else { //Exit
                System.out.println("Goodbye!");
                break;
            }
        }
        scr.close();
    }
}
