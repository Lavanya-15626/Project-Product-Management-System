"testing crud operation"
import pytest
import client.cli as cli
def test_add_product_success():
    product = {'name' : 'Laptop',
        'quantity' : 5,
        'price' : 90000}
    created_product = cli.add_product(product)
    queried_product = cli.search_product(created_product['id'])
    #assertions
    assert queried_product is not None
    assert queried_product['name'] == product['name']
