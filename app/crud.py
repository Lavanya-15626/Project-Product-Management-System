"provides crud operations"
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.models import db, Product
from .exceptions import  ProductAlreadyExistError, DatabaseError
from .logger import logging
def read_all_products():
    "reads all the products"
    products = db.session.query(Product).all()
    logging.info("Read all products.")
    return products
def add_product(product):
    "adds the product"
    try:
        db.session.add(product)
        db.session.commit()
        logging.info('Product Added Successfully')
    except IntegrityError as ex:
        db.session.rollback()
        logging.error("Duplicate product id:%s",ex)
        raise ProductAlreadyExistError(f"Product id={product['id']} exists already.") from ex
    except SQLAlchemyError as ex:
        db.session.rollback()
        logging.error("Database error in creating product:%s",ex)
        raise DatabaseError("Error in creating product.") from ex
def search_product(id):
    "searches for the product"
    product = db.session.query(Product).filter_by(id = id).first()
    logging.info("Read product for given id.")
    return product
def update_product(id, price,quantity):
    "Updates the product"
    old_product = search_product(id)
    if not old_product:
        logging.info('Product Not Found.')
        return
    old_product.price = price
    old_product.quantity=quantity
    db.session.commit()
    logging.info('Product Updated Successfully')
def delete_product(id):
    "Deletes the product"
    old_product = search_product(id)
    if not old_product:
        logging.info('Product Not Found.')
        return
    db.session.delete(old_product)
    db.session.commit()
    logging.info('Product Deleted Successfully')
