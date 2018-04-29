from raspberry.Webserver.externals.externalmodel import plant
import threading
class ExternalsController:

    instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ExternalsController.instance == None:
            ExternalsController()
        return ExternalsController.instance

    def __init__(self):
        """ Virtually private constructor. """
        if ExternalsController.instance != None:
            raise Exception("This class is a singleton!")
        else:
            ExternalsController.instance = self
            self.plants = dict()

    def readPlantStatus(self, newPlant):
        if(newPlant not in self.plants):
            self.createPlant(newPlant)

        p = self.plants.get(newPlant)
        try:
            moistness = p.getMoistness()
        except:
            raise RuntimeError('Could not get value from plant')
        return moistness

    def createPlant(self, newPlant):
        if(newPlant not in self.plants):
            p = plant.Plant(newPlant)
            p.start()
            p.name = "plant" + str(newPlant)
            self.plants[newPlant] = p

    def terminatePlant(self, oldPlant):
        if(newPlant in self.plants):
            p = self.plants.get(oldPlant)
            p.runSignal = False
            p.join()
            del self.plants[oldPlant]

    def waterPlant(self, plantID):
        try:
            self.plants.get(plantID).waterPlant()
        except:
            raise RuntimeError('Could not start watering')

    def turnOffSprinkler(self, plantID):
        try:
            self.plants.get(plantID).abortWatering()
        except:
            raise RuntimeError('Could not turn off watering')

    def updateMinDryness(self, plantID, minDryness):
        if(newPlant in self.plants):
            self.plants.get(plantID).setDrynessTrigger(minDryness)

    def setEmailForPlant(self, plantID, userEmail):
        pass

    def isActive(self, plantID):
        if plantID not in self.plants:
            running = False
        else:
            running = self.plants.get(plantID).isAlive()
        return running
