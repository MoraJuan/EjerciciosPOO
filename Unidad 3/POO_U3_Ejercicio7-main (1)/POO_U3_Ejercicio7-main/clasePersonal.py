import abc
from abc import ABC

class Personal(ABC):
    #Atributos
    _cuil = ''
    _apellido = ''
    _nombre = ''
    _basico = 0
    _antiguedad = 0

    def __init__(self,cuil='',apellido='',nombre='',basico=0,antiguedad=0,carrera='',cargo='',catedra='',area='',tipo=''):
        self._cuil = cuil
        self._apellido = apellido
        self._nombre = nombre
        self._basico = basico
        self._antiguedad = antiguedad
    
    def mostrarDatos(self):
        print('| {0:49}|'.format('Datos PERSONAL'))
        print('| -Nombre y apellido: {0:29}|'.format(self._nombre + ' ' + self._apellido))
        print('| -CUIL: {0:42}|'.format(self._cuil))
        print('| -Sueldo basico: {0:33}|'.format(str(self._basico)))
        print('| -Antiguedad: {0:36}|'.format(str(self._antiguedad)))

    def getCuil(self):
        return self._cuil
    def getApellido(self):
        return self._apellido    
    def getNombre(self):
        return self._nombre
        
    @abc.abstractmethod
    def getTipo(self):
        pass
    
    @abc.abstractmethod
    def calcSueldo(self):
        pass

    def toJSON(self):
        dic = dict(
            clase=self.__class__.__name__,
            atributos= dict(
                cuil=self._cuil,
                apellido = self._apellido,
                nombre = self._nombre,
                basico = self._basico,
                antiguedad = self._antiguedad))
        return dic