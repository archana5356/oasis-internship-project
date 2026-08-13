"""
WeatherSphere Configuration File

Stores API settings and application constants.
"""


# OpenWeatherMap API Key
# Replace this with your own API key

API_KEY = "0997163c41ece157b65e2f1b7efed893"



# OpenWeatherMap Base URLs

WEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather"
)


FORECAST_URL = (
    "https://api.openweathermap.org/data/2.5/forecast"
)


AIR_QUALITY_URL = (
    "https://api.openweathermap.org/data/2.5/air_pollution"
)



# Default Application Settings


DEFAULT_CITY = "Bengaluru"


DEFAULT_UNIT = "metric"


REQUEST_TIMEOUT = 10



# Application Information

APP_NAME = "WeatherSphere"

VERSION = "1.0.0"