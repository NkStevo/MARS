import flask
from app import app
from flask import Flask
from flask import render_template
from flask_restful import Api

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'test'

@app.route('/index')
def index():
	return url_for('index')
