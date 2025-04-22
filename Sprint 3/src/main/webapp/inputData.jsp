<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Input Carb & Glucose Data</title>
</head>
<body>
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
