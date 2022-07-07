class Ramo:
    __flores = []
    __tamaño = None

    def __init__(self, tamaño):
        self.__flores = []
        if tamaño <= 4:
            self.__tamaño = tamaño
    def agregar(self, flor):
        self.__flores.append(flor)
    def getTamaño(self):
        return self.__tamaño

    def getFlor(self):
        i = 0
        s = None
        for i in range(self.__Tamaño):
          s+= self.__flores[i].getNombre() + '\n'
        return s

    def getFlor(self):
        return self.__flores
