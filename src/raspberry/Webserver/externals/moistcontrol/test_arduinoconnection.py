import pytest
from .arduinoconnection import ArduinoConnection

def testArduinoConnection():
	a = ArduinoConnection()
	assert a.getValue()
