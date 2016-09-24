""" This file contains commands to manage the website """

from __future__ import absolute_import, division, print_function  # Python 3 features
from future_builtins import *
from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
