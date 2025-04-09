import requests
from bs4 import BeautifulSoup

registration_url = "http://127.0.0.1:5000/register"

session = requests.Session()


def test_registration():
    registration_page = session.get(registration_url)

    soup = BeautifulSoup(registration_page.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

    username = 'test'
    password = 'test'

    registration_data = {
        'csrf_token': csrf_token,
        'username': username, 
        'password': password,  
        'first_name': 'Test',  
        'last_name': 'User',  
        'submit': 'Register'
    }

    registration_response = session.post(registration_url, data=registration_data)

    if registration_response.status_code == 200:
        print("Registration successful, user created.")
    else:
        print(f"Registration failed with status code {registration_response.status_code}")


test_registration()
