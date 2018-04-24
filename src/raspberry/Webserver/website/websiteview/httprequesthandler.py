from flask import Flask, render_template, request, url_for, redirect, flash
from raspberry.Webserver.website.websitecontroller.websitecontroller import WebsiteController

app = Flask(__name__)
wc = WebsiteController()

@app.route('/') #alternativt "GET", "POST"
def showWebsite():
    #testdata = ["123", "456", "789"]
    #testd = f1.fuktvarde()
    #wc = WebsiteController()
    testd = wc.getPlants()
    return render_template('index.html', testd = '{}'.format(testd))

@app.route('/', methods=['GET', 'POST'])
def doLogin():
    #wc = WebsiteController()
    if request.method == 'POST':
        if "loginButton" in request.form:
            uname = request.form['username']
            pwd = request.form['password']
            testi = wc.login(uname, pwd)
            return render_template('loggedIn.html', testi = '{}'.format(testi))
        elif "wateringButton" in request.form:
            testi = 'vatten knappen tryckt'
            return render_template('loggedIn.html', testi = '{}'.format(testi))
    
    #return render_template('index.html', testd = '{}'.format(testd))


# EXPORT FLASK_APP=httprequesthandler.py