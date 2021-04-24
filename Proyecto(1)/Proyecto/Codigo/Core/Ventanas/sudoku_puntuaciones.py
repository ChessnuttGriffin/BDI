#-*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk

class Puntuaciones:
    def show():
        #Cambiar por una query de
        tempLista = [['L33t', '0.33','10/11/2017'], ['L33t', '0.67','09/12/2011'], ['N00b', '0.67','02/13/2009'], ['N00b', '0.5','08/01/2012']]
        tempLista.sort(key=lambda e: e[1], reverse=True)

        for i, (Board,Tiempo,Fecha) in enumerate(tempLista, start=1):
            listBox.insert("", "end", values=(i,Board,Tiempo,Fecha))

    def tablero(self, master)
        self.pantallaScore = tkinter.Toplevel(master)
        label1 = tk.Label(self.pantallaScore,text="Puntuaciones mas altas", font=("Arial",30)).grid(row=0, columnspan=3)
        # columnas del arbol
        columnas = ('Posicion', 'Board', 'Tiempo', 'Fecha')
        # Se crea el arbol de las puntuaciones
        listBox = ttk.Treeview(self.pantallaScore, columns=columnas, show='headings')
        # Se establece encabezado de columna
        for col in columnas:
            listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)

        mostrarScores = tk.Button(self.pantallaScore,text="Mostrar Puntuaciones", width=15, command=show).grid(row=4, column=0)
        CerrarBtn = tk.Button(self.pantallaScore,text="Cerrar", width=15, command=exit).grid(row=4, column=1)

        self.pantallaScore.mainloop()