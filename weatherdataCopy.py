from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def getWeatherData(lat, lon):
    apiKey = "c773577f1996cf4908ae6e9be2c687ab"
    endpoint = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}"

    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error Fetching Weather Data {e}")
        return None

@app.route('/weather', methods=["GET"])
def weather():
    try:
        lat = float(request.args.get("lat"))
        lon = float(request.args.get("lon"))
    except (TypeError, ValueError):
        return jsonify({"error" : "Invalid Latitude or Longitude"}), 400
    
    weatherData = getWeatherData(lat, lon)

    if weatherData:
        areaNam = weatherData['name']
        wind = weatherData['wind']
        temp = weatherData['main']['temp']
        visibility = weatherData['visibility']

        return jsonify({
            'latitude' : lat,
            'longitude' : lon,
            'areaNam' : areaNam,
            'wind' : wind,
            'temp' : temp,
            'visibility' : visibility
        }), 200
    else:
        return jsonify({'error': 'Error fetching weather data'}), 500

if __name__ == '__main__':
    app.run(debug=True,port=5000)


