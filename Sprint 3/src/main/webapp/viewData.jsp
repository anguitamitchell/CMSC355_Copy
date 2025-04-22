<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="java.util.List" %>
<%@ page import="java.util.Map" %>
<%
    HttpSession currentSession = request.getSession(false);
    String username = (currentSession != null) ? (String) currentSession.getAttribute("username") : null;
    List<Map<String, String>> entries = (List<Map<String, String>>) request.getAttribute("entries");

    if (username == null) {
        currentSession.invalidate();
        response.sendRedirect("login.jsp");
        return;
    }
%>
<!DOCTYPE html>
<html>
<head>
    <title>GlucoTracker - View Data</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f4f8;
            margin: 0;
            padding: 0;
            text-align: center;
        }

        h1 {
            background: #4a90e2;
            color: white;
            margin: 0;
            padding: 1rem;
        }

        .container {
            margin: 2rem auto;
            width: 80%;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            margin-top: 2rem;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        th, td {
            padding: 0.75rem;
            border: 1px solid #ccc;
        }

        th {
            background: #e4eaf1;
        }

        .back-button {
            background: #4a90e2;
            color: white;
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 5px;
            margin-top: 1.5rem;
            text-decoration: none;
            display: inline-block;
        }

        .footer {
            font-size: 0.8rem;
            margin-top: 3rem;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>GlucoTracker - Your Health Data</h1>

    <table>
        <tr>
            <th>Date</th>
            <th>Carbs (g)</th>
            <th>Glucose (mg/dL)</th>
            <th>Insulin Units</th>
        </tr>
        <%
            if (entries != null && !entries.isEmpty()) {
                for (Map<String, String> entry : entries) {
                    //if(entry.get("username").equals(request.getSession.getAttribute("username"))) {
        %>
        <tr>
            <td><%= entry.get("date") %></td>
            <td><%= entry.get("carbs") %></td>
            <td><%= entry.get("glucose") %></td>
            <td><%= entry.get("insulinUnits") %></td>
        </tr>
        <%
                    //}
                }
            } else {
        %>
        <tr>
            <td colspan="4">No data available.</td>
        </tr>
        <% } %>
    </table>

    <form action="dashboard.jsp" method="get" style="margin-top: 1rem;">
        <button type="submit" style="padding: 0.5rem 1rem; font-size: 1rem;">Back to Dashboard</button>
    </form>

    <div class="footer">
        Created by Daniel Soorani, Griffin Ramsey, Hunter Priest, Naimul Naim, Rachel Dolfi, and Abanoub Salam
    </div>
</body>
</html>
