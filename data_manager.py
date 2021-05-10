import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.city = ''
        self.code = ''
        self.price = ''
        self.endpoint = "https://api.sheety.co/6908813dfc831abe26a53f2b064e330a/flightDeals/prices"
        

    def post_data(self):
        data = {
            "price":{
                "city": self.city,
                "iataCode": self.code,
                "lowestPrice": self.price               
            }
        }
        sheet_res = requests.post(url=self.endpoint, json=data)
        print(sheet_res.json())

    def get_data(self):
        response = requests.get(self.endpoint)
        response.raise_for_status()
        return response.json()["prices"]

    def update(self, id_):
        data = {
            "price":{
                "city": self.city,
                "iataCode": self.code,
                "lowestPrice": self.price               
            }
        }
        update_res = requests.put(url=f"{self.endpoint}/{id_}", json=data)