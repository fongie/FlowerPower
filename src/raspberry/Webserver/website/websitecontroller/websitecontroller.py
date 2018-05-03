from raspberry.Webserver.externals.externalscontroller.externalscontroller import ExternalsController
from raspberry.Webserver.website.websitemodel.useraccounthandler import UserAccountHandler

ec = ExternalsController.getInstance()

class WebsiteController:
    def __init__(self):
        pass

    def getPlants(self):
        try:
            moistValue = ec.readPlantStatus(1)
            
        except: 
            moistValue = 'Moist value could not be read.'
            
        return moistValue
    
    def login(self, uname, pwd):
        uah = UserAccountHandler()
        result = uah.login(uname, pwd)
        return result

    def setMinDryness(self, minDryness):
        try:
            ec.updateMinDryness(1, int(minDryness))
            result = "Updated!"
            
        except:
            result = 'Minimum dryness value could not be set.'
        
        return result

    def waterPlant(self):
        try:
            ec.waterPlant(1)
            result = 'Plant watered!'
            return result
        except:
            error = 'Could not water plant.'
            return error
