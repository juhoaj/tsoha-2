## Sovelluksen pakkaukset, polut ja funktiot

`viestit` -pakkaus näyttää viestit ja hallinnoi viestejä, bonuksena haku
  * GET / näyttää kaikki viestit
  * GET /viesti/# näyttää viestin jonka id on #
  * GET /viesti/#/lukijat näyttää viestin # lukijat
  * GET /viesti/uusi kirjoitusnäkymä uudelle viestille `viesti_muokkaa_uusi`
  * POST /viesti lähettää uuden viestin `viesti_uusi`
  * GET /haku näyttää haun tulokset
  * POST /haku lähettää uuden haun


 `tagit` -pakkaus tägien hallinta ja niihin liitettyjen viestien näyttäminen. tarjoaa listan kaikista ja käyttäjän tageista.
  * GET /tagi/nimi_tahi_# näyttää tagin 'nimi' tahi # näkymän ?????? `tagi` 
  * GET /omat omien tagien näkymä `omat`
  * GET /tagi_hallinta näyttää tagien hallintanäkymän `tagi_hallinta`
  * GET /tagi_hallinta/uusi kirjoitusnäkymä uudelle tagille `tagi_muokkaa_uusi`
  * GET /tagi_hallinta/#/muokkaa näyttää tagin # muokkausnäkymän `tagi_muokkaa`
  * POST /tagi_hallinta lähettää uuden tagin `tagi_uusi`
  * POST /tagi_hallinta/* päivittää tagin # `tagi_paivita`


`vastaukset` -pakkaus näyttää viestin ja sen vastaukset, hallinnoi vastauksia 
  * GET /viesti/#/#/lukijat näyttää viestin # vastauksen # lukijat
  * GET /viesti/#/uusi kirjoitusnäkymä viestin # uudelle vastaukselle
  * POST /viesti/# lähettää uuden vastauksen viestiin jonka id on #
 

`auktorisointi` -pakkaus käyttäjänhallinta ja kirjautuminen
  * GET /kirjaudu näyttää kirjautumisnäkymän
  * POST /kirjaudu lähettää kirjautumisen
  * POST /kirjaudu/uusi lähettää uuden käyttäjän
  * GET /admin näyttää ylläpidon ylläpitäjille
    