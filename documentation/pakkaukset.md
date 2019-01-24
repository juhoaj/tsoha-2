## Sovelluksen pakkaukset ja polut

`viestit` -pakkaus näyttää viestit ja hallinnoi viestejä, bonuksena haku
  * GET / näyttää kaikki viestit
  * GET /viesti/# näyttää viestin jonka id on #
  * GET /viesti/#/lukijat näyttää viestin # lukijat
  * GET /viesti/uusi kirjoitusnäkymä uudelle viestille
  * POST /viesti lähettää uuden viestin
  * GET /haku näyttää haun tulokset
  * POST /haku lähettää uuden haun

 `tagit` -pakkaus ???tarvitaanko??? onko erillinen vai meneekö jonnekin muualle? tägien hallinta ja niihin liitettyjen viestien näyttäminen. tarjoaa listan kaikista ja käyttäjän tageista.
  * GET /tag/nimi näyttää tagin 'nimi' näkymän
  * GET /omat omien tagien näkymä

`vastaukset` -pakkaus näyttää viestin ja sen vastaukset, hallinnoi vastauksia 
  * GET /viesti/#/#/lukijat näyttää viestin # vastauksen # lukijat
  * GET /viesti/#/uusi kirjoitusnäkymä viestin # uudelle vastaukselle
  * POST /viesti/# lähettää uuden vastauksen viestiin jonka id on #
 
`auktorisointi` -pakkaus käyttäjänhallinta ja kirjautuminen
  * GET /kirjaudu näyttää kirjautumisnäkymän
  * POST /kirjaudu lähettää kirjautumisen
  * POST /kirjaudu/uusi lähettää uuden käyttäjän
  * GET /admin näyttää ylläpidon ylläpitäjille
