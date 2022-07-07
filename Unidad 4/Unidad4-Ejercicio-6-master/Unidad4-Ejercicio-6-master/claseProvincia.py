import re

class Provincia(object):
    #telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")
    __nombre=None
    __capital=None
    __cantidadHabitantes=None
    __cantdadDepartamentos=None
    
    def __init__(self,nombre,capital,cant_habitantes,cant_departamentos):
        self.__nombre=self.requerido(nombre, 'Nombre es un valor requerido')
        self.__capital=self.requerido(capital, 'Capital es un valor requerido')
        self.__cantidadHabitantes=self.requerido(cant_habitantes, 'Cantidad de Habitantes es un valor requerido')
        self.__cantdadDepartamentos=self.requerido(cant_departamentos, 'Cantidad de departamentos es un valor requerido')
        
    def getNombre(self):
        return self.__nombre

    def getCapital(self):
        return self.__capital

    def getCantidadHabitantes(self):
        return self.__cantidadHabitantes

    def getCantidadDepartamentos(self):
        return self.__cantdadDepartamentos

    def requerido(self,valor,mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor


    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                                    nombre=self.__nombre,
                                    capital=self.__capital,
                                    cant_habitantes=self.__cantidadHabitantes,
                                    cant_departamentos=self.__cantdadDepartamentos
                                )
                )
        return d