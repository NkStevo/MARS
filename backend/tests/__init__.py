from __future__ import absolute_import, division, print_function	# Python 3 features
from future_builtins import *
import pytest

from app import app

@pytest.fixture
def client(request):
    return app.test_client()