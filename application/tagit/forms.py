from flask_wtf import FlaskForm
from wtforms import StringField

class TagiForm(FlaskForm):
    nimi = StringField("Taagin nimi")
 
    class Meta:
        csrf = False