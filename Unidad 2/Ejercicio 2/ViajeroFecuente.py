
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
         
    def __str__(self):
        return str(self.__numviajero, self.__millas)
    

    def getNumero(self):
        return self.__numviajero
                
   
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
        