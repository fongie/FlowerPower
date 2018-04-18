from raspberry.Webserver.externals.externalscontroller import externalscontroller
import pytest, time, threading

def test_getInstance():
    excntr1 = externalscontroller.ExternalsController.getInstance()
    excntr2 = externalscontroller.ExternalsController.getInstance()
    assert excntr1 == excntr2

def test_readPlantStatus():
    excntr = externalscontroller.ExternalsController.getInstance()
    value = excntr.readPlantStatus(1)
    assert value == 0
    excntr.terminatePlant(1)

def test_readPlantStatusAgain():
    excntr = externalscontroller.ExternalsController.getInstance()
    value1 = excntr.readPlantStatus(1)
    time.sleep(4)
    value2 = excntr.readPlantStatus(1)
    assert value1 == value2
    excntr.terminatePlant(1)

def test_createPlantPutsInDict():
    excntr = externalscontroller.ExternalsController.getInstance()
    excntr.createPlant(1)
    assert excntr.plants.get(1)
    excntr.terminatePlant(1)

def test_createPlantCreatesProcess():
    excntr = externalscontroller.ExternalsController.getInstance()
    excntr.createPlant(1)
    threads = threading.enumerate()
    testPassed = False
    for p in threads:
        if p.name == "plant" + str(1):
            testPassed = True

    assert testPassed
    excntr.terminatePlant(1)

def test_terminatePlant():
    excntr = externalscontroller.ExternalsController.getInstance()
    excntr.createPlant(1)
    excntr.terminatePlant(1)
    time.sleep(4)
    threads = threading.enumerate()
    testPassed = True
    for p in threads:
        if p.name == "plant" + str(1):
            testPassed = False

    assert testPassed
