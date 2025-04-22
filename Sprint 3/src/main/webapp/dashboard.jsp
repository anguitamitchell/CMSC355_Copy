<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>GlucoTracker - User Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        h1 {
            font-size: 28px;
        }
        .button-container {
            margin-top: 30px;
        }
        .button-container form {
            margin: 10px;
        }
        button {
            padding: 10px 25px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Welcome to Your GlucoTracker Dashboard</h1>

    <div class="button-container">
        <form action="viewData.jsp">
            <button type="submit">View Health Data</button>
        </form>
        <form action="editMealtime.jsp">
            <button type="submit">Edit Mealtimes & Carb Ratio</button>
        </form>
        <form action="inputData.jsp">
            <button type="submit">Input Carb & Glucose Levels</button>
        </form>
        <form action="login.jsp">
            <button type="submit">Logout</button>
        </form>
    </div>

    <div class="footer">
        Created by Daniel Soorani, Griffin Ramsey, Hunter Priest, Naimul Naim, Rachel Dolfi, and Abanoub Salam
    </div>
</body>
</html>
