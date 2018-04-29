import pytest
from raspberry.Webserver.website.database.databasehandler import DatabaseHandler

dbh = DatabaseHandler()

def test_isValid():
    try:
        uname = 'testuname'
        pwd = 'testpwd'
        result = dbh.isValid(uname, pwd)
        
    except:
        result = 'Could not login, invalid username and/or password.'
        
    assert result
    
def test_databaseConnection():
    try:
        result = dbh.databaseConnection()
        
    except:
        result = 'Could not connect to database.'
        
    assert result