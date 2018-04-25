import pytest
from .notificationsender import NotificationSender

def test_sendNotification():
    n = NotificationSender(1, "flowerpowerkth@gmail.com")

    assert n.sendDrynessNotification(533) == True

def test_sendWateringNotification():
    n = NotificationSender(1, "flowerpowerkth@gmail.com")

    assert n.sendWateringNotification() == True
