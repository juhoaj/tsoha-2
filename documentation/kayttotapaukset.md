## Käyttäjätapaukset todo
  * (Vain) ylläpitäjä näkee ylläpitäjän näkymässä käyttäjät
  * Ylläpitäjä voi poistaa käyttäjän
  * (Vain) ylläpitäjä voi lisätä, poistaa ja muokata (nimi) tageja ylläpitonäkymässä
  

## Käyttäjätapaukset tehty
  * Käyttäjä näkee tietokannasta tietoa sivulla
  * Käyttäjä voi luoda palveluun tunnukset
  * Käyttäjä voi kirjautua palveluun / palvelusta pois
  * Käyttäjä näkee aloitusnäkymässä viestilistauksen (kaikkien viestien otsikoista)
  * Käyttäjä voi luoda uuden viestin
  * Käyttäjä voi vaihtaa salasanansa
  * Käyttäjä voi muuttaa itsensä ylläpitäjäksi (jotta toteutus katselmoitavissa helpommin)
  * Viestilistauksen viestiä (otsikko) klikkaamalla näkee viestiketjun (koko viestin ja sen mahdolliset vastaukset)
  * Uuteen viestiin voi viestiä kirjoittaessa lisätä tageja
  * Käyttäjä voi lisätä vastauksen viestiin

## Käyttäjätapaukset, jatkokehitys
  * Käyttäjän lukemista viesteistä ja vastauksista pidetään kirjaa
  * Lukemattomat viestit (ja vastaukset) korostetaan käyttäjälle  
  * Käyttäjä näkee viestiketjussa ketkä ovat nähneet viestin (ei ketkä lukeneet vastaukset)
  * Viestilistausta voi rajata ajan perusteella
  * Käyttäjä voi poistaa oman tilinsä
  * Käyttäjä voi tarkastella valittuun tagiin liitettyjä viestejä viestilistauksessa
  * Käyttäjä voi valita tageja seurattavaksi
  * Käyttäjä näkee seuraamiinsa tageihin liitetyt viestit viestilistauksena

## Tekniset stoorit todo 
  * käyttäjä 1, poistettu
  * Lisää luontilause parille tagille
  * Kenttien validointi (myös ylipitkät syötteet)
  * ylläpidon urleihin myös tarkastus että käyttäjä on ylläpitäjä
  * Käyttötapausten yhteydessä kuvattuna toimivat ja järkevät SQL-kyselyt
  * dokumentaatiossa CREATE TABLE -lauseet sekä indeksien lisäykset
  * isoksi kasvavissa listauksissa sivutus
  * SQL-virheiden käsittely
  * Mahdolliset virhetilanteet tuottavat ymmärrettäviä virheviestejä. 
  * ei pois-kommentoitua koodia 