
### Projektin rakenne

```
── application
│   ├── src - sisältää frontendin lähdekoodin (scss)
│   ├── static - sisältää frontendin lähteet (css jne.)
│   ├── tasks
│   ├── templates
├── package.json - sisältää frontendin riippuvuudet
├── requirements.txt - virtuaaliympäristön riippuvuudet
├── Procfile - ohjeistus tiedoston käynnistämiseen Herokussa
...
```

### Backend
Noudattaa materiaalin esimerkkejä.

Kehittämisen loitsut juuresta:
* virtuaaliympäristöjen aktivointi `source venv/bin/activate`
* pakettien hakeminen `pip install -r requirements.txt`
* käynnistäminen lokaalisti `python run.py`

Pääriippuvuudet:
  * Flask - sivujen piirtämiseen
  * SQLAlchemy - SQL-loitsinnan helpottaamiseen
  * Gunicorn - sovelluksen käynnistämiseksi Herokussa

### Frontend tooling
Poikkeaa materiaalin esimerkistä jotta Boostrap olisi elegantimmin muokattavissa. Front-endin tarvitsemat paketit haetaan NPM:llä. Kehittämistä varten paketit pitää ensin käydä hakemassa loitsimalla projektin juuressa `npm i`.

Gulp-taski kääntää tarvittavat tiedostot ja tallentaa ne /application/static kansioon. Gulpia varten on tarjolla seuraavat loitsut jotka ovat loitsittavissa juuresta:

  * `build` - kääntää tiedostot ja laittaa ne oikeille paikoilleen /application/static kansion alle
  * `watch` - kuten build mutta havaitessaan muutoksia application/sources/scss -kansioissa kääntää muuttuneet tiedostot ja opioi ne /application/static/scss -kansioon
  * `update` - kopioi Bootstrapin npm-paketista tarvittavat tiedostot /application/src -kansioon

Pääriippuvuudet:
  * Bootstrap 
  * Sass - css-tiedostojen kääntämistä varten
  * Gulp - automatisointi 