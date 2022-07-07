from zope.interface import Interface

class Icoleccion(Interface):
    #Inserta elemento en posicion dada
    def insertarElemento(elemento,posicion):
        pass
    #Agrega elemento al final
    def agregarElemento(elemento):
        pass
    #Cambia el dato almacenado en el nodo de la posicion dada
    def cambiarElemento(elemento):
        pass
    #Muestra el elemento en la posicion dada
    def mostrarElemento(posicion):
        pass
    