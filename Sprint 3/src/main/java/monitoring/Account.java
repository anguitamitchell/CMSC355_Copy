package monitoring;

public class Account {
    private String firstName;
    private String lastName;
    private String username;
    private String email;
    private String dob;
    private String password;
    private String userType;

    public Account(String firstName, String lastName, String username, String email, String dob, String password, String userType) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.username = username;
        this.email = email;
        this.dob = dob;
        this.password = password;
        this.userType = userType;
    }

    public String getUsername() {
        return username;
    }

    public String getEmail() {
        return email;
    }

    public String getDob() {
        return dob;
    }

    public String getFullName() {
        return firstName + " " + lastName;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String newPass){
        this.password = newPass;
        return;
    }

    public String getUserType() {
        return userType;
    }
}
