from ClaseCama import Camas
from ClaseMedicamento import Medicamento
import csv

class ManejadorMedicamento:
    __lista = []
    
    def __init__(self):
        self.__lista = []
    
    def cargaLista(self):
        archivo=open('medicamentos.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            UnMedicamento=Medicamento(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5], fila[6])
            self.__lista.append(UnMedicamento)
            
    def Mostrar(self, o):
        total=0
        
        print ('Medicamnento       Presentacion        Cantidad        Precio')
        for i in range(len(self.__lista)):
            if( int(o)== int(self.__lista[i].getidCama())):
                total += int(self.__lista[i].precioT())
                print('{medicamento}       {Presentacion}            {Cantidad}             {Precio}'.format(medicamento=self.__lista[i].getnombComercial(), Presentacion=self.__lista[i].getpresentacion(), Cantidad=self.__lista[i].getCantap(), Precio=self.__lista[i].precioT()))
        print('Total: {}'. format(total))                                       
            