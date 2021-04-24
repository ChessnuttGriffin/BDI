#-*- coding: utf-8 -*-
from .sudoku import *
from .ConnectionConfig import ConnectionConfig
from .MySQLEngine import MySQLEngine
from tkinter import *

class Inicio_user:
    def pantalla_inicio_user(self):
        self.pantallaInicio = tk()
        self.pantallaInicio.geometry("400x300")
        self.pantallaInicio.title("Inicio")
        Label(self.pantallaInicio,text="").pack()
        Button(self.pantallaInicio,text="Reanudar juego", height="2", width="30", command="reanudarJuego").pack()
        Label(self.pantallaInicio,text="").pack()
        Button(self.pantallaInicio,text="Nuevo Juego", height="2", width="30", command="nuevoJuego").pack()
        Label(self.pantallaInicio,text="").pack()
        Button(self.pantallaInicio,text="Tabla de Score", height="2", width="30").pack()
        Label(self.pantallaInicio,text="").pack()

        self.pantallaInicio.mainloop()

    def reanudarJuego(self,idUsuario):
        self.engine=engine
        ver=engine.obtenerUltimoJuego(idUsuario)
        if ver:
            newGame=false
            engine.__draw_puzzle(newGame,idUsuario)
            self.Inicio_user.destroyed()
        else
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
