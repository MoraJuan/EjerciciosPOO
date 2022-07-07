from ViajeroFecuente import Viajero
import csv

if __name__ == '__main__':
    listaObjeto=[]
    archivo=open('persona.csv')
    reader=csv.reader(archivo,delimiter=',')
    for fila in reader:
        objeto=Viajero(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
        listaObjeto.append(objeto)
    Vfmaximo= listaObjeto[0]
    i=1
    for i in range(len(listaObjeto)):
        if listaObjeto[i] > Vfmaximo:
            Vfmaximo = listaObjeto[i]
            
    print('Valor {}'.format(Vfmaximo.getNombre()))        
            
    numero=int(input('Ingrese numero de VP : '))
    opcion = None
    valor0=0
    
    for objeto in listaObjeto:
        if numero == objeto.getNumero():
            while opcion!='d':
                print('a- Cant millas')
                print('b- Acum millas')
                print('c- Canjear millas')
                print('d- Salir')
                opcion=input('\nIngrese opcion: ')
                
                if opcion=='a':
                    cant1=objeto.cantidadTotaldeMillas()
                    print('Millas A:{}'.format(cant1))
                    
                elif opcion=='b':
                    acum_millas=int(input('Ingrese la cantidad de millas a acumular: '))
                    listaObjeto[numero-1]= listaObjeto[numero-1] + acum_millas 
                    print('La cantidad de millas es {}'.format(listaObjeto[numero-1].getMillas()))
                elif opcion=='c':
                    millas_canjear=int(input('Ingrese millas a canjear: '))
                    listaObjeto[numero-1]= listaObjeto[numero-1] - millas_canjear
                    print('La cantidad de millas es {}'.format(listaObjeto[numero-1].getMillas()))
                elif opcion=='d':
                    valor_ing= int(input('Ingrese valor a comparar'))
                    if listaObjeto[numero-1] == valor_ing:
                         print('Son iguales')
                    else:
                         print('No son iguales')