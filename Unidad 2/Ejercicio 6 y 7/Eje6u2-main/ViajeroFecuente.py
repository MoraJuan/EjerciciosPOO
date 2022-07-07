
class Viajero:
    __numviajero = int
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas= int
     
    def __init__(self, numviajero, dni, nombre, apellido, millas):
         self.__numviajero = numviajero
         self.__dni = dni
         self.__nombre = nombre
         self.__apellido = apellido
         self.__millas = millas
         

    
    def getNombre(self):
        return self.__nombre
    def getNumero(self):
        return self.__numviajero
    def getMillas(self):
        return self.__millas
                

    def cantidadTotaldeMillas(self):
        return 'Cantidad de millas realizadas \n' + str(self.__millas)
    
    def Acummillas(self, acum_millas):
        
        acum = self.__millas + acum_millas
        self.__millas=acum
        return (self.__millas)
    def canjearMillas(self, millas_canjear):
        if millas_canjear <= self.__millas:
            self.__millas = self.__millas - millas_canjear 
        else:
            print('No es posible el cambio las millas a canjear son mayores a las millas totales')
        return self.__millas

    def __gt__(self, other):
        Valor = False
        if(self.__millas > other.getMillas()):
            Valor = True 
        return Valor

    def __add__(self, other): 
        return Viajero(self.__numviajero, self.__dni, self.__nombre, self.__apellido, self.__millas + other)
    
    def __sub__(self,other):
        if other <= self.__millas:    
            return Viajero(self.__numviajero, self.__dni, self.__nombre, self.__apellido, self.__millas - other)
        else:
            print('No se puede canjear')
            return Viajero(self.__numviajero, self.__dni, self.__nombre, self.__apellido, self.__millas)
    def __eq__(self, other):
        if self.__millas == other:
            return True
        else:
            return False
        
        