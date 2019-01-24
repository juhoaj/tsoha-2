from application import db

class Kayttaja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    # date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    # onupdate=db.func.current_timestamp())
    kayttajanimi = db.Column(db.String(144), nullable=False)
    salasana = db.Column(db.String(144), nullable=False)
    yllapitaja = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, salasana):
        self.name = name
        self.name = salasana
        self.yllapitaja = False