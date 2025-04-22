package monitoring.servlet;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.*;
import java.io.*;
import java.util.HashMap;
import java.util.Map;
import com.google.gson.Gson;
import java.nio.file.Files;
import java.nio.file.Paths;

public class EditMealtimeServlet extends HttpServlet {

    private static final String FILE_PATH = "src/main/webapp/data/mealtime.json";

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        String breakfast = request.getParameter("breakfastTime");
        String lunch = request.getParameter("lunchTime");
        String dinner = request.getParameter("dinnerTime");
        String carbRatio = request.getParameter("carbRatio");

        Map<String, String> data = new HashMap<>();
        data.put("breakfast", breakfast);
        data.put("lunch", lunch);
        data.put("dinner", dinner);
        data.put("carbRatio", carbRatio);

        Gson gson = new Gson();
        String json = gson.toJson(data);

        Files.createDirectories(Paths.get("src/main/webapp/data"));
        try (FileWriter writer = new FileWriter(FILE_PATH)) {
            writer.write(json);
        }

        response.sendRedirect("dashboard.jsp");
    }
}
