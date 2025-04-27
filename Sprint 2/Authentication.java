/**
 * Medical Adherence System
 * Sprint 1
 * CMSC 355 - Fundamentals of Software Engineering
 *
 */

import java.util.HashMap;

public class Authentication {
    private HashMap<String, User> users;

    //creates hashmap using current user
    public Authentication(){
        this.users = new HashMap<>();
    }

    /**
     * Checks availability of username
     * @param username
     * @return false if username is taken, true if username is available
     */
    public boolean usernameAvail(String username){
        if(users.containsKey(username)){
            System.out.println("Username already taken.");
            return false;
        }
        else {
            return true;
        }
    }

    public boolean register(String username, String password) {
        if (users.containsKey(username)) {
            System.out.println("Username already taken.");
            return false;
        }
        users.put(username, new User(username,password));
        System.out.println("User registerd successfully!");
        return true;
    }

    public boolean login(String username, String password) {
        if (!users.containsKey(username)){
            System.out.println("User not found");
            return false;
        }
        User user = users.get(username);
        if (user.checkPassword(password)) {
            System.out.println("login successful!");
            return true;
        }
        else {
            System.out.println("Incorrect password.");
            return false;
        }
    }

}
