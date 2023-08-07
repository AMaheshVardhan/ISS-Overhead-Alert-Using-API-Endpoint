from twilio.rest import Client
import requests
import json
OWP_Endpoint = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "fae6c85a467f2740f948a7df34ddabd9"
parameters = {
    "q":"Hyderabad",
    "appid": api_key,
}
response = requests.get(OWP_Endpoint, params=parameters)
weather_data = response.json()
weather_slice = weather_data["weather"][0]["id"]
if weather_slice < 700:
    print("Bring an umbrella")
