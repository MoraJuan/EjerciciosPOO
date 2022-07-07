from ManejadorFacultad import ManejadorFacultad

class Menu:
    opcion= None


    def __init__(self):
        self.__opcion=0
    def mostrar(self):
        Obj= ManejadorFacultad()
        while(self.__opcion)!= -1:
            print('[1]')
            print('[2]')

            self.__opcion= input('\nIngrese opcion')
            if self.__opcion == '1':
                Obj.cargaLista()
                n=int(input('Ingrese Facultad: '))
                Obj.mostrarFacultad(n)
            if self.__opcion == '2':
                Obj.cargaLista()
                nombre = input('Ingrese nombre de la carrera: ')
                Obj.mostrarNfaculta(nombre)
