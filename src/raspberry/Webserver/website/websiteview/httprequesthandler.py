from flask import Flask, render_template
from raspberry.Webserver.website.websitecontroller.websitecontroller import WebsiteController
#import fuktvarden as f1

app = Flask(__name__)

@app.route('/')
def index():
    #testdata = ["123", "456", "789"]
    #testd = f1.fuktvarde()
    wc = WebsiteController()
    testd = wc.getPlants()
    return render_template('index.html', testd = '{}'.format(testd))

    
@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/showmoistvalue')
def showMoistValue():
    return render_template('showmoistvalue.html')
    wc = WebsiteController()
    testd = wc.getPlants()
    return render_template('index.html', testd = '{}'.format(testd))

@app.route('/insertmoistvaluesensitivity')
def insertMoistValueSensitivity():
    return render_template('insertmoistvaluesensitivity.html')


# EXPORT FLASK_APP=httprequesthandler.py
