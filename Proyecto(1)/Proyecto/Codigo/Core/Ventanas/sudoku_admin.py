#-*- coding: utf-8 -*-

from tkinter 
import os
import re
import tkinter.messagebox

class Admin:

    def __init__(self,master,engine):
        self.engine = engine

        #Ventana principal
        self.manejoUsuario = tkinter.Toplevel(master)
        self.manejoUsuario.title("Administrador")
        self.manejoUsuario.geometry("500x700")
        self.manejoUsuario.resizable(0,0)

        #Label de la tabla de la lista de usuarios
        self.usuarioListLabel = tkinter.Label(self.manejoUsuario, text = "Usuarios Operadores", font=('arial', 18, 'bold'))
        self.usuarioListLabel.place(x=50,y=20)

        #Botón para crear nuevos usuarios operadores
        self.addButton = tkinter.Button(self.manejoUsuario, text="Agregar", font=('arial', 12), cursor='hand2', command=self.addUser)
        self.addButton.place(x=370,y=20, width=80)

        #Widget para la lista de usuarios
        self.list = tkinter.Listbox(self.manejoUsuario, font=('arial', 15))
        self.list.pack(pady=15)
        self.list.place(x=50,y=70,width=400, height=280)
        scrollbar = tkinter.Scrollbar(self.list, orient="vertical")
        scrollbar.config(command=self.list.yview)
        scrollbar.pack(side="right", fill="y")
        self.list.config(yscrollcommand=scrollbar.set)

        listaUsuarios = engine.getOperatorUser()
        self.users = {}
        contador = 0
        for userID, nombreUsuario in listaUsuarios:
            self.users[nombreUsuario] = userID
            self.list.insert(contador, nombreUsuario)
            contador += 1

        self.list.bind('<<ListboxSelect>>', self.onselect)

        #label para usuario seleccionado
        self.usuarioLabel = tkinter.Label(self.manejoUsuario, text = "Usuario seleccionado:", font=('arial', 12,'bold'))
        self.usuarioLabel.place(x=50,y=370)

        #Label del nombre del actual usuario seleccionado
        self.usuarioLabelActual = tkinter.Label(self.manejoUsuario, text = "", font=('arial', 12))
        self.usuarioLabelActual.place(x=170,y=370)
        
        #User admin butons
        self.botonActualizar = tkinter.Button(self.manejoUsuario, text="Update", font=('arial', 12), cursor='hand2', command=self.updateUser)
        self.botonActualizar.place(x=50,y=400, width=80)
        
        self.botonEliminar = tkinter.Button(self.manejoUsuario, text="Delete", font=('arial', 12), cursor='hand2',command=self.deleteUser)
        self.botonEliminar.place(x=150,y=400, width=80)

        #Label de la configuración del usuario
        self.configUsuarioLabel = tkinter.Label(self.manejoUsuario, text = "User Config", font=('arial', 18, 'bold'))
        self.configUsuarioLabel.place(x=50,y=455)

        #Input PenColor
        self.penColorLabel = tkinter.Label(self.manejoUsuario, text = "PenColor: ", font=('arial', 14))
        self.penColorLabel.place(x=100,y=500)
        self.penColorEntry = tkinter.Entry(self.manejoUsuario, font=('arial',13))
        self.penColorEntry.place(x=200,y=500, height=28 )

        #Input FillColor
        self.fillColorLabel = tkinter.Label(self.manejoUsuario, text = "FillColor: ", font=('arial', 14))
        self.fillColorLabel.place(x=100,y=535)
        self.fillColorEntry = tkinter.Entry(self.manejoUsuario, font=('arial',13))
        self.fillColorEntry.place(x=200,y=535, height=28 )

        #Input Radius
        self.radiusLabel = tkinter.Label(self.manejoUsuario, text = "Radius: ", font=('arial', 14))
        self.radiusLabel.place(x=100,y=570)
        self.radiusEntry = tkinter.Entry(self.manejoUsuario, font=('arial',13))
        self.radiusEntry.place(x=200,y=570, height=28 )

        #Input Width
        self.widthLabel = tkinter.Label(self.manejoUsuario, text = "Width: ", font=('arial', 14))
        self.widthLabel.place(x=100,y=605)
        self.widthEntry = tkinter.Entry(self.manejoUsuario, font=('arial',13))
        self.widthEntry.place(x=200,y=605, height=28 )

        #save config
        self.saveConfigButton = tkinter.Button(self.manejoUsuario, text="Save Config", font=('arial', 12), cursor='hand2',command=self.saveConfig)
        self.saveConfigButton.place(x=185,y=650, width=120)

   
        
        

   