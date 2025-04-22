package monitoring.servlet;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.*;

import java.io.*;
import java.util.*;
import com.google.gson.reflect.TypeToken;
import com.google.gson.Gson;

public class InputDataServlet extends HttpServlet {

    private static final String FILE_PATH = "src/main/resources/entries.json";

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        String date = request.getParameter("date");
        String glucose = request.getParameter("glucose");
        String carbs = request.getParameter("carbs");
        String units = request.getParameter("units");

        Map<String, String> newEntry = new HashMap<>();
        newEntry.put("username", (String) request.getSession().getAttribute("username"));
        newEntry.put("date", date);
        newEntry.put("glucose", glucose);
        newEntry.put("carbs", carbs);
        newEntry.put("units", units);

        Gson gson = new Gson();
        List<Map<String, String>> allEntries = new ArrayList<>();

        File file = new File(FILE_PATH);
        if (file.exists()) {
            try (Reader reader = new FileReader(file)) {
                allEntries = gson.fromJson(reader, new TypeToken<List<Map<String, String>>>() {}.getType());
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        allEntries.add(newEntry);

        try (Writer writer = new FileWriter(FILE_PATH)) {
            gson.toJson(allEntries, writer);
        }

        response.sendRedirect("dashboard.jsp");
    }
}
