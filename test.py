from flask import Flask, request, jsonify
import sqlite3
from weather import get_weather

app = Flask(__name__)

@app.route('/')
def show_weather():
    conn = sqlite3.connect('base.db')
    c = conn.cursor()
    weather_list = get_weather("Falun")
    c.execute('''DROP TABLE IF EXISTS weather_table''')
    c.execute('''CREATE TABLE IF NOT EXISTS weather_table (
    city VARCHAR(32) NOT NULL,
    temperature INTEGER NOT NULL,
    pressure INTEGER NOT NULL,
    humidity INTEGER NOT NULL)''')
    c.execute('''INSERT INTO weather_table(city, temperature, pressure, humidity)
        VALUES(?, ?, ?, ?)''', weather_list)
    c.execute('''SELECT city, temperature, pressure, humidity FROM weather_table''')
    weather = c.fetchall()
    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)
