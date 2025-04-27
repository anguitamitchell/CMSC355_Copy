import javax.swing.*;
import java.awt.*;
import java.util.List;

public class Main extends JFrame{
    private CardLayout cardLayout; //organizes multiple pages
    private JPanel mainPanel;//main panel

    Authentication auth = new Authentication(); //calls authentication method
    User user = new User(); //creates a new user
    MedicationLogging app = new MedicationLogging();

    /*
    * Main method that navigates the app
    *
     */
    public Main() {
        setTitle("Medical Adherence System");
        setSize(500, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        cardLayout = new CardLayout();
        mainPanel = new JPanel(cardLayout);
        mainPanel.setBackground(new Color(173, 216, 230));
        mainPanel.add(createWelcomePanel(), "Welcome");
        mainPanel.add(createRegisterPanel(), "Register");
        mainPanel.add(createLoginPanel(), "Login");
        mainPanel.add(createDashboardPanel(), "Dashboard");
        mainPanel.add(createDoctorPanel(), "AddDoctor");
        mainPanel.add(createPrescriptionPanel(),"PrescriptionHome");
        mainPanel.add(createAddPrescriptionPanel(), "AddPrescription");
        mainPanel.add(createRetrievePrescriptionPanel(),"RetrieveMeds");
        mainPanel.add(createLogMedicationPanel(), "LogMedication");
        mainPanel.add(createReminderPanel(), "Reminder");
        mainPanel.add(createReportPanel(), "ComplianceReport");

        add(mainPanel);
        cardLayout.show(mainPanel, "Welcome");
    }

    /*
    * Creates buttons
     */
    private JButton styledButton(String text, Runnable action) {
        JButton button = new JButton(text);
        button.setFont(new Font("Arial", Font.PLAIN, 14));
        button.setMaximumSize(new Dimension(200, 40));
        button.setAlignmentX(Component.CENTER_ALIGNMENT);
        button.addActionListener(e -> action.run());
        return button;
    }

    //Welcome Page
    private JPanel createWelcomePanel() {
        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        panel.setBorder(BorderFactory.createEmptyBorder(40, 40, 40, 40));
        panel.setBackground(new Color(173, 216, 230));

        JLabel label = new JLabel("Welcome to the Medical Adherence System");
        label.setFont(new Font("Arial", Font.BOLD, 18));
        label.setAlignmentX(Component.CENTER_ALIGNMENT);

        panel.add(label);
        panel.add(Box.createRigidArea(new Dimension(0, 40)));
        panel.add(styledButton("Register", () -> cardLayout.show(mainPanel, "Register")));
        panel.add(Box.createRigidArea(new Dimension(0, 20)));
        panel.add(styledButton("Login", () -> cardLayout.show(mainPanel, "Login")));

        return panel;
    }

    //Register Page
    private JPanel createRegisterPanel() {
        JPanel panel = new JPanel(new GridLayout(7, 2, 10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        panel.setBackground(new Color(173, 216, 230));

        panel.add(new JLabel("First Name:"));
        panel.add(new JTextField());
        panel.add(new JLabel("Last Name:"));
        panel.add(new JTextField());
        panel.add(new JLabel("Phone:"));
        panel.add(new JTextField());
        panel.add(new JLabel("Email:"));
        JTextField emailReg = new JTextField();
        panel.add(emailReg);
        panel.add(new JLabel("Password:"));
        JTextField passwordReg = new JTextField();
        panel.add(passwordReg);

        panel.add(styledButton("Confirm", () -> {

            if (auth.usernameAvail(emailReg.getText())) {
                auth.register(emailReg.getText(), passwordReg.getText());
                user.setUsername(emailReg.getText());
                cardLayout.show(mainPanel, "Login");
            }
            else {
                JOptionPane.showMessageDialog(panel, "Invalid Credentials");
            }
        }));

        panel.add(styledButton("Back", () -> cardLayout.show(mainPanel, "Welcome")));

        return panel;
    }

    //Login Page
    private JPanel createLoginPanel() {
        JPanel panel = new JPanel(new GridLayout(3, 2, 10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        panel.setBackground(new Color(173, 216, 230));

        panel.add(new JLabel("Email:"));
        JTextField emailLog = new JTextField();
        panel.add(emailLog);
        panel.add(new JLabel("Password:"));
        JTextField passwordLog = new JTextField();
        panel.add(passwordLog);

        panel.add(styledButton("Confirm", () -> {
            user.setUsername(emailLog.getText().trim());

            if (auth.login(emailLog.getText().trim(),passwordLog.getText().trim()) == true)
            {
                cardLayout.show(mainPanel, "Dashboard");
            } else {
                JOptionPane.showMessageDialog(panel, "Invalid Credentials");
            }
        }));

        panel.add(styledButton("Back", () -> cardLayout.show(mainPanel, "Welcome")));
        return panel;
    }

    //Dashboard
    private JPanel createDashboardPanel() {
        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        panel.setBorder(BorderFactory.createEmptyBorder(30, 40, 30, 40));
        panel.setBackground(new Color(173, 216, 230));

        panel.add(styledButton("Add Doctor Information", () -> cardLayout.show(mainPanel, "AddDoctor")));
        panel.add(Box.createRigidArea(new Dimension(0, 10)));
        panel.add(styledButton("Prescription Information", () -> cardLayout.show(mainPanel, "PrescriptionHome")));
        panel.add(Box.createRigidArea(new Dimension(0, 10)));
        panel.add(styledButton("Log Medication", () -> cardLayout.show(mainPanel, "LogMedication")));
        panel.add(Box.createRigidArea(new Dimension(0, 10)));
        JButton reminderButton = styledButton("Reminders", () -> cardLayout.show(mainPanel, "Reminder")); // <-- ADD THIS
        panel.add(reminderButton);
        panel.add(Box.createRigidArea(new Dimension(0, 10)));
        panel.add(styledButton("Request Compliance Report", () -> cardLayout.show(mainPanel, "ComplianceReport")));
        panel.add(Box.createRigidArea(new Dimension(0, 10)));
        panel.add(styledButton("Logout", () -> cardLayout.show(mainPanel, "Welcome")));

        return panel;
    }

    //Doctor Page
    private JPanel createDoctorPanel() {
        JPanel panel = new JPanel(new GridLayout(5, 2, 10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        panel.setBackground(new Color(173, 216, 230));

        panel.add(new JLabel("Doctor Name:"));
        JTextField docName = new JTextField();
        panel.add(docName);
        panel.add(new JLabel("Phone:"));
        JTextField phoneNum = new JTextField();
        panel.add(phoneNum);
        panel.add(new JLabel("Email:"));
        JTextField emailDoc = new JTextField();
        panel.add(emailDoc);

        panel.add(styledButton("Confirm", () -> {
            user.setDoctor(docName.getText());
            DoctorName.addDoctorInfo(user,user.getDoctor());
            user.setDocPhone(phoneNum.getText());
            user.setDocEmail(emailDoc.getText());
            cardLayout.show(mainPanel, "Dashboard");
        }));
        panel.add(styledButton("Back to Dashboard", () -> cardLayout.show(mainPanel, "Dashboard")));

        return panel;
    }

    //Rx Page
    private JPanel createPrescriptionPanel(){
        JPanel panel = new JPanel(new GridLayout(3, 2, 10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        panel.setBackground(new Color(173, 216, 230));

        panel.add(styledButton("Add Prescription", () -> cardLayout.show(mainPanel, "AddPrescription")));
        panel.add(styledButton("Retrieve Medication", () -> cardLayout.show(mainPanel,"RetrieveMeds")));
        panel.add(styledButton("Back to Dashboard", () -> cardLayout.show(mainPanel, "Dashboard")));

        return panel;
    }

    //Add Rx Page
    private JPanel createAddPrescriptionPanel() {
        JPanel panel = new JPanel(new GridLayout(7, 2, 10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        panel.setBackground(new Color(173, 216, 230));

        panel.add(new JLabel("Rx Number:"));
        JTextField rxNumberField = new JTextField();
        panel.add(rxNumberField);
        panel.add(new JLabel("Medication Name:"));
        JTextField medNameField = new JTextField();
        panel.add(medNameField);
        panel.add(new JLabel("Frequency:"));
        JTextField frequencyField = new JTextField();
        panel.add(frequencyField);
        panel.add(new JLabel("Doctor Name:"));
        JTextField docNameField = new JTextField();
        panel.add(docNameField);

        panel.add(styledButton("Confirm", () -> {
            Prescription prescription = new Prescription(rxNumberField.getText(),medNameField.getText(),frequencyField.getText());
            PrescriptionNumberVerification.addPrescriptions(rxNumberField.getText(), prescription);
            cardLayout.show(mainPanel, "PrescriptionHome");
        }));
        panel.add(styledButton("Back to Dashboard", () -> cardLayout.show(mainPanel, "PrescriptionHome")));

        return panel;
    }

    //Retrieve Rx Page
    private JPanel createRetrievePrescriptionPanel() {
        JPanel panel = new JPanel(new GridLayout(3, 2, 10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        panel.setBackground(new Color(173, 216, 230));

        panel.add(new JLabel("Enter Rx Number:"));
        JTextField rxNumberField = new JTextField();
        panel.add(rxNumberField);

        panel.add(new JLabel("Medication: "));
        JTextField foundMeds = new JTextField();
        panel.add(foundMeds);

        panel.add(styledButton("Confirm", () -> {
            String medStats = PrescriptionNumberVerification.retrievePrescription(rxNumberField.getText());
            foundMeds.setText(medStats);
        }));
        panel.add(styledButton("Back to Dashboard", () -> cardLayout.show(mainPanel, "PrescriptionHome")));

        return panel;
    }

    //Log Medication Page
    private JPanel createLogMedicationPanel() {
        JPanel panel = new JPanel(new GridLayout(5, 2, 10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        panel.setBackground(new Color(173, 216, 230));

        panel.add(new JLabel("Medication Name:"));
        JTextField medNameField = new JTextField();
        panel.add(medNameField);

        panel.add(new JLabel("Hour (1-12):"));
        JTextField hourField = new JTextField();
        panel.add(hourField);

        panel.add(new JLabel("Minute (0-59):"));
        JTextField minuteField = new JTextField();
        panel.add(minuteField);

        panel.add(new JLabel("AM or PM:"));
        JTextField ampmField = new JTextField();
        panel.add(ampmField);

        panel.add(styledButton("Confirm", () -> {
            // Get user inputs
            String medName = medNameField.getText();
            int hour = Integer.parseInt(hourField.getText());
            int minute = Integer.parseInt(minuteField.getText());
            String ampm = ampmField.getText();

            MedicationLogging.logMedication(medName, hour, minute, ampm);

            cardLayout.show(mainPanel, "Dashboard");
        }));

        panel.add(styledButton("Back to Dashboard", () -> cardLayout.show(mainPanel, "Dashboard")));

        return panel;
    }

    //create Reports
    private JPanel createReportPanel() {
        JPanel panel = new JPanel(new BorderLayout());
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        panel.setBackground(new Color(230, 230, 250));

        JTextArea reportArea = new JTextArea();
        reportArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(reportArea);
        panel.add(scrollPane, BorderLayout.CENTER);

        JPanel controls = new JPanel(new GridLayout(2, 2, 10, 10));

        JTextField nameField = new JTextField();
        JTextField scheduleField = new JTextField();
        JTextField adherenceField = new JTextField();
        JTextField sideEffectsField = new JTextField();

        controls.add(new JLabel("Name:"));
        controls.add(nameField);
        controls.add(new JLabel("Schedule:"));
        controls.add(scheduleField);
        controls.add(new JLabel("Adherence:"));
        controls.add(adherenceField);
        controls.add(new JLabel("Side Effects:"));
        controls.add(sideEffectsField);

        panel.add(controls, BorderLayout.NORTH);

        JPanel buttonPanel = new JPanel();

        buttonPanel.add(styledButton("View Report", () -> ReportSystem.generateReport(user, reportArea)));
        buttonPanel.add(styledButton("Add Medicine", () -> {
            ReportSystem.addMedicine(
                    nameField.getText(),
                    scheduleField.getText(),
                    adherenceField.getText(),
                    sideEffectsField.getText()
            );
            reportArea.setText("Medicine added successfully!\n");
        }));
        buttonPanel.add(styledButton("Remove Medicine", () -> {
           ReportSystem.removeMedicine(nameField.getText());
            reportArea.setText("Medicine removed successfully!\n");
        }));
        buttonPanel.add(styledButton("Back to Dashboard", () -> cardLayout.show(mainPanel, "Dashboard")));

        panel.add(buttonPanel, BorderLayout.SOUTH);

        return panel;
    }

    //Reminder Page
    private JPanel createReminderPanel() {
        JPanel panel = new JPanel(new BorderLayout());
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        panel.setBackground(new Color(250, 250, 210));

        ReminderService reminderService = new ReminderService();

        JTextArea reminderArea = new JTextArea();
        reminderArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(reminderArea);
        panel.add(scrollPane, BorderLayout.CENTER);

        JPanel inputPanel = new JPanel(new GridLayout(2, 2, 10, 10));
        JTextField userField = new JTextField();
        JTextField medField = new JTextField();

        inputPanel.add(new JLabel("Username:"));
        inputPanel.add(userField);
        inputPanel.add(new JLabel("Medication:"));
        inputPanel.add(medField);

        panel.add(inputPanel, BorderLayout.NORTH);

        JPanel buttonPanel = new JPanel();

        buttonPanel.add(styledButton("Add Reminder", () -> {
            reminderService.addReminder(userField.getText(), medField.getText());
            reminderArea.setText("Reminder added successfully!\n");
        }));

        buttonPanel.add(styledButton("Send Reminders", () -> {
            StringBuilder output = new StringBuilder();
            List<Reminder> reminders = reminderService.getReminders();

            for (Reminder r : reminders) {
                if (!r.isAcknowledged()) {
                    output.append("Reminder for ").append(r.getUsername())
                            .append(": Take ").append(r.getMedication()).append("\n");
                }
            }

            if (output.length() == 0) {
                reminderArea.setText("No pending reminders.\n");
            } else {
                reminderArea.setText(output.toString());
            }
        }));

        buttonPanel.add(styledButton("Acknowledge Reminder", () -> {
            String username = userField.getText();
            String medication = medField.getText();
            boolean found = false;

            for (Reminder r : reminderService.getReminders()) {
                if (r.getUsername().equalsIgnoreCase(username) &&
                        r.getMedication().equalsIgnoreCase(medication) &&
                        !r.isAcknowledged()) {
                    r.acknowledge();
                    reminderArea.setText("Reminder acknowledged!\n");
                    found = true;
                    break;
                }
            }

            if (!found) {
                reminderArea.setText("No matching pending reminder found.\n");
            }
        }));

        buttonPanel.add(styledButton("Back to Dashboard", () -> cardLayout.show(mainPanel, "Dashboard")));

        panel.add(buttonPanel, BorderLayout.SOUTH);

        return panel;
    }

    //Runs the program
    public static void main(String[] args) {
        Main window = new Main();
        window.setVisible(true);
    }

}
