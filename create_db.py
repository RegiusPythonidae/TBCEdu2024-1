from ext import app, db
from models import Product, User

products = [
    {"name": "Samsung Galaxy A24", "price": 900, "img": "surati.jpg"},
    {"name": "Samsung Galaxy S24 Ultra", "price": 3200, "img": "surati.jpg"},
    {"name": "iPhone 13 PRO MAX", "price": 4000, "img": "surati.jpg"},
    {"name": "Sony Xperia V", "price": 1500, "img": "surati.jpg"}
]

users = {
    "giorgi": {"fullname": "Giorgi", "age": 24, "img": "surati.jpg", "role": "admin"},
    "john": {"fullname": "John Doe", "age": 32, "img": "surati.jpg", "role": "moderator"},
    "jane": {"fullname": "Jane Doe", "age": 26, "img": "surati.jpg", "role": "user"}
}

with app.app_context():
    db.drop_all()
    db.create_all()

    for product in products:
        new_product = Product(name=product["name"], price=product["price"], img=product["img"])
        new_product.create()

    for user in users.values():
        new_user = User(username=user["fullname"], age=user["age"], password="password123", img=user["img"])
        new_user.create()
