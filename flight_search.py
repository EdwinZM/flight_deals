import requests
from pprint import pprint
import datetime as dt

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.cities = ''
        self.apiKey = "U_SYg1fInoAuNTLVFJ3mW9Dur00RRgT9"
        self.codes = []
        self.now = dt.datetime.now()
        self.tomorrow = int(self.now.day) + 1
        self.six_months = int(self.now.month) + 6
        

    def get_data(self):
        for city in self.cities:
            headers = {
            "apikey": self.apiKey
            }
            params = {
                "term": city,
                "location_types": "city"
            }
            response = requests.get("https://tequila-api.kiwi.com/locations/query", params=params, headers=headers)
            response.raise_for_status()
            data = response.json()["locations"]
            code = data[0]["code"]
            self.codes.append(code)

    def check_flights(self, code):
        headers = {
            "apikey": self.apiKey
        }
        params = {
            "fly_from": "city:CUN",
            "fly_to": f"city:{code}",
            "curr": "USD"
        }
        response = requests.get(url="https://tequila-api.kiwi.com/v2/search", params=params, headers=headers)
        response.raise_for_status()
        data = response.json()["data"]
        flight_datas = []
        for d in data:
            route = d["route"][0]
            local_departure = route["local_departure"].split("T")[0]
            local_month = local_departure.split("-")[1]
            local_day = local_departure.split("-")[0]
            if int(local_day) >= self.tomorrow and int(local_month) < self.six_months:
                city = d["cityTo"]
                price = d["price"]
                flight_data = {
                    "cityTo": city,
                    "cityFrom": "CUN",
                    "timeFrom": local_departure,
                    "timeTo": route["return"],
                    "price": price,
                    "url": d["booking_token"]
                }
                flight_datas.append(flight_data)
            else:
                print("No Flights")
        return flight_datas
                