from claseConjunto import  conjunto
import os
def menu():
 os.system('cls') # NOTA para windows tienes que cambiar clear por cls
 print ("Selecciona una opción")
 print ("\t1 - unir conjuntos")
 print ("\t2 - diferencia de conjuntos")
 print ("\t3 - chekear igualdad de conjuntos")

if __name__ == '__main__':
 cant = int(input('ingrese tamaña del primer conjunto '))
 a = conjunto()
 i = 0
 while i < int(cant):
  num = int(input('ingrese un valor '))
  a.agregarNumero(num)
  i += 1
 cant = int(input('ingrese tamaña del segundo conjunto '))
 b = conjunto()
 i=0
 while i < int(cant):
  num = int(input('ingrese un valor '))
  b.agregarNumero(num)
  i += 1
 a.mostrar()
 b.mostrar()
 l = True
 while l == True:
  menu()
  opcion = input()
  if opcion == '1':
   v = a.__add__(b)
   v.mostrar()
  elif opcion == '2':
   m = a.__sub__(b)
   m.mostrar()
  elif opcion == '3':
   if  a == b:
    print(' son iguales')
   else:
     print(' No son iguales')
  else:
   l = False
   print('opcion incorrecta')
 print('programa terminado')