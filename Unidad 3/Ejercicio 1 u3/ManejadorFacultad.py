from ClaseFacultad import Facultad
import csv

class ManejadorFacultad:
    __lista = []

    def __init__(self):
        self.__lista = []
    
    def cargaLista(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo, delimiter=',')
        fila = next(reader)
        bandera = True
        while bandera:
            listaCarrera = []
            filaCarrera=next(reader)
            while bandera and fila[0]==filaCarrera[0]:
                listaCarrera.append(filaCarrera)
                try:
                    filaCarrera=next(reader)
                except StopIteration:
                    bandera=False
            UnaFacultad = Facultad(fila[0], fila[1], fila[2], fila[3],fila[4], listaCarrera)
            self.__lista.append(UnaFacultad)        
            fila=filaCarrera
        archivo.close()
        


    def mostrarFacultad(self, n):
        i=0
        j=0
        while n != int(self.__lista[i].getCodigo()):
            i+=1
        print('Nombre de la facultad {}'.format(str(self.__lista[i].getNombre())))
        while j < int(self.__lista[i-1].getCodCarrera(j)):
            if n != int(self.__lista[i-1].getCodigo()):
                print('Carreras: {}, Duracion: {}'.format(str(self.__lista[i-1].getCarrera(j)) , str(self.__lista[i-1].getDuracion1(j))))
                j+=1
            else:
                i+=1
            j+=1
       
    def mostrarNfaculta(self, nombre):
        i=0
        j=0
        while nombre != self.__lista[i-1].getCarrera(j):
            j+=1
        print('Nombre de la facultad {} Localidad: {}'.format(str(self.__lista[i-1].getNombre()), self.__lista[i-1].getLocalidad()))
        i+=1

        



