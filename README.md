# Taagi-tietokantasovellus

Taagi on keskustelufoorumi jossa viestejä jaotellaan aiheryhmien sijasta liittämällä ne avainsanoihin ja yhteen viestiin voi liittää useamman avainsanan. 

Aloitusnäkymässä kävijä näkee kaikki viestit aikajärjestyksessä. Näkymässä on apunavigaatio jossa on listattu kaikki avainsanat, taagit. Niitä klikkaamalla siirrytään avainsana-näkymään jossa listataan kaikki avainsanaan liitetyt viestit. 

Jos viestillä on vastauksia näkee käyttäjä niiden lukumäärän viestilistauksessa. Aloitus- ja avainsana-näkymien viestilistauksissa päästään viestiä klikkaamalla  viestin näkymään jossa viesti ja sen mahdolliset vastaukset ovat luettavissa. 

Käyttäjän on luotava itsellensä käyttäjätili jotta hän voi lähettää uusia viestejä tai vastata viesteihin. 

Foorumin ylläpitäjällä on oma näkymä jonka kautta hän voi hallinnoida palvelun käyttäjiä ja avainsanoja.

Sovellus on nähtävissä osoitteessa [https://tsoha-taagi.herokuapp.com](https://tsoha-taagi.herokuapp.com)


### Työn ja sovelluksen rajoitteet

Sovelluksen nykyinen kehitysversiota soveltuu suljettuun koekäyttöön jatkokehityksen tueksi. Sovellus ei tallenna ja varmista käyttäjän sähköpostiosoitetta eivätkä käyttäjän salasanat ole kryptattu. Lisäksi kirjautuneella käyttäjällä on mahdollisuus muuttaa itsensä ylläpitäjäksi katselmoinnin helpottamiseksi.

Käyttöliittymää ei ole käyttäjätestattu ja on hyvin mahdollista että ensimmäisen testauksen tuloksena on, että visuaalista hierarkia pitää jumpata saavutettavuuden parantamiseksi. Nykyinen käyttöliittymä on kuitenkin perusteltu sillä kiinnostavaa on juurikin selvittää kuinka paljon hierarkiaa pitää jumpata.

Nykyinen front end tooling on valittu lähinnä sen takia että se on tuttu ja siihen löytyi helposti sovellettavissa oleva pohja aiemmista projekteista. Mikäli projektia jatkokehitetään MVC-monoliittina olisi syytä tarkistella front end toolingia tarkemmin.


### Omat kokemukset

Harjoitustyössä oli muutama suurempi haaste. Alkuun Pythonin kanssa sinuiksi pääsemisessä meni aikansa ja monesta moneen suhteet SQLAlchemyn ja WTFormsin kanssa eivät olleet yksiselitteisiä. Esimerkiksi uuden viestin näkymän checkbox listan toimimaan saaminen oli hyvin haastavaa. PostgreSQL:n ja SQLite toiminnalliset eroavaisuudet olivat kaikkinensa hyvin turhauttavia.

Hyvin ilahduttavaa oli kuinka tehokas harjoitustyöhön valittu stack oli ja loppua kohden sovelluksen kehittäminen tuntui hyvyin mielekkäälle. Kurssi vastasi tehokkaasti mieltäni aiemmin askartaneeseen kysymykseen "miksi monet arvostavat Pythonia ja sen ekosysteemiä backend -käytössä".


### Dokumentaatio

  * [Loppukäyttäjäohje](https://github.com/juhoaj/tsoha-2/blob/master/documentation/loppukayttajaohje.md)
  * [Asentaminen, kehittäminen ja pääriippuvuudet](https://github.com/juhoaj/tsoha-2/blob/master/documentation/kehittaminen.md)
  * [Käyttäjäryhmät ja -tarinat (toteutettu/jatkokehitys)](https://github.com/juhoaj/tsoha-2/blob/master/documentation/kayttajatapaukset.md)
  * [Tietokantakaavio](https://github.com/juhoaj/tsoha-2/blob/master/documentation/tietokantakaavio.pdf) 
  * [Tietokantataulut](https://github.com/juhoaj/tsoha-2/blob/master/documentation/tietokantataulut.md)
  * [Sovelluksen pakkaukset, route ja funktiot](https://github.com/juhoaj/tsoha-2/blob/master/documentation/reitit.md)
