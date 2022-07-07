from tkinter import *
from tkinter import ttk, font, messagebox
import tkinter as tk



class Aplicacion():
    __ventana = None
    __altura = None
    __peso = None
    __imc = None
    __composicion = None

    def __init__(self):
        #Configuracion de la ventana
        self.__ventana = Tk()
        self.__ventana.geometry('420x300')
        self.__ventana.title('Calculadora de IMC')
        self.__ventana.resizable(1, 1) #Cambia entre si se puede modificar el tamaño
        
        mainframe = ttk.Frame(self.__ventana, padding = "5 5 12 12")
        mainframe.grid(column = 0, row = 0, columnspan=3)
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)
        mainframe['borderwidth'] = 4
        mainframe['relief'] = 'sunken'
        #SE LLAMAN A LAS VARIABLES
        self.__altura = StringVar()
        self.__peso = StringVar()
        self.__imc = StringVar()
        self.__composicion = StringVar()

        # VALORES 1
        ttk.Label(mainframe, text="Altura:").grid(column= 0, row=0)
        self.alturaEntry = ttk.Entry(mainframe, width = 52, textvariable = self.__altura)
        self.alturaEntry.grid(column=1, row=0)
        ttk.Label(mainframe, text = "cm").grid(column=2, row=0)

        #VALORES 2
        ttk.Label(mainframe, text = "Peso:").grid(column=0, row=1)
        self.pesoEntry = ttk.Entry(mainframe, width=52, textvariable=self.__peso)
        self.pesoEntry.grid(column=1, row=1)
        ttk.Label(mainframe, text="kg").grid(column=2, row=1)
        
        for hijo in mainframe.winfo_children():
            hijo.grid_configure(padx = 5, pady = 5)

        #botones
        self.boton1=tk.Button(self.__ventana, text="Calcular", command=self.calcular, bg="green").grid(column=0, row= 1, pady = 10)
        self.boton2=tk.Button(self.__ventana, text="Limpiar", command=self.limpiar, bg="green").grid(column=2, row=1, pady=0, columnspan=1)
        
        #frame con resultados

        frameResultados = ttk.Frame(self.__ventana, padding="3 3 12 12")
        frameResultados.grid(column=0, row=3, columnspan= 2)
        frameResultados.columnconfigure(0, weight=1)
        frameResultados.rowconfigure(0, weight=1)

        #Resultados
        fuenteIMC = font.Font(size = 10, weight='bold')
        fuenteComp = font.Font(size = 12)
        ttk.Label(frameResultados, text="Tu indice de masa corporal es:").grid(column=0, row=0)
        ttk.Label(frameResultados, textvariable=self.__imc, font=fuenteIMC).grid(column=1, row=0)
        ttk.Label(frameResultados, textvariable=self.__composicion, font=fuenteComp).grid(column=0, row=1, columnspan=2)
        
        self.alturaEntry.focus()
        self.__ventana.mainloop()

    def calcular(self):

             #Calculo IMC
            altura = float(self.alturaEntry.get()) / 100
            peso = float(self.pesoEntry.get())
            imc = peso / altura**2
            imc = round(imc,2)
                #averiguo composicion corporal
            if imc < 18.5:
                composicion = "Peso inferior al normal"
            elif imc >= 18.5 and imc < 25:
                composicion = "Peso normal"
            elif imc >= 25 and imc < 30:
                composicion = "Peso superior al normal"
            else:
                composicion = "Obesidad"
                
            self.__imc.set(str(imc) + ' kg/m2')
            self.__composicion.set(composicion)

    def limpiar(self):
        self.__peso.set(0)
        self.__altura.set(0)
        self.__composicion.set(0)
        self.__imc.set(0)
       




def testAPP():
    mi_app = Aplicacion()
    
if __name__ == '__main__':
    testAPP()
