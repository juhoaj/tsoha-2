from application import db

class Kayttaja(db.Model):

    __tablename__ = "kayttaja"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
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