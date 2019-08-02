import requests
import time
import json

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

        return self.sendMessage(data)
    
    def sendMessage(self, data):
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        message = f"Hello, \r\nThis is the weather forecast for the day.\r\nIn {self.name}, it will be {temp}&#176;C.\r\nThe weather: {weather}.\r\nHave a great day !"
        # message = f"Hello, \r\nThis is the weather forecast for the day.\r\nIn {self.name}, it will be {temp}°C.\r\nThe weather: {weather}.\r\nHave a great day !"

        return message

class CacheManager:
    cached = False
    value = None
    registeredTime = None

    def __init__(self, cached = False, value = None, registeredTime = None):
        self.cached = cached
        self.value = value
        self.registeredTime = registeredTime
        return

    def getCurrentTime(self):
        return time.asctime()
    
    def getRegisteredTime(self):
        return self.registeredTime if self.registeredTime != None else "no registered time" 

    def getTimeDiff(self):
        diff = None

        if self.registeredTime == None:
            return f"{json.dumps(self.getCurrentTime())}"
        else:
            diff = "hello"
            return f"{json.dumps(diff)}"