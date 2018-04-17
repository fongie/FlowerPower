import pytest, threading, time
from .plant import Plant

def test_getMoistness():
    p = Plant(1, 13)
    assert p.getMoistness() == 13

def test_startAsThread():
    thread1 = Plant(1)
    thread2 = Plant(2)

    thread1.start()
    thread2.start()

    time.sleep(2)
    # main thread + 2 new threads = 3 that should run
    assert threading.active_count() == 3
    time.sleep(1)
    thread1.runSignal = False
    thread2.runSignal = False

def test_getDifferentMoistnessFromThreads():
    p1 = Plant(1, 10)
    p2 = Plant(2, 25)

    p1.start()
    p2.start()

    time.sleep(1)
    assert p1.getMoistness() == 10
    assert p2.getMoistness() == 25
    time.sleep(1)

    p1.runSignal = False
    p2.runSignal = False
