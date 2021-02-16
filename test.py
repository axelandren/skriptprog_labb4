from flask import Flask, request, jsonify
import sqlite3
from weather import get_weather

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'hello {name}!'


@app.route('/users')
def users():
    conn = sqlite3.connect('base.db')
    c = conn.cursor()
    weather_dict = get_weather("Falun")
    city = weather_dict[0]
    temp = weather_dict[1]
    pressure = weather_dict[2]
    humidity = weather_dict[3]
    c.execute('''DROP TABLE IF EXISTS weather_table''')
    c.execute('''CREATE TABLE IF NOT EXISTS weather_table (
    city VARCHAR(32) NOT NULL,
    temperature INTEGER NOT NULL,
    pressure INTEGER NOT NULL,
    humidity INTEGER NOT NULL)''')
    c.execute('''INSERT INTO weather_table(city, temperature, pressure, humidity)
        VALUES(?, ?, ?, ?)''', (city, temp, pressure, humidity))
    c.execute('''SELECT city, temperature, pressure, humidity FROM weather_table''')
    weather = c.fetchall()
    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)
