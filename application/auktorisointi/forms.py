from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class LoginForm(FlaskForm):
    kayttajanimi = StringField("Käyttäjänimi")
    salasana = PasswordField("Salasana")
 
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    kayttajanimi = StringField("Haluamasi käyttäjänimi")
    salasana = PasswordField("Anna alasana")
    toistettuSalasana = PasswordField("Toista alasana")
    # vahvistaSalasana = PasswordField("Salasana uudestaan")
    
    class Meta:
        csrf = False

