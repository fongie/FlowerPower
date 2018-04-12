import threading

class Plant(threading.Thread):

    def __init__(self, plantID):
        threading.Thread.__init__(self)
        self.lastMoistReading = 0
        self.plantID = plantID

    def run(self):
        while True:
            pass

    def getMoistness(self):
        return self.lastMoistReading

    def abortWatering():
        pass

    def updateMinDryness():
        pass
