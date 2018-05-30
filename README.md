# projectgaming

Scrum training project at the Royal Institute of Technology, where a group consisting of five students, Erik Holm, Max Körlinge, Nicole Othman, Hampus Pukitis Furhoff and Kim Säther, created a remotely controlled watering system for plants called **FlowerPower**. It enables you to monitor the moist value of your plant by going to a website, and to then water your plant using a simple button. If the plant dries out, the system will also send you a notification by email so that you can log in and water your plant. You can find all the documentation regarding the project such as project plan, architecture, design, testing, etc. in the [Wiki](https://github.com/fongie/projectgaming/wiki).

## Installation
Before you can start monitoring your plants and live that high-life you always have dreamt about you have some configuring to do. 

If you don't already have it, go ahead and install the arduino developing tool from https://www.arduino.cc/en/Main/Software as well as python 3.5 from https://www.python.org/downloads/

### Arduino Config
Download and open up the file projectgaming/src/arduino/flowerpower/flowerpowerwifi.ino using the Arduino IDE. 
Change the wifi settings at line 11 and 12 accordingly to the wifi-ssid and pass that you will be using.
Verify and upload to the arduino-board using the usb-cable.
Open up the serial monitor (icon in the top right corner) to see that it is functioning properly and to get the IP-adress of the arduino.
You can now save the file and close the arduino IDE.
Plug in the usb-cable to a power supply.

### Raspberry Config
Install the telldus-core package on the Raspberry system and configure it to turn on/off your device as device number "1".
Install the Python modules listed in the Pipfile, either globally on the system or in a virtual environment of your choice. The system was developed using [Pipenv](https://docs.pipenv.org/) to handle virtual environments.
Change the IP at line 10 in projectgaming/src/raspberry/Webserver/externals/moistcontrol/arduinoconnection.py to the one from the Arduino retrieved from serialmonitor above.
Change the email and password at line 16 and 17 in projectgaming/src/raspberry/Webserver/externals/notification/notificationsender.py to a valid email and password. 

## To run:
* SSH into your Raspberry Pi with ssh pi@RASPBERRYIP , password is "flowerpower", from a computer connected to the same wifi network as the Raspberry.
* Type the command: cd projectgaming
* (*if using Pipenv*) Type the command: pipenv shell 
* Type the command: ./start_server.bash

You can now access the website on the same network on http://RASPBERRYPIIP:5000

## Further development
To further develop the system you can **fork** the repository on GitHub. You will find detailed documentation on the different subsystems in the [Technical Documentation](https://github.com/fongie/projectgaming/wiki/Teknisk-Dokumentation) part of the wiki.
