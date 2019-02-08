from application import app, db, views
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.viestit.models import Viesti
from application.tagit.models import Tagi, Tagitus
from application.viestit.forms import ViestiForm

@app.route("/viesti/uusi")
@login_required
def viesti_muokkaa_uusi():
    tagit = Tagi.query.all()
    return render_template("viesti/uusi.html", form = ViestiForm(), tagit=tagit)

@app.route("/viesti", methods=["POST"])
@login_required
def viesti_uusi():
    form = ViestiForm(request.form)

    if not form.validate():
        return render_template("viesti/uusi.html", form = form)
    
    viesti = Viesti(form.otsikko.data, form.sisalto.data)
    viesti.kayttaja_id = current_user.id
    db.session().add(viesti)
    db.session().flush()


    tagit = form.tagit.data
    # for tagi in tagit:
    #     t = Tagitus(int(tagi), viesti.id)
    #     db.session().add(t)
    #     db.session().commit()


    return redirect(url_for("index"))

# viestin näyttäminen
@app.route("/viesti/<viesti_id>")
def viesti(viesti_id):
    # form = VastausForm(request.form)

    viesti = Viesti.query.get(viesti_id)
    return render_template("viesti/viesti.html", viesti=viesti )   

# viestien näyttäminen omista tageista
@app.route("/omat")
@login_required
def omat():
    return render_template("viesti/omat.html", form = ViestiForm())