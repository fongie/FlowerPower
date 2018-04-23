import pytest, time
from .tellstickhandler import TellstickHandler

def test_initializer():
    t = TellstickHandler()
    assert t.isTurnedOn == False

def test_turnOnAndOff():
    t = TellstickHandler()
    assert t.turnOn() == True
    assert t.isTurnedOn == True
    time.sleep(2.5)
    assert t.turnOff() == True
    assert t.isTurnedOn == False
