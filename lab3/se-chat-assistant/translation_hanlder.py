import json
from query_handler_base import QueryHandlerBase
import random
import requests

class TranslationHandler(QueryHandlerBase):
    def can_process_query(self, query):
        if "translate" in query:
            return True
        return False

    def process(self, query):
        _split = query.split()
        input = _split[1]
        translate_from = _split[2]
        translate_to = _split[3]


        try:
            result = self.call_api(input, translate_from, translate_to)

            translation = result["data"]["translations"][0]["translatedText"]
            self.ui.say(f"{translation}")
        except: 
            self.ui.say("Oh no! There was an error trying to contact Google Translate api.")
            self.ui.say("Try something else!")
    
    def call_api(self, input, translate_from, translate_to):

        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        payload = f"q={input}&target={translate_to}&source={translate_from}"
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "application/gzip",
            "X-RapidAPI-Key": "82ba35bf0amsh3d8939f0f6c3c50p143864jsn8d70f6372921",
            "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        return json.loads(response.text)


