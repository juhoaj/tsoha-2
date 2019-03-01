from flask import redirect, render_template, request, url_for
from flask_login import current_user
from sqlalchemy.sql import text, func, exists

from application import app, db, views, login_required
from application.tagit.models import Tagi
from application.tagit.forms import TagiForm


# tagien hallinta
@app.route("/yllapito/tagit/", methods=["GET"])
@login_required(role="ADMIN")
def tagien_hallinta():
    return render_template("tagit/tagien_hallinta.html", tagit = Tagi.query.all())


# uusi tagi
@app.route("/yllapito/tagit/uusi", methods=["GET", "POST"])
@login_required(role="ADMIN")
def uusi_tagi():

    form = TagiForm(request.form)

    if request.method == "GET":
        return render_template("tagit/uusi_tagi.html", form=form)

    if not form.validate():
        return render_template("tagit/uusi_tagi.html", 
            form = form, 
            sanoma = "Taagin pitää olla vähintään neljä ja enintään kymmenen merkkiä pitkä"
        )
    if Tagi.query.filter_by(nimi = form.nimi.data).count() > 0:
        return render_template("tagit/uusi_tagi.html", 
            form = form,
            sanoma = "Taaginimi on jo käytössä"
        )
    tagi = Tagi(form.nimi.data,)
    db.session().add(tagi)
    db.session().commit()

    return redirect(url_for("tagien_hallinta"))


# tagin muokkauksen näkymä
@app.route("/yllapito/tagit/<tagi_id>/muokkaa", methods=["GET", "POST"])
@login_required(role="ADMIN")
def muokkaa_tagi(tagi_id):
    form = TagiForm(request.form)
    if request.method == "GET":
        
        t = Tagi.query.get(tagi_id)
        return render_template("tagit/muokkaa_tagi.html", tagi=t, form=form )   

    if not form.validate():
        return render_template("tagit/uusi_tagi.html", 
            form = form, 
            sanoma = "Taagin pitää olla vähintään neljä ja enintään kymmenen merkkiä pitkä"
        )
    if Tagi.query.filter_by(nimi = form.nimi.data).count() > 0:
        return render_template("tagit/uusi_tagi.html", 
            form = form,
            sanoma = "Taaginimi on jo käytössä"
        )
    t = Tagi.query.get(tagi_id)
    t.nimi = request.form.get("nimi")
    db.session().commit()

    return redirect(url_for("tagien_hallinta"))


# tagin poisto
@app.route("/yllapito/tagit/<tagi_id>/poista", methods=["POST"])
@login_required(role="ADMIN")
def tagi_poista(tagi_id):
    t = request.form.get("poista")
  
    if Tagi.query.count() == 1:
        return render_template("tagit/tagien_hallinta.html", 
            form = TagiForm(request.form),
            sanoma = "Kaikkia tageja ei voi poistaa", 
            tagit = Tagi.query.all()
        )
        
    
    if t == 'poistele':
        Tagi.poista_tagi(tagi_id)
        
    return redirect(url_for("tagien_hallinta"))