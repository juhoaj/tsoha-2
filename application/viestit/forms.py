from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, widgets
from application.tagit.models import Tagi, Tagitus
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField

# class MultiCheckboxField(SelectMultipleField):
#     widget = widgets.ListWidget(prefix_label=False)
#     option_widget = widgets.CheckboxInput()

class MultiCheckboxField(QuerySelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class ViestiForm(FlaskForm):
    otsikko = StringField("Viestin otsikko", [validators.Length(min=2)])
    sisalto = TextAreaField("Viestin sisältö", [validators.Length(max=2000)])

    tagit = MultiCheckboxField(get_label='nimi')
    class Meta:
        csrf = False