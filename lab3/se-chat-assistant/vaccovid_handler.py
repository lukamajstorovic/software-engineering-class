import json
from query_handler_base import QueryHandlerBase
import random
import requests

class VacCovidHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "covid" in query:
            return True
        return False

    def process(self, query):
        _split = query.split()
        country = _split[1]

        try:
            result = self.call_api(country)

            total_cases = result[0]["total_cases"]
            new_cases = result[0]["new_cases"]
            self.ui.say(f"\n{country}:\nTotal cases: {total_cases}\nNew cases: {new_cases}")
        except: 
            self.ui.say("Oh no! There was an error trying to contact VACCOVID api.")
            self.ui.say("Try something else!")
    
    def call_api(self, country):

        url = f"https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/covid-ovid-data/sixmonth/{country}"

        headers = {
            "X-RapidAPI-Key": "82ba35bf0amsh3d8939f0f6c3c50p143864jsn8d70f6372921",
	        "X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        return json.loads(response.text)


