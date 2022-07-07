class Pasta:
    __tipo_pasta = ''
    __marca= ''
    __peso = ''
    __valor = ''
    
    def __init__(self, tipo, marca, peso, valor):
        self.__tipo_pasta = tipo
        self.__marca = marca
        self.__peso = peso
        self.__valor = valor
        
    def GetTipo(self):
        return self.__tipo_pasta
    def GetMarca(self):
        return self.__marca
    def GetPeso(self):
        return self.__peso
    def GetValor(self):
        return self.__valor
    
    def __eq__(self, cad):
        if cad == self.__tipo_pasta:
            return self.__tipo_pasta
        elif cad == self.__marca:
            return self.__marca
        elif cad == self.__peso:
            return self.__peso
        elif cad == self.__valor:
            return self.__valor
        

        
        