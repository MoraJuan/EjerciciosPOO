"""
@author: Juan
"""
class Camas:
    __idCama = None
    __habitacion = None
    __estado = bool()
    __NombYAp = None
    __diagnostico = None 
    __fecha_int=None
    __fecha_alt=None
    
    def __init__(self,idCama, habitacion,estado, NombYAp, diagnostico, fecha_int, fecha_alt):
        self.__idCama = idCama
        self.__habitacion = habitacion
        self.__estado = estado
        self.__NombYAp = NombYAp
        self.__diagnostico = diagnostico
        self.__fecha_int = fecha_int
        self.__fecha_alt = fecha_alt
    
    def getIdcama(self):
        return self.__idCama
    def getEstado(self):
        return self.__estado
    def getNombre(self):
        return self.__NombYAp
    def getDiagnostico(self):
        return self.__diagnostico
    def getFechaInt(self):
        return self.__fecha_int
    def getFechaAlt(self, fecha):
        self.__fecha_alt = fecha
        return self.__fecha_alt
    
    
    
    def CambiarEstado(self, false):
     self.__estado = false

        