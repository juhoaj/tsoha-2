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
    otsikko = StringField("Otsikko", [
        validators.Length(min=4,max=30, message='Otsikon pitää olla vähintään neljä ja enintään kolmekymmentä merkkiä pitkä'),
        validators.DataRequired(),
        ])
    sisalto = TextAreaField("Sisältö", [
        validators.Length(min=4,max=1000, message='Viestin pitää olla vähintään neljä ja enintään tuhat merkkiä pitkä')
    ])

    tagit = MultiCheckboxField(get_label='nimi')
    class Meta:
        csrf = False

class VastausForm(FlaskForm):
    sisalto = TextAreaField("Sisältö", [
        validators.Length(min=4,max=1000, message='Vastauksen pitää olla vähintään neljä ja enintään tuhat merkkiä pitkä')
    ])

    class Meta:
        csrf = False