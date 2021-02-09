from spreadsheet_data_manager import SpreadsheetDataManager
from flight_data_manager import FlightDataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from ui import UI


class App:
    def __init__(self):
        self.ui = UI()
        self.flight_data_manager = FlightDataManager()
        self.spreadsheet_data_manager = SpreadsheetDataManager(self.flight_data_manager)
        self.notification_manager = NotificationManager()
        self.flight_search = FlightSearch(
            self.spreadsheet_data_manager,
            self.flight_data_manager,
            self.notification_manager
        )

    # PUBLIC METHODS
    def start(self):
        self.flight_search.check_flights()
