from datetime import datetime

class CacheManager:
    cached = False
    storage = {}
    registeredTime = None

    def __init__(self, cached = False, storage = {}):
        self.cached = cached
        self.storage = storage

    def getCurrentTime(self):
        print("this is the time")
        return datetime.now()
    
    def getRegisteredTime(self):
        return self.registeredTime if self.registeredTime != None else self.getCurrentTime() 

    def getTimeDiff(self):
        print(self.registeredTime != None)

        if self.registeredTime == None:
            print("hello")
            self.registeredTime = self.getCurrentTime()
            return f"{self.registeredTime.ctime()}"
        else:
            then = self.getRegisteredTime()
            now = self.getCurrentTime()
            diff =  now - then
            return f"{diff.seconds}"
    
    def registerValue(self, key, value):
        self.storage[key] = value
    
    def getValue(self, key):
        return self.storage[key]