from weather_api import City
from weather_api import CacheManager

# instanciating here to prevent resetting values on each request
city = City()
cacheMan = CacheManager()

def getCity():
  return city.getWeatherData()

def getTime():
  return cacheMan.getTimeDiff()

routes = {
  "/" : getCity,
  "/goodbye" : "Goodbye World",
  "/time": getTime,
  "/favicon.ico": "nothing" #prevents the browser to look for favicon.ico and crash
}