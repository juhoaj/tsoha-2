from sqlalchemy import Column, Table, Integer, ForeignKey, text

from application import db
from application.models import Base
from application.viestit.models import Viesti
from application.auktorisointi.models import Kayttaja

class Tagi(Base):
    __tablename__ = 'tagi'

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(40), nullable=False)
    viestit = db.relationship("Tagitus", backref="tagi")

    def __init__(self, nimi):
        self.nimi = nimi

    @staticmethod
    def kaikki_tagit_vastausmaarilla():
        stmt=text(
        " SELECT tagi.id, tagi.nimi, viesteja FROM tagi "
            " LEFT JOIN ( "
                " SELECT tagitus.tagi_id, "
                " COUNT(tagitus.tagi_id) AS viesteja "
                " FROM tagitus "
                " GROUP BY tagitus.tagi_id "
                " ) AS subquery "
            " ON tagi.id = subquery.tagi_id; "
        )
        res = db.engine.execute(stmt)
        tagit = []
        for row in res:
            tagit.append({"id":row[0], "nimi":row[1], "viesteja":row[2]})
        return tagit
        
    @staticmethod
    def tagit_viestille(viesti_id):
        stmt=text(" SELECT DISTINCT tagi.id, tagi.nimi FROM tagitus, tagi " 
              " WHERE tagitus.viesti_id = :viesti_id "
              " AND tagi.id = tagitus.tagi_id ").params(viesti_id=viesti_id)
        res1 = db.engine.execute(stmt)
        tagit = []
        for row in res1:
            tagit.append({"id":row[0], "nimi":row[1]})
        return tagit

    @staticmethod
    def poista_tagi(tagi_id):
        stmt=text(" DELETE FROM tagitus WHERE tagi_id = :id").params(id=tagi_id)
        db.engine.execute(stmt)
        db.session().commit()

        stmt=text(" DELETE FROM tagi WHERE id = :id").params(id=tagi_id)
        db.engine.execute(stmt)


class Tagitus(db.Model):
    __tablename__ = 'tagitus'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tagi_id = db.Column(db.Integer, db.ForeignKey('tagi.id'), nullable=False)
    viesti_id = db.Column(db.Integer, db.ForeignKey('viesti.id'), nullable=False)

    def __init__(self, tagi_id, viesti_id):
        self.tagi_id = tagi_id
        self.viesti_id = viesti_id

    @staticmethod
    def tallenna_viestin_tagit(tagit, viesti_id):
        print('..........')
        for t in tagit:
            print(t.id)
            stmt=text("INSERT INTO tagitus (tagi_id, viesti_id)" 
                  "VALUES (:tagi, :viesti)").params(tagi=t.id, viesti=viesti_id)
            db.engine.execute(stmt)
