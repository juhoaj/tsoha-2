from application import db

class Viesti(db.Model):
    __tablename__ = 'viesti'
    id = db.Column(db.Integer, primary_key=True)
    luotu = db.Column(db.DateTime, default=db.func.current_timestamp())
    # date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    # onupdate=db.func.current_timestamp())
    # kayttajanimi = db.Column(db.String(144), nullable=False)
    otsikko = db.Column(db.String(144), nullable=False)
    # sisalto = db.Column(db.String(144), nullable=False)

    def __init__(self, otsikko):
        self.otsikko = otsikko
        # self.sisalto = sisalto

    def get_id(self):
        return self.id