'''
    api crud
'''
import requests 

BASE_URL = 'http://127.0.0.1:5000'

def read_all_products():
    url = f'{BASE_URL}/products'
    response = requests.get(url)
    products = response.json()
    return products 

def add_product(product):
    url = f'{BASE_URL}/products'
    response = requests.post(url, json = product)
    created_prdct = response.json()
    return created_prdct

def search_product(id): 
    url = f'{BASE_URL}/products/{id}'
    response = requests.get(url)
    product = response.json()

    if response.status_code != 200:
        return None 
    return product
 
'''def update_product(id, price,quantity):
    url = f'{BASE_URL}/products/{id}'
    body = {'price' : price}
    body = {"quantity" : quantity}
    response = requests.put(url, json = body)
    if response.status_code != 200:
        return None 
    product = response.json()
    return product  '''



def update_product(id, price, quantity):
    url = f'{BASE_URL}/products/{id}'
    body = {
        "price": price,
        "quantity": quantity
    }
    response = requests.put(url, json=body)
    if response.status_code != 200:
        print(f"Error updating product: {response.status_code} - {response.text}")
        return None
    product = response.json()
    return product

  
def delete_product(id):
    url = f'{BASE_URL}/products/{id}'
    response = requests.delete(url)
    if response.status_code != 200:
        return None 
    message = response.json()
    return message



import sys
import os
# Add parent directory to path (so we can import from app)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import batch calculations module
import app.batch_calc as batch_calc


# ================= MAIN MENU =================
def main_menu():
    while True:
        print("""
=====================================
📦 PRODUCT MANAGEMENT SYSTEM
=====================================
1 - Create Product
2 - Search Product
3 - Update Product
4 - Delete Product
5 - List All Products
6 - Batch Calculations Menu
7 - Exit
=====================================
""")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input('Enter Product Name: ')
            quantity = input('Enter Quantity: ')
            price = input('Enter Price: ')
            product = {'name': name, 'quantity': quantity, 'price': price}
            created_product = add_product(product)
            if created_product:
                print(f'✅ Product added successfully: {created_product}')

        elif choice == '2':
            id = input('Enter Product ID: ')
            product = search_product(id)
            if not product:
                print('❌ Product Not Found.')
            else:
                print(product)

        elif choice == '3':
            id = input('Enter Product ID: ')
            product = search_product(id)
            if not product:
                print('❌ Product Not Found.')
            else:
                print(product)
                new_price = input('Enter New Price: ')
                new_quantity = input("Enter New Quantity: ")
                updated = update_product(id, new_price, new_quantity)
                if updated:
                    print('✅ Product updated successfully.')

        elif choice == '4':
            id = input('Enter Product ID: ')
            product = search_product(id)
            if not product:
                print('❌ Product Not Found.')
            else:
                print(product)
                confirm = input('Are you sure to delete (y/n)? ').upper()
                if confirm == 'Y':
                    delete_product(id)
                    print('🗑️ Product deleted successfully.')

        elif choice == '5':
            products = read_all_products()
            if not products:
                print('No products found.')
            else:
                print('📋 List of Products:')
                for product in products:
                    print(product)

        elif choice == '6':
            print("📊 Opening Batch Calculations Menu...")
            batch_calc_menu()  # Opens secondary batch calculations menu

        elif choice == '7':
            print("👋 Exiting... Thank you for using the Product Management System.")
            break

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 7.")


# ================= BATCH CALCULATIONS MENU =================
def batch_calc_menu():
    while True:
        print("""
=====================================
📊 BATCH CALCULATIONS MENU
=====================================
1 - Total Stock Value
2 - Average Product Price
3 - Highest Priced Product
4 - Lowest Priced Product
5 - Back to Main Menu
=====================================
""")

        choice = input("Enter your choice: ")

        if choice == '1':
            batch_calc.total_stock_value()
        elif choice == '2':
            batch_calc.average_price()
        elif choice == '3':
            batch_calc.highest_priced_product()
        elif choice == '4':
            batch_calc.lowest_priced_product()
        elif choice == '5':
            print("🔙 Returning to Main Menu...")
            break
        else:
            print("❌ Invalid option. Please try again.")


# ================= ENTRY POINT =================
if __name__ == '__main__':
    main_menu()
