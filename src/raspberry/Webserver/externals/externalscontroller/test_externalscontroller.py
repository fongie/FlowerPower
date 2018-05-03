from raspberry.Webserver.externals.externalscontroller import externalscontroller
import pytest, threading

def test_getInstance():
    excntr1 = externalscontroller.ExternalsController.getInstance()
    excntr2 = externalscontroller.ExternalsController.getInstance()
    assert excntr1 == excntr2

def test_readPlantStatus():
    excntr = externalscontroller.ExternalsController.getInstance()

    value = 1337
    try:
        value = excntr.readPlantStatus(1)
    except RuntimeError:
        value = 666

    excntr.terminatePlant(1)
    assert value > -1 and value < 1025

def test_createPlantPutsInDict():
    excntr = externalscontroller.ExternalsController.getInstance()
    excntr.createPlant(2)

    p = excntr.plants.get(2)

    excntr.terminatePlant(2)
    assert p

def test_createPlantCreatesProcess():
    excntr = externalscontroller.ExternalsController.getInstance()
    excntr.createPlant(3)

    threads = threading.enumerate()
    testPassed = False
    for p in threads:
        if p.name == 'plant' + str(3):
            testPassed = True

    excntr.terminatePlant(3)
    assert testPassed

def test_terminatePlant():
    excntr = externalscontroller.ExternalsController.getInstance()
    excntr.createPlant(4)

    p1 = threading.active_count()
    excntr.terminatePlant(4)
    p2 = threading.active_count()

    assert p1 == p2 + 1

def test_waterPlant():
    excntr = externalscontroller.ExternalsController.getInstance()
    excntr.createPlant(5)

    try:
        excntr.waterPlant(5)
        managedToWaterWithoutProblem = True
    except RuntimeError:
        managedToWaterWithoutProblem = False

    excntr.terminatePlant(5)
    assert managedToWaterWithoutProblem

def test_turnOffSprinkler():
    excntr = externalscontroller.ExternalsController.getInstance()
    excntr.createPlant(6)

    try:
        excntr.waterPlant(6)
        excntr.turnOffSprinkler(6)
        turnedOn = excntr.plants.get(6).tellstickHandler.isTurnedOn
        caughtException = False
    except RuntimeError:
        caughtException = True


    excntr.terminatePlant(6)
    assert caughtException or (turnedOn == False)

def test_updateMinDryness():
    excntr = externalscontroller.ExternalsController.getInstance()
    excntr.createPlant(7)

    testPassed = False
    newValue = 500
    excntr.updateMinDryness(7, newValue)
    if excntr.plants.get(7).drynessTrigger == newValue:
        testPassed = True

    excntr.terminatePlant(7)
    assert testPassed

def test_setEmailForPlant():
    excntr = externalscontroller.ExternalsController.getInstance()
    excntr.createPlant(8)

    newEmail = "hampus.p.f@gmail.com"
    excntr.setEmailForPlant(8, newEmail)
    email = excntr.plants.get(8).notificationSender.to_addr

    excntr.terminatePlant(8)
    assert newEmail == email

def test_isActive():
    excntr = externalscontroller.ExternalsController.getInstance()
    excntr.createPlant(9)

    shouldBeActive = excntr.isActive(9)

    excntr.terminatePlant(9)
    assert shouldBeActive
