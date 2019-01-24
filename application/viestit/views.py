from application import app, db, views
from flask import redirect, render_template, request, url_for
from application.viestit.models import Viesti

@app.route("/viesti/uusi/")
def tasks_form():
    return render_template("viesti/uusi.html")

@app.route("/viesti/", methods=["POST"])
def viesti_luo():
    t = Viesti(request.form.get("otsikko"))
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("index"))