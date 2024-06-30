# Weather App:
## Automatic formatted 7-day forecast via the Weather.gov API

![Forecast Screenshot](https://raw.githubusercontent.com/ebohler/WeatherApp/main/forecast.png)
[Example HTML Table](https://github.com/ebohler/WeatherApp/blob/main/39.7456%2C-97.0892.html)

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
4. Run weather.py
   ```
   python weather.py
   ```
5. Enter your desired longitude and latitude
   ```
   Longitude: 39.3813
   Latitude: -97.1211
   ```
7. Open the created HTML file in your browser of choice
   ```
   39.3813,-97.1211.html
   ```
