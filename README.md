# Taagi-tietokantasovellus

Taagi on keskustelufoorumi jossa viestejä jaotellaan aiheryhmien sijasta liittämällä ne avainsanoihin ja yhteen viestiin voi liittää useamman avainsanan. 

Aloitusnäkymässä kävijä näkee kaikki viestit aikajärjestyksessä. Näkymässä on apunavigaatio jossa on listattu kaikki avainsanat, taagit. Niitä klikkaamalla siirrytään avainsana-näkymään jossa listataan kaikki avainsanaan liitetyt viestit. 

Jos viestillä on vastauksia näkee käyttäjä niiden lukumäärän viestilistauksessa. Aloitus- ja avainsana-näkymien viestilistauksissa päästään viestiä klikkaamalla  viestin näkymään jossa viesti ja sen mahdolliset vastaukset ovat luettavissa. 

Käyttäjän on luotava itsellensä käyttäjätili jotta hän voi lähettää uusia viestejä tai vastata viesteihin. 

Foorumin ylläpitäjällä on oma näkymä jonka kautta hän näkee hallinnoida palvelun käyttäjiä ja avainsanoja.

Sovellus on nähtävissä osoitteessa [https://tsoha-taagi.herokuapp.com](https://tsoha-taagi.herokuapp.com)


### Työn ja sovelluksen rajoitteet

Nykytilassaan sovellusta ei voida ottaa laajempaan käyttöön. Se ei tallenna ja varmista käyttäjän sähköpostiosoitetta sekä käyttäjän salasanat ovat plain textinä tietokannassa. Sen käyttöliittymää ei myöskään ole käyttäjätestattu.

Sovelluksen nykyinen kehitysversiota soveltuu hyvin pienen piirin koekäyttöön jatkokehityksen tueksi. Nyt kirjautuneella käyttäjällä on mahdollisuus muuttaa itsensä ylläpitäjäksi sovelluksen katselmoinnin helpottamiseksi ja ennen koekäyttöä voisi olla järkevintä muuttaa ylläpitäjät ylläpito-oikeuksien jakajiksi. 

Nykyinen front end tooling on valittu lähinnä sen takia että se on tuttu ja siihen löytyi helposti sovellettavissa oleva pohja aiemmista projekteista. Mikäli projektia jatkokehitetään MVC-monoliittina olisi syytä tarkistella front end toolingia tarkemmin.


### Omat kokemukset

Harjoitustyössä suurimmat haasteet olivat ensiksi Pythonin kanssa sinuiksi pääseminen ja toiseksi monesta moneen suhteet SQLAlchemyn ja WTFormsin kanssa. Esimerkiksi uuden viestin luomisen näkymän checkbox listan toimimaan saaminen vaati pajassa ohjaajaltakin luovuutta.

Hyvin ilahduttavaa oli kuinka tehokas harjoitustyöhön valittu stack oli ja loppua kohden sovelluksen kehittäminen tuntui hyvyin mielekkäälle.


### Dokumentaatio

  * [Loppukäyttäjäohje](https://github.com/juhoaj/tsoha-2/blob/master/documentation/loppukayttajaohje.md)
  * [Asentaminen, kehittäminen ja pääriippuvuudet](https://github.com/juhoaj/tsoha-2/blob/master/documentation/kehittaminen.md)
  * [Käyttäjäryhmät ja -tarinat (toteutettu/jatkokehitys)](https://github.com/juhoaj/tsoha-2/blob/master/documentation/kayttajatapaukset.md)
  * [Tietokantakaavio](https://github.com/juhoaj/tsoha-2/blob/master/documentation/tietokantakaavio.pdf)
  * [Tietokantataulut](https://github.com/juhoaj/tsoha-2/blob/master/documentation/tietokantataulut.md)
  * [Sovelluksen pakkaukset, route ja funktiot](https://github.com/juhoaj/tsoha-2/blob/master/documentation/reitit.md)
