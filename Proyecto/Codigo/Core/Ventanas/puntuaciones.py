#-*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import *

class puntuaciones:

    def __init__(self, idUsuario,engine):
        self.engine=engine
        self.idUsuario=idUsuario
        self.pantallaScore = Tk()
        label1 = tk.Label(self.pantallaScore,text="Puntuaciones mas altas", font=("Arial",30)).grid(row=0, columnspan=3)
        # columnas del arbol
        columnas = ('Posicion', 'Partida', 'Tiempo', 'Nombre','Tablero')
        # Se crea el arbol de las puntuaciones
        listBox = ttk.Treeview(self.pantallaScore, columns=columnas, show='headings')
        # Se establece encabezado de columna
        for col in columnas:
            listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)

        mostrarScores = tk.Button(self.pantallaScore,text="Mostrar Puntuaciones", width=15, command="show").grid(row=4, column=0)
        CerrarBtn = tk.Button(self.pantallaScore,text="Cerrar", width=15, command=exit).grid(row=4, column=1)
        self.pantallaScore.mainloop()

    def show():
        tempLista = self.engine.obtenerPuntuaciones()
        tempLista.sort(key=lambda e: e[1], reverse=True)
        for i, (Partida,Tiempo,Nombre,Tablero) in enumerate(tempLista, start=1):
            listBox.insert("", "end", values=(i,Partida,Tiempo,Nombre,Tablero))

  