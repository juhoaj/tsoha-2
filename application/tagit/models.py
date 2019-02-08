from sqlalchemy import Column, Table, Integer, ForeignKey

from application import db
from application.models import Base
from application.viestit.models import Viesti
from application.auktorisointi.models import Kayttaja

class Tagi(Base):
    __tablename__ = 'tagi'

    nimi = db.Column(db.String(40), nullable=False)
    poistettu = db.Column(db.Boolean, nullable=False)

    # tagitus = db.relationship('Tagitus', backref='viestin_tagit', lazy=True)
    # seuraajat = db.relationship("Kayttaja", backref='kayttajan_tagit', lazy=True)

    def __init__(self, nimi):
        self.nimi = nimi

class Tagitus(db.Model):
    __tablename__ = 'tagitus'

    tagi_id = db.Column(db.Integer, db.ForeignKey('tagi.id'), primary_key=True),
    viesti_id = db.Column(db.Integer, db.ForeignKey('viesti.id'), primary_key=True)

    def __init__(self, tagi_id, viesti_id):
        self.tagi_id = tagi_id
        self.viesti_id = viesti_id


class Seuratut(db.Model):
    __tablename__ = 'seuratut'

    tagi_id = db.Column(db.Integer, db.ForeignKey('tagi.id'), primary_key=True),
    kayttaja_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'), primary_key=True)
