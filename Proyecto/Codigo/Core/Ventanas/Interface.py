#-*- coding: utf-8 -*-
from Core.Conexion.ConnectionConfig import ConnectionConfig
from Core.Conexion.MySQLEngine import MySQLEngine
from Core.Ventanas.inicioAdmin import inicioAdmin
from Core.Ventanas.inicioUsuario import inicioUsuario

from tkinter import *
import os

class Interface:
    def __init__(self,engine):
        self.engine = engine
        self.pantallaMain()
       
        

        
        
    def pantallaMain(self):
        global pantallaMain
        pantallaMain =Tk()
        pantallaMain.geometry("400x300")
        pantallaMain.title("Login")
        Label(text="Seleccione su opcion:", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command = self.login).pack()
        pantallaMain.mainloop()

    def destruirMain():
        pantallaMain.destroy()

    def splash(self):
        self.pantallaSplash = Toplevel(pantallaMain)
        self.pantallaSplash.title("Bienvenido")
        self.pantallaSplash.geometry("300x250")
        Label( text="Bienvenido!", font=18).pack()
        self.pantalla_splash.after(3000) 

    def destruirSplash():

        splash.destroy()

    
    # Designing window for login 

    def login(self):
        global pantallaLogin
        self.pantallaLogin = Toplevel(pantallaMain)
        self.pantallaLogin.title("Login")
        self.pantallaLogin.geometry("300x250")
        Label(self.pantallaLogin, text="Ingresar datos para login: ").pack()
        Label(self.pantallaLogin, text="").pack()

        global verificarUsuario
        global verificarContrasenia

        verificarUsuario = StringVar()
        verificarContrasenia = StringVar()

        global entradaUsuarioLogin
        global entradaContraseniaLogin

        Label(self.pantallaLogin, text = "Nombre de Usuario * ").pack()
        entradaUsuarioLogin = Entry(self.pantallaLogin, textvariable = verificarUsuario)
        entradaUsuarioLogin.pack()
        Label(self.pantallaLogin, text = "").pack()
        Label(self.pantallaLogin, text = "Contraseña * ").pack()
        entradaContraseniaLogin = Entry(self.pantallaLogin, textvariable = verificarContrasenia, show= '*')
        entradaContraseniaLogin.pack()
        Label(self.pantallaLogin, text="").pack()
        Button(self.pantallaLogin, text="Login", width=10, height=1 ,command=self.verificarLogin).pack()
       
        

    


    def verificarLogin(self):
      
        
        usuario1 = verificarUsuario.get()
        contrasenia1 = verificarContrasenia.get()
        entradaUsuarioLogin.delete(0, END)
        entradaContraseniaLogin.delete(0, END)
        idUsuario=self.engine.autenticar(usuario1,contrasenia1)
        if contrasenia1 == self.engine.obtenerPassword(usuario1,contrasenia1):
            if idUsuario == 1:
                pagina="inicioAdmin"
                """global pLoginSuccess
                pLoginSuccess = Toplevel(self.pantallaLogin)
                pLoginSuccess.title("Satisfactorio!")
                pLoginSuccess.geometry("150x100")
                Label(pLoginSuccess, text="Inicio Satisfactorio!").pack()
                Button(pLoginSuccess, text="OK", command=self.siguiente(idUsuario,"inicioAdmin")).pack()"""
                inicioAdmin(idUsuario,self.engine)
            
            """global pLoginSuccess
            pLoginSuccess = Toplevel(self.pantallaLogin)
            pLoginSuccess.title("Satisfactorio!")
            pLoginSuccess.geometry("150x100")
            Label(pLoginSuccess, text="Inicio Satisfactorio!").pack()
            Button(pLoginSuccess, text="OK", command=self.siguiente(idUsuario,"sudoku_inicio_admin")).pack()
            """
            inicioUsuario(idUsuario,self.engine)
            self.siguiente(idUsuario,"sudoku_inicio")
        else:
            self.ContraseniaNoReconocida


    def siguiente(self, idUsuario,pagina):
        inicioAdmin()




    # Designing popup for login success
    def loginSuccess(self):
        global pLoginSuccess
        pLoginSuccess = Toplevel(self.pantallaLogin)
        pLoginSuccess.title("Satisfactorio!")
        pLoginSuccess.geometry("150x100")
        Label(pLoginSuccess, text="Inicio Satisfactorio!").pack()
        Button(pLoginSuccess, text="OK", command=EliminarLoginSuccess).pack()

    # Designing popup for login invalid contrasenia
    def ContraseniaNoReconocida(self):
        global pContraseniaNoRe
        pContraseniaNoRe = Toplevel(self.pantallaLogin)
        pContraseniaNoRe.title("Satisfactorio")
        pContraseniaNoRe.geometry("150x100")
        Label(pContraseniaNoRe, text="Contraseña invalida").pack()
        Button(pContraseniaNoRe, text="OK", command=eliminarContraseniaNoRe).pack()

    # Designing popup for user not found


    # Deleting popups
    def EliminarLoginSuccess(self):
        pLoginSuccess.destroy()


    def eliminarContraseniaNoRe(self):
        pContraseniaNoRe.destroy()



        

    


