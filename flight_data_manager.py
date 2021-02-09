import requests as req
from datetime import datetime, timedelta
from decouple import config


class FlightDataManager:
    def __init__(self):
        self.ENDPOINT = config("TEQUILA_ENDPOINT")
        self.KEY = config("TEQUILA_KEY")

    def get_destination_city_code(self, city_name):
        location_endpoint = f"{self.ENDPOINT}/locations/query"
        headers = {"apikey": self.KEY}
        params = {"term": city_name, "location_types": "city"}
        res = req.get(url=location_endpoint, headers=headers, params=params)
        res.raise_for_status()
        code = res.json()["locations"][0]["code"]
        return code

    def get_flight_data(self, origin_city_code, destination_city_code):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime(f"%m/%d/%Y")
        six_months_from_today = (datetime.now() + timedelta(days=(6 * 30))).strftime(f"%m/%d/%Y")

        endpoint = f"{self.ENDPOINT}/v2/search"
        headers = {"apikey": self.KEY}
        params = {
            "curr": "GBP",
            "date_from": tomorrow,
            "date_to": six_months_from_today,
            "flight_type": "round",
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "max_stopovers": 0,
            # "nights_in_dst_from": 7,
            # "nights_in_dst_to": 28,
            # "one_for_city": 1
        }

        res = req.get(url=endpoint, headers=headers, params=params)
        res.raise_for_status()

        try:
            return res.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None
