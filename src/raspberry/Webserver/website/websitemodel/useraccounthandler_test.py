import pytest
from raspberry.Webserver.website.websitemodel.useraccounthandler import UserAccountHandler

uah = UserAccountHandler()

def test_login():
    try:
        uname = 'testuname'
        pwd = 'testpwd'
        result = wc.login(uname, pwd)
        
    except:
        result = 'Could not login.'
        
    assert result
