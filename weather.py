# # # # # # # # # # # # # # # # # # # # # #
# CS325 Weather App by Evan Bohler        #
# --------------------------------------- #
# Creates an HTML table with a 7-day      #
# forecast from the NWS weather.gov API   #
# for the given latitude and longitude    #
# # # # # # # # # # # # # # # # # # # # # #

from urllib.request import urlopen
from time import sleep
import json

def main():
    print("Weather App Prototype:\nEnter the latitude and longitude of a place in the US to receive the forecast")
    latitude = input("Latitude: ")
    longitude = input("Longitude: ")

    points_url = "https://api.weather.gov/points/" + latitude + "," + longitude
    for i in range (3):
        try:
            points_response = urlopen(points_url)
        except:
            print ("Error: connection failed to " + points_url + "\nRetrying...")
            sleep(2)
    points_json = json.loads(points_response.read())
    #print(points_json)

    gridpoints_url = points_json["properties"]["forecast"]
    for i in range (3):
        try:
            gridpoints_response = urlopen(gridpoints_url)
        except:
            print("Error: connection failed to " + points_url + "\nRetrying...")
            sleep(2)
    gridpoints_json = json.loads(gridpoints_response.read())
    #print(gridpoints_json)

if __name__ == "__main__":
    main()