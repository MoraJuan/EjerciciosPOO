class Conjunto:
    
    __lista=[]
    
    def __init__(self):
        
        self.__lista = []
        
    def tamaño(self):
        return len(self.__lista)
    
    def getConjunto(self):
        return self.__lista
    
    def Agregar(self, Vconjunto):
        if Vconjunto not in self.getConjunto():
            if Vconjunto != self.getConjunto():
                self.__lista.append(Vconjunto)
    def mostrar(self):
        print(self.__lista)
    
    def __add__(self, other):
        for i in range(other.tamaño()):
            if not other.getConjunto() in self.getConjunto():
                self.Agregar(other.getConjunto())
        return self
    
    def __sub__(self, other):
         for i in range(other.tamaño()):
             if not other.getConjunto() in self.getConjunto():
                 self.Agregar(other.getConjunto())
         return self
        
    def __eq__(self, other):
        band = False
        band2 = True
        if self.tamaño() == other.tamaño():
            band = True
            for x in range(0, self.tamaño()):
                if not self.getConjunto() in other.getConjunto():
                    band2 = False
            if band == band2:
                return  True
            else:
                return  False  
        
        