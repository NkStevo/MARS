from __future__ import absolute_import, division, print_function  # Python 3 features

from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask_cors import CORS, cross_origin

from app.extensions import db

app = Flask(__name__, static_folder='static')
CORS(app)  # CORS

app.config.from_pyfile('../config.py')
app.url_map.strict_slashes = False
db.init_app(app)


from app.api.products.controllers import products

api = Api(app)


app.register_blueprint(products)



class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
