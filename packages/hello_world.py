from weather_api import CacheManager
# basic interactive greeting script
def helloWorld(name = "Sacha"):
    print(f"Hello, {name}")

helloWorld("blyat")

cache = CacheManager()

print(cache.getCurrentTime())