from ClasePasta import Pasta
import csv


if __name__=='__main__':
    
    
    lista_pasta= []  #Declaramos la lista
    archivo = open('Pastas.csv')  #Abrimos CSV
    reader = csv.reader(archivo,delimiter=',') #Leemos el Archivo
    
    for fila in reader:
        unaPasta= Pasta(fila[0], fila[1], fila[2], fila[3]) #Cargamos lista
        lista_pasta.append(unaPasta) #Se agrega el objeto creado
    archivo.close()
    
    print('Cantidad de pastas de marca Lucchetti ', lista_pasta.count('Luchetti'))
     
    lista_pasta2 = [] #Declaramos la lista
    archivo = open('Pastas2.csv')  #Abrimos CSV
    reader = csv.reader(archivo,delimiter=',') #Leemos el Archivo
    
    for fila in reader:
        unaPasta2= Pasta(fila[0], fila[1], fila[2], fila[3]) #Cargamos lista
        lista_pasta.append(unaPasta2) #Se agrega el objeto creado
    archivo.close()
    
    lista_pasta.extend(lista_pasta2) #Se une las dos listas lista 1 y 2
    
    for i in range(len(lista_pasta)):
        print('[Tipo de pasta] {},   [Marca] :{},    [Peso] :{},      [Valor] :{}'.format(lista_pasta[i].GetTipo(),lista_pasta[i].GetMarca(),lista_pasta[i].GetPeso(),lista_pasta[i].GetValor())) 
        
        
        
        