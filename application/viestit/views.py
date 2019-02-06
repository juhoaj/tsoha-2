from application import app, db, views
from flask import redirect, render_template, request, url_for
from application.viestit.models import Viesti
from application.viestit.forms import ViestiForm

@app.route("/viesti/uusi/")
def viesti_muokkaa_uusi():
    return render_template("viesti/uusi.html", form = ViestiForm())

@app.route("/viesti/", methods=["POST"])
def viesti_uusi():
    form = ViestiForm(request.form)

    if not form.validate():
        return render_template("viesti/uusi.html", form = form)
    
    t = Viesti(form.otsikko.data)
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("index"))

# viestin näyttäminen

@app.route("/viesti/<viesti_id>/")
def viesti(viesti_id):
    # form = VastausForm(request.form)

    t = Viesti.query.get(viesti_id)
    # iidee = t.id 
    # db.session().commit()
    return render_template("viesti/index.html", viesti=t )   