from flask import Flask, request, jsonify
import sqlite3, requests, json

app = Flask(__name__)

@app.route('/')
def show_weather():
    conn = sqlite3.connect('base.db')
    c = conn.cursor()
    weather_list = get_weather("Malmö")
    c.execute('''CREATE TABLE IF NOT EXISTS weather_table (
    city VARCHAR(32) NOT NULL,
    temperature INTEGER NOT NULL,
    pressure INTEGER NOT NULL,
    humidity INTEGER NOT NULL)''')
    c.execute('''INSERT INTO weather_table(city, temperature, pressure, humidity) VALUES(?, ?, ?, ?)''', weather_list)
    c.execute('''SELECT city, temperature, pressure, humidity FROM weather_table''')
    weather = c.fetchall()
    return jsonify(weather)

def get_weather(city):
    api_key = "767c44b52263b80bee21a57d5c2461c0"
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="
    complete_url = base_url + city + "&appid=" + api_key
    response = requests.post(complete_url)
    r = response.json()
    if r["cod"] != "404":
        x = r["main"]
        weather_dict = [city, x["temp"], x["pressure"], x["humidity"]]
        print(weather_dict)
        return weather_dict
    else:
        print("City not found.")

if __name__ == '__main__':
    app.run(debug=True)
