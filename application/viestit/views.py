from application import app, db, views
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from sqlalchemy.sql import text, func, exists

from application.viestit.models import Viesti
from application.tagit.models import Tagi, Tagitus, Seuratut
from application.viestit.forms import ViestiForm, VastausForm

@app.route("/")
def index():
    return render_template("viestit/index.html", viestit = Viesti.query.filter_by(vastaus_idlle = "null"), tagit=Tagi.query.all())

# näyttää viestit tagista #
@app.route("/tagi/<tagi_id>")
def tagi(tagi_id):
    t = Tagi.query.get(tagi_id)

    print("-----------------")

    # filtteröitävä tagi_id:llä ja current userilla, eka if että on kirjautunut
    seurattu = Tagitus.query.filter_by(tagi_id=5).count()
    if seurattu > 0:
        arvo='seuraa'
    else:
        arvo='poista'

    stmt=text(" SELECT viesti.id, viesti.otsikko FROM tagitus, viesti " 
              " WHERE tagitus.tagi_id = :tagi_id "
              " AND viesti.id = tagitus.viesti_id ").params(tagi_id=tagi_id)
    res = db.engine.execute(stmt)
    viestit = []
    for row in res:
        viestit.append({"id":row[0], "otsikko":row[1]})
    return render_template("viestit/tagi.html", tagi=t, viestit=viestit, arvo=arvo)

# ottaa vastaan tagin seuraamisen ja muuttaa sen tilaa
@app.route("/tagi/<int:tagi_id>", methods=["POST"])
@login_required
def tagi_seuraa(tagi_id):
    
    t = request.form.get("seuraa")
  
    if t == 'kiinnostelee':
        stmt=text("INSERT INTO seuratut (tagi_id, kayttaja_id)" 
                  "VALUES (:tagi, :kayttaja)").params(tagi=tagi_id, kayttaja=1)
        db.engine.execute(stmt)

    return redirect(url_for("tagi", tagi_id=tagi_id, nappiteksti=nappiteksti))


# viestien näyttäminen omista tageista
@app.route("/omat")
@login_required
def omat():
    return render_template("viestit/omat.html")

# viestin # näyttäminen
@app.route("/viesti/<viesti_id>")
def viesti(viesti_id):
    # haetaan viestin tagit
    stmt=text(" SELECT DISTINCT tagi.id, tagi.nimi FROM tagitus, tagi " 
              " WHERE tagitus.viesti_id = :viesti_id "
              " AND tagi.id = tagitus.tagi_id ").params(viesti_id=viesti_id)
    res1 = db.engine.execute(stmt)
    tagit = []
    for row in res1:
        tagit.append({"nimi":row[1]})
     
    # haetaan viestin sisältö
    viesti = Viesti.query.get(viesti_id)

    # haetaan viestin luonut käyttäjä
    stmt=text(" SELECT kayttaja.kayttajanimi FROM kayttaja " 
              " WHERE kayttaja.id = :kayttaja_id " ).params(kayttaja_id=viesti.kayttaja_id)
    kayttaja=db.engine.execute(stmt).fetchone()

    # haetaan vastaukset ja liitetään niihin käyttäjät
    stmt=text(" SELECT * FROM viesti, kayttaja  " 
              " WHERE viesti.kayttaja_id = kayttaja.id " 
              " AND viesti.vastaus_idlle = :id ").params(id=viesti.id)
    res2 = db.engine.execute(stmt)
    vastaukset = []
    for row in res2:
        vastaukset.append({"luotu":row[0], "id":row[1], "sisalto":row[3], "kayttajanimi":row[8]})

    return render_template("viestit/viesti.html", viesti=viesti, tagit=tagit, kayttaja=kayttaja, vastaukset=vastaukset )   

# uusi viesti-näkymä
@app.route("/viesti/uusi")
@login_required
def viesti_muokkaa_uusi():
    tagit = Tagi.query.all()

    form = ViestiForm()
    form.tagit.query = Tagi.query.all()
    return render_template("viestit/uusiViesti.html", form=form)

# uusi viesti-vastaanotto
@app.route("/viesti", methods=["POST"])
@login_required
def viesti_uusi():
    form = ViestiForm(request.form)
    form.tagit.query = Tagi.query.all()
    
    if not form.validate():
        return render_template("viestit/uusiViesti.html", form = form, sanoma = "Lorem ipsum")
    
    viesti = Viesti(form.otsikko.data, form.sisalto.data, "null")
    viesti.kayttaja_id = current_user.id

    db.session().add(viesti)
    db.session().commit()

    # lisätään viestin tagit tagitukseen

    for t in form.tagit.data:
        print (t.id)
        stmt=text("INSERT INTO tagitus (tagi_id, viesti_id)" 
                  "VALUES (:tagi, :viesti)").params(tagi=t.id, viesti=viesti.id)
        db.engine.execute(stmt)

    return redirect(url_for("index"))

# uusi vastaus-näkymä
@app.route("/viesti/<viesti_id>/uusivastaus")
@login_required
def vastaus_muokkaa_uusi(viesti_id):
    form = VastausForm()
    viesti = Viesti.query.get(viesti_id)
    return render_template("viestit/uusiVastaus.html", form=form, viesti=viesti)

# uusi vastaus-vastaanotto
@app.route("/viesti/<viesti_id>", methods=["POST"])
@login_required
def vastaus_uusi(viesti_id):
    form = VastausForm(request.form)
    viesti = Viesti.query.get(viesti_id)
    
    if not form.validate():
        return render_template("viestit/uusiVastaus.html", form = form, sanoma = "Lorem ipsum", viesti = viesti)
     
    vastaus = Viesti("null", form.sisalto.data, int(viesti_id))
    vastaus.kayttaja_id = current_user.id

    db.session().add(vastaus)
    db.session().commit()

    return redirect(url_for("viesti", viesti_id = viesti_id))