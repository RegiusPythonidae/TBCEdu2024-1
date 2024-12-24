from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileSize, FileAllowed
from wtforms.fields import StringField,IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, length, equal_to, ValidationError

from datetime import datetime


class ProductForm(FlaskForm):
    name = StringField("პროდუქტის სახელი", validators=[DataRequired(),
                                                       length(min=8)])

    price = IntegerField("პროდუქტის ფასი", validators=[DataRequired()])
    img = FileField("სურათი", validators=[FileRequired(),
                                          FileSize(1000 * 1000, message="ფაილი ძაან დიდია"),
                                          FileAllowed(["jpg", "png", "jpeg"], message="ფაილი უნდა იყოს სურათის")
                                          ])

    submit = SubmitField("შენახვა")


class RegisterForm(FlaskForm):
    username = StringField("იუზერნეიმი", validators=[DataRequired()])
    password = PasswordField("პაროლი", validators=[DataRequired(),
                                                   length(min=8)])
    repeat_password = PasswordField("გაიმეორეთ პაროლი", validators=[equal_to("password")])

    register = SubmitField("რეგისტრაცია")


class LoginForm(FlaskForm):
    username = StringField("იუზერნეიმი", validators=[DataRequired()])
    password = PasswordField("პაროლი", validators=[DataRequired(),
                                                   length(min=8)])

    login = SubmitField("ავტორიზაცია")
