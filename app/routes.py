import app.crud as crud

from flask import Flask, request, jsonify

from app.emailer import send_gmail, to_address

from datetime import datetime

application = Flask(__name__)

# configure the db 
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prdct_app_db.sqlite'
application.config['SQLALCHEMY_ECHO'] = True
crud.db.init_app(application)
#       create tables
with application.app_context():
    crud.db.create_all()
# end configure the db 


@application.route('/products', methods = ['GET'])
def read_all_products():
    products = crud.read_all_products()
    products_dict = [product.to_dict() for product in products]
    return jsonify(products_dict)

@application.route('/products/<prdct_id>', methods = ['GET'])
def read_product_by_id(prdct_id):
    prdct_id = int(prdct_id)
    queried_product = crud.search_product(prdct_id)
    if not queried_product: #
        return jsonify({'error' : 'Product Not Found.'}), 404  #
    return jsonify(queried_product.to_dict())

@application.route('/products', methods = ['POST'])
def create_product():
    form_product = request.json
    product = crud.Product(name = form_product['name'],
            quantity = form_product['quantity'],
            price = form_product['price'])
    
    
    try:
        crud.add_product(product)
        created_product = crud.search_product(product.id)
    except crud.ProductAlreadyExistError as ex:
        return jsonify({'error' : 'Server Error'}), 500
    except crud.DatabaseError as ex:
        return jsonify({'error' : 'Server Error'}), 500

    #sending creation mail
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

    subject = f'[{date_time_str}] - {created_product.name} is created'
    body = f'''ID : {created_product.id}
Name: {created_product.name}
quantity: {created_product.quantity}
Price : {created_product.price}
'''
    send_gmail(to_address = to_address,
               subject = subject,
               body = body)
    # log the mail sent info
    #end sending creation mail
    return jsonify(created_product.to_dict()), 201
    #crud.add_product(product)
    #created_product = crud.search_product(product.id)
    #return jsonify(created_product.to_dict()), 201

@application.route('/products/<prdct_id>', methods = ['PUT'])
def update_product(prdct_id):
    prdct_id = int(prdct_id)
    queried_product = crud.search_product(prdct_id)
    if not queried_product: #
        return jsonify({'error' : 'Product Not Found.'}), 404  #
    
    form_product = request.json
    crud.update_product(prdct_id, form_product['price'],form_product["quantity"] )


    updated_product = crud.search_product(prdct_id)
    return jsonify(updated_product.to_dict())

@application.route('/products/<prdct_id>', methods = ['DELETE'])
def delete_product(prdct_id):
    prdct_id = int(prdct_id)
    queried_product = crud.search_product(prdct_id)
    if not queried_product: #
        return jsonify({'error' : 'Product Not Found.'}), 404  #
    
    crud.delete_product(prdct_id)
    return jsonify({'message' : 'Product Deleted Successfully'})

#application.run(debug = True)