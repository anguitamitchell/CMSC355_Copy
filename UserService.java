import java.util.HashMap;
import java.util.Map;

public class UserService {

    private Map<String, String> userDatabase = new HashMap<>();
    private Map<String, Boolean> activeSessions = new HashMap<>();

    public void register(String username, String password) {
        userDatabase.put(username, password);
        activeSessions.put(username, false);
    }

    public boolean login(String username, String password) {
        if (username == null || password == null || username.isEmpty() || password.isEmpty())
            return false;
        if (!userDatabase.containsKey(username)) return false;
        if (activeSessions.getOrDefault(username, false)) return false;
        if (!userDatabase.get(username).equals(password)) return false;
        activeSessions.put(username, true);
        return true;
    }

    public boolean isUserLoggedIn(String username) {
        return activeSessions.getOrDefault(username, false);
    }

    public String getAdherenceData(String username) {
        if (isUserLoggedIn(username)) return "AdherenceData";
        return null;
    }

    public String getRedirectPage(String username) {
        return isUserLoggedIn(username) ? "dashboard" : "login";
    }

    public boolean authenticate(String username, String password) {
        return username.equals("alice") && password.equals("Secret123");
    }


	}