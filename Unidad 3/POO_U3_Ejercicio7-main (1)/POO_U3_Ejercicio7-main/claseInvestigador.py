from clasePersonal import Personal

class Investigador(Personal):
    _area = ''
    _tipo = ''

    def __init__(self,cuil='',apellido='',nombre='',basico=0,antiguedad=0,carrera='',cargo='',catedra='',area='',tipo=''):
        super().__init__(cuil,apellido,nombre,basico,antiguedad,carrera,cargo,catedra,area,tipo)
        self._area = area
        self._tipo = tipo

    def mostrarDatos(self):
        super().mostrarDatos()
        print('| {0:49}|'.format('Datos INVESTIGADOR'))
        print('| -Area: {0:42}|'.format(self._area))    
        print('| -Tipo: {0:42}|'.format(self._tipo))

    def getArea(self):
        return self._area

    def getTipo(self):
        return 'Investigador'

    def calcSueldo(self):
        sueldo = self._basico * (1 + 0.01*self._antiguedad)
        return round(sueldo,2)

    def toJSON(self):
        dic = super().toJSON()
        dic['clase'] = self.__class__.__name__
        atribInvestigador = dict(
            area = self._area,
            tipo = self._tipo)
        dic['atributos'].update(atribInvestigador)
        return dic