from ClaseCama import Camas
import numpy as np
from ClaseMedicamento import Medicamento
from ManejadorMedicamento import ManejadorMedicamento
from datetime import datetime
import csv


class ManejadorCama:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension=5, incremento=5):
        self.__camas = np.empty(dimension, dtype=Camas)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregar(self, cama):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__camas.resize(self.__dimension)
        self.__camas[self.__cantidad] = cama
        self.__cantidad += 1

    def CargaArreglo(self):
        archivo = open('camas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for linea in reader:
            cama=Camas(linea[0], linea[1] , linea[2],linea[3], linea[4], linea[5], linea[6]);
            self.agregar(cama)
    
    
    def darAlta(self, Nombre, Medicamentos):
        for i in range(self.__cantidad):
            if(self.__camas[i].getNombre().lower() == Nombre.lower()):
                if(self.__camas[i].getEstado()):
                    fecha = datetime.today().strftime('%d/%m/%Y')
                    print('Nombre:{}    Cama:{}'.format(self.__camas[i].getNombre(), self.__camas[i].getIdcama()))
                    print('Diagnostico:{}        Fecha de internacion:{}'.format(self.__camas[i].getDiagnostico(), self.__camas[i].getFechaInt()))
                    print('Fecha de alta : {}'.format(self.__camas[i].getFechaAlt(fecha)))
                    
                    Medicamentos.Mostrar(i+1)
                    self.__camas[i].CambiarEstado(False)
                    
                    
                    
    def MostrarOcupada(self, diagnostico):
        print('-------PACIENTES CAMA OCUPADA-------')
        for i in range(self.__cantidad):
            if (self.__camas[i].getEstado()):
                if(self.__camas[i].getDiagnostico() == diagnostico):
                    print('Nombre:{}    Cama:{}'.format(self.__camas[i].getNombre(), self.__camas[i].getIdcama()))
                    print('Diagnostico:{}        Fecha de internacion:{}'.format(self.__camas[i].getDiagnostico(), self.__camas[i].getFechaInt()))
            else:
                print('Paciente dado de ALTA')
            
        
        
