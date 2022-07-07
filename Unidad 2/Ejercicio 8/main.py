from ClaseConjunto import Conjunto

if __name__=='__main__':
    
    Tconjunto=int(input('Ingrese tamaño del conjunto:'))
    i=0
    Objeto1 = Conjunto()
    while i < Tconjunto:
        Vconjunto=int(input('Ingrese valores del conjunto:'))
        Objeto1.Agregar(Vconjunto)
        i += 1
    T2conjunto=int(input('Ingrese tamaño del conjunto:'))
    i=0
    Objeto2 = Conjunto()
    while i < T2conjunto:
        V2conjunto=int(input('Ingrese valores del conjunto:'))
        Objeto2.Agregar(V2conjunto)
        i += 1
    opcion=None
    while opcion != '-1':
            print('[1] Unir ')
            print('[2] Suma')
            print('[3] Igualdad')
            opcion=input('\nIngrese opcion:')
            
            if(opcion == '1'):
                v = Objeto1.__add__(Objeto2)
                v.mostrar()
            if(opcion  == '2'):
                v = Objeto1.__sub__(Objeto2)
                v.mostrar()
            if(opcion == '3'):
                if Objeto1 == Objeto2:
                    print('Son Iguales')
                else: 
                    print('No son iguales')
               
                
            

            
        