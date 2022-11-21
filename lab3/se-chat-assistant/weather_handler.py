import json
from query_handler_base import QueryHandlerBase
import requests

class WeatherHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "weather" in query:
            return True
        return False

    def process(self, query):
        _split = query.split()
        lon = _split[1]
        lat = _split[2]

        try:
            result = self.call_api(lon, lat)
            city_name = result["data"][0]["city_name"]
            snow = result["data"][0]["snow"]

            self.ui.say(f"\nCity: {city_name}\nSnow:{snow}")
        except: 
            self.ui.say("Oh no! There was an error trying to contact Weather api.")
            self.ui.say("Try something else!")
    
    def call_api(self, lon, lat):

        url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

        querystring = {"lon":lon,"lat":lat}

        headers = {
            "X-RapidAPI-Key": "82ba35bf0amsh3d8939f0f6c3c50p143864jsn8d70f6372921",
            "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return json.loads(response.text)
