# Weather App:
## Automatic formatted 7-day forecast via the Weather.gov API

![Forecast Screenshot](https://raw.githubusercontent.com/ebohler/WeatherApp/main/forecast.png)

- Takes a US longitude and latitude as input
- Downloads and parses JSON from the weather.gov API for those coordinates
- Extracts date, time, temperature, and info for the next 7 days and nights
- Dynamically creates HTML table displaying the forecast

### Usage:
#### Prerequisites: 
Python 3.10.9 is the only requirement. This program only uses the standard library so you shouldn't need any packages.
#### Running:
1. Create a folder to store the .py file and HTML output
   ```
   mkdir WeatherApp
   ```
3. Navigate to that directory using command prompt
   ```
   cd WeatherApp
   ```
4. Run weather.py and enter your desired longitude and latitude
   ```
   python weather.py
   ```
6. Open the created HTML file in your browser of choice
