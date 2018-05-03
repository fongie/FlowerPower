from flask import Flask, render_template, request, url_for, redirect, session
from raspberry.Webserver.website.websitecontroller.websitecontroller import WebsiteController

app = Flask(__name__)
app.secret_key = 'super secret key'
wc = WebsiteController()

@app.route('/')
def showHomePage():
    moistValue = wc.getPlants()
    return render_template('index.html', moistValue = '{}'.format(moistValue))

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
        
@app.route('/login')
def showLogin():
    moistValue = wc.getPlants()
    return render_template('login.html', moistValue = '{}'.format(moistValue))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if "loginButton" in request.form:
            uname = request.form['username']
            pwd = request.form['password']
            result = wc.login(uname, pwd)
            moistValue = wc.getPlants()
            if result == uname:
                session['logged_in'] = True
                session['username'] = uname
                username = session['username']
                return render_template('indexWhenLoggedIn.html', username = '{}'.format(username), moistValue = '{}'.format(moistValue))
            else:
                username = result
                return render_template('logIn.html', moistValue = '{}'.format(moistValue))

@app.route('/logOut')
def logOut():
    moistValue = wc.getPlants()
    session['logged_in'] = False
    return render_template('index.html', moistValue = '{}'.format(moistValue))

@app.route('/waterplant')
def waterPlant():
    username = session['username']
    moistValue = wc.getPlants()
    if session.get('logged_in') == True:
        return render_template('waterPlant.html', username = '{}'.format(username), moistValue = '{}'.format(moistValue))
    else:
        return render_template('index.html', moistValue = '{}'.format(moistValue))

@app.route('/waterplant', methods=['GET', 'POST'])
def waterButton():
    if request.method == 'POST':
        if "wateringButton" in request.form:
            result = wc.waterPlant()
            username = session['username']
            moistValue = wc.getPlants()
            return render_template('waterPlant.html', result = '{}'.format(result), username = '{}'.format(username), moistValue = '{}'.format(moistValue))
    
@app.route('/homepageloggedin')
def homepageloggedin():
    wc = WebsiteController()
    moistValue = wc.getPlants()
    username = session['username']
    if session.get('logged_in') == True:
        return render_template('indexWhenLoggedIn.html', moistValue = '{}'.format(moistValue), username = '{}'.format(username))
    else:
        return render_template('index.html', moistValue = '{}'.format(moistValue))

@app.route('/homepage')
def homepage():
    wc = WebsiteController()
    moistValue = wc.getPlants()
    return render_template('index.html', moistValue = '{}'.format(moistValue))

@app.route('/insertMoistValueSensitivity')
def insertMoistValueSensitivityPage():    
    username = session['username']
    moistValue = wc.getPlants()
    if session.get('logged_in') == True:
        return render_template('insertmoistvaluesensitivity.html', username = '{}'.format(username), moistValue = '{}'.format(moistValue))
    else:
        return render_template('index.html', moistValue = '{}'.format(moistValue))

@app.route('/insertMoistValueSensitivity', methods=['GET', 'POST'])
def insertMoistValueSensitivity():
    if request.method == 'POST':
        if "moistValueSensitivityNumberOk" in request.form:
            minDryness = request.form['moistValueSensitivityNumber']
            result2 = wc.setMinDryness(minDryness)
            username = session['username']
            moistValue = wc.getPlants()
            return render_template('insertmoistvaluesensitivity.html', result2 = '{}'.format(result2), username = '{}'.format(username), moistValue = '{}'.format(moistValue))

# export FLASK_APP=httprequesthandler.py