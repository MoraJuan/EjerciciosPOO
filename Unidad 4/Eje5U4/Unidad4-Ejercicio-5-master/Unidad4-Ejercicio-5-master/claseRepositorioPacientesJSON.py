from clasePaciente import Paciente

from claseObjectEncoder import ObjectEncoder

from claseManejadorPacientes import ManejadorPacientes

class RespositorioPacientes(object):
    __conn=None
    __manejador=None

    def __init__(self, conn):
        self.__conn = conn
        diccionario=self.__conn.leerJSONArchivo()
        self.__manejador=self.__conn.decodificarDiccionario(diccionario)

    def to_values(self, unPaciente):
        return unPaciente.getApellido(),unPaciente.getNombre(),unPaciente.getTelefono(),unPaciente.getAltura(),unPaciente.getPeso()

    def obtenerListaPacientes(self):
        return self.__manejador.getListaPacientes()

    def agregarPaciente(self, unPaciente):
        self.__manejador.agregarPaciente(unPaciente)
        return unPaciente

    def modificarPaciente(self, unPaciente):
        self.__manejador.updatePaciente(unPaciente)
        return unPaciente

    def borrarPaciente(self, unPaciente):
        self.__manejador.deletePaciente(unPaciente)

    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())