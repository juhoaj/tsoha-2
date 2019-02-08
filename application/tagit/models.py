from sqlalchemy import Column, Table, Integer, ForeignKey

from application import db
from application.models import Base
from application.viestit.models import Viesti

class Tagi(Base):
    __tablename__ = 'tagi'

    nimi = db.Column(db.String(40), nullable=False)
    poistettu = db.Column(db.Boolean, nullable=False)

    def __init__(self, nimi):
        self.nimi = nimi
        self.poistettu = False

class Tagitus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tagi = db.Column(db.Integer, db.ForeignKey(Tagi.id))
    viesti = db.Column(db.Integer, db.ForeignKey(Viesti.id))