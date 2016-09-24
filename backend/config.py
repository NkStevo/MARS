""" This file contains configuration used by the Flask app,
written as python commands
"""

from __future__ import absolute_import, division, print_function  # Python 3 features
from future_builtins import *

# database connection data
MONGODB_SETTINGS = {
    "DB": "development",
    "USERNAME": "",
    "PASSWORD": "",
    "HOST": "localhost",
    "PORT": 27017
}
