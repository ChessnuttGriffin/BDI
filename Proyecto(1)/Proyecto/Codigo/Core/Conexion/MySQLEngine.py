import mysql.connector
import tkinter
import re
import json

class MySQLEngine:
    
    def __init__(self, config):
        self.server = config.server
        self.port = config.port
        self.user = config.user
        self.password = config.password
        self.database = config.database

        self.start()

    def start(self):
        self.con = mysql.connector.connect(
            host = self.server,
            port = self.port,
            user = self.user,
            password = self.password,
            database = self.database
        )

        self.link = self.con.cursor()

    def select(self, query=""):
        self.link.execute(query)

        return self.link.fetchall()

    
    def insert(self, tableName, argsList = [], dataElement = ()):
        tupleStr = []
        for _ in range(len(dataElement)):
            tupleStr.append("%s")

        addElement = "INSERT INTO %s (%s) VALUES (%s)" % (tableName, ",".join(argsList), ",".join(tupleStr) )

        self.link.execute(addElement, dataElement)
        elementId = self.link.lastrowid
        self.con.commit()
        return elementId

    def update(self, elementID, tableName, argsList = [], dataList = []):
        updateList = []
        for i in range(len(dataList)):
            updateList.append("%s = %s" % (argsList[i], dataList[i]))

        updateSQL = "UPDATE %s SET %s WHERE id = %s" % (tableName, ",".join(updateList), elementID)
        try:
            self.link.execute(updateSQL)
            self.con.commit()
            return True
        except:
            print("Error durante la actualización")
            return False

    def obtenerPassword(self, nombre,Cpassword):
        contra=self.Call("sp_obtenerPassword",[nombre,Cpassword,"password"])
        return contra

    def Call(self, procedureName, argsList):
        result_args = self.link.callproc(procedureName, argsList)
        return result_args[-1]

    def obtenerUltimoJuego(self, idUsuario):
        partida=self.Call("sp_obtenerUltimoJuego",[idUsuario,"jsonPartida"])
        partida=json.loads(partida)
        return partida["savePuzzle"]

    def guardarUltimoJuego(self, puzzle, idUsuario, tiempo):
        #CONVERTIR GAME PUZZLE A DICCIONARIO
        game={"savePuzzle":puzzle}
        game=json.dumps(game)
        self.Call("sp_ActualizarJuego",[idUsuario, tiempo, game]) 

    def autenticar(self, nombre, Cpassword):
        idUsuario=self.Call("sp_autenticar",[nombre, Cpassword, "idUsuario"])
        return idUsuario

    def obtenerRol(self, nombre, Cpassword):
        rol=self.Call("sp_ObtenerRol", [nombre, Cpassword, "Rol"])
        return rol

    def obtenerTiempo(self, idUsuario):
        tiempo=self.Call("sp_obtenerTiempo",[idUsuario,"tiempo"])
        return tiempo

    def EliminarJuego(self, idPartida):
        self.Call("sp_EliminarJuego", [idPartida])

    def IniciarJuego(self, nombrePartida, idUsuario, jsonPartida):
        self.Call("sp_IniciarJuego",[nombrePartida, idUsuario, jsonPartida," "])

    def crearUsuario(self, nombre, Cpassword):
        self.Call("sp_crearUsuario", [nombre, Cpassword, " "])

    def modificarUsuario(self, idUsuario, nombre, Cpassword):
        self.Call("sp_modificarUsuario", [idUsuario, nombre, Cpassword, " "])

    def eliminarUsuario(self, idUsuario):
        self.Call("sp_eliminarUsuario", [idUsuario, " "])

    def obtenerTablero(self, idUsuario):
        tablero=self.Call("sp_obtenerTablero", [idUsuario,"jsonTablero"])
        tablero=json.loads(tablero)
        return tablero["saveTablero"]

    def obtenerTablero2(self, idTablero):
        tablero2=self.Call("sp_obtenerTablero2", [idTablero,"jsonTablero"])
        tablero2=json.loads(tablero2)
        return tablero2["saveTablero2"]
         
       

    def obtenerNombrePartida(self,idUsuario):
        nombrePartida=self.Call("sp_obtenerNombrePartida",[idUsuario,"nombre"])
        return nombrePartida

    def guardarPuntuacion(self, idPuntuacion, nombrePartida, tiempo, idCuenta, idTablero):
        self.Call("sp_guardarPuntuacion",[idPuntuacion, nombrePartida, tiempo, idCuenta, idTablero])


    

    