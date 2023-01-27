import requests
from secret import API_key
import json
import datetime
from notifypy import Notify
from time import sleep

location = input("Enter your location : ")
location_capitalize = location.capitalize()

if location_capitalize == "":
  print("You haven't entered any location")
  location = input("Please enter your location : ")
  location_capitalize = location.capitalize()
else:
  pass

print("You have entered the location " +location_capitalize)

def get_location(location_capitalize):
  url = f"http://api.openweathermap.org/geo/1.0/direct?q={location_capitalize}&limit=5&appid={API_key}"
  location_response = requests.get(url)
  response_status = location_response.status_code

  if response_status != 200:
    print("Something went wrong with the connection from API")
    print("Check whether you have entered the location")
    print("Please try again")
    exit()
  else:
    print("Successfully connected with the location API \nStatus Code : "+str(response_status))
    print("\n")
    pass

  location_jsonresponse = location_response.json()

  print("--------------------JSON DATA OF LOCATION--------------------")
  print(location_jsonresponse)
  print("\n")

  with open('locationdata.json', 'w') as json_data_file:
    json.dump(location_jsonresponse, json_data_file)
    json_data_file.close()
  
  if location_jsonresponse == []:
    print("LOCATION NOT FOUND, Please enter a major city name")
    new_location = input("Enter new location : ")
    new_location_capitalize = new_location.capitalize()
    print("You have entered " + new_location_capitalize)
    get_location(new_location_capitalize)
  else:
    print("LOCATION FOUND")
    lattitude = location_jsonresponse[0]['lat']
    print("Lattitude : "+str(lattitude))
    longitude = location_jsonresponse[0]['lon']
    print("Longitude : "+str(longitude))
    print("\n")
    print("===========================================================")
    print("\n")
  return lattitude, longitude

lat, lon = get_location(location_capitalize)

def get_weather():
  url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
  weather_response = requests.get(url)
  weather_response_status = weather_response.status_code

  if weather_response_status != 200:
    print("Something went wrong with the connection with the API")
    print("Check whether you have entered a location")
    print("Please try again")
    exit()
  else:
    print("Successfully connected with the weather API \nStatus Code : "+str(weather_response_status))
    print("\n")
    pass

  weather_jsonresponse = weather_response.json()

  print("--------------------JSON DATA OF WEATHER--------------------")
  print(weather_jsonresponse)
  print("\n")

  with open('weatherdata.json', 'w') as json_data_file:
    json.dump(weather_jsonresponse, json_data_file)
    json_data_file.close()

  # Country
  country = weather_jsonresponse['sys']['country']
  print(f"Country: {country}")

  # City name
  city_name = weather_jsonresponse['name']
  print(f"City name: {city_name}")

  # Time
  time = weather_jsonresponse['timezone']
  # Timezone shift in seconds from UTC
  timezone_offset = time
  now = datetime.datetime.utcnow()
  offset = datetime.timedelta(seconds=timezone_offset)
  local_time = now + offset
  print(f"Time: {local_time}")

  # Temperature
  temperature = weather_jsonresponse['main']['temp']
  temp_roundfig = round(temperature)
  print(f"Current temperature: {temp_roundfig}°C ")

  # Feels like
  feels_like = weather_jsonresponse['main']['feels_like']
  feels_like_roundfig = round(feels_like)
  print(f"Feels like: {feels_like_roundfig}°C")

  # Minimum temperature
  temperature_min = weather_jsonresponse['main']['temp_min']
  temperature_min_roundfig = round(temperature_min)
  print(f"Minimum temperature: {temperature_min_roundfig}°C")

  # Maximum temperature
  temperature_max = weather_jsonresponse['main']['temp_max']
  temperature_max_roundfig = round(temperature_max)
  print(f"Maximum temperature: {temperature_max_roundfig}°C")

  # Humidity
  humidity = weather_jsonresponse['main']['humidity']
  print(f"Humidity: {humidity}%")

  # Weather condition
  weather_condition = weather_jsonresponse['weather'][0]['main']
  print(f"Weather condition: {weather_condition}")

  # Weather description
  weather_description = weather_jsonresponse['weather'][0]['description']
  weather_desc_capitalize = weather_description.capitalize()
  print(f"Weather description: {weather_desc_capitalize}")

  # Sunrise
  sunrise = weather_jsonresponse['sys']['sunrise']
  # Converting unix UTC sunrise time to local time
  unix_sunriset_time = sunrise
  local_sunrise_time = datetime.datetime.fromtimestamp(unix_sunriset_time)
  print("Sunrise: ", local_sunrise_time.strftime("%Y-%m-%d %H:%M:%S"))

  # Sunset
  sunset = weather_jsonresponse['sys']['sunset']
  # Converting unix UTC sunset time to local time
  unix_sunset_time = sunset
  local_sunset_time = datetime.datetime.fromtimestamp(unix_sunset_time)
  print("Sunset: ", local_sunset_time.strftime("%Y-%m-%d %H:%M:%S"))

  print("\n")
  print("--------------------------------------------------------------")

  # Desktop notification
  notification = Notify()
  notification.application_name = "Weather Update"
  notification.title = f"Weather at {city_name}"
  notification.message = f"🌡️ Temperature: {temp_roundfig}°C \nFeels like: {feels_like_roundfig}°C \n{weather_desc_capitalize}"
  notification.icon = "./icon.png"
  notification.audio = "./notificationsound.wav"
  notification.send()

while True:
  get_weather()
  sleep(900)