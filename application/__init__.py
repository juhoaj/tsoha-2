# coding=utf-8
# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy
# Käytetään tasks.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///kanta.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

from application import views

from application.viestit import models
from application.viestit import views

from application.tagit import models
from application.tagit import views

from application.auktorisointi import models
from application.auktorisointi import views

# kirjautuminen
from application.auktorisointi.models import Kayttaja
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "kirjaudu"
login_manager.login_message = "Kirjaudu käyttääksesi palvelua"

@login_manager.user_loader
def load_user(user_id):
    return Kayttaja.query.get(user_id)


# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()