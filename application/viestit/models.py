from application import db
from application.models import Base


class Viesti(Base):
    __tablename__ = 'viesti'

    id = db.Column(db.Integer, primary_key=True)
    otsikko = db.Column(db.String(144), nullable=False)
    sisalto = db.Column(db.String(2048), nullable=False)
    kayttaja_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'),
                            nullable=False)
    # vastaus_idlle = db.Column(db.Integer, nullable=True)
    tagit = db.relationship('Tagitus', backref='tagit', lazy=True)

    def __init__(self, otsikko, sisalto):
        self.otsikko = otsikko
        self.sisalto = sisalto

    def get_id(self):
        return self.id