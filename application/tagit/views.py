from application import app, db, views
from flask import redirect, render_template, request, url_for
# from application.viestit.models import Viesti
from application.tagit.models import Tagi


@app.route("/tagi_hallinta/", methods=["GET"])
def tagi_hallinta():
    return render_template("tagi_hallinta/index.html", tagit = Tagi.query.all())

# uusi tagi

@app.route("/tagi_hallinta/uusi/")
def tagi_muokkaa_uusi():
    return render_template("tagi_hallinta/uusi.html")

@app.route("/tagi_hallinta/", methods=["POST"])
def tagi_uusi():
    t = Tagi(request.form.get("nimi"))
    db.session().add(t)
    db.session().commit()
    return redirect(url_for("tagi_hallinta"))


# tagin muokkaus

@app.route("/tagi_hallinta/<tagi_id>/muokkaa/")
def tagi_muokkaa(tagi_id):
    t = Tagi.query.get(tagi_id)
    # iidee = t.id 
    # db.session().commit()
    return render_template("tagi_hallinta/muokkaa.html", tagi=t )   

@app.route("/tagi_hallinta/<tagi_id>/", methods=["POST"])
def tagi_paivita(tagi_id):
    t = Tagi.query.get(tagi_id)
    t.nimi = request.form.get("nimi")
    db.session().commit()

    return redirect(url_for("tagi_hallinta"))
