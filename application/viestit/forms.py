from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, widgets, SelectMultipleField
from application.tagit.models import Tagi, Tagitus

# class MultiCheckboxField(SelectMultipleField):
#     widget = widgets.ListWidget(prefix_label=False)
#     option_widget = widgets.CheckboxInput()

class ViestiForm(FlaskForm):
    otsikko = StringField("Viestin otsikko", [validators.Length(min=2)])
    sisalto = TextAreaField("Viestin sisältö", [validators.Length(max=2000)])
    # tagit = MultiCheckboxField(choices=[(str(t.id), t.nimi) for t in Tagi.query.all()])
    class Meta:
        csrf = False