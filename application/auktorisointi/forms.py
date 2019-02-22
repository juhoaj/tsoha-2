from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class LoginForm(FlaskForm):
    kayttajanimi = StringField("Käyttäjänimi")
    salasana = PasswordField("Salasana")
 
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    kayttajanimi = StringField("Haluamasi käyttäjänimi", [
        validators.Length(min=4,max=20, message='Käyttäjänimen pitää olla vähintään neljä ja enintään kaksikymmentä merkkiä pitkä'),
        validators.DataRequired(),
    ])
    salasana = PasswordField("Anna salasana", [
        validators.Length(min=4, max=20 ,message='Salasanan pitää olla vähintään neljä ja enintään kaksikymmentä merkkiä pitkä'),
    ])
    toistettuSalasana = PasswordField("Toista salasana")
    
    class Meta:
        csrf = False

class ChangePasswordForm(FlaskForm):
    nykyinenSalasana = PasswordField("Nykyinen salasana")
    salasana = PasswordField("Anna salasana")
    toistettuSalasana = PasswordField("Toista salasana")
    
    class Meta:
        csrf = False

