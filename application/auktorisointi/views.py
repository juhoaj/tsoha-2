from flask import redirect, render_template, request, url_for
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.sql import text, func, exists

from application import app, db, views
from application.auktorisointi.models import Kayttaja
from application.auktorisointi.forms import LoginForm, SignupForm, ChangePasswordForm

# kirjautuminen
@app.route("/kirjaudu", methods=["GET", "POST"])
def kirjaudu():
    if request.method == "GET":
        return render_template("auktorisointi/kirjaudu.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = Kayttaja.query.filter_by(kayttajanimi=form.kayttajanimi.data).first()
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
    return redirect(url_for("index"))

# omat asetukset
@app.route("/asetukset", methods=["GET"])
@login_required
def kayttaja():
    return render_template("auktorisointi/kayttaja.html", kayttaja = current_user)

# ylläpitäjuuden paivitys
@app.route("/asetukset/<kayttaja_id>/admin", methods=["POST"])
@login_required
def kayttaja_paivita_admin(kayttaja_id):
    if request.form.get("admin") != "vaihda":
        return redirect(url_for("kayttaja"))
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
    return render_template("auktorisointi/kayttaja_muokkaa.html", form=ChangePasswordForm() )   

# salasanan päivitys
@app.route("/asetukset/<kayttaja_id>/salasana", methods=["POST"])
@login_required
def kayttaja_paivita_salasana(kayttaja_id):
    form = ChangePasswordForm(request.form)
    if int(kayttaja_id) != current_user.id:
        return render_template("auktorisointi/kayttaja_muokkaa.html", form = form,
                               sanoma = "Väärä käyttäjä")

    t = Kayttaja.query.get(kayttaja_id)

    if form.salasana.data != form.toistettuSalasana.data:
        return render_template("auktorisointi/kayttaja_muokkaa.html", form = form,
                               sanoma = "Uudet salasanat eivät täsmää")
    if form.nykyinenSalasana.data != current_user.salasana:
        return render_template("auktorisointi/kayttaja_muokkaa.html", form = form,
                               sanoma = "Vanha salasana ei ole oikein")

    t.salasana = form.salasana.data
    db.session().commit()
    return redirect(url_for("kayttaja"))

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
    return render_template("auktorisointi/kayttaja_hallinta.html", kayttajat = kayttajat)

# käyttäjän poisto
@app.route("/asetukset/<kayttaja_id>/poista", methods=["POST"])
@login_required
def kayttaja_poista(kayttaja_id):
    #tarkistetaan ettei poisteta itseä
    if int(kayttaja_id) == current_user.id:
        kayttajat = Kayttaja.query.all()
        sanoma="Et voi poistaa itseäsi"
        return render_template("auktorisointi/kayttaja_hallinta.html", sanoma=sanoma, kayttajat = kayttajat)
    t = request.form.get("poista")
    if t == 'poistele':
        print('poistele--------------------')
    #poista käyttäjä
        stmt=text(" DELETE FROM kayttaja WHERE id = :id").params(id=kayttaja_id)
        db.engine.execute(stmt)
        
        #muuta viestien kirjoittajaksi poistettu, eli kayttaja_id=1
        stmt=text(" UPDATE viesti SET kayttaja_id = 1 WHERE kayttaja_id = :id").params(id=kayttaja_id)
        db.engine.execute(stmt)
        db.session().commit()
 
    return redirect(url_for("kayttaja_hallinta"))