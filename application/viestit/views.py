from application import app, db
from flask import render_template, request
from application.viestit.models import Viesti

@app.route("/viesti/uusi/")
def tasks_form():
    return render_template("viesti/uusi.html")

@app.route("/viesti/", methods=["POST"])
def viesti_luo():
    t = Viesti(request.form.get("otsikko"))
    db.session().add(t)
    db.session().commit()

    return "lisäilty!"