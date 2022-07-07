from clasePaciente import Paciente

class ManejadorPacientes:
    indice=0
    __pacientes=None

    def __init__(self):
        self.__pacientes=[]

    def agregarPaciente(self,unPaciente):
        assert isinstance(unPaciente,Paciente)
        unPaciente.rowid=ManejadorPacientes.indice
        ManejadorPacientes.indice+=1
        self.__pacientes.append(unPaciente)

    def getListaPacientes(self):
        return self.__pacientes

    def deletePaciente(self,unPaciente):
        assert isinstance(unPaciente,Paciente)
        indice=self.obtenerIndicePaciente(unPaciente)
        self.__pacientes.pop(indice)

    def updatePaciente(self,unPaciente):
        assert isinstance(unPaciente,Paciente)
        indice=self.obtenerIndicePaciente(unPaciente)
        self.__pacientes[indice]=unPaciente

    def obtenerIndicePaciente(self,unPaciente):
        assert isinstance(unPaciente,Paciente)
        se_encontro=False
        i=0
        while se_encontro==False and i < len(self.__pacientes):
            if self.__pacientes[i].rowid == unPaciente.rowid:
                se_encontro=True
            else:
                i+=1
        return i

    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                pacientes=[unPaciente.toJSON() for unPaciente in self.__pacientes]
                )
        return d