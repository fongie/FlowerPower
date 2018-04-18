import threading, time

'''
The Plant class symbolizes a Plant in the system. It handles all communication
with the external hardware connected with the plant, such as the moist-sensoring
Arduino, and the Tellstick Duo for irrigation.
The class is meant to run as a separate Thread. It loops forever until you call
set the variable runSignal to False on the thread, then it stops.
https://stackoverflow.com/questions/19033818/how-to-call-a-function-on-a-running-python-thread
TODO: prevent race condition
'''
class Plant(threading.Thread):

    def __init__(self, *args):
        threading.Thread.__init__(self)
        if len(args) == 1:
            self.lastMoistReading = 0
            self.plantID = args[0]
            self.runSignal = True
        elif len(args) == 2: # for testing purposes. provides a hardcoded moistnessvalue
            self.lastMoistReading = args[1]
            self.plantID = args[0]
            self.runSignal = True

    def run(self):
        while self.runSignal:
            self.updateMinDryness()
            time.sleep(2) # how often we poll the Arduino for moistness, in seconds

    def getMoistness(self):
        return self.lastMoistReading

    def abortWatering(self):
        pass

    def updateMinDryness(self):
        pass
