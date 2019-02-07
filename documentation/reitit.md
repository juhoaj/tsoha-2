## Sovelluksen pakkaukset, routet ja funktiot

`viestit` -pakkaus näyttää viestit ja hallinnoi viestejä, bonuksena haku
  * GET / näyttää kaikki viestit `index`
  * GET /viesti/# näyttää viestin jonka id on # `viesti`
  * GET /viesti/#/lukijat näyttää viestin # lukijat
  * GET /viesti/uusi `X` kirjoitusnäkymä uudelle viestille `viesti_muokkaa_uusi`
  * POST /viesti `X` lähettää uuden viestin `viesti_uusi`
  * GET /haku näyttää haun tulokset
  * POST /haku lähettää uuden haun

 `tagit` -pakkaus tägien hallinta ja niihin liitettyjen viestien näyttäminen. tarjoaa listan kaikista ja käyttäjän tageista.
  * GET /tagi/# näyttää tagin 'nimi' tahi # näkymän `tagi` 
  * GET /omat `X` omien tagien näkymä `omat`
  * GET /tagi_hallinta `X` näyttää tagien hallintanäkymän `tagi_hallinta`
  * GET /tagi_hallinta/uusi `X` kirjoitusnäkymä uudelle tagille `tagi_muokkaa_uusi`
  * GET /tagi_hallinta/#/muokkaa `X` näyttää tagin # muokkausnäkymän `tagi_muokkaa`
  * POST /tagi_hallinta `X` lähettää uuden tagin `tagi_uusi`
  * POST /tagi_hallinta/# `X` päivittää tagin # `tagi_paivita`
  * POST /tagi_hallinta/#/poista `X` poistaa tagin # jos poista-kentän value="jebateukka" `tagi_poista`


`vastaukset` -pakkaus näyttää viestin ja sen vastaukset, hallinnoi vastauksia 
  * POST /viesti/# `X` lähettää uuden vastauksen viestiin jonka id on #
  * GET /viesti/#/#/lukijat `X` näyttää viestin # vastauksen # lukijat
 

`auktorisointi` -pakkaus käyttäjänhallintaan ja kirjautumiseen
  * GET /kirjaudu näyttää kirjautumisnäkymän ja ottaa vastaan kirjautumisen `kirjaudu`
  * GET /luo_tili syötä uusi käyttäjä `kayttaja_muokkaa_uusi`
  * POST /luo_tili `X` lähettää uuden käyttäjän `kayttaja_uusi`
  * GET /asetukset `X` paikka mistä pääsee vaihtamaan salasanan `kayttaja` 
  * GET /asetukset/#/paivita `X/XX` vaihda käyttäjän # salasana `kayttaja_muokkaa`
  * POST /asetukset/# `XXX/XX` päivittää käyttäjän # salasanan `kayttaja_paivita`
  * GET /hallinta `XX` näyttää ylläpidon ylläpitäjille `yllapito`
  * GET /hallinta/kayttajat `XX` paikka mistä näkee käyttäjät `kayttaja_hallinta` 
  * POST /asetukset/#/poista `XX` poistaa käyttäjän # jos poista-kentän value="jebateukka" `kayttaja_poista`
    
`X` = reitti on vain kirjautuneen käyttäjän käytettävissä
`XX` = reitti on vain ylläpitäjän käytettävissä
`XXX` = reitti tarkistaa että id on sama kuin käyttäjällä