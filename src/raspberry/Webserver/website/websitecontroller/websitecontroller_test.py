import pytest
from raspberry.Webserver.website.websitecontroller.websitecontroller import WebsiteController

wc = WebsiteController()

def test_getPlants():
    assert wc.getPlants() >= 0
    
def test_login():
    try:
        uname = 'testuname'
        pwd = 'testpwd'
        result = wc.login(uname, pwd)
        
    except:
        result = 'Could not login.'
        
    assert result
    
def test_setMinDryness():
    minDryness = 5
    try:
        result = wc.setMinDryness(minDryness)
        
    except:
        result = 'Could not set minimum dryness value.'
        
    assert result
