## Sovelluksen pakkaukset, routet ja funktiot

Huom! html-templatet ovat pakkauksiensa nimisissä kansioissa nimettynä funktion mukaan, esim. `/tagit/omat.html` on `tagi`-pakkauksessa olevan `omat`-funktion käyttämä template.

`viestit` -pakkaus näyttää viestit ja hallinnoi viestejä, bonuksena haku
  * GET / näyttää kaikki viestit `index`
  * GET /tagi/# näyttää tagin 'nimi' tahi # näkymän `tagi` 
  * POST /tagi/# lisää käyttäjälle seurattaviin tageihin tagin # jos seuraa value="kiinnostelee" ja poistaa jos seuraa value ="poistele" `tagi_seuraa`
  * GET /viesti/# näyttää viestin jonka id on # `viesti`
  * GET /viesti/uusi kirjoitusnäkymä uudelle viestille `viesti_muokkaa_uusi`
  * POST /viesti lähettää uuden viestin `viesti_uusi`
* GET /viesti/#/uusi kirjoitusnäkymä uudelle vastaukselle `vastraus_muokkaa_uusi`
  * POST /viesti/# lähettää uuden vastauksen viestille # `vastaus_uusi`
  * GET /haku näyttää haun tulokset
  * POST /haku lähettää uuden haun

 `tagit` -pakkaus tägien hallinta
  * GET /tagi_hallinta näyttää tagien hallintanäkymän `tagi_hallinta`
  * GET /tagi_hallinta/uusi kirjoitusnäkymä uudelle tagille `tagi_muokkaa_uusi`
  * GET /tagi_hallinta/#/muokkaa näyttää tagin # muokkausnäkymän `tagi_muokkaa`
  * POST /tagi_hallinta lähettää uuden tagin `tagi_uusi`
  * POST /tagi_hallinta/# päivittää tagin # `tagi_paivita`
  * POST /tagi_hallinta/#/poista poistaa tagin # jos poista-kentän value="poistele" `tagi_poista`

`auktorisointi` -pakkaus käyttäjänhallintaan ja kirjautumiseen
  * GET /kirjaudu näyttää kirjautumisnäkymän ja ottaa vastaan kirjautumisen `kirjaudu`
  * GET /luo_tili syötä uusi käyttäjä `kayttaja_muokkaa_uusi`
  * POST /luo_tili  lähettää uuden käyttäjän `kayttaja_uusi`
  * GET /asetukset paikka mistä pääsee vaihtamaan salasanan `kayttaja` 
  * GET /asetukset/#/paivita vaihda käyttäjän # salasana `kayttaja_muokkaa`
  * POST /asetukset/# päivittää käyttäjän # salasanan `kayttaja_paivita`
  * GET /hallinta näyttää ylläpidon ylläpitäjille `yllapito`
  * GET /hallinta/kayttajat paikka mistä näkee käyttäjät `kayttaja_hallinta` 
  * POST /asetukset/#/poista poistaa käyttäjän # jos poista-kentän value="poistele" `kayttaja_poista`
    