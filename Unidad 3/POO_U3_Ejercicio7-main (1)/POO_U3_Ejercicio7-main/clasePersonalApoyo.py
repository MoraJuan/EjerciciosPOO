from clasePersonal import Personal

class PersonalApoyo(Personal):
    __categoria = 0

    def __init__(self, cuil='', apellido='', nombre='', basico=0, antiguedad=0,categoria=0):
        super().__init__(cuil, apellido, nombre, basico, antiguedad)
        self.__categoria = categoria

    def mostrarDatos(self):
        super().mostrarDatos()
        print('| {0:49}|'.format('Datos PERSONAL APOYO'))
        print('| -Categoria: {0:37}|'.format(self.__categoria))
    
    def getTipo(self):
        return 'Personal de apoyo'

    def calcSueldo(self):
        sueldo = self._basico * (1 + 0.01*self._antiguedad)
        if self.__categoria >= 1 and self.__categoria <= 10:
            porc = 0.1
        elif self.__categoria >= 11 and self.__categoria <= 20:
            porc = 0.2
        else: #Categoria de 21 a 22
            porc = 0.3
        sueldo += porc*self._basico
        return round(sueldo,2)

    def toJSON(self):
        dic = super().toJSON()
        dic['clase'] = self.__class__.__name__
        atribPersonalApoyo = dict(
            categoria = self.__categoria)
        dic['atributos'].update(atribPersonalApoyo)
        return dic