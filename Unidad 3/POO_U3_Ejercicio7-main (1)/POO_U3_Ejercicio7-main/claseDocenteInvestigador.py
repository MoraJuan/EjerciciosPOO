from claseDocente import Docente
from claseInvestigador import Investigador

class DocenteInvestigador(Investigador,Docente):
    categorias = ['I', 'II', 'III', 'IV', 'V']
    #Atributos
    __categoria = ''
    __extra = 0

    def __init__(self,cuil='',apellido='',nombre='',basico=0,antiguedad=0,carrera='',cargo='',catedra='',area='',tipo='',categoria='',extra=0):
        super().__init__(cuil,apellido,nombre,basico,antiguedad,carrera,cargo,catedra,area,tipo)
        self.__categoria = categoria
        self.__extra = extra
       
    def mostrarDatos(self):
        super().mostrarDatos()
        print('| {0:49}|'.format('Datos DOCENTE INVESTIGADOR'))
        print('| -Categoria: {0:37}|'.format(str(self.__categoria)))    
        print('| -Extra: {0:41}|'.format(str(self.__extra)))

    def getTipo(self):
        return 'Docente Investigador'
    def getCategoria(self):
        return self.__categoria
    def getExtra(self):
        return self.__extra

    def calcSueldo(self):
        sueldo = Docente.calcSueldo(self)
        sueldo += self.__extra
        return round(sueldo,2)

    def toJSON(self):
        #Leera diccionario de Docente y luego Investigador por el MRO
        dic = super().toJSON()
        dic['clase'] = self.__class__.__name__
        atribDocenteInvestigador = dict(
            categoria = self.__categoria,
            extra = self.__extra)
        dic['atributos'].update(atribDocenteInvestigador) 
        return dic