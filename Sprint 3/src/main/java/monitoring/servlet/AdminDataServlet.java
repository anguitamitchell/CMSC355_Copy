package monitoring.servlet;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import monitoring.Entry;

import java.io.*;
import java.lang.reflect.Type;
import java.util.*;

public class AdminDataServlet extends HttpServlet {

    private static final String ENTRIES_FILE = "src/main/resources/entries.json";

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String username = (String) request.getSession().getAttribute("username");
        System.out.println("AdminDataServlet: " + username);

        if (username == null) {
            request.getSession().invalidate();
            response.sendRedirect("login.jsp");
            return;
        }

        List<Entry> allEntries = loadEntries();
        request.setAttribute("entries", allEntries);
        request.getRequestDispatcher("adminData.jsp").forward(request, response);
    }

    private List<Entry> loadEntries() {
        try (Reader reader = new FileReader(ENTRIES_FILE)) {
            Type listType = new TypeToken<List<Entry>>() {}.getType();
            List<Entry> entries = new Gson().fromJson(reader, listType);
            return entries != null ? entries : new ArrayList<>();
        } catch (IOException e) {
            e.printStackTrace();
            return new ArrayList<>();
        }
    }
}
