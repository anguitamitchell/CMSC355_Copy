import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

import org.junit.Before;
import org.junit.Test;
import org.junit.validator.PublicClassValidator;

public class login {

    private UserService userService;

    @Before
   public void setup() {
        userService = new UserService();
        userService.register("johndoe", "Password123");
    }

    @Test
   public void testSuccessfulLogin() {
        assertTrue(userService.login("johndoe", "Password123"));
    }

    @Test
   public void testLoginWithInvalidUsername() {
        assertFalse(userService.login("notexist", "Password123"));
    }

    @Test
   public void testLoginWithIncorrectPassword() {
        assertFalse(userService.login("johndoe", "WrongPassword"));
    }

    @Test
   public void testLoginWithEmptyFields() {
        assertFalse(userService.login("", ""));
    }

    @Test
   public void testLoginAlreadyLoggedInSession() {
        assertTrue(userService.login("johndoe", "Password123"));
        assertTrue(userService.isUserLoggedIn("johndoe"));
        assertFalse(userService.login("johndoe", "Password123"));
    }

    @Test
   public void testRetrieveAdherenceDataAfterLogin() {
        assertTrue(userService.login("johndoe", "Password123"));
        String data = userService.getAdherenceData("johndoe");
        assertNotNull(data);
    }

    @Test
   public void testLoginRedirectsToCorrectPage() {
        assertTrue(userService.login("johndoe", "Password123"));
        String page = userService.getRedirectPage("johndoe");
        assertEquals("dashboard", page);
    }
}