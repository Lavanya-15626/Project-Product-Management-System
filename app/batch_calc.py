"""
Batch calculations on products.
This module provides functions to compute product statistics like
total stock value, average price, highest and lowest priced products.
"""
import requests

BASE_URL = 'http://127.0.0.1:5000'

def fetch_all_products():
    """Fetch all products from the API."""
    url = f'{BASE_URL}/products'
    response = requests.get(url,timeout=10)
    if response.status_code != 200:
        print('Error fetching products')
        return []
    return response.json()
def total_stock_value():
    "Gives Total stock value"
    products = fetch_all_products()
    total = sum(float(p['price']) * int(p['quantity']) for p in products)
    print(f'\n Total Stock Value: {total}')
def average_price():
    "Gives average price"
    products = fetch_all_products()
    if not products:
        print('No products found for average calculation.')
        return
    avg = sum(float(p['price']) for p in products) / len(products)
    print(f'Average Price of Products: {avg:.2f}')
def highest_priced_product():
    "returns highest priced product"
    products = fetch_all_products()
    if not products:
        print('No products found.')
        return
    highest = max(products, key=lambda p: float(p['price']))
    print(f'Highest Priced Product: {highest}')
def lowest_priced_product():
    "returns lowest priced product"
    products = fetch_all_products()
    if not products:
        print('No products found.')
        return
    lowest = min(products, key=lambda p: float(p['price']))
    print(f'Lowest Priced Product: {lowest}')
