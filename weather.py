# # # # # # # # # # # # # # # # # # # # # #
# CS325 Weather App by Evan Bohler        #
# --------------------------------------- #
# Creates an HTML table with a 7-day      #
# forecast from the NWS weather.gov API   #
# for the given latitude and longitude    #
# # # # # # # # # # # # # # # # # # # # # #

from urllib.request import urlopen, Request
from datetime import datetime
from time import sleep
import json, sys

class WeatherApp:
    def coords_input(self):
        print("Enter the latitude and longitude of a place in the US to receive the forecast")
        latitude = input("Latitude: ")
        longitude = input("Longitude: ")
        coords = latitude + "," + longitude
        return coords

class JSONParser:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def get_points_json(self):
        points_url = "https://api.weather.gov/points/" + self.coordinates
        for i in range (3):
            try:
                points_response = urlopen(Request(points_url, headers={'User-Agent': 'Mozilla'}))
            except:
                print ("Error: could not connect to " + points_url)
                if i == 2:
                    sys.exit("Connection failed after 3 retries. Ending process...")
                sleep(2)
        points_json = json.loads(points_response.read())
        return points_json
    
    def get_gridpoints_json(self, points_json):
        gridpoints_url = points_json["properties"]["forecast"]
        for i in range (3):
            try:
                gridpoints_response = urlopen(Request(gridpoints_url, headers={'User-Agent': 'Mozilla'}))
            except:
                print("Error: could not connect to " + gridpoints_url + "\n")
                if i == 2:
                    sys.exit("Connection failed after 3 retries. Ending process...")
                sleep(2)
        gridpoints_json = json.loads(gridpoints_response.read())
        return gridpoints_json
    
    def create_periods_list(gridpoints_json):
        periods = []
        for p in gridpoints_json["properties"]["periods"]:
            period = Period(p["number"],p["name"],p["startTime"],p["temperature"],p["shortForecast"])
            periods.append(period)
        return periods

class Period:
    def __init__(self, number, name, startTime, temperature, shortForecast):
        self.number = number
        self.name = name
        self.startTime = startTime
        self.temperature = temperature
        self.shortForecast = shortForecast

class TextFile:
    def __init__(self, filename):
        self.filename = filename + ".txt"

    # Adds .txt extension to given string
    def change_filename(self, name):
        self.filename = name + ".txt"

    # Uses datetime module to reformat from JSON's ISO format to regular date format i.e. June 30, 2024 06:00 PM
    def format_date(self, input_date):
        dt = datetime.fromisoformat(input_date)
        formatted_date = dt.strftime('%B %d, %Y\n%I:%M %p')
        return formatted_date
    
    # Creates/overwrites file of self.filename, adds degree symbol to temp and calls format_date to convert ISO date into a more readable format, then closes file
    def write_file(self, periods):
        with open(self.filename, "w") as textfile:
            for p in periods:
                formatted_temp = str(p.temperature) + "\u00B0F\n"
                formatted_date = self.format_date(p.startTime)
                textfile.write(p.name + "\n" + formatted_date + "\n" + formatted_temp + p.shortForecast + "\n\n")

class HTMLTable:
    def __init__(self, filename):
        self.filename = filename + ".html"

    # Adds .html extension to given string
    def change_filename(self, name):
        self.filename = name + ".html"

    def create_table(self, textfilename):
        with open(textfilename + ".txt", "r") as file:
            lines = file.read().splitlines()

        with open(self.filename, "w") as file:
            file.write(
                """
                <html>
                <head>
                <title>Forecast</title>
                <style>
                    body {
                        background: rgb(34,143,195);
                        background: linear-gradient(0deg, rgba(34,143,195,1) 0%, rgba(240,255,255,1) 100%); 
                        background-repeat: no-repeat;
                        background-attachment: fixed;
                        padding: 12px;  
                    }    
                    table {
                        font-family: 'Helvetica', 'Arial', sans-serif;
                        margin: 50px auto;
                        overflow: hidden;
                        border: 1px solid #ddd;
                        border-collapse: separate;
                        border-left: 0;
                        border-radius: 4px;
                        border-spacing: 0px;
                    }
                    thead {
                        display: table-header-group;
                        vertical-align: middle;
                        border-color: inherit;
                        border-collapse: separate;
                    }
                    tr {
                        display: table-row;
                        vertical-align: inherit;
                        border-color: inherit;
                    }
                    td {
                        border-top: 1px solid #ddd;   
                        padding: 24px 12px 24px 12px; 
                        text-align: center;
                        vertical-align: top;
                        border-left: 1px solid #ddd;  
                    }
                    thead:first-child tr:first-child th:first-child, tbody:first-child tr:first-child td:first-child {
                        border-radius: 4px 0 0 0;
                    }
                    thead:last-child tr:last-child th:first-child, tbody:last-child tr:last-child td:first-child {
                        border-radius: 0 0 0 4px;
                    }
                    tr:nth-child(even) {
                        background-color: #f9f9f9;
                    }
                    tr:nth-child(odd) {
                        background-color: #f2f2f2;
                    }
                </style>
                </head>
                <body>
                <table>
                <tr>\n
                """
            )

            for line in lines:
                if line.strip() == "":
                    file.write("</tr>\n<tr>\n")
                else:
                    file.write(f"<td>{line.strip()}</td>\n")

            file.write("</tr>\n</table>\n</body>\n</html>")

def main():
    print("Weather App by ebohler")
    
    weather = WeatherApp()
    coordinates = weather.coords_input()

    json = JSONParser(coordinates)
    gridpoints_json = json.get_gridpoints_json(json.get_points_json())
    periods = JSONParser.create_periods_list(gridpoints_json)

    text = TextFile(coordinates)
    text.write_file(periods)

    html = HTMLTable(coordinates)
    html.create_table(coordinates)
    
if __name__ == "__main__":
    main()