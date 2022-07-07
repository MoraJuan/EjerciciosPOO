from tkinter import *
from tkinter import font
from functools import partial
from fractions import Fraction
import tkinter
from ClaseFraccion import Fraccion

class Calculadora:
    __ventana=None
    __operador=None
    __panel=None
    
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('207x220')
        self.__ventana.title('Calculadora')
        self.__ventana.resizable(0,0)
       

        self.__operador = StringVar()
        self.__panel = StringVar()
        self.__operadorAux = None

        mainframe=Frame(self.__ventana,padx=8,pady=8,bg='#1d1d1c')
        mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
        mainframe.columnconfigure(0,weight=1)
        mainframe.rowconfigure(0,weight=1)

        self.clearBtn=Button(mainframe,text='C',command=self.limpiar,width=7).grid(column=2,row=1,sticky=W)

        self.operadorLbl=Label(mainframe,textvariable=self.__operador, width=7,borderwidth=2,relief="groove").grid(column=0,row=0,sticky=W)
        self.ingresoEntry=Entry(mainframe,textvariable=self.__panel, width=20, insertbackground='white',justify='right')
        self.ingresoEntry.grid(column=1,row=0,columnspan=2,sticky=W)
        
        self.unoBtn=Button(mainframe,text='1',command=partial(self.ponerNumero,'1'), width=7).grid(column=0,row=2,sticky=W)
        self.dosBtn=Button(mainframe,text='2',command=partial(self.ponerNumero,'2'), width=7).grid(column=1,row=2,sticky=W)
        self.tresBtn=Button(mainframe,text='3',command=partial(self.ponerNumero,'3'), width=7).grid(column=2,row=2,sticky=W)

        self.cuatroBtn=Button(mainframe,text='4',command=partial(self.ponerNumero,'4'), width=7).grid(column=0,row=3,sticky=W)
        self.cincoBtn=Button(mainframe,text='5',command=partial(self.ponerNumero,'5'), width=7).grid(column=1,row=3,sticky=W)
        self.seisBtn=Button(mainframe,text='6',command=partial(self.ponerNumero,'6'), width=7).grid(column=2,row=3,sticky=W)

        self.sieteBtn=Button(mainframe,text='7',command=partial(self.ponerNumero,'7'), width=7).grid(column=0,row=4,sticky=W)
        self.ochoBtn=Button(mainframe,text='8',command=partial(self.ponerNumero,'8'), width=7).grid(column=1,row=4,sticky=W)
        self.nueveBtn=Button(mainframe,text='9',command=partial(self.ponerNumero,'9'), width=7).grid(column=2,row=4,sticky=W)

        self.ceroBtn=Button(mainframe,text='0',command=partial(self.ponerNumero,'0'),width=7).grid(column=0,row=5,sticky=W)
        self.sumaBtn=Button(mainframe,text='+',command=partial(self.ponerOperador,'+'), width=7).grid(column=1,row=5,sticky=W)
        self.restaBtn=Button(mainframe,text='-',command=partial(self.ponerOperador,'-'), width=7).grid(column=2,row=5,sticky=W)

        self.multBtn=Button(mainframe,text='*',command=partial(self.ponerOperador,'*'), width=7).grid(column=0,row=6,sticky=W)
        self.porcBtn=Button(mainframe,text='%',command=partial(self.ponerOperador,'%'), width=7).grid(column=1,row=6,sticky=W)
        self.divBtn=Button(mainframe,text='/',command=partial(self.ponerNumero,'/'), width=2).grid(column=2,row=6,sticky=W)
        self.igualBtn=Button(mainframe,text='=',command=partial(self.ponerOperador,'='), width=2).grid(column=2,row=6,sticky=E)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=2,pady=2)

        self.__panel.set('')
        self.ingresoEntry.focus()

        self.__ventana.mainloop()

    def ponerNumero(self, numero):
        if self.__operadorAux == None:
            valor = self.__panel.get()
            self.__panel.set(valor + numero)
        else:
            self.__operadorAux = None
            valor = self.__panel.get()
            if valor.find('/') != -1:
                num, den = valor.split('/')
                fraccion = Fraccion(int(num), int(den))
            else:
                num = valor
                fraccion = Fraccion(int(num),1)    
            self.__primerFraccion = fraccion
            self.__panel.set(numero)
            
    def borrarPanel(self):
        self.__panel.set('')

    def resolverOperacion(self, fraccion1, operacion, fraccion2):
        resultado=''

        if operacion=='+':
            resultado=fraccion1+fraccion2
        elif operacion=='-':
            resultado=fraccion1-fraccion2
        elif operacion=='*':
            resultado=fraccion1*fraccion2
        elif operacion=='%':
            resultado=fraccion1/fraccion2

        if fraccion1.getDenominador()!=1 or fraccion2.getDenominador()!=1:
            resultado.simplificar()
            self.__panel.set((str(resultado)))
        else:
            if self.__operador.get() == '%':
                resultado.simplficar()
                self.__panel.set(str(resultado))
            else:
                resultado.simplificar()
                self.__panel.set(str(resultado))

    def ponerOperador(self, op):
        if op == '=':
            operacion = self.__operador.get()
            valor = self.__panel.get()
            if valor.find('/') != -1:
                num, den = valor.split('/')
                fraccion2 = Fraccion(int(num), int(den))
            else:
                num = valor
                fraccion2 = Fraccion(int(num),1) 

            self.__segundaFraccion = fraccion2
            self.resolverOperacion(self.__primerFraccion, operacion, self.__segundaFraccion)
            self.__operador.set('')
            self.__operadorAux=None
        else:
            if self.__operador.get() == '':
                self.__operador.set(op)
                self.__operadorAux=op
            else:
                operacion = self.__operador.get()
                self.__segundaFraccion = int(self.__panel.get())
                self.resolverOperacion(self.__primerFraccion, operacion, self.__segundaFraccion)
                self.__operador.set(op)
                self.__operadorAux=op
            
    def limpiar(self):
        self.__operador.set('')
        self.__panel.set('')
        self.__operadorAux=None
        self.ponerNumero('')
def main():
    calculadora=Calculadora()
    
if __name__=='__main__':
    main()