from clasePersonal import Personal
class Docente(Personal):
    cargos = ['simple','semiexclusivo','exclusivo']
    #Atributos
    _carrera = ''
    _cargo = ''
    _catedra = ''
    def __init__(self,cuil='',apellido='',nombre='',basico=0,antiguedad=0,carrera='',cargo='',catedra='',area='',tipo=''):
        super().__init__(cuil,apellido,nombre,basico,antiguedad,carrera,cargo,catedra,area,tipo)
        self._carrera = carrera
        self._cargo = cargo
        self._catedra = catedra

    def mostrarDatos(self):
        super().mostrarDatos()
        print('| {0:49}|'.format('Datos DOCENTE'))
        print('| -Carrera: {0:39}|'.format(self._carrera))        
        print('| -Cargo: {0:41}|'.format(self._cargo))
        print('| -Catedra: {0:39}|'.format(self._catedra))

    def getCarrera(self):
        return self._carrera
    def getTipo(self):
        return 'Docente'
    
    def calcSueldo(self):
        sueldo = self._basico * (1 + 0.01*self._antiguedad)
        if self._cargo.lower() == 'simple':
            porc = 0.1
        elif self._cargo.lower() == 'semiexclusivo':
            porc = 0.2
        else:   #cargo exclusivo
            porc = 0.5
        sueldo += porc*self._basico
        return round(sueldo,2)

    def toJSON(self):
        dic = super().toJSON()
        dic['clase'] = self.__class__.__name__
        atribDocente = dict(
            carrera = self._carrera,
            cargo = self._cargo,
            catedra = self._catedra)
        dic['atributos'].update(atribDocente)
        return dic