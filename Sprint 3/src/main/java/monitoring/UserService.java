package monitoring;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Reader;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

public class UserService {
    private Map<String, String> credentials = new HashMap<>();
    private Map<String, Account> userAccounts = new HashMap<>();
    private Map<String, Boolean> sessionStatus = new HashMap<>();
    private static final String FILE_PATH = "src/main/resources/accounts.json";
    private final Gson gson = new Gson();

    public UserService() {
        loadAccountsFromFile();
    }

    public boolean register(String username, String password, Account account) {
        if (!credentials.containsKey(username)) {
            credentials.put(username, password);
            userAccounts.put(username, account);
            sessionStatus.put(username, false);
            saveAccountsToFile();
            return true;
        }
        return false;
    }

    public boolean login(String username, String password) {
        return credentials.containsKey(username) && credentials.get(username).equals(password);
    }

    public boolean isUserLoggedIn(String username) {
        return sessionStatus.getOrDefault(username, false);
    }

    public void logout(String username) {
        sessionStatus.put(username, false);
    }

    public String getAdherenceData(String username) {
        if (isUserLoggedIn(username)) {
            return "Adherence data for " + username;
        }
        return null;
    }

    public String getRedirectPage(String username) {
        if (isUserLoggedIn(username)) {
            return "dashboard";
        }
        return "login";
    }

    private void saveAccountsToFile() {
        List<Account> accounts = new ArrayList<>(userAccounts.values());
        try (FileWriter writer = new FileWriter(FILE_PATH)) {
            gson.toJson(accounts, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void loadAccountsFromFile() {
        File file = new File(FILE_PATH);
        if (!file.exists()) return;
    
        try (Reader reader = new FileReader(file)) {
            Type listType = new TypeToken<List<Account>>() {}.getType();
            List<Account> accounts = gson.fromJson(reader, listType);
            if (accounts != null) {
                for (Account account : accounts) {
                    String username = account.getUsername();
                    credentials.put(username, account.getPassword());
                    userAccounts.put(username, account);
                    sessionStatus.put(username, false);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    private List<Account> loadAccounts() {
        List<Account> accounts = new ArrayList<>();
        File file = new File("src/main/resources/accounts.json");

        if (!file.exists()) {
            return accounts; // return empty list if file doesn't exist
        }

        try (Reader reader = new FileReader(file)) {
            Gson gson = new Gson();
            Type accountListType = new TypeToken<List<Account>>() {}.getType();
            accounts = gson.fromJson(reader, accountListType);
        } catch (IOException e) {
            e.printStackTrace();
        }

        return accounts;
    }

    public boolean authenticate(String username, String password) {
        List<Account> accounts = loadAccounts();
        for (Account acc : accounts) {
            if (acc.getUsername().equalsIgnoreCase(username) && acc.getPassword().equals(password)) {
                return true;
            }
        }
        return false;
    }
}