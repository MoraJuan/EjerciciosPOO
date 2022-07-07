from RegistroC import Registro

import csv

if __name__=='__main__':
    dia = 31
    horas = 23
    lista=[]
    for i in range(dia):
        lista.append([0]*horas)
    archivo=open('archivo1.csv')
    reader=csv.reader(archivo,delimiter=';')
    bandera=True
    for linea in reader:
        if bandera:
            #salteo primera linea
            bandera=False
        else:
            dia=int(linea[0])
            horas=int(linea[1])
            temperatura=float(linea[2])
            humedad=int(linea[3])
            presatmos=int(linea[4])
            lista[dia-1][horas-1]=Registro(temperatura,humedad,presatmos)
    lista[0][0].mostrarDatos()
    lista[dia-1][horas-1].tempmaxima(lista,horas,dia)