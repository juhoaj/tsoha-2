from flask import redirect, render_template, request, url_for
# from application.viestit.models import Viesti
from flask_login import login_user, logout_user, login_required

from application import app, db, views
from application.auktorisointi.models import Kayttaja
from application.auktorisointi.forms import LoginForm, SignupForm

# kirjautuminen
@app.route("/kirjaudu", methods=["GET", "POST"])
def kirjaudu():
    if request.method == "GET":
        return render_template("auktorisointi/kirjaudu.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = Kayttaja.query.filter_by(kayttajanimi=form.kayttajanimi.data, salasana=form.salasana.data).first()
    if not user:
        return render_template("auktorisointi/kirjaudu.html", form = form,
                               viesti = "No such username or password")
    login_user(user)
    return redirect(url_for("index"))   

@app.route("/kirjaudupois")
def kirjaudupois():
    logout_user()
    return redirect(url_for("index"))    


# uusi käyttäjä
@app.route("/luo_tili", methods=["GET"])
def kayttaja_muokkaa_uusi():
    return render_template("auktorisointi/kayttaja_muokkaa_uusi.html", form=SignupForm())

# luo uusi käyttäjä
@app.route("/luo_tili", methods=["POST"])
def kayttaja_uusi():
    form = LoginForm(request.form)

    # lisää vahvistus jotta salasana täsmää

    t = Kayttaja(form.kayttajanimi.data, form.salasana.data)
    db.session().add(t)
    db.session().commit()
    return redirect(url_for("kirjaudu"))

# asetukset
@app.route("/asetukset", methods=["GET"])
@login_required
def kayttaja():
    t = Kayttaja.query.get(1)
    return render_template("auktorisointi/kayttaja.html", kayttaja = t)


# salasanan muokkaus
@app.route("/asetukset/<kayttaja_id>/paivita", methods=["GET"])
@login_required
def kayttaja_muokkaa(kayttaja_id):
    # form = LoginForm(request.form)
    # t = Kayttaja.query.get(kayttaja_id)
    # db.session().commit()
    return render_template("auktorisointi/kayttaja_muokkaa.html", form=LoginForm() )   

# salasanan päivitys
@app.route("/asetukset/<kayttaja_id>", methods=["POST"])
@login_required
def kayttaja_paivita(kayttaja_id):
    t = Kayttaja.query.get(kayttaja_id)
    t.salasana = request.form.get("salasana")
    db.session().commit()

    return redirect(url_for("asetukset"))

# ylläpito
@app.route("/hallinta", methods=["GET"])
@login_required
def yllapito():
    t = Kayttaja.query.get(1)
    return render_template("auktorisointi/yllapito.html", kayttaja = t)

# käyttäjien listaus
@app.route("/hallinta/kayttajat", methods=["GET"])
@login_required
def kayttaja_hallinta():
    kayttajat = Kayttaja.query.all()
    return render_template("auktorisointi/kayttajat.html", kayttajat = kayttajat)

# Käyttäjän poisto
@app.route("/asetukset/<kayttaja_id>/poista", methods=["POST"])
@login_required
def kayttaja_poista(kayttaja_id):

    # !!! muista tarkistaa että käyttäjä on kayttaja_id

    return redirect(url_for("kayttaja_hallinta"))