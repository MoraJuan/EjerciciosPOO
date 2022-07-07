from ClasesPlan import ClasesPlan
import csv

class ManejadorPlanes:
    __lista=[]
    
    def __init__(self):
        self.iniciar()
        
    def iniciar(self):
        archivo=open('planes.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            UnRegistro=ClasesPlan(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            self.__lista.append(UnRegistro)
            
    def actualizar(self):
        for i in range(len(self.__lista)):
            print('\nCodigo Plan: {} '.format(self.__lista[i].getcodPlan()))
            print('\nModelo: {}'.format(self.__lista[i].getmodelo()))
            print('\nVersion:{} '.format(self.__lista[i].getversion()))
            nuevo=input('\nIngrse valor nuevo del vehiculo:')
            self.__lista[i].nuevovalor(nuevo)
    
    def mostrardetalle(self, valor):
        for i in range(len(self.__lista)):
                if float(valor) >= self.__lista[i].valorcuotas():
                    print('Codigo Plan: {} '.format(self.__lista[i].getcodPlan()))
                    print('Modelo: {}'.format(self.__lista[i].getmodelo()))
                    print('Version:{} '.format(self.__lista[i].getversion()))
                else:
                        print('ERROR!')
    
    def mostrarmonto(self):
        for i in range(len(self.__lista)):
            monto = (float(self.__lista[i].getcantLicVeh()) * self.__lista[i].valorcuotas())
            print('\nModelo: {}'.format(self.__lista[i].getmodelo()))
            print('Monto para licitar', float(monto))
    
    def codlicitar(self, cod):
        for i in range(len(self.__lista)):
            print(i)
            if cod == int(self.__lista[i].getcodPlan()):
                nuevo=int(input('Nuevas cuotas para pagar'))
                self.__lista[i].nuevovalor2(nuevo)
                print('¡Cuotas Actualizadas!')
                
            
        
                  
                                   
