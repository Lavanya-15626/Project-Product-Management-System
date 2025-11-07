"Writing models"
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Product(db.Model):
    "Creating product class"
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    def __repr__(self):
        "representation"
        return f'[id = {self.id}, name = {self.name}, quantity = {self.quantity}, price = {self.price}]'
    def to_dict(self):
        "dictionary"
        return {'id' : self.id, 'name' : self.name, 'quantity' : self.quantity,
            'price' : self.price}
