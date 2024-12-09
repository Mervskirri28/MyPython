import http.client
import json

def get_weather(city_name, api_key):
    # Connect to OpenWeather API
    conn = http.client.HTTPSConnection("api.openweathermap.org")
    
    # Make the GET request to the weather endpoint
    endpoint = f"/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    conn.request("GET", endpoint)
    
    # Get the response
    response = conn.getresponse()
    data = response.read()
    
    # Close the connection
    conn.close()
    
    # Convert the response to a JSON object
    weather_data = json.loads(data.decode("utf-8"))
    
    return weather_data

def display_weather(weather_data):
    if weather_data.get('cod') != 200:
        print(f"Error: {weather_data.get('message', 'Unknown error')}")
        return
    
    main_info = weather_data.get('main', {})
    weather_info = weather_data.get('weather', [{}])[0]
    
    city = weather_data.get('name', 'Unknown City')
    temperature = main_info.get('temp', 'N/A')
    humidity = main_info.get('humidity', 'N/A')
    weather_description = weather_info.get('description', 'No description')
    
    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_description.capitalize()}")
    
def main():
    # Get your API key from OpenWeatherMap
    api_key = "api.openweathermap.org/data/2.5/weather?id=524901&appid=142a61daae40e9f6a5577cfe75972cc6"  # Replace with your actual API key
    
    # Ask the user for a city name
    city_name = input("Enter the name of the city: ")
    
    # Get the weather data
    weather_data = get_weather(city_name, api_key)
    
    # Display the weather information
    display_weather(weather_data)

if __name__ == "__main__":
    main()
