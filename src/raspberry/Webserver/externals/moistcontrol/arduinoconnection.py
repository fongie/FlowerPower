import requests

class ArduinoConnection:
    #def __init__(self):
    #wlan = WLAN(mode=WLAN.STA)
    #wlan.connect("Isabels iPhone", auth=(net.sec, "ifpejnn09q53y"), timeout=5000)

        def getValue(self):
            r = requests.get('http://192.168.43.160/')
            return int(r.text)
