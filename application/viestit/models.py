from application import db
from application.models import Base
from sqlalchemy.sql import text

class Viesti(Base):
    __tablename__ = 'viesti'

    id = db.Column(db.Integer, primary_key=True)
    otsikko = db.Column(db.String(144), nullable=True)
    sisalto = db.Column(db.String(2048), nullable=False)
    kayttaja_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'),
                            nullable=False)
    vastaus_idlle = db.Column(db.Integer, nullable=True)
    tagit = db.relationship('Tagitus', backref='tagit', lazy=True)

    def __init__(self, otsikko, sisalto, vastaus_idlle):
        self.otsikko = otsikko
        self.sisalto = sisalto
        self.vastaus_idlle = vastaus_idlle

    def get_id(self):
        return self.id
    
    @staticmethod
    def kaikki_viestit_vastausmaarilla():
        stmt=text(
        " SELECT viesti.id, viesti.otsikko, vastauksia FROM viesti "
            " LEFT JOIN ( "
                " SELECT viesti.vastaus_idlle, "
                " COUNT(viesti.vastaus_idlle) AS vastauksia "
                " FROM viesti WHERE viesti.vastaus_idlle IS NOT NULL "
                " GROUP BY viesti.vastaus_idlle "
            " ) AS subquery "
            " ON viesti.id = subquery.vastaus_idlle "
            " WHERE viesti.otsikko IS NOT NULL; "
        )
        res = db.engine.execute(stmt)
        viestit = []
        for row in res:
            viestit.append({"id":row[0], "otsikko":row[1], "vastauksia":row[2]})
        return viestit

    @staticmethod
    def viestit_tagista_vastausmaarilla(tagi_id):
        stmt=text(
        " SELECT viesti.id, viesti.otsikko, subquery.vastauksia FROM viesti " 
            " JOIN tagitus"  
            " ON viesti.id = tagitus.viesti_id "
            " LEFT JOIN ( "
                " SELECT viesti.vastaus_idlle, "
                " COUNT(viesti.vastaus_idlle) AS vastauksia "
                " FROM viesti WHERE viesti.vastaus_idlle IS NOT NULL "
                " GROUP BY viesti.vastaus_idlle "
            " ) AS subquery "
            " ON viesti.id = subquery.vastaus_idlle "
            " WHERE viesti.otsikko IS NOT NULL "
                " AND tagitus.tagi_id = :tagi_id; "
        ).params(tagi_id=tagi_id) 
        res = db.engine.execute(stmt) 
        viestit = [] 
        for row in res:
            viestit.append({"id":row[0], "otsikko":row[1], "vastauksia":row[2]} )

        return viestit



    @staticmethod
    def kaikki_vastaukset_kayttajanimilla(viesti_id):
        stmt=text(" SELECT * FROM viesti, kayttaja  " 
              " WHERE viesti.kayttaja_id = kayttaja.id " 
              " AND viesti.vastaus_idlle = :id").params(id=viesti_id)
        res2 = db.engine.execute(stmt)
        vastaukset = []
        for row in res2:
            vastaukset.append({"luotu":row[0], "id":row[1], "sisalto":row[3], "kayttajanimi":row[8]})
        return vastaukset

