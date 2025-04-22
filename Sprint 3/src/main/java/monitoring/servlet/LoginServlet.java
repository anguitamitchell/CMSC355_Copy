package monitoring.servlet;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.IOException;
import monitoring.UserService;

public class LoginServlet extends HttpServlet {
    private final UserService userService = new UserService();

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        // Get login credentials from form
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        // Check against stored accounts
        boolean success = userService.authenticate(username, password);
        if (success) {
            request.getSession().setAttribute("username", username);
            response.sendRedirect("dashboard");
        } else {
            request.setAttribute("error", "Invalid username or password.");
            request.getRequestDispatcher("login.jsp").forward(request, response);
        }
    }
}
