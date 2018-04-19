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
        if(newPlant in self.plants):
            p = self.plants.get(newPlant)
            return p.getMoistness()
        else:
            self.createPlant(newPlant)
            p = self.plants.get(newPlant)
            return p.getMoistness()

    def createPlant(self, newPlant):
        p = plant.Plant(newPlant)
        p.start()
        p.name = "plant" + str(newPlant)
        self.plants[newPlant] = p

    def terminatePlant(self, oldPlant):
        p = self.plants.get(oldPlant)
        p.runSignal = False
        p.join()
        del self.plants[oldPlant]
