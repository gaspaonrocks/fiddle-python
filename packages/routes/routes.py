from weather_api import City
from weather_api import CacheManager

# instanciating here to prevent resetting values on each request
city = City()
cacheMan = CacheManager()

def getCity():
  return city.getWeatherData()

def getTime():
  return cacheMan.getTimeDiff()

def returnMethod(arg: str):
  routes = {
    "/" : getCity,
    "/time": getTime,
    #"/favicon.ico": None #prevents the browser to look for favicon.ico and crash #makes the script bug because it tries to call the value associated
  }
  return routes.get(arg, lambda: "Invalid route")()