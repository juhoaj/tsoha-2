## Sovelluksen pakkaukset, routet ja funktiot

Huom! html-templatet ovat pakkauksiensa nimisissä kansioissa nimettynä funktion mukaan, esim. `/tagit/tagien_hallinta.html` on `tagi`-pakkauksessa olevan `tagien_hallinta`-routen käyttämä template.

`viestit` -pakkaus näyttää viestit ja hallinnoi viestejä, bonuksena haku
  * GET / näyttää kaikki viestit `index`
  * GET /tagi/# näyttää tagin 'nimi' tahi # näkymän `tagi` 
  * GET /viesti/# näyttää viestin jonka id on # `viesti`
  * GET, POST /viesti/uusi_viesti kirjoitusnäkymä ja vastaanotto uudelle viestille `uusi_viesti`
  * POST /viesti/# vastaanottaa uuden vastauksen viestille # `uusi_vastaus`

 `tagit` -pakkaus tägien hallinta
  * GET /yllapito/tagit näyttää tagien hallintanäkymän `tagien_hallinta`
  * GET, POST /yllapito/tagit/uusi lomake ja vastaanotto uudelle tagille `uusi_tagi`
  * GET, POST /yllapito/tagit/#/muokkaa lomake ja vastaanotto tagin muokkaamiselle `muokkaa_tagi`
  * POST /yllapito/tagit/#/poista poistaa tagin # jos poista-kentän value="poistele" `tagi_poista`

`auktorisointi` -pakkaus käyttäjänhallintaan ja kirjautumiseen
  * GET,POST /kirjaudu näyttää kirjautumisnäkymän ja ottaa vastaan kirjautumisen `kirjaudu`
  * GET, POIST /luo_tili näyttää ja ottaa vastaan uuden käyttäjän `uusi_kayttaja`
  * GET /asetukset paikka mistä pääsee vaihtamaan salasanan `asetukset` 
  * GET, POST /asetukset/#/muokkaa_salasanaa näyttää lomakkeen ja ottaa vastaan käyttäjän # muutetun salasana `muokkaa_salasanaa`
  * GET /yllapito näyttää ylläpidon ylläpitäjille `yllapito`
  * GET /yllapito/kayttajien_hallinta paikka mistä näkee käyttäjät `kayttajien_hallinta` 
  * POST /yllapito/#/poista poistaa käyttäjän # jos poista-kentän value="poistele" `poista_kayttaja`
    