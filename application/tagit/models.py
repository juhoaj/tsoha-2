from sqlalchemy import Column, Table, Integer, ForeignKey
from application import db
from application.viestit.models import Viesti

class Tagi(db.Model):
    __tablename__ = 'tagi'
    id = db.Column(db.Integer, primary_key=True)
    # date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    # date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    # onupdate=db.func.current_timestamp())
    nimi = db.Column(db.String(40), nullable=False)
    poistettu = db.Column(db.Boolean, nullable=False)

    def __init__(self, nimi):
        self.nimi = nimi
        self.poistettu = False

class Tagitus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tagi = db.Column(db.Integer, db.ForeignKey(Tagi.id))
    viesti = db.Column(db.Integer, db.ForeignKey(Viesti.id))