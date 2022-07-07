
class ClaseCalefactor:
    __marca = None
    __modelo = None

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
    

    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo

