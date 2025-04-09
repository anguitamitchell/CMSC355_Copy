import requests
from bs4 import BeautifulSoup

workout_url = "http://127.0.0.1:5000/workout-log"
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

def test_workout_log():
    if not login():
        print("Login failed")
        return

    workout_page = session.get(workout_url)
    soup = BeautifulSoup(workout_page.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

    workout_data = {
        'csrf_token': csrf_token,
        'exercise_input': 'Push Ups',
        'sets_field': 3,
        'reps_field': 12,
        'submit': 'Submit'
    }

    response = session.post(workout_url, data=workout_data)

    if response.status_code == 200:
        print("Workout log submission successful.")
    else:
        print(f"Workout log submission failed: {response.status_code}")


test_workout_log()
