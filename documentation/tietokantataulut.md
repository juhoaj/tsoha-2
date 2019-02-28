## Tietokantataulut

````
CREATE TABLE kayttaja (
	luotu DATETIME,
	id INTEGER NOT NULL,
	kayttajanimi VARCHAR(144) NOT NULL,
	salasana VARCHAR(144) NOT NULL,
	yllapitaja BOOLEAN NOT NULL,
	PRIMARY KEY (id),
	CHECK (yllapitaja IN (0, 1))
);
````

````
CREATE TABLE tagi (
	luotu DATETIME,
	id INTEGER NOT NULL,
	nimi VARCHAR(40) NOT NULL,
	PRIMARY KEY (id)
);
````

````
CREATE TABLE viesti (
	luotu DATETIME,
	id INTEGER NOT NULL,
	otsikko VARCHAR(144),
	sisalto VARCHAR(2048) NOT NULL,
	kayttaja_id INTEGER NOT NULL,
	vastaus_idlle INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(kayttaja_id) REFERENCES kayttaja (id)
);
````

````
CREATE TABLE seuratut (
	id INTEGER NOT NULL,
	tagi_id INTEGER NOT NULL,
	kayttaja_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(tagi_id) REFERENCES tagi (id),
	FOREIGN KEY(kayttaja_id) REFERENCES kayttaja (id)
);
````

````
CREATE TABLE tagitus (
	id INTEGER NOT NULL,
	tagi_id INTEGER NOT NULL,
	viesti_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(tagi_id) REFERENCES tagi (id),
	FOREIGN KEY(viesti_id) REFERENCES viesti (id)
);
````