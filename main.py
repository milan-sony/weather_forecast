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
