from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class LoginForm(FlaskForm):
    kayttajanimi = StringField("Käyttäjänimi")
    salasana = PasswordField("Salasana")
 
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    kayttajanimi = StringField("Haluamasi käyttäjänimi")
    salasana = PasswordField("Anna salasana")
    toistettuSalasana = PasswordField("Toista salasana")
    
    class Meta:
        csrf = False

class ChangePasswordForm(FlaskForm):
    nykyinenSalasana = PasswordField("Nykyinen salasana")
    salasana = PasswordField("Anna salasana")
    toistettuSalasana = PasswordField("Toista salasana")
    
    class Meta:
        csrf = False

