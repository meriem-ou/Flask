import requests
from flask import request, jsonify


def weather(city):
        api_key='28e98f672b2502726976e91bcc55c821'
        #city = request.args.get('city')
        #user_input = input("Enter Your City : ")
        
        #weather_data = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid={api_key}')
        weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}')

        if weather_data.status_code == 200:

            weather = weather_data.json()['weather'][0]['main']
            desc = weather_data.json()['weather'][0]['description']
            temp = weather_data.json()['main']['temp']
            humidity = weather_data.json()['main']['humidity']
            
            weatherData = {
                'found': True,
                'data': {
                    "weather" : weather,
                    "desc": desc,
                    "temp" : temp,
                    "humidity": humidity
                }
            }

            return weatherData
            
        else:
            if weather_data.status_code == 404:
                weatherData = {
                    'found': False
                }
                return "City not found"
            else:
                weatherData = {
                    'found': False 
                }
                return f'Error fetching weather. || Weather data : {weather_data}'
    








