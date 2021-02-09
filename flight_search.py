class FlightSearch:
    def __init__(self, spreadsheet_data_manager, flight_data_manager, notification_manager):
        self.spreadsheet_data_manager = spreadsheet_data_manager
        self.flight_data_manager = flight_data_manager
        self.notification_manager = notification_manager

    def check_flights(self):
        data = self.spreadsheet_data_manager.get_data()
        data_sheet = data["prices"]

        for destination in data_sheet:
            origin_city_code = "LON"
            des_city_code = destination["iataCode"]
            des_city = destination["city"]
            max_price = destination["lowestPrice"]

            flight_data = self.flight_data_manager.get_flight_data(origin_city_code, des_city_code)

            if flight_data is None:
                continue

            origin_city = flight_data["cityFrom"]
            current_price = flight_data["price"]
            out_date = flight_data["out_date"]
            return_date = flight_data["return_date"]

            if current_price is not None and current_price <= max_price:
                message = f"Low price alert! Only £{current_price} to fly from {origin_city}-{origin_city_code} to " \
                          f"{des_city}-{des_city_code}, from {out_date} to {return_date}."
                self.notification_manager.send_sms(message)

                user_data = self.spreadsheet_data_manager.get_user_data()

                for user in user_data["users"][0]:
                    self.notification_manager.send_email(user)
