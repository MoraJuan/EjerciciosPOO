class Registro:
    temperatura=''
    humedad=''
    presion=''

    def init(self,temperatura,humedad,presion):
        self.temperatura=temperatura
        self.humedad=humedad
        self.presion=presion

    def getTemperatura(self):
        return self.temperatura
    def getHumedad(self):
        return self.humedad
    def getPresion (self):
        return self.presion

    def mostrarDatos(self):
        print(str(self.temperatura)+','+str(self.humedad)+','+str(self.presion))