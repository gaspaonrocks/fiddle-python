import requests
import json
from cache_manager import CacheManager

apiKey = "1bb8b9643fcf40f10d845bc78c254b76"
# to get the weather during the day 
# see how to deal with time increments
apiUrlForecast = "http://api.openweathermap.org/data/2.5/forecast"
apiUrlCurrent = "http://api.openweathermap.org/data/2.5/weather"

class City:
    id = 6455058
    name = "Bordeaux"
    country = "FR"
    coord = { 
        # A property can only have a string as name
        # no single/double quotes means it is a variable
        "lon": -0.56667,
        "lat": 44.833328
    }
    cacheManager = CacheManager()

    def __init__(self, name = None):
        print("This is the city constructor method")
        # TODO: get name/coordinates from GPS to list of city, 
        # => map method and return the city we're in
        if name == None:
            return
        else:
            self.name = name
    
    def getCoord(self):
        # accessing a property of an object
        longitude, latitude = self.coord["lon"], self.coord["lat"]
        print(f'Lon: {longitude}, lat: {latitude} are the coordinates of {self.name}')

    def getWeatherData(self):
        params = {
            "id": {self.id},
            "APPID": {apiKey},
            "units": "metric"
        }

        # parameters must ALL be fulfilled and affected to their real names
        r = requests.get(url = apiUrlCurrent, params = params)

        data = r.json()

        self.cacheManager.registerValue(key = "forecast", value = data)

        return self.sendMessage(self.cacheManager.getValue(key = "forecast"))
    
    def sendMessage(self, data):
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        message = f"Hello,<br>This is the weather forecast for the day.<br>In {self.name}, it will be {temp}&#176;C.<br>The weather: {weather}.<br>Have a great day !"

        return message