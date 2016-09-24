""" This file contains controllers (aka routes) associated with this module """

from __future__ import absolute_import, division, print_function  # Python 3 features
from future_builtins import *   # Python 3 features

from flask import Blueprint
from flask_restful import Api
from flask_restful import Resource
from .views import *

products = Blueprint('products', __name__, url_prefix='/products')

api = Api(products)

api.add_resource(Products, '')
api.add_resource(ProductDetails, '/<string:productName>')
