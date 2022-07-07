from claseProvincia import Provincia

from claseObjectEncoder import ObjectEncoder

from claseManejadorProvincias import ManejadorProvincias

class RespositorioProvincias(object):
    __conn=None
    __manejador=None

    def __init__(self, conn):
        self.__conn = conn
        diccionario=self.__conn.leerJSONArchivo()
        self.__manejador=self.__conn.decodificarDiccionario(diccionario)

    def to_values(self, unaProvincia):
        assert isinstance(unaProvincia,Provincia)
        return unaProvincia.getNombre(),unaProvincia.getCapital(),unaProvincia.getCantidadHabitantes(),unaProvincia.getCantidadDepartamentos()

    def obtenerListaProvincias(self):
        return self.__manejador.getListaProvincias()

    def agregarProvincia(self, unaProvincia):
        assert isinstance(unaProvincia,Provincia)
        self.__manejador.agregarProvincia(unaProvincia)
        return unaProvincia

    def modificarProvincia(self, unaProvincia):
        assert isinstance(unaProvincia,Provincia)
        self.__manejador.updateProvincia(unaProvincia)
        return unaProvincia

    def borrarProvincia(self, unaProvincia):
        assert isinstance(unaProvincia,Provincia)
        self.__manejador.deleteProvincia(unaProvincia)

    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())