<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Edit Mealtimes & Carb-to-Unit Ratio</title>
</head>
<body>
    <h2>Edit Mealtimes & Carb-to-Unit Ratio</h2>
    <form action="editMealtime" method="post">
        <label>Breakfast Time (e.g., 07:30 AM):</label><br>
        <input type="text" name="breakfastTime" required><br><br>

        <label>Lunch Time (e.g., 12:00 PM):</label><br>
        <input type="text" name="lunchTime" required><br><br>

        <label>Dinner Time (e.g., 06:30 PM):</label><br>
        <input type="text" name="dinnerTime" required><br><br>

        <label>Carb-to-Unit Ratio (e.g., 10):</label><br>
        <input type="number" name="carbRatio" step="0.01" required><br><br>

        <input type="submit" value="Save Changes">
    </form>
    <br>
    <a href="dashboard.jsp">Back to Dashboard</a>
</body>
</html>
