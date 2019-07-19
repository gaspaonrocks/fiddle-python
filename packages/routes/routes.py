from weather_api import City

def getCity():
    city = City()
    return city.getWeatherData()

routes = {
  "/" : getCity(),
  "/goodbye" : "Goodbye World"
}