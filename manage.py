""" This file contains commands to manage the website """
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flight import Flight
from flight_dump import Flight_Dump
from flask_restful import Api

app = Flask(__name__)

api = Api(app)
bair_name = "TEST"


@app.route("/", methods=['GET'])
def index(air_name = ""):
    
    #air_name = bair_name
    #if request.method == 'POST':
     # user = request.form['loginForm']
      #return redirect(url_for('index',name = user))

    return render_template('index.html', airport = air_name)

@app.route("/api/flightinfo/<idp>/<date>")
def getFlightInfo(idp, date):
    flightA = Flight([idp, date])

    return redirect(url_for('index',air_name=flightA.airport_name))

if __name__ == "__main__":
    app.run(debug=True)
