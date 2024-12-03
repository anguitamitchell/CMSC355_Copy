package src;

import java.sql.SQLException;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void showmenu1() throws SQLException {
        Scanner scanner = new Scanner(System.in);
        String choice;
        do {
            System.out.printf("-------------Main Menu---------------\n");
            System.out.printf("What search would you like? \n");
            System.out.printf("1. Basic search...\n");
            System.out.printf("2. Advanced search...\n");
            System.out.printf("3. Print all Patients...\n");
            System.out.printf("4. Call a doctor...\n");
            System.out.printf("9. Exit\n");

            choice = scanner.nextLine();

            if (choice.equalsIgnoreCase("1")) {
                System.out.printf("--------Basic Search-------------\n");
                System.out.printf("Enter patient first name...\n");
                String firstName = scanner.nextLine();
                System.out.printf("Enter patient last name...\n");
                String lastName = scanner.nextLine();
                String[] patientNames = basicPatientSearch(firstName, lastName);
                if (patientNames.length == 0) {
                    System.out.printf("No patients found with that name.\n");
                } else {
                    System.out.printf("Patients found:\n");
                    for (String name : patientNames) {
                        System.out.println(name);
                    }
                }
            } else if (choice.equalsIgnoreCase("2")) {
                showmenu2();
            } else if (choice.equalsIgnoreCase("3")) {
                List<PatientType> patients = PatientDBService.getAllPatients();
                int start = 0;
                int end = Math.min(100, patients.size());
                scanner = new Scanner(System.in);

                while (start < patients.size()) {
                    for (int i = start; i < end; i++) {
                        PatientType patient = patients.get(i);
                        System.out.println(patient.getPatientFName() + " " + patient.getPatientLName());
                    }
                    if (end == patients.size()) {
                        break;
                    }
                    System.out.println("Press Enter to see the next 100 patients...");
                    scanner.nextLine();
                    start = end;
                    end = Math.min(end + 100, patients.size());
                }
            } else if (choice.equalsIgnoreCase("4")) {
                System.out.printf("Calling doctor on call");
                callingDr();
            }
        } while (!(choice.equals("9")));
    }

    public static void showmenu2() throws SQLException {
        Scanner scanner = new Scanner(System.in);
        String choice;

        do {
            System.out.printf("--------Advanced Search-------------\n");
            System.out.printf("Search by... \n");
            System.out.printf("1. Room number \n");
            System.out.printf("2. Medical Record Number \n");
            System.out.printf("3. Admission Date \n");
            System.out.printf("4. Primary Care Provider \n");
            System.out.printf("9. Exit \n");
            choice = scanner.nextLine();
            String[] patientNames = new String[0];

            if (choice.equalsIgnoreCase("1")) {
                System.out.printf("Enter the room\n");
                String room = scanner.nextLine();
                patientNames = roomSearch(room);
            } else if (choice.equalsIgnoreCase("2")) {
                System.out.printf("Enter the MRN\n");
                String MRN = scanner.nextLine();
                patientNames = mrnSearch(MRN);
            } else if (choice.equalsIgnoreCase("3")) {
                System.out.printf("Enter the Admission Date in day, month, year \n");
                int addDay = scanner.nextInt();
                int addMonth = scanner.nextInt();
                int addYear = scanner.nextInt();
                scanner.nextLine(); // Consume the newline character
                patientNames = admissionDateSearch(addDay, addMonth, addYear);
            } else if (choice.equalsIgnoreCase("4")) {
                System.out.printf("Enter the PCP\n");
                String PCP = scanner.nextLine();
                patientNames = pcpSearch(PCP);
            }

            if (patientNames.length == 0) {
                System.out.printf("No patients found.\n");
            } else {
                System.out.printf("Patients found:\n");
                for (String name : patientNames) {
                    System.out.println(name);
                }
            }
        } while (!(choice.equals("9")));
    }

    public static void callingDr() {
        for (int i = 0; i < 3; i++) {
            try {
                Thread.sleep(900);
            } catch (InterruptedException e) {
                System.err.println("Interrupted: " + e.getMessage());
            }
            System.out.printf(".");
            if (i == 2)
                System.out.printf("\n");
        }
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            System.err.println("Interrupted: " + e.getMessage());
        }
        System.out.println("But no one answered...");
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            System.err.println("Interrupted: " + e.getMessage());
        }
        System.out.println("Good luck lol");
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            System.err.println("Interrupted: " + e.getMessage());
        }
    }

    public static String[] basicPatientSearch(String fname, String lname) throws SQLException {
        List<PatientType> patients = PatientDBService.searchPatientName(fname, lname);
        String[] patientNames = new String[patients.size()];

        if (!patients.isEmpty()) {
            for (int i = 0; i < patients.size(); i++) {
                PatientType patient = patients.get(i);
                String fullname = patient.getPatientFName() + " " + patient.getPatientLName() + " " + patient.getMRN();
                patientNames[i] = fullname;
            }
        }
        return patientNames;
    }

    public static String[] roomSearch(String roomNum) throws SQLException {
        List<PatientType> patients = PatientDBService.searchPatientByRoom(roomNum);
        String[] patientNames = new String[patients.size()];

        if (!patients.isEmpty()) {
            for (int i = 0; i < patients.size(); i++) {
                PatientType patient = patients.get(i);
                String fullname = patient.getPatientFName() + " " + patient.getPatientLName() + " " + patient.getMRN();
                patientNames[i] = fullname;
            }
        }
        return patientNames;
    }

    public static String[] mrnSearch(String MRN) throws SQLException {
        List<PatientType> patients = PatientDBService.searchPatientsByMRN(MRN);
        String[] patientNames = new String[patients.size()];

        if (!patients.isEmpty()) {
            for (int i = 0; i < patients.size(); i++) {
                PatientType patient = patients.get(i);
                String fullname = patient.getPatientFName() + " " + patient.getPatientLName() + " " + patient.getMRN();
                patientNames[i] = fullname;
            }
        }
        return patientNames;
    }

    public static String[] pcpSearch(String PCP) throws SQLException {
        List<PatientType> patients = PatientDBService.searchPatientByPCP(PCP);
        String[] patientNames = new String[patients.size()];
        if (!patients.isEmpty()) {
            for (int i = 0; i < patients.size(); i++) {
                PatientType patient = patients.get(i);
                String fullname = patient.getPatientFName() + " " + patient.getPatientLName() + " " + patient.getMRN();
                patientNames[i] = fullname;
            }
        }
        return patientNames;
    }

    public static String[] admissionSearch(String search) throws SQLException {
        List<PatientType> patients = PatientDBService.searchPatientAdmissionDate(search);
        String[] patientNames = new String[patients.size()];
        if (!patients.isEmpty()) {
            for (int i = 0; i < patients.size(); i++) {
                PatientType patient = patients.get(i);
                String fullname = patient.getPatientFName() + " " + patient.getPatientLName() + " " + patient.getMRN();
                patientNames[i] = fullname;
            }
        }
        return patientNames;
    }

    public static String[] admissionDateSearch(int day, int month, int year) throws SQLException {
        String search = year + "-" + (month < 10 ? "0" + month : month) + "-" + (day < 10 ? "0" + day : day);
        return admissionSearch(search);
    }

    public static String[] ptnSelected(String ptn) throws SQLException {
        String parts[] = ptn.split(" ",3);
        if (parts.length < 3) {
            throw new IllegalArgumentException("Input string does not contain enough parts");
        }
        String mrn = parts[2];
        //PatientType patient = mrnSearch(mrn);
        List<PatientType> patients = PatientDBService.searchPatientsByMRN(mrn);
        PatientType newpatient = null;
        if (!patients.isEmpty()) {
            newpatient = patients.get(0);
        }
        String ptnInfo[] = new String[6];
        if (newpatient != null) {
            ptnInfo[0] = newpatient.getPatientLName() + " " + newpatient.getPatientFName();
            ptnInfo[1] = newpatient.getMRN();
            ptnInfo[2] = newpatient.getRoomNumber();
            ptnInfo[3] = newpatient.getPcpString();
            ptnInfo[4] = newpatient.getDiagnosis();
            ptnInfo[5] = newpatient.getGender();
        }
        return ptnInfo;
    }

    public static String[] searchSelect(String searchType, String searchParam) throws SQLException {
        switch (searchType) {
            case "Last Name First Name":
                String parts[] = searchParam.split(" ", 2);
                String lastName = parts[0];
                String firstName = parts[1];
                return basicPatientSearch(firstName, lastName);
            case "Room Number":
                return roomSearch(searchParam);
            case "Medical Record Number":
                return mrnSearch(searchParam);
            case "Primary Care Provider ":
                return pcpSearch(searchParam);
            case "Admission Date":
                return admissionSearch(searchParam);
            default:
                return null;
        }
    }

    public static void main(String[] args) throws SQLException {
        PatientType patient = new PatientType();
        showmenu1();
    }
}