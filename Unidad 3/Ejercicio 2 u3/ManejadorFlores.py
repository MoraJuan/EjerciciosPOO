import numpy as np
import csv
from ClaseFlores import Flores
class ManejadorFlores:
    __cantidad = 0
    __incremento = 0
    __dimension = 5

    def __init__(self, dimension=5):
        self.__flores = np.empty(dimension , dtype=Flores)
        self.__cantidad = 0
        self.__dimension = dimension
    
    def agregar(self, flor):
        if self.__cantidad == self.__dimension:
            self.__cantidad += self.__dimension
            self.__flores.resize(self.__dimension)
        self.__flores[self.__cantidad] = flor
        self.__cantidad += 1
    
    def CargaArreglo(self):
        archivo = open('flores.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            flor = Flores(fila[0], fila[1], fila[2], fila[3])
            self.agregar(flor)
        archivo.close()

    def retornar(self,numero):
        return self.__flores[numero-1]
