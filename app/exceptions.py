"Exceptions"
class ProductException(Exception):
    "Product Exception"
    pass
class ProductNotFoundError(ProductException):
    "Product Not Found Error"
    pass
class ProductAlreadyExistError(ProductException):
    "Product Already Exist Error"
    pass
class DatabaseError(ProductException):
    "Database Error"
    pass
