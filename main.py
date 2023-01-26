import requests
import json

location = input("Enter your location : ")
location_capitalize = location.capitalize()

if location_capitalize == "":
  print("You haven't entered any location")
  location = input("Please enter your location : ")
  location_capitalize = location.capitalize()
else:
  pass

print("You have entered the location " +location_capitalize)

# Read API key from API file
API_key_file = open("API_key", "r")
API_key = API_key_file.read()
API_key_file.close()

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