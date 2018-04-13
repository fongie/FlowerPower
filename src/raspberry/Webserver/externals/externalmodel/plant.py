import threading

'''
https://stackoverflow.com/questions/19033818/how-to-call-a-function-on-a-running-python-thread

men ska vi verkligen köra en thread hela tiden?? kanke bättre att först åtminstone låta externalcontroller spawna trådar som kollar alla blommor vid behov i stället
'''

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
