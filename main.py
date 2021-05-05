#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager


manager = DataManager("Cancun", "CUN", "300")
f_search = FlightSearch()

sheet_data = manager.get_data()

cities = []
for data in sheet_data:
    if data["iataCode"] == "":
        cities.append(data["city"])

f_search.cities = cities

print(f_search.cities)