from raspberry.Webserver.externals.externalscontroller.externalscontroller import ExternalsController
from raspberry.Webserver.website.websitemodel.useraccounthandler import UserAccountHandler

class WebsiteController:
    def __init__(self):
        pass

    def getPlants(self):
        ec = ExternalsController.getInstance()
        moistValue = ec.readPlantStatus(1)
        return moistValue
    
    def login(self, uname, pwd):
        uah = UserAccountHandler()
        testi = uah.login(uname, pwd)
        return testi