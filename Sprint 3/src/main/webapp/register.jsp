<html>
<head><title>GlucoTracker - Register</title>
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
        width: 300px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    input[type="text"], input[type="password"], input[type="email"], input[type="date"] {
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

    .error {
        color: red;
        margin-bottom: 1rem;
    }
</style>
</head>
<body>
<h2>Create Account</h2>
<% String error = (String) request.getAttribute("error");
   if (error != null) { %>
    <p style="color: red; text-align: center;"><%= error %></p>
<% } %>
<form method="post" action="register">
  First Name: <input type="text" name="firstName" required>
  Last Name: <input type="text" name="lastName" required>
  Username: <input type="text" name="username" required>
  Email: <input type="email" name="email" required>
  DOB: <input type="text" name="dob" placeholder="MM/DD/YYYY" required>
  Password: <input type="password" name="password" required>
  Confirm Password: <input type="password" name="confirmPassword" required>
  <input type="submit" value="Register">
</form>
<a href="login.jsp">Already have an account? Login</a>

<div class="footer">
  Created by Daniel Soorani, Griffin Ramsey, Hunter Priest, Naimul Naim, Rachel Dolfi, and Abanoub Salam
</div>

</body>
</html>