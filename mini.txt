from flask import Flask
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField

class NewUser(FlaskForm):
    new_user = StringField('Registrar Usuario.')
    new_password = PasswordField('Password.')
    submit = SubmitField('Registrar.')

class LoginUserForm(FlaskForm):
    user = StringField('Usuario.')
    password = PasswordField('Password')
    submit = SubmitField('Ingresar.')
