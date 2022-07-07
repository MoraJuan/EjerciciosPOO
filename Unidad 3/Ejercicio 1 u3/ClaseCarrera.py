from mailbox import NoSuchMailboxError



class Carrera:
    __codigo = None
    __nombre = None
    __duracion = None
    __titulo = None
    __grado = None
    
    def __init__(self,codigo,nombre,titulo , duracion,grado):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__duracion = duracion
        self.__titulo =titulo
        self.__grado = grado    
    
    def __str__(self):
        return self.__codigo + self.__nombre  + self.__duracion + self.__titulo + self.__grado   
        
    def getCodigoC(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getDuracion(self):
        return self.__duracion
    def getTitulo(self):
        return self.__titulo
    def getGrado(self):
        return self.__grado