import os
import requests
from json import JSONDecodeError
from cachetools import cached, TTLCache

DARKSKY_BASE_URL = os.environ.get('DARKSKY_BASE_URL', 'https://api.pirateweather.net/')
DARKSKY_API_KEY = os.environ.get('DARKSKY_API_KEY', 'NO_API_KEY')
LATITUDE = os.environ.get('LATITUDE', '0.00')
LONGITUDE = os.environ.get('LONGITUDE', '0.00')


def current_weather():
    return _current_weather(_forecast(LATITUDE, LONGITUDE))


def todays_forecast():
    return _todays_forecast(_forecast(LATITUDE, LONGITUDE))


def weekly_forecast():
    return _weekly_forecast(_forecast(LATITUDE, LONGITUDE))


def _current_weather(forecast_response):
    current_weather = forecast_response['currently']
    weather_summary = "{weather_summary} {temperature} C".format(
        **{
            'weather_summary':  current_weather['summary'],
            'temperature':  current_weather['temperature']
        })

    if forecast_response.get('precipProbability', 0) != 0:
        weather_summary += " {precip_probability} chance of {precip_type} with intensity {precip_intensity}".format(
            **{
                'precip_probability':   current_weather['precipProbability'] * 100,
                'precip_type':  current_weather['precipType'],
                'precip_intensity':  current_weather['precipIntensity']
            }
        )
    return weather_summary


def _todays_forecast(forecast_response):

    return forecast_response['hourly']['summary']


def _weekly_forecast(forecast_response):

    return forecast_response['daily']['summary']


@cached(cache=TTLCache(maxsize=10, ttl=600))
def _forecast(latitude, longitude):
    api_response = requests.get(_forecast_request_url(latitude, longitude))
    if not api_response.ok:
        return 'Cannot fetch weather from darksky'
    try:
        json_response = api_response.json()
    except (JSONDecodeError, KeyError):
        return 'Cannot parse darksky response'

    return json_response


def _forecast_request_url(latitude, longitude, units='si'):
    return "{base_url}/forecast/{api_key}/{latitude},{longitude}?units={units}".format(
        **{
            'base_url': DARKSKY_BASE_URL,
            'api_key': DARKSKY_API_KEY,
            'latitude': latitude,
            'longitude': longitude,
            'units': units
        }
    )
