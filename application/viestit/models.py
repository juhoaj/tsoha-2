from application import db
from application.models import Base


class Viesti(Base):
    __tablename__ = 'viesti'

    otsikko = db.Column(db.String(144), nullable=False)
    sisalto = db.Column(db.String(2048), nullable=False)
    kayttaja_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'),
                            nullable=False)
    vastaus = db.Column(db.Integer, nullable=True)

    # tagitus = db.relationship('Tagitus', backref='tagin_viestit', lazy=True)

    def __init__(self, otsikko, sisalto):
        self.otsikko = otsikko
        self.sisalto = sisalto

    def get_id(self):
        return self.id

    @staticmethod
    def tagit():
        stmt = text("SELECT tagi_id, viesti_id FROM tagitus"
                     " LEFT JOIN tagitus ON Viesti.id = tagitus.viesti_id"
                     " GROUP BY tagitus.tagi_id" )
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row)

        return response