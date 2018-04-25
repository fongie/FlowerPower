import requests

class ArduinoConnection:
    #def __init__(self):
    #wlan = WLAN(mode=WLAN.STA)
    #wlan.connect("Isabels iPhone", auth=(net.sec, "ifpejnn09q53y"), timeout=5000)

        def readValue(self):
            try:
                r = requests.get('http://192.168.43.160/', timeout=5)
            except:
                raise requests.ConnectionError("Server did not return status code 200")
            return int(r.text)
