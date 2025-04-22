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
import java.util.stream.Collectors;

public class ViewDataServlet extends HttpServlet {

    private static final String ENTRIES_FILE = "src/main/webapp/data/entries.json";

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String username = (String) request.getSession().getAttribute("username");
        System.out.println("ViewDataServlet - Username from session: " + username);

        if (username == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        List<Entry> allEntries = loadEntries();
        List<Entry> userEntries = allEntries.stream()
            .filter(e -> e.getUsername() != null && e.getUsername().equals(username))
            .collect(Collectors.toList());

        request.setAttribute("entries", userEntries);
        request.getRequestDispatcher("viewData.jsp").forward(request, response);
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
