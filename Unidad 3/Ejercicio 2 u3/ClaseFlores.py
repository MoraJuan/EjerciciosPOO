class Flores:
    __numero = None
    __nombre = None
    __color = None
    __descripcion = None

    def __init__(self, numero, nombre, color, descripcion):
        self.__numero = numero
        self.__nombre = nombre
        self.__color = color
        self.__descripcion = descripcion
    
    def getNumero(self):
        return self.__numero
    def getNombre(self):
        return self.__nombre
    def getDescripcion(self):
        return self.__descripcion
    def getColor(self):
        return self.__color
        


