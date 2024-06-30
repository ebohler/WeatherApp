# # # # # # # # # # # # # # # # # # # # # #
# CS325 Weather App by Evan Bohler        #
# --------------------------------------- #
# Creates an HTML table with a 7-day      #
# forecast from the NWS weather.gov API   #
# for the given latitude and longitude    #
# # # # # # # # # # # # # # # # # # # # # #
# TODO:
# Program should exit after 3 retries
# Convert datetime to readable format
# Dynamically create HTML file from .txt and decorate w/ CSS
# After prototype is fully working, put everything in classes and functions
# -
# Clean up code and add comments where needed
# Create YAML file of conda env
# Write detailed README for github
# Submit github repo link to moodle

from urllib.request import urlopen, Request
from datetime import datetime
from time import sleep
import json

class Period:
    def __init__(self, number, name, startTime, temperature, shortForecast):
        self.number = number
        self.name = name
        self.startTime = startTime
        self.temperature = temperature
        self.shortForecast = shortForecast

def format_date(input_date):
    dt = datetime.fromisoformat(input_date)
    formatted_date = dt.strftime('%B %d, %Y %I:%M %p')
    return formatted_date

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


    periods = []
    for p in gridpoints_json["properties"]["periods"]:
        period = Period(p["number"],p["name"],p["startTime"],p["temperature"],p["shortForecast"])
        periods.append(period)


    textfile = open(coordinates + ".txt", "w")
    for p in periods:
        formatted_temp = str(p.temperature) + "\u00B0F\n"
        formatted_date = format_date(p.startTime)
        textfile.write(p.name + "\n" + formatted_date + "\n" + formatted_temp + p.shortForecast + "\n\n")
    textfile.close()


    with open(coordinates + ".txt", "r") as file:
        lines = file.read().splitlines()

    html_content = """
    <html>
    <head>
    <title>Forecast</title>
    <style>
        table {
            font-family: arial, sans-serif;
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
    </head>
    <body>
    <table>
    """

    html_content += "<tr>\n"
    for line in lines:
        if line.strip() == "":
            html_content += "</tr>\n<tr>\n"
        else:
            html_content += f"<td>{line.strip()}</td>\n"
    html_content += "</tr>\n"

    html_content += "</table>\n</body>\n</html>"

    with open(coordinates + ".html", "w") as file:
        file.write(html_content)

if __name__ == "__main__":
    main()