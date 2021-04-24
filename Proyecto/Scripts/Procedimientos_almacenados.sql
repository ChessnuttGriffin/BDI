USE BaseDeDatos1;

DROP PROCEDURE IF EXISTS sp_actualizarJuego;
DROP PROCEDURE IF EXISTS sp_autenticar;
DROP PROCEDURE IF EXISTS sp_crearUsuario;
DROP PROCEDURE IF EXISTS sp_eliminarJuego;
DROP PROCEDURE IF EXISTS sp_eliminarUsuario;
DROP PROCEDURE IF EXISTS sp_guardarPuntuacion;
DROP PROCEDURE IF EXISTS sp_iniciarJuego;
DROP PROCEDURE IF EXISTS sp_modificarUsuario;
DROP PROCEDURE IF EXISTS sp_obtenerNombrePartida;
DROP PROCEDURE IF EXISTS sp_obtenerPassword;
DROP PROCEDURE IF EXISTS sp_obtenerRol;
DROP PROCEDURE IF EXISTS sp_obtenerTablero;
DROP PROCEDURE IF EXISTS sp_obtenerTablero2;
DROP PROCEDURE IF EXISTS sp_obtenerTiempo;
DROP PROCEDURE IF EXISTS sp_obtenerUltimoJuego;



delimiter //


/*sp_obtenerPassword*/
CREATE PROCEDURE sp_obtenerPassword (IN nombre TEXT,IN Cpassword TEXT, OUT Vpassword TEXT)
       BEGIN
         SELECT Cuenta.txt_password INTO Vpassword FROM Cuenta
         WHERE (BINARY Cuenta.txt_nombre = nombre ) AND ( BINARY Cuenta.txt_password = Cpassword );

       END// 

/*sp_autenticar */

CREATE PROCEDURE sp_autenticar (IN nombre TEXT,IN Cpassword TEXT, OUT idUsuario INT)
       BEGIN
         SELECT Cuenta.id INTO idUsuario FROM Cuenta
         WHERE (BINARY Cuenta.txt_nombre = nombre ) AND ( BINARY Cuenta.txt_password = Cpassword );

         IF idUsuario IS NOT NULL THEN
            INSERT INTO Bitacora(id_cuenta, txt_accion, dat_fecha) VALUES(
                idUsuario,
                'AUTENTICACION',
                NOW()
              );
              COMMIT;
          END IF;
         END//


/*sp_obtenerRol*/

CREATE PROCEDURE sp_obtenerRol (IN nombre TEXT,IN Cpassword TEXT, OUT datos TEXT)
       BEGIN
         SELECT Rol.txt_nombreRol INTO datos FROM Cuenta JOIN Rol ON Cuenta.id_rol = Rol.id
         WHERE (BINARY Cuenta.txt_nombre = nombre) AND (BINARY Cuenta.txt_password = Cpassword) ;
       END//

/*sp_obtenerUltimoJuego*/

CREATE PROCEDURE sp_obtenerUltimoJuego ( IN idUsuario INT, OUT jsonPartida LONGTEXT)
      BEGIN
        SELECT PartidaEspera.jso_partida INTO jsonPartida FROM PartidaEspera WHERE PartidaEspera.id_cuenta= idUsuario ;        
          INSERT INTO Bitacora(id_user, txt_accion, dat_fecha) VALUES(
                idUsuario,
                "REANUDAR JUEGO",
                NOW()
              );
          COMMIT;
      END//
  
/* sp_obtenerTablero*/

CREATE PROCEDURE sp_obtenerTablero ( IN idUsuario INT,OUT jsonTablero LONGTEXT)
      BEGIN
        SELECT Tableros.jso_partida INTO jsonTablero FROM PartidaEspera  
        INNER JOIN Tableros        
        ON PartidaEspera.id_tablero=Tableros.id
        WHERE PartidaEspera.id_cuenta= idUsuario;
      END//
    
/* sp_obtenerTablero2*/

CREATE PROCEDURE sp_obtenerTablero2 ( IN idTablero INT,OUT jsonTablero LONGTEXT)
      BEGIN
        SELECT Tableros.jso_partida INTO jsonTablero FROM Tableros  WHERE Tableros.id= idTablero;
      END//

/* sp_obtenerTiempo*/

CREATE PROCEDURE sp_obtenerTiempo ( IN idUsuario INT,OUT tiempo INT)
      BEGIN
        SELECT PartidaEspera.int_tiempo INTO tiempo FROM PartidaEspera WHERE PartidaEspera.id_cuenta= idUsuario;
      END//

/*sp_obtenerNombrePartida*/

CREATE PROCEDURE sp_obtenerNombrePartida ( IN idUsuario INT,OUT nombrePartida TEXT)
      BEGIN
        SELECT PartidaEspera.txt_partida INTO nombrePartida FROM PartidaEspera WHERE PartidaEspera.id_cuenta= idUsuario;
      END//

/*sp_actualizarJuego*/
 
