from weakref import ref
from ClaseCalefactor import ClaseCalefactor
from ClaseElectrico import ClaseElectrico
from ClaseGas import ClaseGas
import numpy as np
import csv


class ManejadorCalefactores:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension=5):
        self.__Calefactor = np.empty(dimension, dtype=ClaseCalefactor)
        self.__cantidad = 0
        self.__dimension = dimension

    def Agregar(self, calefactor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__Calefactor.resize(self.__dimension, refcheck=False)
        self.__Calefactor[self.__cantidad] = calefactor
        self.__cantidad += 1
    
    def CargaArreglo(self):
        archivoG = open('calefactor-a-gas.csv')
        reader = csv.reader(archivoG, delimiter=';')
        for fila in reader:
            UnGas = ClaseGas(fila[0], fila[1], fila[2], fila[3]) 
            self.Agregar(UnGas)
        archivoG.close()
        archivoE = open('calefactor-electrico.csv', encoding="utf-8")
        reader = csv.reader(archivoE, delimiter=';')
        for fila2 in reader:
            UnElectrico = ClaseElectrico(fila2[0], fila2[1], fila2[2])
            self.Agregar(UnElectrico)
        archivoE.close()
    
    def mostrar(self):
        for i in range(self.__cantidad):
            print(str(self.__Calefactor[i].getMarca()))

    def MenorCostoGas(self,costo,cantidad):
        menor = 100000000
        i=0
        calefactor= None
        for i in range(self.__cantidad):
            if type(self.__Calefactor[i]) == ClaseGas:
                total = self.__Calefactor[i].menorcosto(costo,cantidad)
                if total < menor:
                    menor = total
                    calefactor= self.__Calefactor[i]
        return  calefactor
    
    def MenorCostoELectrico(self,costo,cantidad):
        menor = 100000000
        i=0
        calefactor= None
        for i in range(self.__cantidad):
            if type(self.__Calefactor[i]) == ClaseElectrico:
                total = self.__Calefactor[i].menorcosto2(costo,cantidad)
                if total < menor:
                    menor = total
                    calefactor= self.__Calefactor[i]
        return  calefactor
