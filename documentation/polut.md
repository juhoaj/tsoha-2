  
  * GET / näyttää kaikki viestit
  * GET /tag/nimi näyttää tagin 'nimi' näkymän
  * GET /omat omien tagien näkymä
  * GET /viesti/uusi kirjoitusnäkymä uudelle viestille
  * GET /viesti/# näyttää viestin jonka id on #
  * GET /viesti/#/uusi kirjoitusnäkymä viestin # uudelle vastaukselle
  * GET /admin näyttää ylläpidon ylläpitäjille
  * GET /haku näyttää haun tulokset
  * GET /kirjaudu näyttää kirjautumisnäkymän

  * GET /viesti/#/lukijat näyttää viestin # lukijat
  * GET /viesti/#/#/lukijat näyttää viestin # vastauksen # lukijat

  * POST /viesti/uusi lähettää uuden viestin
  * POST /viesti/#/uusi lähettää uuden vastauksen viestiin jonka id on #
  * POST /haku lähettää uuden haun
  * POST /kirjaudu lähettää kirjautumisen
  * POST /kirjaudu/uusi lähettää uuden käyttäjän