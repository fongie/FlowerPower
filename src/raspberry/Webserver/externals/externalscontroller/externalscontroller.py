class ExternalsController:

    instance = None
    plants = dict()

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

    def readPlantStatus(self, plant):
        if(plant in plants):
            p = plants.get(plant)
            return p.getMoistness()
        else:
            createPlant(plant)
            p = plants.get(plant)
            return p.getMoistness()

    def createPlant(self, plant):
        p = Plant(plant)
        p.start()
        plants.d([plant]) = p
