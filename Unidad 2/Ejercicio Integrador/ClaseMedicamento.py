class Medicamento:
    __idCama = None
    __idMed = None
    __nombComercial = None
    __monodroga = None
    __presentacion= None
    __cant_ap= None
    __precioT= None
    
    def __init__(self, idCama, idMed, nombComercial, monodroga, presentacion, cant_ap, precioT):
        self.__idCama = idCama
        self.__idMed = idMed
        self.__nombComercial = nombComercial
        self.__monodroga = monodroga
        self.__presentacion = presentacion
        self.__cant_ap = cant_ap
        self.__precioT = precioT
        
    def getidCama(self):
        return self.__idCama
    def getidMed(self):
        return self.__idMed
    def getnombComercial(self):
        return self.__nombComercial
    def getmonodroga(self):
        return self.__monodroga
    def getpresentacion(self):
        return self.__presentacion
    def getCantap(self):
        return self.__cant_ap
    def precioT(self):
        return self.__precioT
    
        