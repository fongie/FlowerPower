import pytest, threading, time
from .plant import Plant

def test_wateringPlant():
    p = Plant(1,3)
    p.start()
    try:
        p.waterPlant()
    except AssertionError:
        print('cannot water')
    time.sleep(1)
    p.runSignal = False
    time.sleep(2)
    assert p.isAlive() == False


def test_getMoistnessFromArduino():
    p = Plant(1)
    p.updateMinDryness()
    try:
        assert (p.getMoistness() >= 0) and (p.getMoistness() < 1025)
    except ValueError:
        pass

def test_getMoistnessFromArduinoAsThread():
    r = Plant(1,3)
    r.start()
    try:
        assert (r.getMoistness() >= 0) and (r.getMoistness() < 1025)
    except ValueError:
        print('did not get conn to arduino')
    r.runSignal = False
    time.sleep(7.5)
    assert r.isAlive() == False

"""
WAIT UNTIL TESTING FOR SEVERAL PLANTS
def test_startAndStopAsThread():
    thread1 = Plant(1)
    thread2 = Plant(2)
    thread1.start()
    thread2.start()
    time.sleep(1)
    # main thread + 2 new threads = 3 that should run
    assert threading.active_count() == 3
    # time.sleep(1)
    thread1.runSignal = False
    thread2.runSignal = False
    time.sleep(1.5) #give the run method time to stop
    assert threading.active_count() == 1
    """
