'''
    batch calculations on products
'''
import requests

BASE_URL = 'http://127.0.0.1:5000'

def fetch_all_products():
    url = f'{BASE_URL}/products'
    response = requests.get(url)
    if response.status_code != 200:
        print('Error fetching products')
        return []
    return response.json()


def total_stock_value():
    products = fetch_all_products()
    total = sum(float(p['price']) * int(p['quantity']) for p in products)
    print(f'\n Total Stock Value: {total}')


def average_price():
    products = fetch_all_products()
    if not products:
        print('No products found for average calculation.')
        return
    avg = sum(float(p['price']) for p in products) / len(products)
    print(f'Average Price of Products: {avg:.2f}')


def highest_priced_product():
    products = fetch_all_products()
    if not products:
        print('No products found.')
        return
    highest = max(products, key=lambda p: float(p['price']))
    print(f'Highest Priced Product: {highest}')


def lowest_priced_product():
    products = fetch_all_products()
    if not products:
        print('No products found.')
        return
    lowest = min(products, key=lambda p: float(p['price']))
    print(f'Lowest Priced Product: {lowest}')

'''def batch_menu():
    while True:
        print("""
===============================
📊 BATCH CALCULATIONS MENU
===============================
1 - Total Stock Value
2 - Average Price
3 - Highest Priced Product
4 - Lowest Priced Product
5 - Back to Main Menu
===============================
""")
        choice = input("Enter your choice: ")

        if choice == '1':
            total_stock_value()
        elif choice == '2':
            average_price()
        elif choice == '3':
            highest_priced_product()
        elif choice == '4':
            lowest_priced_product()
        elif choice == '5':
            print("🔙 Returning to Main Menu...")
            break
        else:
            print("❌ Invalid option, try again.")'''