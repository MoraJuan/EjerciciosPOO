class Fraccion():
    def __init__(self, numerador = None, denominador = None):
        self.__numerador = numerador
        self.__denominador = denominador

    def __str__(self):
        return f'{self.__numerador}/{self.__denominador}'    


    def getDenominador(self):
        return self.__denominador    

    def getResto(self, m, n):
        while m % n != 0:
            mViejo = m
            nViejo = n

            m = nViejo
            n = mViejo % nViejo
        return n     

    def simplificar(self):
        resto = self.getResto(self.__numerador,self.__denominador)
        self.__numerador = int(self.__numerador/resto)
        self.__denominador = int(self.__denominador/resto)
        
    def __add__(self, p2):
        assert isinstance(p2,Fraccion)
        fraccion = None
        if self.__denominador != p2.__denominador:
            denom = self.minimo_comun_multiplo(self.__denominador , p2.__denominador)
            numerador = ((denom / self.__denominador)*self.__numerador) + ((denom / p2.__denominador)*p2.__numerador)
            fraccion = Fraccion(numerador,denom)
        else:
            denom = self.__denominador
            numerador = ((denom / self.__denominador)*self.__numerador) + ((denom / p2.__denominador)*p2.__numerador)
            fraccion = Fraccion(numerador,denom)
        return fraccion

    def __sub__(self, p2):
        assert isinstance(p2,Fraccion)
        fraccion = None
        if self.__denominador != p2.__denominador:
            denom = self.minimo_comun_multiplo(self.__denominador , p2.__denominador)
            numerador = ((denom / self.__denominador)*self.__numerador) - ((denom / p2.__denominador)*p2.__numerador)
            fraccion = Fraccion(numerador,denom)
        else:
            denom = self.__denominador
            numerador = ((denom / self.__denominador)*self.__numerador) - ((denom / p2.__denominador)*p2.__numerador)
            fraccion = Fraccion(numerador,denom)
        return fraccion

    def __mul__(self, p2):
        assert isinstance(p2, Fraccion)
        fraccion = Fraccion(self.__numerador*p2.__numerador,self.__denominador*p2.__denominador)
        return fraccion

    def __truediv__(self, p2):
        assert isinstance(p2, Fraccion)
        fraccion = Fraccion(self.__numerador * p2.__denominador, self.__denominador * p2.__numerador)
        return fraccion

    def maximo_comun_divisor(self,a, b):
        temporal = 0
        while b != 0:
            temporal = b
            b = a % b
            a = temporal
        return a


    def minimo_comun_multiplo(self,a, b):
        return (a * b) / self.maximo_comun_divisor(a, b)   