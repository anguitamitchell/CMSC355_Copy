/**
 * Medical Adherence System
 * Sprint 1
 * CMSC 355 - Fundamentals of Software Engineering
 *
 */
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class User {
    private String username = null;
    private String doctor = null;
    private String docPhone = null;
    private String docEmail = null;

    public User(){
        this.username = null;
    }

    public String getUsername(){
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setDoctor(String doctor) {
        this.doctor = doctor;
    }

    public String getDoctor() {
        return doctor;
    }

    public String getDocPhone() {
        return docPhone;
    }

    public void setDocPhone(String docPhone) {
        this.docPhone = docPhone;
    }

    public String getDocEmail() {
        return docEmail;
    }

    public void setDocEmail(String docEmail) {
        this.docEmail = docEmail;
    }
}