CREATE PROCEDURE sp_actualizarJuego (IN idUsuario INT, IN tiempo INT, IN jsonPartida LONGTEXT )
      BEGIN
        
        
        UPDATE PartidaEspera SET
          jso_partida = jsonPartida,
          int_tiempo = tiempo
        WHERE
          id_cuenta = idUsuario;

        COMMIT;
        
      END//

/*sp_eliminarJuego*/
 
CREATE PROCEDURE sp_eliminarJuego (IN partidaId INT)
      BEGIN
        
        DECLARE existe INT;

        SELECT PartidaEspera.id INTO existe FROM PartidaEspera WHERE BINARY partidaId = PartidaEspera.id;
        
        IF existe IS NOT NULL THEN
          DELETE FROM PartidaEspera
          WHERE PartidaEspera.id = partidaId;
          COMMIT;
        END IF;
        
      END//

/*sp_iniciarJuego*/
CREATE PROCEDURE sp_iniciarJuego(IN nombrePartida TEXT, IN idUsuario INT, IN jsonPartida LONGTEXT, OUT existe INT, OUT nombre TEXT)
      BEGIN

        
        SELECT PartidaEspera.id INTO existe FROM PartidaEspera WHERE (BINARY PartidaEspera.txt_partida = nombrePartida) AND (PartidaEspera.id_cuenta = idUsuario);

        IF existe IS NULL THEN
          INSERT INTO BaseDeDatos1.PartidaEspera (txt_partida, tim_date, id_cuenta, partidaJSON) VALUES (
            nombrePartida,
            NOW(),
            idUsuario,
            jsonPartida
          );
          INSERT INTO Bitacora(id_cuenta, txt_accion, dat_fecha) VALUES(
                idUsuario,
                "INICIAR JUEGO",
                NOW()
              );
          SELECT PartidaEspera.id INTO existe FROM PartidaEspera WHERE (BINARY PartidaEspera.txt_partida = nombrePartida) AND (PartidaEspera.id_cuenta = idUsuario);
          COMMIT;
        ELSE
          SELECT NULL INTO existe;
        END IF;

      END//

/*sp_crearUsuario */
CREATE PROCEDURE sp_crearUsuario (IN nombre TEXT, IN Cpassword TEXT, OUT valido INT)
      BEGIN
        SELECT Cuenta.id INTO valido FROM Cuenta WHERE (Cuenta.txt_nombre = nombre );

        IF valido IS NULL THEN
          INSERT INTO Cuenta(txt_nombre, txt_password) 
          VALUES
          (
            nombre,
            Cpassword
          );
          COMMIT;
        END IF;

      END//

/*sp_modificarUsuario*/
CREATE PROCEDURE sp_modificarUsuario (IN idUsuario INT, IN nombre TEXT, IN Cpassword TEXT, OUT existe INT)
  BEGIN

    SELECT Cuenta.id INTO existe FROM Cuenta WHERE (Cuenta.txt_nombre = nombre );

        IF existe IS NULL THEN
          UPDATE Cuenta SET
            txt_nombre = nombre,
            txt_password = Cpassword
          WHERE id = idUsuario;

          COMMIT;
        END IF;

    COMMIT;
  END//

/*sp_eliminarUsuario*/
CREATE PROCEDURE sp_eliminarUsuario (IN idUsuario INT)
      BEGIN
        DECLARE verificar INT;

        SELECT Cuenta.id INTO verificar FROM Cuenta WHERE BINARY idUsuario = Cuenta.id;
        
        IF verificar IS NOT NULL THEN
          DELETE FROM Cuenta
          WHERE Cuenta.id = idUsuario;

          COMMIT;
        END IF;    
      END//

/*sp_guardarPuntuacion*/
CREATE PROCEDURE sp_guardarPuntuacion (IN idPuntuacion INT, IN nombrePartida INT, IN tiempo INT, IN idCuenta INT, IN idTablero INT , OUT existe INT)
     BEGIN
        SELECT Puntuaciones.id INTO existe FROM Puntuaciones WHERE (BINARY Puntuaciones.txt_partida = nombrePartida) AND (Puntuaciones.id_cuenta = idCuenta);

        IF existe IS NULL THEN
          INSERT INTO BaseDeDatos1.Puntuaciones (txt_partida, int_tiempo, id_cuenta, id_tablero) VALUES (
            nombrePartida,
            tiempo,
            idCuenta,
            idTablero
          );
          
          
          SELECT Puntuaciones.id INTO existe FROM Puntuaciones WHERE (BINARY Puntuaciones.txt_partida = nombrePartida) AND (Puntuaciones.cuentaId = idUsuario);
          COMMIT;

          INSERT INTO Bitacora(id_user, txt_accion, dat_fecha) VALUES(
                idCuenta,
                "INICIAR JUEGO",
                NOW()
              );
          COMMIT;
        ELSE
          SELECT NULL INTO existe;

        END IF;

      END//


delimiter ;
      
SELECT  ROUTINE_CATALOG, ROUTINE_SCHEMA, ROUTINE_NAME, ROUTINE_TYPE  FROM INFORMATION_SCHEMA.ROUTINES
  WHERE ROUTINE_TYPE = 'PROCEDURE';

