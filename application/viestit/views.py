from application import app, db, views
from flask import redirect, render_template, request, url_for, Blueprint
from flask_login import login_required, current_user
from sqlalchemy.sql import text, func, exists
from flask_paginate import Pagination, get_page_parameter, get_page_args

from application.viestit.models import Viesti
from application.tagit.models import Tagi, Tagitus
from application.auktorisointi.models import Kayttaja
from application.viestit.forms import ViestiForm, VastausForm


# aloitussivu, ensimmäinen sivutettu sivu viesteistä
@app.route("/")
def index():
    viesteja = Viesti.query.filter_by(vastaus_idlle = None).count()

    # viritellään paginaatio
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
        tagit=Tagi.kaikki_tagit_vastausmaarilla(),
        per_page=per_page,
        pagination=pagination,
    )


# näyttää viestit tagista #
@app.route("/tagi/<tagi_id>")
def tagi(tagi_id):
    t = Tagi.query.get(tagi_id)
    v = Tagitus.query.filter_by(tagi_id = tagi_id).count()
    viestit = Viesti.viestit_tagista_vastausmaarilla(tagi_id)

    # viritellään paginaatio
    def get_viestit(offset=0, per_page=10):
        return viestit[offset: offset + per_page]
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

# viestin # näyttäminen
@app.route("/viesti/<viesti_id>")
def viesti(viesti_id):
    viesti = Viesti.query.get(viesti_id)
    kayttaja = Kayttaja.query.filter_by(id=viesti.kayttaja_id).first()

    return render_template("viestit/viesti.html", 
        viesti=Viesti.query.get(viesti_id), 
        tagit=Tagi.tagit_viestille(viesti_id), 
        kayttaja=kayttaja, 
        vastaukset=Viesti.kaikki_vastaukset_kayttajanimilla(viesti_id), 
        form=VastausForm(),
    )   

# uusi viesti-näkymä
@app.route("/viesti/uusi" , methods=["GET", "POST"])
@login_required
def uusi_viesti():

    form = ViestiForm(request.form)
    # tagit = Tagi.query.all()
    form.tagit.query = Tagi.query.all()
    print(form.tagit)
    
    if request.method == "GET":
        return render_template("viestit/uusi_viesti.html", form=form)

    if not form.validate():
        return render_template("viestit/uusi_viesti.html", 
            form =form, 
            sanoma = "Otsikon pitää olla vähintään neljä ja enintään neljäkymmentä sekä viestin vähintään neljä ja enintään tuhat merkkiä pitkä"
        )
    
    viesti = Viesti(form.otsikko.data, form.sisalto.data, None)
    viesti.kayttaja_id = current_user.id

    db.session().add(viesti, viesti.id)
    db.session().commit()

    Tagitus.tallenna_viestin_tagit(form.tagit.data, viesti.id)

    return redirect(url_for("index"))


# uusi vastaus-vastaanotto
@app.route("/viesti/<viesti_id>", methods=["POST"])
@login_required
def uusi_vastaus(viesti_id):
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