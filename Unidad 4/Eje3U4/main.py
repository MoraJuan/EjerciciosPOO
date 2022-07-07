from tkinter import *
from tkinter import ttk, font
import tkinter as tk
from claseCotiza import Cotiza

class Ventana():
    __ventana = None
    __dolares = None
    __pesos = None
    __cotizador = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('330x100')
        self.__ventana.title('Conversor dolar')
       

        self.__dolares = StringVar()
        self.__pesos = StringVar()
        self.__cotizador = Cotiza()

        self.mainframe = ttk.Frame(self.__ventana, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(3, weight=3)
        self.mainframe.rowconfigure(3, weight=3)
        self.mainframe['borderwidth'] = 2
       
        self.label1 = ttk.Label(self.mainframe,text='dólares')
        self.label2 = ttk.Label(self.mainframe,text='pesos')
        self.label3 = ttk.Label(self.mainframe,text='es equivalente a')
        self.label4 = ttk.Label(self.mainframe,textvariable=self.__pesos)
        self.dolaresEntry = ttk.Entry(self.mainframe,textvariable=self.__dolares, width=15)
        self.boton = ttk.Button(self.mainframe,text="Salir", command=self.__ventana.destroy)


        self.mainframe.grid(column=0,row=0)
        self.label1.grid(column=2,row=0)
        self.label2.grid(column=2,row=1)
        self.label3.grid(column=0,row=1)
        self.label4.grid(column=1,row=1)
        self.dolaresEntry.grid(column=1,row=0)
        self.boton.grid(column=2,row=2)


        self.__dolares.trace('w',self.calcular)
        self.dolaresEntry.focus()
        self.__ventana.mainloop()

    def calcular(self, *args):
        if self.dolaresEntry.get() != '':
            ventaOficial = self.__cotizador.getCotizacion('oficial')
            dolares = float(self.dolaresEntry.get())
            pesos = ventaOficial * dolares
            self.__pesos.set(pesos)
        else:
            self.dolaresEntry.focus()
            self.__pesos.set('')
            

def testAPP():
    mi_app = Ventana()
    

if __name__ == '__main__':
    testAPP()

