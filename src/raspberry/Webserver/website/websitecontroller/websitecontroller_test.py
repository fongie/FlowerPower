import pytest
from raspberry.Webserver.website.websitecontroller.websitecontroller import WebsiteController

def test_getPlants():
    wc = WebsiteController()
    assert wc.getPlants() >= 0
