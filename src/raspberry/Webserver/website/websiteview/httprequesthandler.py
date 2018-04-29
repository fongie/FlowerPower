from flask import Flask, render_template, request, url_for, redirect, flash
from raspberry.Webserver.website.websitecontroller.websitecontroller import WebsiteController

app = Flask(__name__)
wc = WebsiteController()

@app.route('/')
def showWebsite():
    moistValue = wc.getPlants()
    return render_template('index.html', moistValue = '{}'.format(moistValue))

@app.route('/', methods=['GET', 'POST'])
def buttonHandler():
    if request.method == 'POST':
        if "loginButton" in request.form:
            uname = request.form['username']
            pwd = request.form['password']
            result = wc.login(uname, pwd)
            return render_template('loggedIn.html', result = '{}'.format(result))
        elif "wateringButton" in request.form:
            testi = 'vatten knappen tryckt'
            return render_template('loggedIn.html', testi = '{}'.format(testi))
        elif "setMinDryness" in request.form:
            minDryness = request.form['setMinDryness']
            result2 = wc.setMinDryness(minDryness)
            return render_template('loggedIn.html', result2 = '{}'.format(result2))
    
    #return render_template('index.html', testd = '{}'.format(testd))


# export FLASK_APP=httprequesthandler.py