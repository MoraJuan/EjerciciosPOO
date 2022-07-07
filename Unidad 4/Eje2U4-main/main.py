
from tkinter import *
from tkinter import ttk, messagebox, font
import tkinter as tk


class Aplicacion(tk.Tk):
    __ventana=None
    __siniva=None
    __iva=None
    __precioIVA=None

    def __init__(self):
        self.__ventana = Tk()
        
        self.__ventana.geometry('400x300')
        self.__ventana.title('Conversor IVA')
        fuente=font.Font(font='Verdana 10',weight='normal')
        mainframe = ttk.Frame(self.__ventana, padding="60 60 60 60")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(3, weight=3)
        mainframe.rowconfigure(3, weight=3)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__siniva = StringVar()
        self.__iva = StringVar()
        self.valorMM=IntVar()
        self.__precioIVA = StringVar()

        #self.__siniva.trace('w', self.calcular)
        self.sinivaEntry = ttk.Entry(mainframe, width=8, textvariable=self.__siniva)
        self.sinivaEntry.grid(column=1, row=1, sticky=(N, E))

        

        ttk.Radiobutton(mainframe, text='IVA 21%', value=0, variable= self.valorMM).grid(row =2, column=0, columnspan=1, sticky='w')
        ttk.Radiobutton(mainframe, text='IVA 10.5%', value=1, variable= self.valorMM).grid(row =3, column=0, sticky='w')
        ttk.Label(mainframe, text="Precio sin IVA:").grid(column=0, row=1, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=5, row=6, sticky=W)
        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=1, row= 6)
        ttk.Label(mainframe, text="IVA:").grid(column = 0, row = 4)
        ttk.Label(mainframe, text="Precio con IVA:").grid(column = 0, row = 5)
        
        ttk.Label(mainframe, textvariable=self.__iva, width=8).grid(column=1, row=4)
        ttk.Label(mainframe, textvariable=self.__precioIVA).grid(column=1, row=5)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=10, pady=10)
        #self.pulgadasEntry.focus()
        self.__ventana.mainloop()


    def calcular(self):
        if self.valorMM.get()==0:
            iva = int(self.sinivaEntry.get()) * 21/100
            self.__iva.set(str(iva))
            ivaT = int(self.sinivaEntry.get()) * 21/100 + int(self.sinivaEntry.get())
            self.__precioIVA.set(str(ivaT))


        else:
            if self.valorMM.get()==1:
                
                iva = int(self.sinivaEntry.get()) * 10.5/100
                self.__iva.set(str(iva))
                ivaT = int(self.sinivaEntry.get()) * 10.5/100 + int(self.sinivaEntry.get())
                self.__precioIVA.set(str(ivaT))
            
        





def testAPP():
    mi_app = Aplicacion()



if __name__ == '__main__':
    testAPP()
