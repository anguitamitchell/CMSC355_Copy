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
        String admin = "admin";

        // Check against stored accounts
        boolean success = userService.authenticate(username, password);
        if (success) {
            request.getSession().setAttribute("username", username);
            request.getSession().setAttribute("userType", userService.getAccountData(username, "userType"));
            if (admin.equals((String) request.getSession().getAttribute("userType"))) {
                response.sendRedirect("adminData");
            } else {
                response.sendRedirect("dashboard.jsp");
            }
            
        } else {
            request.setAttribute("error", "Invalid username or password.");
            request.getRequestDispatcher("login.jsp").forward(request, response);
        }
    }

    

}
