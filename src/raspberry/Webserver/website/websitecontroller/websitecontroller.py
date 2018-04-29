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
            result = ec.updateMinDryness(minDryness)
            
        except:
            result = 'Minimum dryness value could not be set.'
        
        return result
