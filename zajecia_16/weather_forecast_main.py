
from weather_forecast import WeatherForecast



# def find_data_in_file():
#     for city, weather in data_in_file.items():
#         if user_city == city:
#             for date, info in data_in_file[city].items():
#                 if user_date == date:
#                     return True
#     return False

# def search_data_in_file():
#     pass


weather_forecast = WeatherForecast()
weather_forecast.read_file()
user_city = input("Podaj miasto, dla którego chcesz sprawdzić pogodę: ")
user_date = input("Podaj datę, dla której chcesz sprawdzić pogodę: ")
weather_forecast.search_for_info(searched_date=user_date, city=user_city)
#print(weather_forecast[user_city, user_date])
#print(weather_forecast.data_from_file.get(user_city).get(user_date))
#weather_forecast["Wroclaw", "2023-11-16"] = "padało"
weather_forecast.write_data_to_file()
# data_in_file: dict = read_data_from_file(file="opady.json")
# if find_data_in_file():
#     search_data_in_file()
# else:
#     search_weather_from_api(searched_date=user_date, city=user_city)
for info in weather_forecast.items():
    print(info)

for info in weather_forecast:
    print(info)