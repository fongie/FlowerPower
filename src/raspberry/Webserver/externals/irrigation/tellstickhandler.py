import tellcore.telldus
#import tellcore.constants

class TellstickHandler:

    def __init__(self):
        self.telldus = tellcore.telldus.TelldusCore()
        self.pump = self.telldus.devices()[0]
        self.isTurnedOn = False

    def turnOn(self):
        if not self.isTurnedOn:
            try:
                self.pump.turn_on()
                self.isTurnedOn = True
                return True
            except:
                return False

    def turnOff(self):
        if self.isTurnedOn:
            try:
                self.pump.turn_off()
                self.isTurnedOn = False
                return True
            except:
                return False


    # You should be able to initialize a new plant (w/ tellstick) through the website, or do initial setup
    #
    # def learnNewDevice(self):
    #     pass
