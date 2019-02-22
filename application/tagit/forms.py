from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TagiForm(FlaskForm):
    nimi = StringField("Taagin nimi", [
        validators.Length(min=4,max=10, message='Taagin pitää olla vähintään neljä ja enintään kymmenen merkkiä pitkä'),
        validators.DataRequired(),
    ])
 
    class Meta:
        csrf = False