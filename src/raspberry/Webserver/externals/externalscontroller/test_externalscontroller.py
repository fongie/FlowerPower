from raspberry.Webserver.externals.externalscontroller import externalscontroller
import pytest, time, threading

def test_getInstance():
    excntr1 = externalscontroller.ExternalsController.getInstance()
    excntr2 = externalscontroller.ExternalsController.getInstance()
    assert excntr1 == excntr2

def test_readPlantStatus():
    excntr = externalscontroller.ExternalsController.getInstance()
    value = excntr.readPlantStatus(1)
    assert value > -1
    excntr.terminatePlant(1)

def test_createPlantPutsInDict():
    excntr = externalscontroller.ExternalsController.getInstance()
    excntr.createPlant(2)
    assert excntr.plants.get(2)
    excntr.terminatePlant(2)

def test_createPlantCreatesProcess():
    excntr = externalscontroller.ExternalsController.getInstance()
    excntr.createPlant(3)
    threads = threading.enumerate()
    testPassed = False
    for p in threads:
        if p.name == "plant" + str(3):
            testPassed = True

    assert testPassed
    excntr.terminatePlant(3)

def test_terminatePlant():
    excntr = externalscontroller.ExternalsController.getInstance()
    excntr.createPlant(4)
    excntr.terminatePlant(4)
    time.sleep(10)
    threads = threading.enumerate()
    testPassed = True
    for p in threads:
        if p.name == "plant" + str(4):
            testPassed = False

    assert testPassed
