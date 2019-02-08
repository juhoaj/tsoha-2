from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class ViestiForm(FlaskForm):
    otsikko = StringField("Viestin otsikko", [validators.Length(min=2)])
    sisalto = TextAreaField("Viestin sisältö", [validators.Length(max=2000)])

    class Meta:
        csrf = False