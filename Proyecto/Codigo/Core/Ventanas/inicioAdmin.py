#-*- coding: utf-8 -*-
from tkinter import *

class inicioAdmin:

    def __init__ (self , idUsuario,engine):
        self.idUsuario=idUsuario
        self.engine=engine
        self.pantallaInicio = Tk()
        self.pantallaInicio.geometry("400x300")
        self.pantallaInicio.title("Inicio")
        Label(self.pantallaInicio, text="").pack()
        Button(self.pantallaInicio, text="Reanudar juego", height="2", width="30" ).pack()
        Label(self.pantallaInicio, text="").pack()
        Button(self.pantallaInicio, text="Nuevo Juego", height="2", width="30" ).pack()
        Label(self.pantallaInicio,text="").pack()
        Button(self.pantallaInicio, text="Crear usuario", height="2", width="30").pack()
        Label(self.pantallaInicio, text="").pack()
        Button(self.pantallaInicio, text="Tabla de Score", height="2", width="30").pack()
        Label(self.pantallaInicio, text="").pack()
        self.pantallaInicio.mainloop()

    def reanudarJuego(self,idUsuario):
        ver=self.engine.obtenerUltimoJuego(idUsuario)
        if ver:
            newGame=false
            self.engine.__draw_puzzle(newGame,idUsuario)
            self.inicioAdmin.destroyed()
        else:
            tkinter.messagebox.showinfo(message="No hay juego encontrado", title=" Juego no encontrado") 

        


    def nuevoJuego(self,idUsuario):
        self.elegirMapa = tk()
        self.elegirMapa.geometry("400x300")
        self.elegirMapa.title("Inicio")
        Label(self.elegirMapa,text="").pack()
        Button(self.elegirMapa,text="Normal", height="2", width="30", command="Normal").pack()
        Label(self.elegirMapa,text="").pack()
        Button(self.elegirMapa,text="Dificil", height="2", width="30", command="Dificil").pack()
        Label(self.elegirMapa,text="").pack()

    def Normal(self):  
        tablero=engine.obtenerTablero(1)
        game=SudokuGame(tablero)
        self.Inicio_user.destroyed()
        game.start()
    
    def Dificil(self):  
        tablero=engine.obtenerTablero(2)
        game=SudokuGame(tablero)
        self.Inicio_user.destroyed()
        game.start()
        

