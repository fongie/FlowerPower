import threading, time, requests
from raspberry.Webserver.externals.moistcontrol.arduinoconnection import ArduinoConnection
from raspberry.Webserver.externals.irrigation.tellstickhandler import TellstickHandler
from raspberry.Webserver.externals.notification.notificationsender import NotificationSender

'''
The Plant class symbolizes a Plant in the system. It handles all communication with the external hardware connected with the plant, such as the moist-sensoring Arduino, and the Tellstick Duo for irrigation.

The class is meant to run as a separate Thread. It loops forever until you call set the variable runSignal to False on the thread, then it stops.

'''
class Plant(threading.Thread):

    ''' Constructor for Plant.
    Params:
        plantID (int), an int identifier.
        wateringTime (int), how long pump is turned on each watering
        emailToNotify (str), where to send notifications'''
    def __init__(self, *args):
        threading.Thread.__init__(self)

        self.noContactWithArduinoCounter = 0
        self.lastMoistReading = -1
        self.drynessTrigger = 500
        self.plantID = args[0]

        self.didNotSendNotificationYet = True

        if len(args) > 1:
            self.wateringTime = args[1]
            if len(args) > 2:
                self.notificationSender = NotificationSender(self.plantID, args[2])
        else:
            self.wateringTime = 3
            self.notificationSender = NotificationSender(self.plantID, "flowerpowerkth@gmail.com") #default, change?

        self.arduinoConnection = ArduinoConnection()
        self.tellstickHandler = TellstickHandler()
        self.runSignal = True

    ''' When started as a thread, loops forever until runSignal is set to False. '''
    def run(self):
        while self.runSignal:
            self.updateMinDryness()
            time.sleep(1) # how often we poll the Arduino for moistness, in seconds
            # time.sleep(60) # production value

    ''' Get the last moist reading from the Arduino connection to this plant '''
    def getMoistness(self):
        if self.lastMoistReading >= 0:
            return self.lastMoistReading
        else:
            #self.runSignal = False
            raise ValueError('Could not get an updated value from the Arduino moistsensor!')

    ''' Set below which value the low moistness notification is sent '''
    def setDrynessTrigger(self, value):
        self.drynessTrigger = value

    ''' Updates current moist value with a new moist reading from the Arduino '''
    def updateMinDryness(self):

        #note: right now only sends notification ONCE and then never again if thread stays alive
        if (0 <= self.lastMoistReading < self.drynessTrigger) and self.didNotSendNotificationYet:
            self.notificationSender.sendDrynessNotification(self.lastMoistReading)
            self.didNotSendNotificationYet = False

        try:
            self.lastMoistReading = self.arduinoConnection.readValue()
        except requests.ConnectionError:
            self.noContactWithArduinoCounter += 1
            if self.noContactWithArduinoCounter > 5: # if we tried too many times to reach arduino and couldnt, we dont have a value
                self.lastMoistReading = -1

    ''' Water the plant by turning on the pump, keeping it on for self.wateringTime seconds, and turning it off. Raises AssertionError if turning on or turning off was unsuccessful. '''
    def waterPlant(self):
        on = self.tellstickHandler.turnOn()
        if not on:
            raise AssertionError('Cannot turn on water pump using TellstickHandler')
        time.sleep(self.wateringTime)
        off = self.tellstickHandler.turnOff()
        if not off:
            raise AssertionError('WARNING Water pump was turned on but not turned off!')
        return

    ''' Set which email notifications are sent to '''
    def setEmail(self,userEmail):
        if hasattr(self, 'notificationSender'):
            self.notificationSender.setEmail(userEmail)

    ''' Instantly turn off ongoing watering '''
    def abortWatering(self):
        self.tellstickHandler.turnOff()
        time.sleep(1)
        self.tellstickHandler.turnOff()
