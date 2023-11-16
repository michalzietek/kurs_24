from typing import Optional
import requests
from geopy.geocoders import Nominatim
import json

class WeatherForecast:
    def __init__(self):
        self.file = "opady.json"
        self.data_from_file: Optional[dict] = None

    def read_file(self):
        with open(self.file) as file:
            self.data_from_file = json.loads(file.read())

    def write_data_to_file(self):
        with open(self.file, mode="w") as file:
            file.write(json.dumps(self.data_from_file))


    def get_longitute_and_latitude_from_city(self, city):
        geolocator = Nominatim(user_agent="weather_forecast")
        location = geolocator.geocode(city)
        return location.latitude, location.longitude

    def parse_response_to_find_rain(self, response):
        response_dict = json.loads(response)
        rain_sum = response_dict.get("daily").get("rain_sum")[0]# zwykla liczba
        if rain_sum == 0:
            return "Nie padało"
        elif rain_sum > 0:
            return "Padało"
        else:
            return "Dane są błędne"
        # sprawdzenie, czy padalo czy nie padalo (instrukcja warunkowa)

    def search_weather_from_api(self, searched_date, city):
        longitude, latitude = self.get_longitute_and_latitude_from_city(city)
        url_address = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain"
                       f"&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}")
        response = requests.get(url=url_address)
        if response.status_code == 200:
            weather_info = self.parse_response_to_find_rain(response.text)
            if self.data_from_file.get(city):
                self.data_from_file[city][searched_date] = weather_info
            else:
                self.data_from_file[city] = {}
                self.data_from_file[city][searched_date] = weather_info
        else:
            print("Niestety, nie mogliśmy pobrać danych pogodowych twojego miasta")

    def __getitem__(self, item):
        searched_city, searched_date = item
        for city_key, city_data in self.data_from_file.items():
            if searched_city == city_key:
                for date, information in city_data.items():
                    if searched_date == date:
                        return f"{information} w dniu {searched_date} w {searched_city}"
        return None

    def __setitem__(self, key, value):
        #to do zrobienia samemu w domu - sprawdzenie czy takie miasto juz mamy
        #tez sprawdzic, czy juz takich danych nie mamy wewnatrz naszego pliku
        city, date = key
        self.data_from_file[city][date] = value
        print(self.data_from_file)

    def items(self):
        for city, city_data in self.data_from_file.items():
            for date, information in city_data.items():
                yield f"{city}, {date}: {information}"

    def __iter__(self):
        return iter(self.data_from_file) #mozna pokombinowac i iterowac po wartosciach albo czym chcecie

    def search_for_info(self, searched_date, city):
        if data_info := self.data_from_file.get(city).get(searched_date):
            print(data_info)
        else:
            self.search_weather_from_api(searched_date, city)