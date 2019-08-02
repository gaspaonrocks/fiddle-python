from weather_api import City
from weather_api import CacheManager

def getCity():
  city = City()
  return city.getWeatherData()

def getTime():
  cacheMan = CacheManager()
  return cacheMan.getTimeDiff()

routes = {
  "/" : getCity(),
  "/goodbye" : "Goodbye World",
  "/time": getTime()
}