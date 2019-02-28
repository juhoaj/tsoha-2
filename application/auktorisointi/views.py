from flask import redirect, render_template, request, url_for
from flask_login import login_user, logout_user, current_user
from sqlalchemy.sql import text, func, exists

from application import app, db, views, login_required
from application.auktorisointi.models import Kayttaja
from application.viestit.models import Viesti
from application.auktorisointi.forms import LoginForm, SignupForm, ChangePasswordForm


# kirjautuminen
@app.route("/kirjaudu", methods=["GET", "POST"])
def kirjaudu():
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("index"))
        return render_template("auktorisointi/kirjaudu.html", form = LoginForm())

    form = LoginForm(request.form)
    
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
@app.route("/luo_tili", methods=["GET", "POST"])
def uusi_kayttaja():
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("index"))

        return render_template("auktorisointi/uusi_kayttaja.html", form=SignupForm())

    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = SignupForm(request.form)
    
    if Kayttaja.query.filter_by(kayttajanimi = form.kayttajanimi.data).count() > 0:
        return render_template("auktorisointi/uusi_kayttaja.html", 
            form = form,
            sanoma = "Käyttäjänimi on varattu"
        )

    if form.salasana.data != form.toistettuSalasana.data:
        return render_template("auktorisointi/uusi_kayttaja.html", 
            form = form,
            sanoma = "Salasana ja toistettu salasana eivät vastaa toisiaan"
        )

    if not form.validate():
        return render_template("auktorisointi/uusi_kayttaja.html", 
            form = form, 
            sanoma = "Käyttäjänimen ja salasanan pitää olla vähintään neljä ja enintään kaksikymmentä merkkiä pitkä"
        )
    
    t = Kayttaja(form.kayttajanimi.data, form.salasana.data)
    db.session().add(t)
    db.session().commit()
    user = Kayttaja.query.filter_by(kayttajanimi=form.kayttajanimi.data).first()
    if not user:
        return render_template("auktorisointi/uusi_kayttaja.html", form = form,
                               sanoma = "Käyttäjää tai salasanaa ei löydy")
    login_user(user)
    return redirect(url_for("index")) 


# omat asetukset
@app.route("/asetukset", methods=["GET"])
@login_required(role="ANY")
def asetukset():
    return render_template("auktorisointi/asetukset.html", kayttaja = current_user)


# ylläpitäjuuden paivitys
@app.route("/asetukset/<kayttaja_id>/admin", methods=["POST"])
@login_required(role="ANY")
def muuta_adminiksi(kayttaja_id):
    if request.form.get("admin") != "vaihda":
        return redirect(url_for("kayttaja"))
    if current_user.yllapitaja==True:
        current_user.yllapitaja=False
    else:
        current_user.yllapitaja=True  
    db.session().commit()
    return redirect(url_for("asetukset"))


# salasanan muokkaus
@app.route("/asetukset/<kayttaja_id>/muokkaa_salasanaa", methods=["GET", "POST"])
@login_required(role="ANY")
def muokkaa_salasana(kayttaja_id):
    if request.method == "GET":
        return render_template("auktorisointi/muokkaa_salasana.html", form=ChangePasswordForm() )   

    form = ChangePasswordForm(request.form)
    if int(kayttaja_id) != current_user.id:
        return render_template("auktorisointi/muokkaa_salasana.html", form = form, sanoma = "Väärä käyttäjä")

    t = Kayttaja.query.get(kayttaja_id)

    if form.salasana.data != form.toistettuSalasana.data:
        return render_template("auktorisointi/muokkaa_salasana.html", form = form, sanoma = "Uudet salasanat eivät täsmää")

    if form.nykyinenSalasana.data != current_user.salasana:
        return render_template("auktorisointi/muokkaa_salasana.html", form = form, sanoma = "Vanha salasana ei ole oikein")

    t.salasana = form.salasana.data
    db.session().commit()
    return redirect(url_for("asetukset"))


# ylläpito
@app.route("/yllapito", methods=["GET"])
@login_required(role="ADMIN")
def yllapito():
    t = Kayttaja.query.get(1)
    return render_template("auktorisointi/yllapito.html", kayttaja = t)


# käyttäjien hallinta
@app.route("/yllapito/kayttajat", methods=["GET"])
@login_required(role="ADMIN")
def kayttajien_hallinta():
    kayttajat = Kayttaja.query.filter(Kayttaja.id != 1)
    return render_template("auktorisointi/kayttajien_hallinta.html", kayttajat = kayttajat)


# käyttäjän poisto
@app.route("/yllapito/<kayttaja_id>/poista", methods=["POST"])
@login_required(role="ANY")
def poista_kayttaja(kayttaja_id):

    if current_user.yllapitaja == False:
        return redirect(url_for("index"))

    if int(kayttaja_id) == current_user.id:
        kayttajat = Kayttaja.query.all()
        sanoma="Et voi poistaa itseäsi"
        return render_template("auktorisointi/kayttajien_hallinta.html", sanoma=sanoma, kayttajat = kayttajat)

    t = request.form.get("poista")
    
    if t == 'poistele':

        poistettavaKayttaja = Kayttaja.query.filter_by(id=kayttaja_id).first()
        db.session.delete(poistettavaKayttaja)
        db.session.commit()
        Viesti.vaihda_viestien_luojaa(poistettavaKayttaja.id)
        
    return redirect(url_for("kayttajien_hallinta"))