## Sovelluksen pakkaukset, routet ja funktiot

Huom! html-templatet ovat pakkauksiensa nimisissä kansioissa nimettynä funktion mukaan, esim. `/tagit/omat.html` on `tagi`-pakkauksessa olevan `omat`-funktion käyttämä template.

`viestit` -pakkaus näyttää viestit ja hallinnoi viestejä, bonuksena haku
  * GET / näyttää kaikki viestit `index`
  * GET /tagi/# näyttää tagin 'nimi' tahi # näkymän `tagi` 
  * POST /tagi/# `X` lisää käyttäjälle seurattaviin tageihin tagin # jos seuraa value="kiinnostelee" ja poistaa jos seuraa value ="poistele" `tagi_seuraa`
  * GET /omat `X` omien tagien näkymä `omat`  
  * GET /viesti/# näyttää viestin jonka id on # `viesti`
  * GET /viesti/#/lukijat näyttää viestin # lukijat
  * GET /viesti/uusi `X` kirjoitusnäkymä uudelle viestille `viesti_muokkaa_uusi`
  * POST /viesti `X` lähettää uuden viestin `viesti_uusi`
* GET /viesti/#/uusi `X` kirjoitusnäkymä uudelle vastaukselle `vastraus_muokkaa_uusi`
  * POST /viesti/# `X` lähettää uuden vastauksen viestille # `vastaus_uusi`
  * GET /haku näyttää haun tulokset
  * POST /haku lähettää uuden haun

 `tagit` -pakkaus tägien hallinta
  * GET /tagi_hallinta `X` näyttää tagien hallintanäkymän `tagi_hallinta`
  * GET /tagi_hallinta/uusi `X` kirjoitusnäkymä uudelle tagille `tagi_muokkaa_uusi`
  * GET /tagi_hallinta/#/muokkaa `X` näyttää tagin # muokkausnäkymän `tagi_muokkaa`
  * POST /tagi_hallinta `X` lähettää uuden tagin `tagi_uusi`
  * POST /tagi_hallinta/# `X` päivittää tagin # `tagi_paivita`
  * POST /tagi_hallinta/#/poista `X` poistaa tagin # jos poista-kentän value="poistele" `tagi_poista`

`auktorisointi` -pakkaus käyttäjänhallintaan ja kirjautumiseen
  * GET /kirjaudu näyttää kirjautumisnäkymän ja ottaa vastaan kirjautumisen `kirjaudu`
  * GET /luo_tili syötä uusi käyttäjä `kayttaja_muokkaa_uusi`
  * POST /luo_tili `X` lähettää uuden käyttäjän `kayttaja_uusi`
  * GET /asetukset `X` paikka mistä pääsee vaihtamaan salasanan `kayttaja` 
  * GET /asetukset/#/paivita `X` vaihda käyttäjän # salasana `kayttaja_muokkaa`
  * POST /asetukset/# `XXX/XX` päivittää käyttäjän # salasanan `kayttaja_paivita`
  * GET /hallinta `XX` näyttää ylläpidon ylläpitäjille `yllapito`
  * GET /hallinta/kayttajat `XX` paikka mistä näkee käyttäjät `kayttaja_hallinta` 
  * POST /asetukset/#/poista `XX` poistaa käyttäjän # jos poista-kentän value="poistele" `kayttaja_poista`
    
`X` = reitti on vain kirjautuneen käyttäjän käytettävissä
`XX` = reitti on vain ylläpitäjän käytettävissä
`XXX` = reitti tarkistaa että id on sama kuin käyttäjällä