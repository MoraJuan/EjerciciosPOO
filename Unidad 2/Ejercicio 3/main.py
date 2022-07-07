from Registro import Registro
import csv
if __name__ == '__main__':
    listaObjeto=[]
    
    
    for i in range(30):
        listaObjeto.insert(0,[])
        for j in range(24):
           listaObjeto[i].insert(0,'Sin datos registrados')     
            
    archivo=open('mes.csv')
    reader=csv.reader(archivo,delimiter=',')
    for fila in reader:
        dia = int(fila[0])
        hora = int(fila[1])
        temperatura = fila[2]
        humedad = fila[3]
        presion = fila[4]
        UnRegistro = Registro(dia, hora, temperatura, humedad, presion)
        listaObjeto[dia-1].append(UnRegistro) 
        
    cant1=UnRegistro.TemperaturaMaxima(listaObjeto)
        
    print('{}'.format(cant1))
  
                    
