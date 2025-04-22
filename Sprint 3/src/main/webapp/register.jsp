<html>
<head><title>GlucoTracker - Register</title>
<style>
  body {
    font-family: Arial, sans-serif;
    background-color: #f4f7f9;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    margin: 0;
    align-items: center;
    justify-content: center;
  }
  h2 {
    text-align: center;
  }
  form {
    background: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
    width: 300px;
  }
  input[type="text"], input[type="email"], input[type="password"] {
    width: 100%;
    padding: 10px;
    margin-top: 6px;
    margin-bottom: 12px;
    border: 1px solid #ccc;
    border-radius: 6px;
  }
  input[type="submit"] {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
  }
  input[type="submit"]:hover {
    background-color: #45a049;
  }
  .footer {
    margin-top: 30px;
    font-size: 0.8em;
    text-align: center;
    color: #555;
  }
  a {
    display: block;
    margin-top: 10px;
    text-align: center;
    color: #663399;
    text-decoration: none;
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