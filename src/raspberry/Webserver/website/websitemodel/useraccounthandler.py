from raspberry.Webserver.website.database.databasehandler import DatabaseHandler


class UserAccountHandler:
    def __init__(self):
        pass
    
    def login(self, uname, pwd):
        dbh = DatabaseHandler()
        testi = dbh.isValid(uname, pwd)
        return testi