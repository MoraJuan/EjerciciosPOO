from ManejadorFlores import ManejadorFlores
from ManejadorRamos import ManejadorRamos

class Menu:
    __opcion=None

    def __init__(self):
        self.__opcion=[]
    
    def mostrarmenu(self):
        Obj = ManejadorFlores()
        Obj2 = ManejadorRamos()

        while self.__opcion!='-1':
            print('\n')
            print('[1] Añdir')
            print('[2]')
            print('[3]')
            self.__opcion=input('Ingrese la opcion a realizar:')

            if self.__opcion=='1':
                Obj.CargaArreglo()
                Obj2.Añadir(Obj)

            elif self.__opcion=='2':
                Obj2.Contar()
