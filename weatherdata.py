from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


def get_weather_data(lat, lon):
    api_key = 'c773577f1996cf4908ae6e9be2c687ab'  # Replace with your actual OpenWeatherMap API key
    endpoint = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
   
    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f'Error fetching weather data: {e}')
        return None


@app.route('/weather', methods=['GET'])
def weather():
    try:
        lat = float(request.args.get('lat'))
        lon = float(request.args.get('lon'))
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid latitude or longitude'}), 400
   
    weather_data = get_weather_data(lat, lon)


    if weather_data:
        areaNam = weather_data['name']
        wind = weather_data['wind']
        countryCode = weather_data['sys']['country']


        return jsonify({
            'latitude': lat,
            'longitude': lon,
            'areaName': areaNam,
            'countryCode':countryCode,
            'wind':wind
            # 'current_temperature': current_temp,
            # 'description': description,
            # Add more relevant data as needed
        }), 200
    else:
        return jsonify({'error': 'Error fetching weather data'}), 500


if __name__ == '__main__':
    app.run(debug=True,port=8080)