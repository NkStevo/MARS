""" This file contains DB models associated with this module """

from __future__ import absolute_import, division, print_function  # Python 3 features
from future_builtins import *
from app.extensions import db

# class Action(db.EmbeddedDocument):
#     title = db.StringField(max_length=50, required=True)


class Product(db.Document):
    name = db.StringField(max_length=50, required=True)
    description = db.StringField(max_length=50, required=True)
    callback_url = db.URLField(required=True)