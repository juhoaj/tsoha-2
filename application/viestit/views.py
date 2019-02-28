from application import app, db, views
from flask import redirect, render_template, request, url_for, Blueprint
from flask_login import login_required, current_user
from sqlalchemy.sql import text, func, exists
from flask_paginate import Pagination, get_page_parameter, get_page_args

from application.viestit.models import Viesti
from application.tagit.models import Tagi, Tagitus, Seuratut
from application.viestit.forms import ViestiForm, VastausForm

# aloitussivu, ensimmäinen sivutettu sivu viesteistä
@app.route("/")
def index():

    # haetaan tagit
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

    # haetaan viestit ja viritellään paginaatio
    viesteja = Viesti.query.filter_by(vastaus_idlle = None).count()

    def get_viestit(offset=0, per_page=10):
        return Viesti.kaikki_viestit_vastausmaarilla()[offset: offset + per_page]
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total=viesteja
    pagination_viestit = get_viestit(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    
    return render_template("viestit/index.html",
        viestit=pagination_viestit,
        viesteja=viesteja,
        page=page,
        tagit=tagit,
        per_page=per_page,
        pagination=pagination,
    )

# näyttää viestit tagista #
@app.route("/tagi/<tagi_id>")
def tagi(tagi_id):
    t = Tagi.query.get(tagi_id)
    v = Tagitus.query.filter_by(tagi_id = tagi_id).count()

    # haetaan viestit tagi_id:llä ja muokataan viestit paginaatiota varten

    viestit = Viesti.viestit_tagista_vastausmaarilla(tagi_id)
    def get_viestit(offset=0, per_page=10):
        return viestit[offset: offset + per_page]

    # viritellään paginaatio
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total=len(viestit)
    pagination_viestit = get_viestit(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    return render_template("viestit/tagi.html",
        viestit=pagination_viestit,
        page=page,
        tagi=t,
        viesteja=v,
        per_page=per_page,
        pagination=pagination,
    )


# ottaa vastaan tagin seuraamisen ja muuttaa sen tilaa
@app.route("/tagi/<int:tagi_id>", methods=["POST"])
@login_required
def tagi_seuraa(tagi_id):
    
    t = request.form.get("seuraa")
  
    if t == 'kiinnostelee':
        stmt=text("INSERT INTO seuratut (tagi_id, kayttaja_id)" 
                  "VALUES (:tagi, :kayttaja)").params(tagi=tagi_id, kayttaja=1)
        db.engine.execute(stmt)

    return redirect(url_for("tagi", 
        tagi_id=tagi_id, 
        nappiteksti='testailumielessa')
    )

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
        tagit.append({"id":row[0], "nimi":row[1]})
     
    # haetaan viestin sisältö
    viesti = Viesti.query.get(viesti_id)

    # haetaan viestin luonut käyttäjä
    stmt=text(" SELECT kayttaja.kayttajanimi FROM kayttaja " 
              " WHERE kayttaja.id = :kayttaja_id " ).params(kayttaja_id=viesti.kayttaja_id)
    kayttaja=db.engine.execute(stmt).fetchone()

    # haetaan vastaukset ja liitetään niihin käyttäjät
    stmt=text(" SELECT * FROM viesti, kayttaja  " 
              " WHERE viesti.kayttaja_id = kayttaja.id " 
              " AND viesti.vastaus_idlle = :id").params(id=viesti.id)
    res2 = db.engine.execute(stmt)
    vastaukset = []
    for row in res2:
        vastaukset.append({"luotu":row[0], "id":row[1], "sisalto":row[3], "kayttajanimi":row[8]})

    #vastausformi
    form = VastausForm()

    return render_template("viestit/viesti.html", 
        viesti=viesti, 
        tagit=tagit, 
        kayttaja=kayttaja, 
        vastaukset=vastaukset, 
        form=form,
    )   

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
        return render_template("viestit/uusiViesti.html", 
            form = form, 
            sanoma = "Otsikon pitää olla vähintään neljä ja enintään neljäkymmentä sekä viestin vähintään neljä ja enintään tuhat merkkiä pitkä"
        )
    
    viesti = Viesti(form.otsikko.data, form.sisalto.data, None)
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

# uusi vastaus-vastaanotto
@app.route("/viesti/<viesti_id>", methods=["POST"])
@login_required
def vastaus_uusi(viesti_id):
    form = VastausForm(request.form)
    viesti = Viesti.query.get(viesti_id)
    
    if not form.validate():
        return render_template("/viesti/<viesti_id>", 
            form = form, 
            sanoma = "Vastauksen pitää olla vähintään neljä ja enintään tuhat merkkiä pitkä", 
            viesti = viesti
        )
     
    vastaus = Viesti(None, form.sisalto.data, int(viesti_id))
    vastaus.kayttaja_id = current_user.id

    db.session().add(vastaus)
    db.session().commit()

    return redirect(url_for("viesti", viesti_id = viesti_id))