import tellcore.telldus, time

class TellstickHandler:
    '''
    Handles all interactions with the Tellstick system controlling the water pump
    '''
    DEVICE_NAME = "Pump"

    ''' Constructor. No parameters '''
    def __init__(self):
        self.telldus = tellcore.telldus.TelldusCore()
        # self.pump = self.telldus.devices()[0]
        self.pump = self._findDevice()
        self.isTurnedOn = False

    def turnOn(self):
        ''' Turns on the tellstick '''
        if not self.isTurnedOn:
            try:
                self.pump.turn_on()
                time.sleep(0.5)
                self.pump.turn_on() # sometimes the switch doesnt recognize the first call
                self.isTurnedOn = True
                return True
            except:
                return False
        else:
            raise AssertionError('Tried to turn on pump that was already on!')

    def turnOff(self):
        ''' Turns off the tellstick '''
        if self.isTurnedOn:
            try:
                self.pump.turn_off()
                self.isTurnedOn = False
                return True
            except:
                return False
        else:
            raise AssertionError('Tried to turn off pump that was not turned on!')

    def _findDevice(self):
        for d in self.telldus.devices():
            if d.name == self.DEVICE_NAME:
                return d

    # You should be able to initialize a new plant (w/ tellstick) through the website, or do initial setup
    #
    # def learnNewDevice(self):
    #     pass
