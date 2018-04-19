import pytest, threading, time
from .plant import Plant

def test_getMoistnessFromArduino():
    p = Plant(1)
    p.updateMinDryness()
    assert p.getMoistness() == 42

def test_getMoistnessFromArduinoAsThread():
    p = Plant(1)
    p.start()
    time.sleep(1)
    assert p.getMoistness() == 42
    p.runSignal = False

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
