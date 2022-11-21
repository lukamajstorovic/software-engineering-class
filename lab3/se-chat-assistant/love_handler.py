import random
import requests
import json
from query_handler_base import QueryHandlerBase

class LoveHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "love" in query:
            return True
        return False

    def process(self, query):
        names = query.split()
        fname = names[1]
        sname = names[2]

        try:
            result = self.call_api(fname, sname)
            score = result["percentage"]
            text = result["result"]
            self.ui.say(f"Love score between {fname} and {sname} is {score}%")
            self.ui.say(f"The doctor said: {text}")
        except: 
            self.ui.say("Oh no! There was an error trying to contact Love api.")
            self.ui.say("Try something else!")



    def call_api(self, fname, sname):
        url = "https://love-calculator.p.rapidapi.com/getPercentage"

        querystring = {"fname":fname,"sname":sname}

        headers = {
                "X-RapidAPI-Key": "82ba35bf0amsh3d8939f0f6c3c50p143864jsn8d70f6372921",
                "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return json.loads(response.text)
