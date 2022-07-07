from zope.interface import implementer
from interface import Icoleccion
from claseNodo import Nodo

@implementer(Icoleccion)
class Lista:
    __comienzo = None
    #Atributos para volverla iterable
    __actual = None #Para saber cual es el elemento actual
    __index = 0 #Lleva la cuenta de los pasos de iteracion (se actualiza en 1 al pasar al siguiente elemento)
    __tope = 0 #Lleva la cuenta total de elementos de la lista (actualizar cuando se agregan o eliminan elementos)

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
    
    #METODOS PARA VOLVERLA ITERABLE
    def __iter__(self):
        return self
    def __next__(self):
        if self.__index == self.__tope:
            self.__actual = self.__comienzo
            self.__index = 0
            raise StopIteration
        else:
            self.__index += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    #METODOS PARA MANIPULACION DE LA LISTA
    #Agrega elementos al final de la lista
    def agregarElemento(self,elemento):
        miNodo = Nodo(elemento)
        miNodo.setSiguiente(None)
        if self.__tope != 0:
            nodo = self.__comienzo
            while nodo != None:
                anterior = nodo
                nodo = nodo.getSiguiente()
            anterior.setSiguiente(miNodo)
        else:
            self.__comienzo = miNodo
            self.__actual = miNodo
        self.__tope += 1
    
    #Inserta elemento segun posicion
    def insertarElemento(self,elemento,posicion):
        resultado = None
        try:
            posicion = int(posicion)
            if posicion >= 0 and posicion < self.__tope:
                miNodo = Nodo(elemento)
                nodo = self.__comienzo
                i = 0
                while i != posicion:
                    anterior = nodo
                    nodo = nodo.getSiguiente()
                    i+=1   
                miNodo.setSiguiente(nodo)
                if posicion == 0:
                    self.__comienzo = miNodo
                    self.__actual = miNodo
                else:
                    anterior.setSiguiente(miNodo)
                self.__tope += 1
                resultado = posicion
            else:
                print('Error: Posicion fuera de los limites de la lista')
        except ValueError:
            print('Error: La posicion debe ser un entero')
        return resultado

    #Muestra elemento segun posicion
    def mostrarElemento(self,posicion):
        dato = None
        try:
            posicion = int(posicion)
            if posicion >= 0 and posicion < self.__tope:
                i=0
                nodo = self.__comienzo
                while i != posicion:
                    nodo = nodo.getSiguiente()
                    i+=1
                dato = nodo.getDato()
            else:
                print('Error: Posicion fuera de los limites de la lista')
        except ValueError:
            print('Error: Posicion fuera de los limites de la lista')
        return dato

    #Cambia el elemento de la posicion dada:
    def cambiarElemento(self,elemento,posicion):
        try:
            posicion = int(posicion)
            if posicion >= 0 and posicion < self.__tope:
                i=0
                nodo = self.__comienzo
                while i != posicion:
                    nodo = nodo.getSiguiente()
                    i+=1
                nodo.setElemento(elemento)
            else:
                print('Error: Posicion fuera de los limites de la lista')
        except ValueError:
            print('Error: Posicion fuera de los limites de la lista')

    def listarDatos(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()
    
    def len(self):
        return self.__tope
    
