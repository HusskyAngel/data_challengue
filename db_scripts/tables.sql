CREATE TABLE IF NOT EXISTS information(
	cod_localidad INT,
	id_provincia  SMALLINT, 
	id_departamento INT,
	categoria       VARCHAR(20),
	provincia       VARCHAR(30),
	localidad		VARCHAR (30),
	nombre 			VARCHAR(30),
	domicilio 		VARCHAR (30),
	cod_postal      INT,	
	num_telefono    BIGINT,
	mail         varchar(254),
	web 		VARCHAR(254)
);
