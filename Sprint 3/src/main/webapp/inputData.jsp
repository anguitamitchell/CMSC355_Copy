<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Input Carb & Glucose Data</title>
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
    <h1>GlucoTracker Data Input</h1>
    <h2>Input Daily Data</h2>
    <form action="inputData" method="post">
        <label>Date (MM/DD/YYYY):</label><br>
        <input type="text" name="date" required><br><br>

        <label>Glucose Level:</label><br>
        <input type="number" name="glucose" required><br><br>

        <label>Carbs Consumed:</label><br>
        <input type="number" name="carbs" required><br><br>

        <label>Insulin Units Taken:</label><br>
        <input type="number" name="units" required><br><br>

        <input type="submit" value="Submit Data">
    </form>
    <br>
    <a href="dashboard.jsp">Back to Dashboard</a>
</body>
</html>
