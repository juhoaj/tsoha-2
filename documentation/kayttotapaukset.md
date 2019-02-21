## Käyttäjätapaukset todo

1) käyttäjänhallinta
  * Käyttäjä voi vaihtaa salasanansa
  * Käyttäjä voi olla ylläpitäjä
  * Käyttäjä voi muuttaa itsensä ylläpitäjäksi (jotta toteutus katselmoitavissa helpommin)
  * (Vain) ylläpitäjän näkymässä näkee käyttäjät
  * Ylläpitäjä voi poistaa käyttäjän
  * (Out of scope?) Käyttäjä voi poistaa oman tilinsä

2) Viestit
  * Viestilistauksen viestiä (otsikko) klikkaamalla näkee viestiketjun (koko viestin ja sen mahdolliset vastaukset)
  * Uuteen viestiin voi viestiä kirjoittaessa lisätä tageja
  * Käyttäjä voi lisätä vastauksen viestiin
  * (Out of scope?) Käyttäjän lukemista viesteistä ja vastauksista pidetään kirjaa
  * (Out of scope?) Lukemattomat viestit (ja vastaukset) korostetaan käyttäjälle  
  * (Out of scope?) Käyttäjä näkee viestiketjussa ketkä ovat nähneet viestin (ei ketkä lukeneet vastaukset)
  * (Out of scope?) Viestilistausta voi rajata ajan perusteella

3) Tagit
  * (Vain) ylläpitäjä voi lisätä, poistaa ja muokata (nimi) tageja ylläpitonäkymässä
  * Käyttäjä voi tarkastella valittuun tagiin liitettyjä viestejä viestilistauksessa
  * (Out of scope?) Käyttäjä voi valita tageja seurattavaksi
  * (Out of scope?) Käyttäjä näkee seuraamiinsa tageihin liitetyt viestit viestilistauksena

## Käyttäjätapaukset done
  * Käyttäjä näkee tietokannasta tietoa sivulla
  * Käyttäjä voi luoda palveluun tunnukset
  * Käyttäjä voi kirjautua palveluun / palvelusta pois
  * Aloitusnäkymässä käyttäjä näkee viestilistauksen (kaikkien viestien otsikoista)
  * Käyttäjä voi luoda uuden viestin

## Tekniset stoorit todo 
  * Lisää luontilause parille tagille
  * Käyttäjä voi muuttaa itsensä ylläpitäjäksi
  * Navin siivous 
  * Tageissa CRUD (liitostaulun siivous)
  * Käyttäjässä CRUD
  * Kenttien validointi (myös ylipitkät syötteet)
  * ylläpidon urleihin myös tarkastus että käyttäjä on ylläpitäjä
  * vain käyttäjä tai ylläpitäjä voi muuttaa käyttäjän oman salasanansa
  * Käyttötapausten yhteydessä kuvattuna toimivat ja järkevät SQL-kyselyt
  * dokumentaatiossa CREATE TABLE -lauseet sekä indeksien lisäykset
  * isoksi kasvavissa listauksissa sivutus
  * SQL-virheiden käsittely
  * Mahdolliset virhetilanteet tuottavat ymmärrettäviä virheviestejä. 
  * ei pois-kommentoitua koodia 