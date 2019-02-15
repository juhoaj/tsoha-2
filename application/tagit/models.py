from sqlalchemy import Column, Table, Integer, ForeignKey

from application import db
from application.models import Base
from application.viestit.models import Viesti
from application.auktorisointi.models import Kayttaja

class Tagi(Base):
    __tablename__ = 'tagi'

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(40), nullable=False)
    viestit = db.relationship("Tagitus", backref="tagi")
    seuraajat = db.relationship("Seuratut", backref="tagi")

    def __init__(self, nimi):
        self.nimi = nimi

class Tagitus(db.Model):
    __tablename__ = 'tagitus'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tagi_id = db.Column(db.Integer, db.ForeignKey('tagi.id'), nullable=False)
    viesti_id = db.Column(db.Integer, db.ForeignKey('viesti.id'), nullable=False)

    def __init__(self, tagi_id, viesti_id):
        self.tagi_id = tagi_id
        self.viesti_id = viesti_id

class Seuratut(db.Model):
    __tablename__ = 'seuratut'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tagi_id = db.Column(db.Integer, db.ForeignKey('tagi.id'), nullable=False)
    kayttaja_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'), nullable=False)

def __init__(self, tagi_id, kayttaja_id):
    self.tagi_id = tagi_id
    self.kayttaja_id = kayttaja_id

