import pytest
from .arduinoconnection import ArduinoConnection

def testArduinoConnection():
    a = ArduinoConnection()
    c = a.getValue()
    assert (c >= 0) and (c < 1025)
