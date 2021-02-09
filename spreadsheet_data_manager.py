import requests as req
from decouple import config


class SpreadsheetDataManager:
    def __init__(self, flight_data_manager):
        self.ENDPOINT = config("SHEETY_ENDPOINT")
        self.ENDPOINT_USERS = config("SHEETY_ENDPOINT_USERS")
        self.TOKEN = config("SHEETY_TOKEN")

        self.flight_data_manager = flight_data_manager

    def get_data(self):
        headers = {"Authorization": f"Bearer {self.TOKEN}"}
        res = req.get(self.ENDPOINT, headers=headers)
        res.raise_for_status()
        return res.json()

    def get_user_data(self):
        headers = {"Authorization": f"Bearer {self.TOKEN}"}
        res = req.get(self.ENDPOINT_USERS, headers=headers)
        res.raise_for_status()
        return res.json()

    def post_user_data(self, f_name, l_name, email):
        headers = {"Authorization": f"Bearer {self.TOKEN}"}
        inputs = {
            "user": {
                "firstName": f_name,
                "lastName": l_name,
                "email": email
            }
        }

        res = req.post(self.ENDPOINT_USERS, json=inputs, headers=headers)
        res.raise_for_status()
        print("'users' sheet post successful")


    def _update_row(self, row_id, column, iata_code):
        headers = {"Authorization": f"Bearer {self.TOKEN}"}
        inputs = {"price": {column: iata_code}}
        req.put(f"{self.ENDPOINT}/{row_id}", json=inputs, headers=headers)

    def _update_city_codes(self):
        data = self.get_data()
        for row in data["prices"]:
            if row["iataCode"] == "":
                code = self.flight_data_manager.get_destination_city_code(row["city"])
                self._update_row(row["id"], "iataCode", code)
