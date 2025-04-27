/**
 * Medical Adherence System
 * Sprint 1
 * CMSC 355 - Fundamentals of Software Engineering
 *
 */
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class User {
    private String username;
    private String hashedPassword;

    public User(String username, String password){
        this.username = username;
        this.hashedPassword = hashPassword(password);
    }

    public String getUsername(){
        return username;
    }

    public String getHashedPassword() {
        return hashedPassword;
    }

    private String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(password.getBytes());
            StringBuilder hexString = new StringBuilder();

            for (byte b : hash){
                hexString.append(String.format("%02x",b));
            }
            return hexString.toString();
        }
        catch (NoSuchAlgorithmException e){
            throw new RuntimeException("Error hashing password", e);
        }
    }

    public boolean checkPassword(String password){
        return this.hashedPassword.equals(hashedPassword(password));
    }

    private String hashedPassword(String password) {
        return this.hashedPassword;
    }
}
