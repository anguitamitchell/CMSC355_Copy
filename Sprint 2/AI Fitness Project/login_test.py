import requests
from bs4 import BeautifulSoup


base_url = "http://localhost:5000"
login_url = f"{base_url}/login"
home_url = f"{base_url}/home"

test_username = 'test'
test_password = 'test'

session = requests.Session()

login_page = session.get(login_url)

soup = BeautifulSoup(login_page.text, 'html.parser')

csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

login_data = {
    'csrf_token': csrf_token,
    'username': test_username,
    'password': test_password,
    'submit': 'Login'
}

login_response = session.post(login_url, data=login_data)

print("\nLogin Response Status Code:", login_response.status_code)

if login_response.status_code == 200:
    if "Welcome" in login_response.text:
        print("Login test passed.")
    elif "Invalid username or password" in login_response.text:
        print("Login failed. Invalid username or password.")
    else:
        print("Login failed with status code 200 but no error message found.")
else:
    print("Login failed. Status code:", login_response.status_code)
    print("Response Content:")
    print(login_response.text)
