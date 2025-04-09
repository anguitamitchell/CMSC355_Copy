import requests
from bs4 import BeautifulSoup

cardio_url = "http://127.0.0.1:5000/cardio-log"
login_url = "http://127.0.0.1:5000/login"

session = requests.Session()

def login():
    login_page = session.get(login_url)
    soup = BeautifulSoup(login_page.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

    login_data = {
        'csrf_token': csrf_token,
        'username': 'test',
        'password': 'test',
        'submit': 'Login'
    }

    response = session.post(login_url, data=login_data)
    return response.status_code == 200

def test_cardio_log():
    if not login():
        print("Login failed")
        return

    cardio_page = session.get(cardio_url)
    soup = BeautifulSoup(cardio_page.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

    cardio_data = {
        'csrf_token': csrf_token,
        'distance_field': '1.5',
        'minute_field': '12',
        'second_field': '30',
        'submit': 'Submit'
    }

    response = session.post(cardio_url, data=cardio_data)

    if response.status_code == 200:
        print("Cardio log submission successful.")
    else:
        print(f"Cardio log submission failed: {response.status_code}")


test_cardio_log()
