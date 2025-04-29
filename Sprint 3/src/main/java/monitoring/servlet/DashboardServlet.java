package monitoring.servlet;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.IOException;

public class DashboardServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        System.out.println("ping");
        if (session == null || session.getAttribute("username") == null) {
            request.getSession().invalidate();
            response.sendRedirect("login.jsp");
            return;
        }

        request.getRequestDispatcher("dashboard.jsp").forward(request, response);
    }
}