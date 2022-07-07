from ManejadorCalefactores import ManejadorCalefactores
from ClaseCalefactor import ClaseCalefactor
class menu:
    opcion=None
    
    def __init__(self):
        self.__opcion=0
    def mostrarmenu(self):
        Obj = ManejadorCalefactores()
        while self.__opcion!=-1:
            print('[1]')
            print('[2] ')
            print('[3] ')
            self.__opcion=input('\nIngrese numero: ')
            if self.__opcion=='1':
                costo=int(input('Ingrese costo a consumir m3: '))
                cantidad=int(input('Ingrese cantidada consumir m3:'))
                calefactor = Obj.MenorCostoGas(costo,cantidad)
                print('El calefon con menor costo {}, modelo: {}'.format(calefactor.getMarca(), calefactor.getModelo()))
            elif self.__opcion=='2':
                costo=int(input('Ingrese costo a consumir k/h: '))
                cantidad=int(input('Ingrese cantidada consumir por h :'))
                calefactor = Obj.MenorCostoELectrico(costo,cantidad)
                print('El calefon con menor costo {}, modelo: {}'.format(calefactor.getMarca(), calefactor.getModelo()))
 




                
            
