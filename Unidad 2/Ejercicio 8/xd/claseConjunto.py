class conjunto:
    __lista = []
   
    def __init__(self):
        self.__lista = []

     

    def __add__(self, con2):
     for x in range (con2.getTamanoLista()):
      if not con2.getConjunto()[x] in self.getConjunto():
       self.agregarNumero(con2.getConjunto()[x])
     return self

    def __sub__(self, con2):
       con = conjunto()
       for x in range(0, self.getTamanoLista()):
           if not self.getConjunto()[x] in con2.getConjunto():
               con.agregarNumero(self.getConjunto()[x])
       return con

    def __eq__(self, con2):
     band = False
     band2 = True
     if self.getTamanoLista() == con2.getTamanoLista():
      band = True
      for x in range(0, self.getTamanoLista()):
         if not self.getConjunto()[x] in con2.getConjunto():
            band2 = False
      if band == band2:
          return  True
      else:
          return  False



    def mostrar(self):
     print(self.__lista)


    def agregarNumero(self, unNumero):
        if type(unNumero) == int:
            if unNumero not in self.getConjunto():
                self.__lista.append(unNumero)

    def getTamanoLista(self):
        return len(self.__lista)

    def getConjunto(self):
        return self.__lista