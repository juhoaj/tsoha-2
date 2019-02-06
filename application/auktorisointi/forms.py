from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class LoginForm(FlaskForm):
    kayttajanimi = StringField("Käyttäjänimi")
    salasana = PasswordField("Salasana")
 
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    kayttajanimi = StringField("Käyttäjänimi")
    salasana = PasswordField("Salasana")
    # vahvistaSalasana = PasswordField("Salasana uudestaan")
    

    class Meta:
        csrf = False