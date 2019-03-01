## Tehdyt käyttäjätapaukset ja SQL-esimerkkilauseet
  * Käyttäjä voi luoda palveluun tunnukset
    ````
    INSERT INTO kayttaja (luotu, kayttajanimi, salasana, yllapitaja) 
        VALUES (CURRENT_TIMESTAMP, "kayttajanimi", "salasana", FALSE);
    ````

  * Käyttäjä voi kirjautua palveluun / palvelusta pois
    ````
    SELECT * FROM kayttaja WHERE kayttajanimi IS :kayttajanimi;
    ````

  * Käyttäjä näkee aloitusnäkymässä viestilistauksen (kaikkien viestien otsikoista)
    
    ````
    SELECT viesti.id, viesti.otsikko, vastauksia FROM viesti
        LEFT JOIN (
            SELECT viesti.vastaus_idlle,
            COUNT(viesti.vastaus_idlle) AS vastauksia
            FROM viesti WHERE viesti.vastaus_idlle IS NOT NULL
            GROUP BY viesti.vastaus_idlle
        ) AS subquery
        ON viesti.id = subquery.vastaus_idlle
        WHERE viesti.otsikko IS NOT NULL;
    ````

  * Käyttäjä näkee aloitusnäkymässä kaikkien tagien viestimäärän
    `````
    SELECT tagi.id, tagi.nimi, viestejä FROM tagi 
        LEFT JOIN ( 
            SELECT tagitus.tagi_id, 
            COUNT(tagitus.tagi_id) AS viestejä 
            FROM tagitus GROUP BY tagitus.tagi_id 
        ) AS subquery 
        ON tagi.id = subquery.tagi_id;
    `````

  * Käyttäjä voi tarkastella tagiin liitettyjä viestejä viestilistauksessa
    ````
    SELECT viesti.id, viesti.otsikko, subquery.vastauksia FROM viesti JOIN tagitus ON viesti.id = tagitus.viesti_id
        LEFT JOIN (
            SELECT viesti.vastaus_idlle,
            COUNT(viesti.vastaus_idlle) AS vastauksia
            FROM viesti WHERE viesti.vastaus_idlle IS NOT NULL
            GROUP BY viesti.vastaus_idlle
        ) AS subquery
        ON viesti.id = subquery.vastaus_idlle
        WHERE viesti.otsikko IS NOT NULL
            AND tagitus.tagi_id = 1;
    ````
  * Käyttäjä voi lukea viestin
    ````
    SELECT * FROM viesti, kayttaja 
        WHERE viesti.kayttaja_id = kayttaja.id 
            AND viesti.id = 2
    ````

  * Käyttäjä näkee viestiä lukiessaan sen vastaukset
    ````
    SELECT * FROM viesti, kayttaja 
        WHERE viesti.kayttaja_id = kayttaja.id 
            AND viesti.vastaus_idlle = 2
    ````
    
  * Kirjautunut käyttäjä voi luoda uuden viestin
    ````
    INSERT INTO viesti (luotu, otsikko, viesti, kayttaja_id) 
        VALUES (CURRENT_TIMESTAMP, "otsikko", "viesti", :2)
    ````

  * Kirjautunut käyttäjä voi viestiä kirjoittaessa liittää siihen tageja, jokaiselle tagille:
    ````
    INSERT INTO tagitus (tagi_id, viesti_id) 
        VALUES (:tagi_id, :viesti_id)
    ````
     

  * Kirjautunut käyttäjä voi vaihtaa oman salasanansa
    ````
    UPDATE kayttaja SET salasana = "uusi_salasana" 
        WHERE id=:kayttaja_id;
    ````

  * Kirjautunut käyttäjä voi muuttaa itsensä ylläpitäjäksi (jotta toteutus katselmoitavissa helpommin)
    ````
    UPDATE kayttaja 
        SET yllapitaja = TRUE 
        WHERE id=:kayttaja_id;
    ````

  * Viestilistauksen viestiä (otsikko) klikkaamalla näkee viestiketjun (koko viestin ja sen mahdolliset vastaukset)
    ````
    SELECT * FROM viesti WHERE vastaus_idlle = 1;
    ````

  * Kirjautunut käyttäjä voi lisätä vastauksen viestiin
    ````
    INSERT INTO kayttaja (luotu, kayttajanimi, salasana, yllapitaja) 
        VALUES (CURRENT_TIMESTAMP, "kayttajanimi", "salasana", FALSE);
    ````

  * (Vain) ylläpitäjä näkee ylläpitäjän näkymässä käyttäjät
    ````
    SELECT * FROM kayttaja WHERE NOT id=1
    ````

  * (Vain) ylläpitäjä voi poistaa käyttäjän (paitsi itsensä)
    ````
    DELETE FROM kayttaja WHERE id = 2;
    
    UPDATE viesti SET kayttaja_id = 1 WHERE kayttaja_id = 2"
    ````

  * (Vain) ylläpitäjä voi lisätä tagin
    ````
    INSERT INTO tagi (luotu, nimi) VALUES (CURRENT_TIMESTAMP, "tagi_nimi");
    ````

  * (Vain) ylläpitäjä voi muokata tagin nimeä 
    ````
    UPDATE tagi SET nimi = "uusi_nimi" WHERE id=:tagi_id;
    ````

  * (Vain) ylläpitäjä voi poistaa tagin
    ````
    DELETE FROM tagitus WHERE tagi_id = 2;
    
    DELETE FROM tagi WHERE id = 2;
    ````


## Käyttäjätapaukset, jatkokehitys
  * Ylläpitäjä voi asettaa toisen käyttäjän ylläpitäjäksi
  * Käyttäjältä kysytään tiliä luotaessa sähköpostiosoite johon lähetetään tilin aktivointia varten koodi
  * Käyttäjä voi tilata sähköpostiinsa salasanan nollaus-linkin
  * Käyttäjä näkee viestinäkymässä takaisin -napin joka vie edelliselle sivulle (etusivu tai jokin tagi-sivu)
  * Käyttäjällä on viestien ja vastauksien kirjoittamisessa käytössä rich text -editori
  * Käyttäjä voi valita tageja seurattavaksi
  * Käyttäjä näkee seuraamiinsa tageihin liitetyt viestit viestilistauksena
  * Viestilistausta voi rajata ajan perusteella
  * Käyttäjän lukemista viesteistä ja vastauksista pidetään kirjaa
  * Lukemattomat viestit (ja vastaukset) korostetaan käyttäjälle  
  * Käyttäjä näkee viestiketjussa ketkä ovat nähneet viestin (ei ketkä lukeneet vastaukset)
