from ClaseCarrera import Carrera
class Facultad:

    __codigo = None
    __nombre = None
    __direccion = None
    __localidad = None
    __telefono = None
    __ListaCarrera = []

    def __init__(self, codigo, nombre, direccion, localidad, telefono, ListaCarrera):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        for i in range(len(ListaCarrera)):
            self.__ListaCarrera.append(Carrera(ListaCarrera[i][1], ListaCarrera[i][2], ListaCarrera[i][3], ListaCarrera[i][4], ListaCarrera[i][5]))
        
    def getCarrera(self, i):
        return self.__ListaCarrera[i].getNombre() 
    def getCodCarrera(self, i):
        return self.__ListaCarrera[i].getCodigoC()

    def getDuracion1(self, i):    
        return self.__ListaCarrera[i].getDuracion()
    
    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getLocalidad(self):
        return self.__localidad
    def getTelefono(self):
        return self.__telefono