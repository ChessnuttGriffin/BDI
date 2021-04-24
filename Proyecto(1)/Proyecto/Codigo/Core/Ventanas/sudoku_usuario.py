#-*- coding: utf-8 -*-
import tkinter
import tkinter.colorchooser
import tkinter.filedialog

class Usuario:
    def __init__(self,master,engine, nombreUsuario, actualizarVentana, ventanaTipo = None):
        self.actualizarVentana  = actualizarVentana
        self.engine = engine
        self.usuarioInput = tkinter.Toplevel(master)
        self.usuarioInput.geometry("400x200")
        self.usuarioInput.configure(background = 'white')
        self.usuarioInput.resizable(0,0)
        self.usuarioAntiguo = nombreUsuario

        if(ventanaTipo == "signUp"):
            #Ventana para logear a los usuarios y sus atributos
            self.usuarioInput.title("Nuevo Usuario")
        else:
            self.usuarioInput.title("Usuario Actualizado")

        #Espacio para ingresar un usuario
        self.usuarioL = tkinter.Label(self.usuarioInput,text='Usuario: ',font = ('arial',15),bd=5,bg="white")
        self.usuarioL.place(x=90,y=50)
        self.usuarioE = tkinter.Entry(self.usuarioInput)
        self.usuarioE.place(x=150,y=50,height=30)
        
        if(ventanaTipo == "actualizar"):
            self.usuarioE.insert(0,self.usuarioAntiguo)        
        
        #Espacio para ingresar una contraseña
        self.contraL = tkinter.Label(self.usuarioInput,text='Contraseña: ',font = ('arial',15),bd=5,bg="white")
        self.contraL.place(x=46,y=100)
        self.contraE = tkinter.Entry(self.usuarioInput,show="*")
        self.contraE.place(x=150,y=100,height=30)

        if(ventanaTipo == "signUp"):
            #Boton para ejecutar la verificacion edl usuario 
            self.loginButton = tkinter.Button(self.usuarioInput,text="INSCRIBIRSE",cursor='hand2',command=self.nuevoUsuario)
        else: 
            self.loginButton = tkinter.Button(self.usuarioInput,text="ACTUALIZAR",cursor='hand2',command=self.actualizarUsuario)

        self.loginButton.place(x=150,y=150)

    def nuevoUsuario(self):

        #obtner los valores de los entry para el usuario y la contraseña 
        usuarioAcc = self.usuarioE.get()
        passwordAcc =  self.contraE.get()
       
        exists = self.engine.createOperatorUser(usuarioAcc,passwordAcc)
        if not exists:
            self.actualizarVentana( )
            self.usuarioInput.destroy()
        else:
            tkinter.messagebox.showinfo(message="El usuario ya existe", title="Error de sesion") 
    
    def actualizarUsuario(self):
        mismoName = False
        usuarioAcc = self.usuarioE.get()
        passwordAcc =  self.contraE.get()
        usersList = self.engine.getOperatorUser()
        oldID = None
        for userID, nombreUsuario in usersList:
            if nombreUsuario == self.usuarioAntiguo:
                oldID = userID
                mismoName = True
                break

        exist = self.engine.updateOperatorUser(oldID,usuarioAcc,passwordAcc)
        if(mismoName or not exist):
            self.actualizarVentana( )
            self.usuarioInput.destroy()
        else:
            tkinter.messagebox.showinfo(message="El usuario ya existe", title="Update error") 
            
