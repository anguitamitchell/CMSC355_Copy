package monitoring.servlet;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.*;
import java.util.*;
import com.google.gson.*;
import com.google.gson.reflect.TypeToken;

public class EditMealtimeServlet extends HttpServlet {
    private final File file = new File("src/main/resources/mealtimes.json");
    private final Gson gson = new GsonBuilder().setPrettyPrinting().create();

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("EditMealtimeServlet GET method reached.");
        HttpSession session = request.getSession(false);
        System.out.println("Session: " + session);
        System.out.println("Username from session: " + (session != null ? session.getAttribute("username") : "null"));
        if (session == null || session.getAttribute("username") == null) {
            System.out.println("EditMealtimeServlet GET: Redirecting because session is " + session + " and username is " + (session != null ? session.getAttribute("username") : "null"));
            response.sendRedirect("login.jsp");
            return;
        }


        String username = (String) session.getAttribute("username");

        Map<String, Map<String, Map<String, Object>>> allData = loadMealtimes();
        Map<String, Map<String, Object>> userMeals = allData.getOrDefault(username, new HashMap<>());
        request.setAttribute("mealtimes", userMeals);

        request.getRequestDispatcher("editMealtime.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("EditMealtimeServlet POST method reached.");
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("username") == null) {
            System.out.println("EditMealtimeServlet GET: Redirecting because session is " + session + " and username is " + (session != null ? session.getAttribute("username") : "null"));
            response.sendRedirect("login.jsp");
            return;
        }

        String username = (String) session.getAttribute("username");

        Map<String, Map<String, Map<String, Object>>> allData = loadMealtimes();
        Map<String, Map<String, Object>> userMeals = new HashMap<>();

        String ratioStr = request.getParameter("carbToUnitRatio");
        int ratio = 0;
        try {
            ratio = Integer.parseInt(ratioStr);
        } catch (NumberFormatException ignored) {}

        for (String meal : Arrays.asList("breakfast", "lunch", "dinner")) {
            String time = request.getParameter(meal + "Time");

            Map<String, Object> mealData = new HashMap<>();
            mealData.put("time", time);
            mealData.put("carbToUnitRatio", ratio);
            userMeals.put(meal, mealData);
        }

        allData.put(username, userMeals);
        saveMealtimes(allData);

        response.sendRedirect("dashboard.jsp");
    }

    private Map<String, Map<String, Map<String, Object>>> loadMealtimes() {
        if (!file.exists()) return new HashMap<>();

        try (Reader reader = new FileReader(file)) {
            return gson.fromJson(reader, new TypeToken<Map<String, Map<String, Map<String, Object>>>>(){}.getType());
        } catch (IOException e) {
            e.printStackTrace();
            return new HashMap<>();
        }
    }

    private void saveMealtimes(Map<String, Map<String, Map<String, Object>>> data) {
        try (Writer writer = new FileWriter(file)) {
            gson.toJson(data, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
