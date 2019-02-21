from flask import redirect, render_template, request, url_for
# from application.viestit.models import Viesti
from flask_login import login_user, logout_user, login_required, current_user

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
                               sanoma = "Käyttäjää tai salasanaa ei löydy")
    login_user(user)
    return redirect(url_for("index"))   

@app.route("/kirjaudupois")
def kirjaudupois():
    logout_user()
    return redirect(url_for("index"))    

# uusi käyttäjä
@app.route("/luo_tili", methods=["GET"])
def kayttaja_muokkaa_uusi():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    return render_template("auktorisointi/kayttaja_muokkaa_uusi.html", form=SignupForm())

# luo uusi käyttäjä
@app.route("/luo_tili", methods=["POST"])
def kayttaja_uusi():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = SignupForm(request.form)
    print(form.salasana.data)
    print(form.toistettuSalasana.data)
    if form.salasana.data != form.toistettuSalasana.data:
        return render_template("auktorisointi/kayttaja_muokkaa_uusi.html", form = form,
                               sanoma = "Salasanat eivät täsmää")
    t = Kayttaja(form.kayttajanimi.data, form.salasana.data)
    db.session().add(t)
    db.session().commit()
    return redirect(url_for("kirjaudu"))

# omat asetukset
@app.route("/asetukset", methods=["GET"])
@login_required
def kayttaja():
    return render_template("auktorisointi/kayttaja.html", kayttaja = current_user)

# ylläpitäjuuden paivitys
@app.route("/asetukset/<kayttaja_id>/admin", methods=["POST"])
@login_required
def kayttaja_paivita_admin(kayttaja_id):
    # if kayttaja_id != current_user.id:
    #    return redirect(url_for("index"))
    if current_user.yllapitaja==True:
        current_user.yllapitaja=False
    else:
        current_user.yllapitaja=True  
    db.session().commit()
    return redirect(url_for("kayttaja"))

# salasanan muokkaus
@app.route("/asetukset/<kayttaja_id>/paivita_salasana", methods=["GET"])
@login_required
def kayttaja_muokkaa_salasana(kayttaja_id):
    # form = LoginForm(request.form)
    # t = Kayttaja.query.get(kayttaja_id)
    # db.session().commit()
    return render_template("auktorisointi/kayttaja_muokkaa.html", form=LoginForm() )   

# salasanan päivitys
@app.route("/asetukset/<kayttaja_id>/salasana", methods=["POST"])
@login_required
def kayttaja_paivita_salasana(kayttaja_id):
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