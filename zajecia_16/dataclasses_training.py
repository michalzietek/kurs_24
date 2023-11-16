from dataclasses import dataclass

class WeatherForecastUpstream:
    def __init__(self, latitude, longitude, rain_sum, daily):
        self.lattitude: str = latitude
        self.longitude: str = longitude
        self.rain_sum: str = rain_sum


@dataclass
class Daily:
    time: list[str]
    rain_sum: list[str]

    def validate_time(self):
        #kod odpowiedzialny za walidacje czasu


@dataclass
class WeatherForecastUpstreamDataclass:
    latitude: str
    longitude: str
    daily: Daily


weather_forecast_response = {"latitude":17.0,"longitude":51.12500,"daily":{"time":["2023-10-10"],"rain_sum":[0.00]}}

weather_forecast_dataclass = WeatherForecastUpstreamDataclass(**weather_forecast_response)
print(weather_forecast_dataclass)

