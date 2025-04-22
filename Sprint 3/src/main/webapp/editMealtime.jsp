<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <title>Edit Mealtimes & Carb Ratio - GlucoTracker</title>
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

        input[type="text"] {
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

        .back-btn {
            margin-top: 1rem;
            display: inline-block;
            color: #4a90e2;
            text-decoration: none;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <h1>GlucoTracker - Edit Mealtimes & Carb Ratio</h1>

    <form method="post" action="editMealtime">
        <input type="text" name="breakfastTime" placeholder="Breakfast Time (e.g. 8:00 AM)" required>
        <input type="text" name="lunchTime" placeholder="Lunch Time (e.g. 12:00 PM)" required>
        <input type="text" name="dinnerTime" placeholder="Dinner Time (e.g. 6:00 PM)" required>
        <input type="text" name="carbRatio" placeholder="Carb-to-Unit Ratio (e.g. 15)" required>
        <input type="submit" value="Save">
    </form>

    <a href="dashboard.jsp" class="back-btn">← Back to Dashboard</a>

    <div class="footer">
        Created by Daniel Soorani, Griffin Ramsey, Hunter Priest, Naimul Naim, Rachel Dolfi, and Abanoub Salam
    </div>
</body>
</html>