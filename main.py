#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager


manager = DataManager()
f_search = FlightSearch()
notifications = NotificationManager()

sheet_data = manager.get_data()

cities = []
ids = []
prices = []

for data in sheet_data:
    #if data["iataCode"] == "":
    cities.append(data["city"])
    prices.append(data["lowestPrice"])
    ids.append(data["id"])
    
f_search.cities = cities
f_search.get_data()

for i in range(len(cities)):
    manager.code = f_search.codes[i]
    manager.city = cities[i]
    flights = f_search.check_flights(f_search.codes[i])
    manager.price = prices[i]
    manager.update(ids[i])
    if flights[i]["price"] < manager.price:
        cityFrom = flights[i]["cityFrom"]
        cityTo = flights[i]["cityTo"]
        price = flights[i]["price"]
        timeFrom = flights[i]["timeFrom"]
        timeTo = flights[i]["timeTo"]
        url = flights[i]["url"]
        message = f"Low Price Alert! Only ${price}USD to fly from {cityFrom} to {cityTo}, on {timeFrom}."
        notifications.send_sms(message)
    


