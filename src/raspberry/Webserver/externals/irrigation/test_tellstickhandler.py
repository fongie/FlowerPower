import pytest
from .tellstickhandler import TellstickHandler

def test_initializer():
    t = TellstickHandler()
    assert t.isTurnedOn == False

def test_turnOn():
    t = TellstickHandler()
    assert t.turnOn() == True
    assert t.isTurnedOn == True

def test_turnOff():
    t = TellstickHandler()
    t.isTurnedOn = True
    assert t.turnOff() == True
    assert t.isTurnedOn == False
