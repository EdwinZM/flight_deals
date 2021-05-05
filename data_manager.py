import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, city, code, price):
        self.city = city
        self.code = code
        self.price = price

    def post_data(self):
        data = {
            "price":{
                "city": self.city,
                "iataCode": self.code,
                "lowestPrice": self.price               
            }
        }
        sheet_res = requests.post(url="https://api.sheety.co/cb662cbd335c18760ecd9cb30b9d13b1/flightDeals/prices", json=data)
        print(sheet_res.json())

    def get_data(self):
        response = requests.get("https://api.sheety.co/cb662cbd335c18760ecd9cb30b9d13b1/flightDeals/prices")
        response.raise_for_status()
        return response.json()["prices"]