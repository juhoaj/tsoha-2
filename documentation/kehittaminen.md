### Projektin rakenne

```
── application
│   ├── src - sisältää frontendin lähdekoodin (scss)
│   ├── static - sisältää frontendin lähteet (css jne.)
│   ├── templates
│   ... pakkaukset
├── package.json - sisältää frontendin riippuvuudet
├── requirements.txt - virtuaaliympäristön riippuvuudet
├── Procfile - ohjeistus tiedoston käynnistämiseen Herokussa
...
```

### Asennus paikalliseen ympäristöön:

* pakettien hakeminen repositiosta hakemisen jälkeen `pip install -r requirements.txt`
* virtuaaliympäristön luonti `python3 -m venv venv` (vain pakettien hakemisen jälkeen)
* virtuaaliympäristöjen aktivointi `source venv/bin/activate`
* käynnistäminen lokaalisti `python run.py`

(Protip: muista deaktivoida muut mahdolliset virtuaaliympäristöt ennen pip install:ia)

### Asennus Herokuun:

* Asenna Heroku CLI ellet ole jo sitä asentanut https://devcenter.heroku.com/articles/heroku-cli
* Kirjaudu Herokuun `heroku login -i`
* `heroku create` luo projektin Herokuun ja kertoo sovelluksen nimen
* Loitsi `git remote -v` ja tarkista että Git remote "heroku" on luotu, jos ei luo manuaalisersti
* Siirtääksesi projektin Herokuun julkaistavaksi loitsi `heroku git:remote -a <saamasi sovellusnimi>`




Pääriippuvuudet:
  * Flask - sivujen piirtämiseen
  * SQLAlchemy - SQL-loitsinnan helpottaamiseen
  * Gunicorn - sovelluksen käynnistämiseksi Herokussa


### Frontend tooling, todo
*Katselmointia varten ei tarvitse asentaa mitään*.

_Frontin kääntäminen kehittämistä varten:_ 

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