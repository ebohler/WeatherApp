# # # # # # # # # # # # # # # # # # # # # #
# CS325 Weather App by Evan Bohler        #
# --------------------------------------- #
# Creates an HTML table with a 7-day      #
# forecast from the NWS weather.gov API   #
# for the given latitude and longitude    #
# # # # # # # # # # # # # # # # # # # # # #
# TODO:
# Urlopen needs user agent to work
# Program should end after 3 retries
# Write period data to text file
# Convert date and time to readable text
# Dynamically create HTML file and decorate w/ CSS
# After prototype is fully working, put everything in classes and functions
# Clean up code and add comments where needed
# Create YAML file of conda env
# Write detailed README for github
# Submit github repo link to moodle

from urllib.request import urlopen, Request
from time import sleep
import json

class Period:
    def __init__(self, number, name, startTime, temperature, shortForecast):
        self.number = number
        self.name = name
        self.startTime = startTime
        self.temperature = temperature
        self.shortForecast = shortForecast

def main():
    print("Weather App Prototype:\nEnter the latitude and longitude of a place in the US to receive the forecast")
    latitude = input("Latitude: ")
    longitude = input("Longitude: ")
    coordinates = latitude + "," + longitude

    points_url = "https://api.weather.gov/points/" + coordinates
    for i in range (3):
        try:
            points_response = urlopen(Request(points_url, headers={'User-Agent': 'Mozilla'}))
        except:
            print ("Error: connection failed to " + points_url + "\nRetrying...")
            sleep(2)
    points_json = json.loads(points_response.read())
    #print(points_json)

    gridpoints_url = points_json["properties"]["forecast"]
    for i in range (3):
        try:
            gridpoints_response = urlopen(Request(gridpoints_url, headers={'User-Agent': 'Mozilla'}))
        except:
            print("Error: connection failed to " + gridpoints_url + "\nRetrying...")
            sleep(2)
    gridpoints_json = json.loads(gridpoints_response.read())
    #print(gridpoints_json)

    periods = []
    
    for p in gridpoints_json["properties"]["periods"]:
        period = Period(p["number"],p["name"],p["startTime"],p["temperature"],p["shortForecast"])
        periods.append(period)

    #for i in periods:
    #    print(i.name + i.startTime + str(i.temperature) + i.shortForecast)

    textfile = open(coordinates + ".txt", "w")
    for p in periods:
        textfile.write(p.name + "\n" + p.startTime + "\n" + str(p.temperature) + "\u00B0F \n" + p.shortForecast + "\n\n")
    textfile.close()



if __name__ == "__main__":
    main()