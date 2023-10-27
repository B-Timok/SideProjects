import tkinter as tk
import requests

# API Key from openweathermap.org
API_key = '5154bc4573c31fee7509b94988b8f03d'

# Define the kelvin_to_fahrenheit function here
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

# Function to get weather data with code from CLI version
def get_weatherData():
    # Retrieve user input from the city_entry widget
    city = city_entry.get()
    
    # Construct the API URL using the user input
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_key}'
    
    # Make API request and process response
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp_kelvin = data['main']['temp']
        temp_fahrenheit = int(kelvin_to_fahrenheit(temp_kelvin))
        descript = data['weather'][0]['description']
        
        # Update the result_label widget with weather information
        result_label.config(text=f'Temperature: {temp_fahrenheit} °F\nDescription: {descript}')
    else:
        # Handle errors or display an error message
        result_label.config(text='Error fetching weather data')

# Create the main Tkinter window
root = tk.Tk()
root.title("Weather App")

# Create widgets (labels, entry field, and button)
city_label = tk.Label(root, text="Enter a city name \n(Ex: Las Vegas,usa): ")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text="Get Weather Data", command=get_weatherData)
fetch_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter main loop
root.mainloop()
