from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db, views
from application.tagit.models import Tagi
from application.tagit.forms import TagiForm

# tagien hallinta
@app.route("/hallinta/tagit/", methods=["GET"])
@login_required
def tagi_hallinta():
    return render_template("tagit/index.html", tagit = Tagi.query.all())

# uusi tagi
@app.route("/hallinta/tagit/uusi")
@login_required
def tagi_muokkaa_uusi():
    return render_template("tagit/uusi.html", form=TagiForm())

@app.route("/hallinta/tagit", methods=["POST"])
@login_required
def tagi_uusi():
    form = TagiForm(request.form)

    if not form.validate():
        return render_template("tagit/uusi.html", form = form)
    
    tagi = Tagi(form.nimi.data,)
    db.session().add(tagi)
    db.session().commit()

    return redirect(url_for("tagi_hallinta"))


# tagin muokkaus
@app.route("/hallinta/tagit/<tagi_id>/muokkaa")
@login_required
def tagi_muokkaa(tagi_id):
    form = TagiForm(request.form)
    
    t = Tagi.query.get(tagi_id)
    return render_template("tagit/muokkaa.html", tagi=t, form=TagiForm() )   

@app.route("/hallinta/tagit/<tagi_id>", methods=["POST"])
@login_required
def tagi_paivita(tagi_id):
    t = Tagi.query.get(tagi_id)
    t.nimi = request.form.get("nimi")
    db.session().commit()

    return redirect(url_for("tagi_hallinta"))

# tagin poisto
@app.route("/hallinta/tagit/<tagi_id>/poista", methods=["POST"])
@login_required
def tagi_poista(tagi_id):
    t = Tagi.query.get(tagi_id)
    #poisto
    db.session().commit()

    return redirect(url_for("tagi_hallinta"))