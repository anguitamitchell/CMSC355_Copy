<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>GlucoTracker - User Dashboard</title>
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
            margin: 3rem auto;
            width: 300px;
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        form {
            margin-top: 1rem;
        }

        input[type="submit"] {
            background: #4a90e2;
            color: white;
            padding: 0.75rem 1.5rem;
            margin: 0.5rem 0;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
        }

        .footer {
            font-size: 0.8rem;
            margin-top: 3rem;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Welcome to Your GlucoTracker Dashboard</h1>

    <div class="button-container">
        <form action="viewData">
            <button type="submit">View Health Data</button>
        </form>
        <form action="editMealtime" method="get">
            <button type="submit">Edit Mealtimes & Carb Ratio</button>
        </form>
        <form action="inputData">
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
