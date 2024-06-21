from twilio.rest import Client
import requests
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get('OWM_KEY_API')
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
num_from = os.environ.get('NUM_FROM')
num_to = os.environ.get('NUM_TO')

MY_LAT = 1.352083
MY_LONG = 103.819839

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_list = weather_data["list"]
for list_item in weather_list:
    weather = list_item["weather"]
    weather_condition_id = weather[0]["id"]

    if weather_condition_id < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It`s going to rain today. Remember to bring an ☔",
            from_=num_from,
            to=num_to,
        )
        print(message.status)
        break
