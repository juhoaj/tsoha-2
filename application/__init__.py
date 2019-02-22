# coding=utf-8
from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
   app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
   app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///kanta.db"    
   app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# kirjautuminen
from application.auktorisointi.models import Kayttaja
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "kirjaudu"
login_manager.login_message = "Kirjaudu käyttääksesi palvelua"

# kirjautumisroolit
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated():
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# sovellussisältö

from application import views

from application.viestit import models
from application.viestit import views

from application.tagit import models
from application.tagit import views

from application.auktorisointi import models
from application.auktorisointi import views

# kirjautuminen jatkuu
@login_manager.user_loader
def load_user(user_id):
   return Kayttaja.query.get(user_id)

# luodaan kanta ellei sitä ole jo luotu
try: 
    db.create_all()
except:
    pass

# jos kannassa ei ole käyttäjää 1 lisätään se ja pari tagia
from application.tagit.models import Tagi
if Kayttaja.query.count() == 0:
    k = Kayttaja('<poistettu>', '<poistettu>')
    t1 = Tagi('Käpistely')
    t2 = Tagi('Yleistä')
  
    db.session().add(t1)
    db.session().add(t2)
    db.session().add(k)
    db.session().commit()