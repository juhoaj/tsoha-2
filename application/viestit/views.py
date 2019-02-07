from application import app, db, views
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.viestit.models import Viesti
from application.viestit.forms import ViestiForm

@app.route("/viesti/uusi")
@login_required
def viesti_muokkaa_uusi():
    return render_template("viesti/uusi.html", form = ViestiForm())

@app.route("/viesti", methods=["POST"])
@login_required
def viesti_uusi():
    form = ViestiForm(request.form)

    if not form.validate():
        return render_template("viesti/uusi.html", form = form)
    
    t = Viesti(form.otsikko.data, form.sisalto.data)
    t.kayttaja_id = current_user.id
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("index"))

# viestin näyttäminen
@app.route("/viesti/<viesti_id>")
def viesti(viesti_id):
    # form = VastausForm(request.form)

    t = Viesti.query.get(viesti_id)
    return render_template("viesti/index.html", viesti=t )   