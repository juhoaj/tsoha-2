from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ViestiForm(FlaskForm):
    otsikko = StringField("Viestin otsikko", [validators.Length(min=2)])
    sisalto = StringField("Viestin sisältö", [validators.Length(min=2)])

    class Meta:
        csrf = False