from ClaseEmail import Email

import csv

if __name__ == '__main__':
   
    print('Ingrese los siguientes datos:')
    
    Nombre = input('Id cuenta Nombre:')
    Dominio = input('Dominio: ')
    Tipodominio = input('Tipo de dominio: ')
    Contraseña = input('Contraseña: ')
    
    Remail=Email(Nombre, Dominio, Tipodominio)
    Unemail=Email(Nombre, Dominio, Tipodominio, Contraseña)
    
    
    
    print('Estimado ' + Nombre + ' te enviaremos tus mensajes a la dirección '+ Remail.retornaEmail())
    print('Dominio '+ Remail.getDominio())
    print('Contraseña ' + Unemail.getContrasena())
    
    nueva = input('Ingrese Contraseña (anterior) ')
    
    print('Nueva contrasña ' + Unemail.setContraseña(nueva))
    
    print(' ')
    OtroEmail=Email()
    OtroEmail.crearCuenta('informatica.fcefn@gmail.com')
    
    lista=[]
    archivo=open('email.csv')
    reader=csv.reader(archivo,delimiter=',')
    id_ing=input('\nIngresa Idcuenta a contar')
    c=0
    for fila in reader:
        lista=fila[0]+fila[1]+fila[2]
        if fila[0]==id_ing:
            c+=1


    archivo.close()

    print('cantidad de emails con ID ingresado {}'.format(c))
