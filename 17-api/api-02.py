import requests

api_key = "8ee06faf23f9c31c7ad3d5b6797ab159"

def get_current_weather_by_city(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()

        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")

    else:
        print("City not found or API error")

def get_current_weather_by_coord(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
        
    else:
        print("API error")


def get_weather_forecast(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        forecast_data = response.json()['list']
        for forecast in forecast_data:
            timestamp = forecast['dt_txt']
            temperature = forecast['main']['temp']
            humidity = forecast['main']['humidity']
            description = forecast['weather'][0]['description']
            
            print(f"Timestamp: {timestamp}")
            print(f"Temperature: {temperature} K")
            print(f"Humidity: {humidity}%")
            print(f"Description: {description}")
            print("------")
    else:
        print("City not found or API error")



city = "London"
# get_current_weather_by_city(city, api_key)
get_weather_forecast(city, api_key)

lat = 51.5074
lon = -0.1278
# get_current_weather_by_coord(lat, lon, api_key)



