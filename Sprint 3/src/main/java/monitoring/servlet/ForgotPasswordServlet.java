package monitoring.servlet;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.IOException;
import monitoring.UserService;

public class ForgotPasswordServlet extends HttpServlet {
    private final UserService userService = new UserService();

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        // Get new password from form
        HttpSession sesh = request.getSession(false);
        String password = request.getParameter("password");
        if(sesh!=null){
            userService.passwordUpdate((String) sesh.getAttribute("username"), password);
        }

        request.getRequestDispatcher("forgotPassword.jsp").forward(request, response);
    }

    

}
