"""
WeatherSphere
Weather API Module
"""

import requests

from config import API_KEY, WEATHER_URL, FORECAST_URL, REQUEST_TIMEOUT


def get_weather(city):
    """
    Fetch current weather data
    """

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        response = requests.get(
            WEATHER_URL,
            params=params,
            timeout=REQUEST_TIMEOUT
        )

        data = response.json()

        if response.status_code != 200:
            return {
                "error": data.get(
                    "message",
                    "Unable to fetch weather."
                )
            }

        weather = {

            "city": data["name"],

            "country": data["sys"]["country"],

            "temperature": data["main"]["temp"],

            "feels": data["main"]["feels_like"],

            "humidity": data["main"]["humidity"],

            "pressure": data["main"]["pressure"],

            "wind": data["wind"]["speed"],

            "visibility": data["visibility"] / 1000,

            "condition": data["weather"][0]["description"],

            "icon": data["weather"][0]["icon"]

        }

        return weather

    except requests.exceptions.Timeout:

        return {
            "error": "Connection Timeout"
        }

    except requests.exceptions.ConnectionError:

        return {
            "error": "No Internet Connection"
        }

    except Exception as e:

        return {
            "error": str(e)
        }


def get_forecast(city):
    """
    Fetch 5-day / 3-hour forecast
    """

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        response = requests.get(
            FORECAST_URL,
            params=params,
            timeout=REQUEST_TIMEOUT
        )

        data = response.json()

        if response.status_code != 200:
            return []

        forecast = []

        for item in data["list"][:10]:

            forecast.append({

                "time": item["dt_txt"],

                "temperature": item["main"]["temp"],

                "condition": item["weather"][0]["description"],

                "icon": item["weather"][0]["icon"]

            })

        return forecast

    except Exception:

        return []