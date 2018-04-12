import pytest, threading
from .plant import Plant


def test_startAsThread():
    thread1 = Plant(1)
    thread2 = Plant(2)

    thread1.start()
    thread2.start()

    # main thread + 2 new threads = 3 that should run
    assert threading.active_count() == 3


def test_getMoistness():
    p = Plant(1)
    assert p.getMoistness() == 0
