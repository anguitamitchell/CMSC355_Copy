<%@ page import="java.util.Map" %>
<%@ page import="jakarta.servlet.http.HttpSession" %>
<%
    HttpSession currentSession = request.getSession(false);
    if (currentSession == null || currentSession.getAttribute("username") == null) {
        response.sendRedirect("login.jsp");
        return;
    }

    Map<String, Map<String, Object>> mealtimes = (Map<String, Map<String, Object>>) request.getAttribute("mealtimes");
%>
<!DOCTYPE html>
<html>
<head>
    <title>GlucoTracker - Edit Mealtimes</title>
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

        form {
            background: white;
            padding: 2rem;
            margin: 2rem auto;
            width: 350px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        input[type="text"], input[type="number"] {
            width: 100%;
            padding: 0.5rem;
            margin-bottom: 1rem;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        input[type="submit"] {
            background: #4a90e2;
            color: white;
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .footer {
            font-size: 0.8rem;
            margin-top: 3rem;
            color: #666;
        }

        .back {
            margin-top: 1rem;
            display: inline-block;
            text-decoration: none;
            color: #4a90e2;
        }
    </style>
</head>
<body>
<h1>GlucoTracker - Edit Password</h1>

<form method="post" action="forgotPassword">
    Password: <input type="password" name="password">
</form>

<a href="dashboard.jsp" class="back">&larr; Back to Dashboard</a>

<div class="footer">
    Created by Daniel Soorani, Griffin Ramsey, Hunter Priest, Naimul Naim, Rachel Dolfi, and Abanoub Salam
</div>
</body>
</html>
