import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        print(f"Weather in {location}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Condition: {weather['description'].capitalize()}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind: {wind['speed']} kph")
    elif response.status_code == 401:
        print("Failed to get weather data: 401 Unauthorized. Please check your API key.")
    elif response.status_code == 404:
        print("Failed to get weather data: 404 Not Found. Please check the location.")
    else:
        print(f"Failed to get weather data: {response.status_code}")

if __name__ == "__main__":
    api_key = "99a6a2eb5a2fc4021c9d718d0e9b092d"  # Replace with your actual OpenWeatherMap API key
    location = "San Francisco"
    get_weather(api_key, location)
