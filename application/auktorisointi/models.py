from application import db
from application.models import Base

class Kayttaja(Base):

    __tablename__ = "kayttaja"

    kayttajanimi = db.Column(db.String(144), nullable=False)
    salasana = db.Column(db.String(144), nullable=False)
    yllapitaja = db.Column(db.Boolean, nullable=False)

    viestit = db.relationship("Viesti", backref='kayttaja', lazy=True)

    def __init__(self, nimi, salasana):
        self.kayttajanimi = nimi
        self.salasana = salasana
        self.yllapitaja = False

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_adminstrator(self):
        return self.yllapitaja