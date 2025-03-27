import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class Authentication {

    private UserService userService;

    @Before
    public void setup() {
        userService = new UserService();
        userService.register("alice", "Secret123");
    }

    @Test
    public void testSuccessfulAuthentication() {
        assertTrue(userService.authenticate("alice", "Secret123"));
    }

    @Test
    public void testAuthenticationWithInvalidUsername() {
        assertFalse(userService.authenticate("bob", "Secret123"));
    }

    @Test
    public void testAuthenticationWithWrongPassword() {
        assertFalse(userService.authenticate("alice", "WrongPass"));
    }

    @Test
    public void testAuthenticationWithEmptyFields() {
        assertFalse(userService.authenticate("", ""));
    }

    @Test
    public void testAuthenticationAfterRegistration() {
        userService.register("newuser", "NewPass456");
        assertTrue(userService.authenticate("newuser", "NewPass456"));
    }
}
