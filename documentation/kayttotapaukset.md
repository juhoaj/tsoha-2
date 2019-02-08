## Käyttäjätapaukset todo

1) käyttäjänhallinta
  * Käyttäjä voi vaihtaa salasanansa
  * Käyttäjä voi olla ylläpitäjä
  * (Vain) ylläpitäjän näkymässä näkee käyttäjät
  * (Vain) ylläpitäjä voi lisätä / poistaa ylläpitäjiä 

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
  * Käyttäjä voi valita tageja seurattavaksi
  * Käyttäjä näkee seuraamiinsa tageihin liitetyt viestit viestilistauksena

## Käyttäjätapaukset done
  * Käyttäjä näkee tietokannasta tietoa sivulla
  * Käyttäjä voi luoda palveluun tunnukset
  * Käyttäjä voi kirjautua palveluun / palvelusta pois
  * Aloitusnäkymässä käyttäjä näkee viestilistauksen (kaikkien viestien otsikoista)
  * Käyttäjä voi luoda uuden viestin

## Tekniset stoorit todo 
  * Tageissa CRUD (liitostaulun siivous)
  * Kenttien validointi
  * ylläpidon urleihin myös tarkastus että käyttäjä on ylläpitäjä
  * vain käyttäjä tai ylläpitäjä voi muuttaa käyttäjän oman salasanansa