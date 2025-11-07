from app.models import db, Product
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from .exceptions import ProductNotFoundError, ProductAlreadyExistError, DatabaseError
from .logger import logging 

def read_all_products():
    products = db.session.query(Product).all()
    logging.info("Read all products.")
    return products


def add_product(product):
    try:
        db.session.add(product)
        db.session.commit()
        logging.info('Product Added Successfully')
    except IntegrityError as ex:
        db.session.rollback()
        logging.error("Duplicate product id:%s",ex)
        raise ProductAlreadyExistError(f"Product id={product['id']} exists already.")
    except SQLAlchemyError as ex:
        db.session.rollback()
        logging.error("Database error in creating product:%s",ex)
        raise DatabaseError("Error in creating product.")
    
def search_product(id): 
    product = db.session.query(Product).filter_by(id = id).first()
    logging.info("Read product for given id.")
    return product
 
def update_product(id, price,quantity):
    old_product = search_product(id)

    if not old_product: 
        logging.info('Product Not Found.')
        return
    old_product.price = price
    old_product.quantity=quantity
    db.session.commit()
    logging.info('Product Updated Successfully')        
    

def delete_product(id):
    old_product = search_product(id)

    if not old_product: 
        logging.info('Product Not Found.')
        return
    
    db.session.delete(old_product)
    db.session.commit()
    logging.info('Product Deleted Successfully')