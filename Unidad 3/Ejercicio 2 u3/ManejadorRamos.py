from ClaseRamo import Ramo
import csv
class ManejadorRamos:
    __listaR = []
    
    def __init__(self):
        self.__listaR = []
    
    def Añadir(self,ManejadorFlores):
        num= int(input('Ingrese numero de flores menores a 4:'))
        ramo = Ramo(num)


        for i in range(num):
             flor=int(input('Flores DISPONIBLES \n 1 --> VIOLETA  \n 2 --> MARGARITAS \n 3 --> AZUCENAS\n 4 --> LIRIO \n 5 --> ROSAS '))
             if flor > 0 and flor < 6:
                ramo.agregar(ManejadorFlores.retornar(flor))
        self.__listaR.append(ramo)
    
    def __str__(self):
        i = 0
        s = None
        for i in range(len(self.__ListaR)):
            s+=self.__ListaR[i].getFlores() + '\n'
        return 

    def Contar(self):
        Lista=[0,0,0,0,0]
        Lista1=['violeta','margaritas','azucenas','lirio','rosas']
        i = 0
        o=0
        for i in range(len(self.__listaR)):
            for o in range(len(self.__listaR[i].getFlor())):
                if self.__listaR[i].getFlor()[o].getNombre()  == 'violeta':
                    Lista[0]+=1
                elif self.__listaR[i].getFlor()[o].getNombre()  == 'margaritas':
                    Lista[1] += 1
                elif self.__listaR[i].getFlor()[o].getNombre()  == 'azucenas':
                    Lista[2] += 1
                elif self.__listaR[i].getFlor()[o].getNombre()  == 'lirio':
                    Lista[3] += 1
                elif self.__listaR[i].getFlor()[o].getNombre()  == 'rosas':
                    Lista[4] += 1
        i=0
        aux = 0
        for i in range(3):
         if Lista[i] < Lista[i+1]:
             Lista1[i],Lista1[i+1] = Lista1[i+1], Lista1[i]
             Lista[i],Lista[i+1] =Lista[i+1], Lista[i]
        print('Las flores mas pedidas en orden son:')
        o=0
        for o in range(len(Lista)):
            print(Lista1[o])
            print(Lista[o])
