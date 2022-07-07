import os
class Menu:
    __opciones = []
    __titulo = ''

    def __init__(self,opciones=[],titulo='MENU'):
        self.__opciones = opciones
        self.__titulo = titulo
  
    def define_menu(self,titulo,opciones):
        self.__titulo = titulo
        self.__opciones = opciones
  
    def selectOption(self):
        op = input('--> ')
        if op.isdigit():
            op = int(op)
            if op > len(self.__opciones) or op < 0:
                input('Opcion invalida, reintente')
                op = None         
        else:
            input('Error: Opcion invalida, debe ingresar un numero entero.')
            op = None
        os.system('cls')
        return op
    
    def showMenu(self):
        os.system('cls')
        header = '+' + '-'*80 + '+'
        print(header)
        print('|{0:^80}|'.format(self.__titulo))
        print(header)
        for opcion in self.__opciones:
            print('| {0:79}|'.format(opcion))
        print(header)   

               
