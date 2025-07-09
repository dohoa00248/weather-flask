from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form['city']

    #API key từ OpenWeatherMap
    api_key = 'f1f051900e3beebc29aeef4c68832c15'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    
    try:
        response = requests.get(url)
        weather_data = response.json()
        print(weather_data)
        return render_template('weather.html', city=city, weather_data=weather_data)
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3000)