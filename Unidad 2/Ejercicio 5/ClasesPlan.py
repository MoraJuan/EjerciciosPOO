class ClasesPlan:
    __codplan= ''
    __modelo= '' 
    __version=''
    __valorvehiculo = ''
    __cantcuota=''
    __cantlicveh=''

    def __init__(self,codplan,modelo,version, valorvehiculo,cantcuota, cantlicveh):
        self.__codplan= codplan
        self.__modelo = modelo
        self.__version = version
        self.__valorvehiculo= valorvehiculo
        self.__cantcuota= cantcuota
        self.__cantlicveh= cantlicveh
    
    def getcodPlan(self):
        return self.__codplan
    def getmodelo(self):
        return self.__modelo
    def getversion(self):
        return self.__version
    def getvalorVehiculo(self):
        return self.__valorvehiculo
    def getcantCuota(self):
        return self.__cantcuota
    def getcantLicVeh(self):
       return self.__cantlicveh
    def nuevovalor(self, nuevo):
       self.__valorvehiculo=nuevo
       return self.__valorvehiculo
    def valorcuotas(self):
       valor = (float(self.__valorvehiculo) / float(self.__cantcuota)) + float(self.__valorvehiculo) * 0.10
       return float(valor)
   
    def nuevovalor2(self, nuevo):
        self.__cantlicveh=nuevo
        return self.__cantlicveh
       
    
