import threading, time
from raspberry.Webserver.externals.moistcontrol.arduinoconnection import ArduinoConnection

'''
The Plant class symbolizes a Plant in the system. It handles all communication with the external hardware connected with the plant, such as the moist-sensoring Arduino, and the Tellstick Duo for irrigation.

The class is meant to run as a separate Thread. It loops forever until you call set the variable runSignal to False on the thread, then it stops.

'''
class Plant(threading.Thread):

# (self, PlantID, ?moistness)

    def __init__(self, plantID):
        threading.Thread.__init__(self)

        self.lastMoistReading = 0
        self.plantID = plantID
        self.arduinoConnection = ArduinoConnection()
        self.runSignal = True

    def run(self):
        while self.runSignal:
            self.updateMinDryness()
            time.sleep(1) # how often we poll the Arduino for moistness, in seconds
            # time.sleep(60) # production value

    def getMoistness(self):
        return self.lastMoistReading

    def abortWatering(self):
        pass

    def updateMinDryness(self):
        self.lastMoistReading = self.arduinoConnection.readValue()
