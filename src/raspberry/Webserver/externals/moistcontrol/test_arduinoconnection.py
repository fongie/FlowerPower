import pytest
from .arduinoconnection import ArduinoConnection

def testArduinoConnection():
    a = ArduinoConnection()
    c = a.readValue()
    assert (c >= 0) and (c < 1025)
