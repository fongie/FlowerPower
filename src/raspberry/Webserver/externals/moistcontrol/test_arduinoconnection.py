import pytest
import requests
from .arduinoconnection import ArduinoConnection

# def testArduinoConnection():
#     a = ArduinoConnection()
#     c = a.readValue()
#     assert (c >= 0) and (c < 1025)

def testExceptionConnection():
    a = ArduinoConnection()
    with pytest.raises(requests.ConnectionError) as e_info:
        c = a.readValue()
