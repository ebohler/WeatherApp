# # # # # # # # # # # # # # # # # # # # # #
# CS325 Weather App by Evan Bohler        #
# --------------------------------------- #
# Creates an HTML table with a 7-day      #
# forecast from the NWS weather.gov API   #
# for the given latitude and longitude    #
# # # # # # # # # # # # # # # # # # # # # #

from urllib.request import urlopen
import json

def main():
    print("Weather App Prototype:\nEnter the latitude and longitude of a place in the US to receive the forecast")
    latitude = input("Latitude: ")
    longitude = input("Longitude: ")

    points_url = "https://api.weather.gov/points/" + latitude + "," + longitude
    points_response = urlopen(points_url)
    points_json = json.loads(points_response.read())

    gridpoints_url = points_json["properties"]["forecast"]
    gridpoints_response = urlopen(gridpoints_url)
    gridpoints_json = json.loads(gridpoints_response.read())
    
    print(gridpoints_json)

if __name__ == "__main__":
    main()