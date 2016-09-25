""" This file contains commands to manage the website """
import flask
from app import app
from flask import render_template
from flask_restful import Api

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
