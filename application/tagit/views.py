from flask import redirect, render_template, request, url_for
from flask_login import current_user
from sqlalchemy.sql import text, func, exists

from application import app, db, views, login_required
from application.tagit.models import Tagi
from application.tagit.forms import TagiForm

# tagien hallinta
@app.route("/hallinta/tagit/", methods=["GET"])
@login_required(role="ADMIN")
def tagi_hallinta():
    return render_template("tagit/tagi_hallinta.html", tagit = Tagi.query.all())

# uusi tagi
@app.route("/hallinta/tagit/uusi")
@login_required(role="ADMIN")
def tagi_muokkaa_uusi():
    return render_template("tagit/uusi.html", form=TagiForm())

@app.route("/hallinta/tagit", methods=["POST"])
@login_required(role="ADMIN")
def tagi_uusi():
    form = TagiForm(request.form)

    if not form.validate():
        return render_template("tagit/uusi.html", form = form)
    
    tagi = Tagi(form.nimi.data,)
    db.session().add(tagi)
    db.session().commit()

    return redirect(url_for("tagi_hallinta"))


# tagin muokkauksen näkymä
@app.route("/hallinta/tagit/<tagi_id>/muokkaa")
@login_required(role="ADMIN")
def tagi_muokkaa(tagi_id):
    form = TagiForm(request.form)
    
    t = Tagi.query.get(tagi_id)
    return render_template("tagit/muokkaa.html", tagi=t, form=form )   

# tagin poiston vastaanotto
@app.route("/hallinta/tagit/<tagi_id>", methods=["POST"])
@login_required(role="ADMIN")
def tagi_paivita(tagi_id):
    t = Tagi.query.get(tagi_id)
    t.nimi = request.form.get("nimi")
    db.session().commit()

    return redirect(url_for("tagi_hallinta"))

# tagin poisto
@app.route("/hallinta/tagit/<tagi_id>/poista", methods=["POST"])
@login_required(role="ADMIN")
def tagi_poista(tagi_id):
    t = request.form.get("poista")
  
    if t == 'poistele':
        #deleta tags from tagitus
        stmt=text(" DELETE FROM tagitus WHERE tagi_id = :id").params(id=tagi_id)
        db.engine.execute(stmt)
        db.session().commit()
        #delete tag
        stmt=text(" DELETE FROM tagi WHERE id = :id").params(id=tagi_id)
        db.engine.execute(stmt)
    return redirect(url_for("tagi_hallinta"))