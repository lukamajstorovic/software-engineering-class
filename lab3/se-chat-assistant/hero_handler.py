import json
from query_handler_base import QueryHandlerBase
import requests

class HeroHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "superhero" in query:
            return True
        return False

    def process(self, query):
        _split = query.split()
        name = _split[1]

        try:
            result = self.call_api(name)

            real_name = result["biography"]["fullName"]
            self.ui.say(f"{real_name}")
        except: 
            self.ui.say("Oh no! There was an error trying to contact SuperHero Search api.")
            self.ui.say("Try something else!")
    
    def call_api(self, name):

        url = "https://superhero-search.p.rapidapi.com/api/"

        querystring = {"hero":name}

        headers = {
            "X-RapidAPI-Key": "82ba35bf0amsh3d8939f0f6c3c50p143864jsn8d70f6372921",
            "X-RapidAPI-Host": "superhero-search.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return json.loads(response.text)


