#-*- coding: utf-8 -*-
from tkinter import *

class Inicio_Admin:
    def pantalla_inicio(self, master):

        self.pantallaInicio = tkinter.Toplevel(master)
        self.pantallaInicio.geometry("400x300")
        self.pantallaInicio.title("Inicio")
        Label(self.pantallaInicio, text="").pack()
        Button(self.pantallaInicio, text="Reanudar juego", height="2", width="30").pack()
        Label(self.pantallaInicio, text="").pack()
        Button(self.pantallaInicio, text="Nuevo Juego", height="2", width="30").pack()
        Label(self.pantallaInicio,text="").pack()
        Button(self.pantallaInicio, text="Crear usuario", height="2", width="30").pack()
        Label(self.pantallaInicio, text="").pack()
        Button(self.pantallaInicio, text="Tabla de Score", height="2", width="30").pack()
        Label(self.pantallaInicio, text="").pack()

        self.pantallaInicio.mainloop()

    

