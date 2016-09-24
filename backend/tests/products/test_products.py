from tests import client
import json
from examples.example_products import *

'''
1. post
2. get
3. post and get
'''
def test_post_and_get_product(client):
    assert 'SUCCESS' in client.post('/products/', data=json.dumps(products[0]),
                                    content_type="application/json").data
    product_data = client.get('/products/'+products[0]["name"]+'/').data
    product_data = json.loads(product_data)
    assert (product_data["name"] == products[0]["name"])

def test_post_products(client):
    for product in products:
        assert 'SUCCESS' in client.post('/products/',data=json.dumps(product),
                         content_type="application/json").data
