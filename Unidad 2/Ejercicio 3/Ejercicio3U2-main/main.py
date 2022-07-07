from Registro import Registro
import csv

if __name__ == '__main__':
    listaObjeto=[]
    
    for i in range(30):
        listaObjeto.append([0]*24)
            
    archivo=open('mes.csv')
    reader=csv.reader(archivo,delimiter=',')
    for fila in reader:
        dia = int(fila[0])
        hora = int(fila[1])
        temperatura = float(fila[2])
        humedad = fila[3]
        presion = int(fila[4])
        UnRegistro = Registro(dia, hora, temperatura, humedad, presion)
        listaObjeto[dia-1][hora-1]=UnRegistro
        
    opcion=None
    for objeto in listaObjeto:
        while opcion != 'd':
             print('\n-1- Mostrar para cada dia cada variable')
             print('\n-2- Mostrar temperatura promedio para cada dia')
             print('\n-3- Dado numero de dia mostrar cada variable')
             print('\n-4- Salir')
             opcion=input('\nIngrese opcion: ')
             
             if opcion == '1':
                 UnRegistro.TemperaturaMaxima(listaObjeto)
                 UnRegistro.TemperaturaMinima(listaObjeto)
                 UnRegistro.HumedadMaxima(listaObjeto)
                 UnRegistro.HumedadMinima(listaObjeto)
                 UnRegistro.PresionMaxima(listaObjeto)
                 UnRegistro.PresionMinima(listaObjeto)
             elif opcion == '2':
                 UnRegistro.TempPromedio(listaObjeto)
             elif opcion == '3':
                 xdia=int((input('Ingrese dia a mostrar: ')))
                 UnRegistro.Mostrar(listaObjeto, xdia) 
             elif opcion == '4':
                 print('¡Good Bye!')
    
   