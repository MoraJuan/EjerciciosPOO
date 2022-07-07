from ClaseCalefactor import ClaseCalefactor

class ClaseElectrico(ClaseCalefactor):
    __potencia = None
    
    def __init__(self,marca, modelo, potencia):
        super().__init__(marca, modelo)
        self.__potencia = potencia  
    
    def menorcosto2(self,costo,cantidad):
        total= (int(self.__potencia)/1000)*int(cantidad)*int(costo)
        return int(total)
        
