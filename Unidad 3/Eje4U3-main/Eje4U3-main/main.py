from menu import menu
from ManejadorCalefactores import ManejadorCalefactores

if __name__ == '__main__':
    menu = menu()
    Tamano = int(input('Ingrese tamaño del arreglo'))
    Obj= ManejadorCalefactores(Tamano)
    Obj.CargaArreglo(Tamano)
    menu.mostrarmenu()


