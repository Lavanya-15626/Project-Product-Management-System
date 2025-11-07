class ProductException(Exception):
    pass 

class ProductNotFoundError(ProductException):
    pass 

class ProductAlreadyExistError(ProductException):
    pass 

class DatabaseError(ProductException):
    pass 