class Registro:
    __dia = ''
    __hora = ''
    __temperatura = ''
    __humedad = ''
    __presion = ''
    
    def __init__(self,dia , hora,temperatura, humedad, presion):
        self.__dia = dia
        self.__hora
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion
    def getTemperatura(self):
        return self.__temperatura
    def getDia(self):
        return self.__temperatura
    def getHora(self):
        return self.__hora
    
    def TemperaturaMaxima(self, listaObjeto):
        maximo = -9999
        dia = None
        hora = None
        for i in range(len(listaObjeto)):
            for j in range(len(listaObjeto[i])):
                if type(listaObjeto[i][j]) == Registro:
                    if listaObjeto[i][j].getTemperatura() > str(maximo):
                        maximo = listaObjeto[i][j].getTemperatura()
                        dia = listaObjeto[i][j].getDia()
                        hora = listaObjeto[i][j].getHora()
        return 'Temperatura maxima registrada: {} en el dia {} hora {}'. format(maximo, dia, hora)
   

