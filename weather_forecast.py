import requests

API_KEY = 'YOUR_API_KEY' #please put your API key here

def get_weather_data(location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if 'main' not in weather_data:
        print('Location not found.')
        return
    
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    weather_description = weather_data['weather'][0]['description']
    
    print(f'Temperature: {temperature}°C')
    print(f'Humidity: {humidity}%')
    print(f'Wind Speed: {wind_speed} m/s')
    print(f'Weather Description: {weather_description}')

def weather_forecast():
    location = input('Enter a location: ')
    weather_data = get_weather_data(location)
    display_weather(weather_data)

weather_forecast()
