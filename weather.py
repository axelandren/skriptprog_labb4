import requests, time, json


def get_weather(city):
    api_key = "767c44b52263b80bee21a57d5c2461c0"
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="
    data_dict = {"ts":time.time()}
    complete_url = base_url + city + "&appid=" + api_key
    response = requests.post(complete_url, json=data_dict)
    r = response.json()
    if r["cod"] != "404":
        x = r["main"]
        weather_dict = [city, x["temp"], x["pressure"], x["humidity"]]
        print(weather_dict)
        return weather_dict
    else:
        print("City not found.")
