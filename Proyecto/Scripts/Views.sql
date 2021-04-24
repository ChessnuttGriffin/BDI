USE BaseDeDatos1

DROP VIEW IF EXISTS Usuarios;

CREATE VIEW Usuarios AS
    SELECT
        id,
        txt_nombre
    FROM
        Cuenta
    WHERE
        id_rol = 2
    ORDER BY
        id ASC
;

DROP VIEW IF EXISTS TopPuntuaciones;

CREATE VIEW TopPuntuaciones AS
    SELECT 
        txt_partida,
        int_tiempo,
        Cuenta.txt_nombre,
        Tableros.txt_fileName
    FROM 
        Puntuaciones
    INNER JOIN
        Cuenta
    ON 
        Puntuaciones.id_cuenta=Cuenta.id
    INNER JOIN
        Tableros        
    ON 
        Puntuaciones.id_tablero=Tableros.id
    WHERE
        int_tiempo < 200
    ORDER BY
        int_tiempo ASC
;