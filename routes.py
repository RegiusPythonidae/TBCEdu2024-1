from flask import render_template, redirect
from flask_login import login_user, logout_user, current_user, login_required
from os import path
from uuid import uuid4

from forms import ProductForm, RegisterForm, LoginForm
from models import Product, User
from ext import app, db


@app.route("/")
def index():
    products = Product.query.all()
    users = User.query.all()
    return render_template("index.html", products=products, users=users)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        new_user.create()
        return redirect("/login")
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/create_product", methods=["GET", "POST"])
@login_required
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        file = form.img.data
        filetype = file.filename.split(".")[-1]
        filename = uuid4()

        filepath = path.join(app.root_path, "static", f"{filename}.{filetype}")
        file.save(filepath)

        new_product = Product(name=form.name.data, price=form.price.data, img=f"{filename}.{filetype}",
                              user_id=current_user.id)
        new_product.create()

        return redirect("/")
    return render_template("product_form.html", form=form)

@app.route("/edit_product/<int:product_id>", methods=["GET", "POST"])
@login_required
def edit_product(product_id):
    product = Product.query.get(product_id)

    form = ProductForm(name=product.name, price=product.price, img=product.img)
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        #product["img"] = form.img.data

        product.save()
        return redirect("/")
    return render_template("product_form.html", form=form)

@app.route("/delete_product/<int:product_id>")
@login_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    product.delete()
    return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/profile/<username>")
def profile(username):
    found_user = User.query.filter(User.username == username).first()
    return render_template("profile.html", user=found_user)