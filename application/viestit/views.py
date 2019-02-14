from application import app, db, views
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.viestit.models import Viesti
from application.tagit.models import Tagi, Tagitus
from application.viestit.forms import ViestiForm

@app.route("/")
def index():
    return render_template("viestit/index.html", viestit = Viesti.query.all(), tagit=Tagi.query.all())

# näyttää viestit tagista #
@app.route("/tagi/<tagi_id>")
def tagi(tagi_id):
    t = Tagi.query.get(tagi_id)
    return render_template("viestit/tagi.html", tagi=t)


@app.route("/tagi/<tagi_id>", methods=["POST"])
@login_required
def tagi_uusi():
    form = TagiForm(request.form)

    t = Tagi(form.nimi.data)
    db.session().add(t)
    db.session().commit()
    return redirect(url_for("tagit"))

# viestien näyttäminen omista tageista
@app.route("/omat")
@login_required
def omat():
    return render_template("viestit/omat.html")

# viestin # näyttäminen
@app.route("/viesti/<viesti_id>")
def viesti(viesti_id):
    # form = VastausForm(request.form)

    viesti = Viesti.query.get(viesti_id)
    return render_template("viestit/viesti.html", viesti=viesti )   

@app.route("/viesti/uusi")
@login_required
def viesti_muokkaa_uusi():
    tagit = Tagi.query.all()
    return render_template("viestit/uusi.html", form = ViestiForm())

@app.route("/viesti", methods=["POST"])
@login_required
def viesti_uusi():
    form = ViestiForm(request.form)

    if not form.validate():
        return render_template("viestit/uusi.html", form = form)
    
    viesti = Viesti(form.otsikko.data, form.sisalto.data)
    viesti.kayttaja_id = current_user.id
    db.session().add(viesti)
    db.session().commit()


    # tagit = form.tagit.data
    # for tagi in tagit:
    #     t = Tagitus(int(tagi), viesti.id)
    #     db.session().add(t)
    #     db.session().commit()


    return redirect(url_for("index"))
