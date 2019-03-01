### Asennus paikalliseen ympäristöön:
Paikallisessa ympäristössä ajaminen edellyttää Python 3:a.

Asentaminen projektin juurikansioista:
* virtuaaliympäristön luonti `python3 -m venv venv` (vain projektin hakemisen jälkeen)
* virtuaaliympäristöjen aktivointi `source venv/bin/activate`
* pakettien hakeminen repositiosta hakemisen jälkeen `pip install -r requirements.txt` (vain projektin hakemisen jälkeen)
* käynnistäminen lokaalisti `python run.py`

(Protip: muista deaktivoida muu mahdollinen python virtuaaliympäristö sen juuresta `deactivate` loitsulla ennen pip install:ia )

### Asennus Herokuun:

* Asenna Heroku CLI ellet ole jo sitä asentanut https://devcenter.heroku.com/articles/heroku-cli
* Kirjaudu Herokuun `heroku login -i`
* `heroku create` luo projektin Herokuun ja kertoo sovelluksen nimen
* Loitsi `git remote -v` ja tarkista että Git remote "heroku" on luotu, jos ei luo manuaalisersti
* Siirtääksesi projektin Herokuun julkaistavaksi loitsi `heroku git:remote -a <saamasi sovellusnimi>`

(Protip: jos lisäät pip:llä paketteja muista päivittää requirements.txt loitsula `pip freeze | grep -v pkg-resources > requirements.txt`)


### Projektin pääriippuvuudet:

  * Flask - sivujen piirtämiseen
  * SQLAlchemy - SQL-loitsinnan helpottaamiseen
  * Gunicorn - sovelluksen käynnistämiseksi Herokussa


### Front end tooling

Sovelluksen asentaminen Herokuun tai ajaminen paikallisesti ei vaadi front endin kääntämistä. Front end tarvitsee kääntää mikäli halutaan kehittää ulkoasua hydyntäen projektin nykyistä toolingia.

Front-endin kääntämiseen tarvitsemat paketit haetaan NPM:llä. Kehittämistä varten paketit pitää ensin käydä hakemassa loitsimalla projektin juuressa `npm i`. 

Automaatiota hoitaa Gulp koska Webpack vaikuttaa hieman raskaalle projektia varten. Gulp-taski kääntää tarvittavat tiedostot ja tallentaa ne /application/static kansioon. Gulpia varten on tarjolla seuraavat loitsut jotka ovat loitsittavissa juuresta:

  * `build` - kääntää /application/static/scss -kansion scss tiedostot ja laittaa ne /application/static/css kansion alle
  * `watch` - kuten build mutta havaitessaan muutoksia application/sources/scss, sekä aplication/templates/* -kansioissa kääntää muuttuneet scss tiedostot ja lähettää muutokset Browsersyncille. _huom! Browsersync ei kannata olla päällä tietokantatoiminnallisuuksia kehittäessä, se saattaa esim. sekoittaa POST kutsuja._
  * `update` - kopioi npm-paketeista tarvittavat tiedostot /application/static -kansion alle

Front-endin pääriippuvuudet:
  * Bootstrap 
  * Sass - css-tiedostojen kääntämistä varten
  * Gulp - automatisointi 
  * Browsersync - selainikkunan päivitys


### Projektin rakenne

```
── application
│   ├── src - sisältää frontendin lähdekoodin (scss)
│   ├── static - sisältää frontendin käännetyt lähteet (css jne.)
│   ├── templates
│   ... pakkaukset
├── package.json - sisältää frontendin riippuvuudet
├── requirements.txt - virtuaaliympäristön riippuvuudet
├── Procfile - ohjeistus tiedoston käynnistämiseen Herokussa
...
```