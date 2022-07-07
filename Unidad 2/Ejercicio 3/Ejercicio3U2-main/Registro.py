class Registro:
    __dia = ''
    __hora = ''
    __temperatura = ''
    __humedad = ''
    __presion = ''
    
    def __init__(self,dia , hora,temperatura, humedad, presion):
        self.__dia = dia
        self.__hora = hora
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion
    def getTemperatura(self):
        return self.__temperatura
    def getDia(self):
        return self.__dia
    def getHora(self):
        return self.__hora
    def getHumedad(self):
        return self.__humedad
    def getPresion(self):
        return self.__presion
    
    def TemperaturaMaxima(self, listaObjeto):
        maximo = -9999
        dia = None
        hora = None
        for i in range(len(listaObjeto)):
            for j in range(len(listaObjeto[i])):
                if listaObjeto[i][j].getTemperatura() > maximo:
                    maximo = listaObjeto[i][j].getTemperatura()
                    dia = listaObjeto[i][j].getDia()
                    hora = listaObjeto[i][j].getHora()
        print('Temperatura maxima registrada: {} en el dia {} hora {}'. format(maximo, dia, hora))
        
    def TemperaturaMinima(self, listaObjeto):
        minimo = 9999999
        dia = None
        hora = None
        for i in range(len(listaObjeto)):
            for j in range(len(listaObjeto[i])):
                if listaObjeto[i][j].getTemperatura() < minimo:
                    minimo = listaObjeto[i][j].getTemperatura()
                    dia = listaObjeto[i][j].getDia()
                    hora = listaObjeto[i][j].getHora()
        print('Temperatura maxima registrada: {} en el dia {} hora {}'. format(minimo, dia, hora))
    
    def HumedadMaxima(self, listaObjeto):
        maximo = -9999
        dia = None
        hora = None
        for i in range(len(listaObjeto)):
            for j in range(len(listaObjeto[i])):
                if listaObjeto[i][j].getHumedad() > str(maximo):
                    maximo = listaObjeto[i][j].getHumedad()
                    dia = listaObjeto[i][j].getDia()
                    hora = listaObjeto[i][j].getHora()
        print('Humedad maxima registrada: {} en el dia {} hora {}'. format(maximo, dia, hora))
        
    def HumedadMinima(self, listaObjeto):
        minimo = 9999999
        dia = None
        hora = None
        for i in range(len(listaObjeto)):
            for j in range(len(listaObjeto[i])):
                if listaObjeto[i][j].getHumedad() < str(minimo):
                    minimo = listaObjeto[i][j].getHumedad()
                    dia = listaObjeto[i][j].getDia()
                    hora = listaObjeto[i][j].getHora()
        print('Humedad mminima registrada: {} en el dia {} hora {}'. format(minimo, dia, hora))
    
    def PresionMaxima(self, listaObjeto):
        maximo = -99999
        dia = None
        hora = None
        for i in range(len(listaObjeto)):
            for j in range(len(listaObjeto[i])):
                if listaObjeto[i][j].getPresion() > maximo:
                    maximo = listaObjeto[i][j].getPresion()
                    dia = listaObjeto[i][j].getDia()
                    hora = listaObjeto[i][j].getHora()
        print('Presion maxima registrada: {} en el dia {} hora {}'. format(maximo, dia, hora))
    
    def PresionMinima(self, listaObjeto):
        minimo = 9999999
        dia = None
        hora = None
        for i in range(len(listaObjeto)):
            for j in range(len(listaObjeto[i])):
                if listaObjeto[i][j].getPresion() < minimo:
                    minimo = listaObjeto[i][j].getPresion()
                    dia = listaObjeto[i][j].getDia()
                    hora = listaObjeto[i][j].getHora()
        print('Presion mminima registrada: {} en el dia {} hora {}'. format(minimo, dia, hora))
    
        
    def TempPromedio(self, listaObjeto):
        count=0
        promedio=0.0
        hora=1
        total=0
        for i in range(len(listaObjeto)):
            for j in range(len(listaObjeto[i])):
                if listaObjeto[i][j].getHora() == hora:
                        count+=1
                        total += listaObjeto[i][j].getTemperatura()
                        hora+=1
                        promedio=total/count
                        print('Promedio mensual de la hora {} {}'.format(hora, promedio))
                        
    def Mostrar(self, listaObjeto, dia):
        hora = 1
        if dia <= 30:
            print('Dia - Temp - Humedad')
            while hora < 24:
                print('{}  -  {}  -  {}'.format(listaObjeto[dia-1][hora].getDia(), listaObjeto[dia-1][hora].getTemperatura(), listaObjeto[dia-1][hora].getHumedad() ))                                             
                hora+=1             

            
               
                    
            
            
   
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
   

