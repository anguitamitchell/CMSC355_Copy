import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;

public class Authentication {
    private HashMap<String, String> users; // Stores username -> hashed password

    public Authentication() {
        this.users = new HashMap<>();
    }

    /**
     * Checks availability of username
     * @param username the username to check
     * @return true if available, false if taken
     */
    public boolean usernameAvail(String username) {
        return !users.containsKey(username);
    }

    /**
     * Registers a new user
     * @param username username
     * @param password password
     * @return true if successful, false if username already taken
     */
    public boolean register(String username, String password) {
        if (users.containsKey(username)) {
            System.out.println("Username already taken.");
            return false;
        }
        String hashed = hashPassword(password);
        users.put(username, hashed);
        System.out.println("User registered successfully!");
        return true;
    }

    /**
     * Attempts to log in
     * @param username username
     * @param password password
     * @return true if login successful, false otherwise
     */
    public boolean login(String username, String password) {
        if (!users.containsKey(username)) {
            System.out.println("User not found.");
            return false;
        }
        String storedHashedPassword = users.get(username);
        String inputHashedPassword = hashPassword(password);

        if (storedHashedPassword.equals(inputHashedPassword)) {
            System.out.println("true");
            return true;
        } else {
            return false;
        }
    }

    /**
     * Hashes a password using SHA-256
     * @param password the password to hash
     * @return hashed password as a hex string
     */
    private String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(password.getBytes());
            StringBuilder hexString = new StringBuilder();

            for (byte b : hash) {
                hexString.append(String.format("%02x", b));
            }
            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Error hashing password", e);
        }
    }
}
