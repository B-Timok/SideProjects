import requests

# API Key from openweathermap.org
API_key = '5154bc4573c31fee7509b94988b8f03d'

# prompt for user to enter a city
city = input('Enter a city name (Ex: Las Vegas,usa): ')

# url to retrieve weather info for city chosen
url = f'HTTP://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_key}'

# make api request and process response
response = requests.get(url)

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

if response.status_code == 200:
    data = response.json()
    temp_K = data['main']['temp']
    temp_F = int(kelvin_to_fahrenheit(temp_K))
    descript = data['weather'][0]['description']
    print(f'Temperature: {temp_F} °F')
    print(f'Description: {descript}')
else:
    print('Error getting weather data')