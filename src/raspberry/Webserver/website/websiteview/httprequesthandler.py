from flask import Flask, render_template, request, url_for, redirect, flash
from raspberry.Webserver.website.websitecontroller.websitecontroller import WebsiteController

app = Flask(__name__)
wc = WebsiteController()

@app.route('/')
def showHomePage():
    return render_template('index.html')

'''@app.route('/', methods=['GET', 'POST'])
def buttonHandler():
    if request.method == 'POST':
        if "loginButton" in request.form:
            uname = request.form['username']
            pwd = request.form['password']
            result = wc.login(uname, pwd)
            return render_template('loggedIn.html', result = '{}'.format(result))
        if "wateringButton" in request.form:
            testi = 'vatten knappen tryckt'
            return render_template('loggedIn.html', testi = '{}'.format(testi))
        elif "setMinDryness" in request.form:
            minDryness = request.form['setMinDryness']
            result2 = wc.setMinDryness(minDryness)
            return render_template('loggedIn.html', result2 = '{}'.format(result2))'''
        
@app.route('/showLogin')
def showLogin():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
    def login():
    if request.method == 'POST':
        if "loginButton" in request.form:
            uname = request.form['username']
            pwd = request.form['password']
            result = wc.login(uname, pwd)
            return render_template('showMoistValue.html', result = '{}'.format(result))
    
@app.route('/showMoistValue')
def showMoistValue():
    wc = WebsiteController()
    moistValue = wc.getPlants()
    return render_template('showMoistValue.html', moistValue = '{}'.format(moistValue))

@app.route('/insertMoistValueSensitivityPage')
def insertMoistValueSensitivityPage():
    return render_template('insertmoistvaluesensitivity.html')

@app.route('/insertMoistValueSensitivity', methods=['GET', 'POST'])
    if request.method == 'POST':
        if "setMinDryness" in request.form:
            minDryness = request.form['setMinDryness']
            result2 = wc.setMinDryness(minDryness)
            return render_template('insertmoistvaluesensitivity.html', result2 = '{}'.format(result2))

# export FLASK_APP=httprequesthandler.py