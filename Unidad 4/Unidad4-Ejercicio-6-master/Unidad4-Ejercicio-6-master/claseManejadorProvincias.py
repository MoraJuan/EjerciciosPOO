from claseProvincia import Provincia

class ManejadorProvincias:
    indice=0
    __provincias=None

    def __init__(self):
        self.__provincias=[]

    def agregarProvincia(self,unaProvincia):
        assert isinstance(unaProvincia,Provincia)
        unaProvincia.rowid=ManejadorProvincias.indice
        ManejadorProvincias.indice+=1
        self.__provincias.append(unaProvincia)

    def getListaProvincias(self):
        return self.__provincias

    def updateProvincia(self,unaProvincia):
        assert isinstance(unaProvincia,Provincia)
        indice=self.obtenerIndiceProvincia(unaProvincia)
        self.__provincias[indice]=unaProvincia

    def deleteProvincia(self,unaProvincia):
        assert isinstance(unaProvincia,Provincia)
        indice=self.obtenerIndiceProvincia(unaProvincia)
        self.__provincias.pop(indice)

    def obtenerIndiceProvincia(self,unaProvincia):
        assert isinstance(unaProvincia,Provincia)
        se_encontro=False
        i=0
        while se_encontro==False and i < len(self.__provincias):
            if self.__provincias[i].rowid == unaProvincia.rowid:
                se_encontro=True
            else:
                i+=1
        return i

    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                provincias=[unaProvincia.toJSON() for unaProvincia in self.__provincias]
                )
        return d