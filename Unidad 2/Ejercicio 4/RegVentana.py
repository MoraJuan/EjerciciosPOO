class Ventana:
    
    __titulo=None
    __verticesupX=None
    __verticesupY=None
    __verticeinfX=None
    __verticeinfY=None
    
    def __init__(self,titulo, verticesupX=0, verticesupY= 0, verticeinfX = 0, verticeinfY = 0):
        self.__titulo = titulo
        if verticesupX >= 0 or verticesupY >= 0:
            self.__verticesupX= verticesupX
            self.__verticesupY= verticesupY
        if verticeinfX < 500 or verticeinfY < 500:
            self.__verticeinfY= verticeinfY
            self.__verticeinfX= verticeinfX
        
    def mostrar(self):  
        print('Titulo : ' + self.__titulo)
        print('Vertices superior izquierdo', '(', self.__verticesupX, ',', self.__verticesupY,')',)
        print('Vertice inferior derecho', '(', self.__verticeinfX, ',', self.__verticeinfY,')',)


    def getTitulo(self):
        return self.__titulo
    
    def alto(self):
        if self.__verticesupX <= self.__verticeinfX:
            if self.__verticesupY <= self.__verticeinfY:
                alto = self.__verticesupY - self.__verticeinfY
        return alto
    def ancho(self):
        if self.__verticesupX <= self.__verticeinfX:
            if self.__verticesupY <= self.__verticeinfY:
                ancho = self.__verticesupX - self.__verticeinfX
        return ancho
    def moverDerecha(self, valor):
        if self.__verticesupX <= self.__verticeinfX:
                self.__verticesupX += valor
                self.__verticeinfX += valor
        else:
                print('ERROR')
    def moverIzquierda(self, valor):    
        if self.__verticeinfX < 500 or self.__verticeinfY < 500:
            if self.__verticesupX <= self.__verticeinfX:
                        self.__verticesupX -= valor
                        self.__verticeinfX -= valor
            else:
                print('ERROR')
    def bajar(self, valor):
            if self.__verticesupY <= self.__verticeinfY:
                self.__verticeinfY -= valor
                self.__verticesupY -= valor
            else: 
                print('ERROR')
    def subir(self, valor):
            if self.__verticesupY <= self.__verticeinfY:
                self.__verticeinfY += valor
                self.__verticesupY += valor
            else:
                print('ERROR')
    
    
    
    
    
    
    
    
    
    
    
    
    