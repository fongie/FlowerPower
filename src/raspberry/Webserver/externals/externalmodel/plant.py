import threading, time
from raspberry.Webserver.externals.moistcontrol.arduinoconnection import ArduinoConnection

'''
The Plant class symbolizes a Plant in the system. It handles all communication with the external hardware connected with the plant, such as the moist-sensoring Arduino, and the Tellstick Duo for irrigation.

The class is meant to run as a separate Thread. It loops forever until you call set the variable runSignal to False on the thread, then it stops.

'''
class Plant(threading.Thread):

    ''' Constructor for Plant. Params: plantID, an int identifier. '''
    def __init__(self, plantID):
        threading.Thread.__init__(self)

        self.lastMoistReading = 0
        self.plantID = plantID
        self.arduinoConnection = ArduinoConnection()
        self.runSignal = True

    ''' When started as a thread, loops forever until runSignal is set to False. '''
    def run(self):
        while self.runSignal:
            self.updateMinDryness()
            time.sleep(1) # how often we poll the Arduino for moistness, in seconds
            # time.sleep(60) # production value

    ''' Get the last moist reading from the Arduino connection to this plant '''
    def getMoistness(self):
        return self.lastMoistReading

    def abortWatering(self):
        pass

    ''' Update with a new moist reading from the Arduino '''
    def updateMinDryness(self):
        self.lastMoistReading = self.arduinoConnection.readValue()
