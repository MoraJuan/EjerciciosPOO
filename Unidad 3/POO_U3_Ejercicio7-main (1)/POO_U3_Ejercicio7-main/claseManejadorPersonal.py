from claseMenu import Menu
from clasePersonal import Personal
from claseDocente import Docente
from claseDocenteInvestigador import DocenteInvestigador
from claseInvestigador import Investigador
from clasePersonalApoyo import PersonalApoyo
from claseLista import Lista
import re

class ManejadorPersonal():
    __personal = None

    def __init__(self):
        self.__personal = Lista()
    
    def decodificarJSON(self,lista):
        for i in range(len(lista)):
            dPersona = lista[i]
            class_name = dPersona['clase']
            class_ = eval(class_name) #Ya obtiene el tipo de clase a crear
            atributos = dPersona['atributos']
            newPersonal = class_(**atributos)
            self.__personal.agregarElemento(newPersonal)
    
    #----------------------------------------------------------#
    #       METODOS PARA EL INGRESO DE DATOS DE AGENTES        #
    #----------------------------------------------------------#

    def datosPersonal(self):
        strings = ['CUIL (xx-xxxxxxxx-x)','Apellido','Nombre','Sueldo basico','Antiguedad']
        datos = []
        for string in strings:
            dato = input('{0}: '.format(string))
            if string == strings[0]:
                #Valido formato cuil : 20-05854965-3 y que no este en el sistema
                esta = self.__buscarCuil(dato)
                while re.search(r'^[\d]{2}[-][\d]{8}[-][\d]{1}$',dato) == None or esta:
                    if esta:
                        print('La persona ya se encuentra ingresado en el sistema,reintente')
                    else:
                        print('Formato de CUIL erroneo, reintente.')
                    dato = input('{0}: '.format(string))
                    esta = self.__buscarCuil(dato)

            elif string == strings[3] or string == strings[4]:
                #Valido que el sueldo basico y la antiguedad sean un enteros
                while not dato.isdigit():
                    print('Debe introducir un numero entero, reintente.')
                    dato = input('{0}: '.format(string))
                dato = int(dato)
            datos.append(dato)
        return datos

    def datosDocente(self,datos):
        if isinstance(datos,list):
            dato = input('Carrera: ')
            datos.append(dato)
            print('Cargo {0}'.format(Docente.cargos))
            dato = input('--> ')
            while dato.lower() not in Docente.cargos:
                 print('Cargo no valido, reintente.')
                 dato = input('--> ')
            datos.append(dato.lower())
            dato = input('Catedra: ')
            datos.append(dato)            
        return datos
    
    def datosInvestigador(self,datos):
        datos.append(input('Area: '))
        datos.append(input('Tipo: '))
        return datos
    
    def datosDocenteInvestigador(self,datos):
        if isinstance(datos,list):
            print('Categoria: {0}'.format(DocenteInvestigador.categorias))
            dato = input('--> ')
            while dato.upper() not in DocenteInvestigador.categorias:
                print('Categoria no valida, reintente.')
                dato = input('--> ')
            datos.append(dato.upper())
            dato = input('Importe extra por docencia e investigacion: ')
            while not dato.isdigit():
                print('El importe debe ser un entero, reintente.')
                dato = input('Importe extra por docencia e investigacion: ')
            datos.append(int(dato))           
        return datos
    
    def datosPersonalApoyo(self,datos):
        dato = input('Categoria (1 a 22): ')
        #Valido categoria
        while not dato.isdigit() or (int(dato) < 1 or int(dato) > 22) :
            if not dato.isdigit():
                print('La categoria debe ser un entero, reintente')
            else:
                print('La categoria no admitida, reintente')
            dato = input('Categoria (1 a 22): ')
        datos.append(int(dato)) 
        return datos

    def crearAgente(self):
        menu = Menu()
        menu.define_menu('CREAR NUEVO AGENTE',['[1]- Docente','[2]- Investigador','[3]- Docente Investigador','[4]- Personal de apoyo','[0]- Volver al menu principal.'])
        menu.showMenu()
        op = menu.selectOption()
        newPersonal = None
        if op != 0:
            datos = self.datosPersonal()
            if op == 1:
                datos = self.datosDocente(datos)
                newPersonal = Docente(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7])
            elif op == 2:
                datos = self.datosInvestigador(datos)
                newPersonal = Investigador(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6])
            elif op == 3:
                datos = self.datosDocente(datos)
                datos = self.datosInvestigador(datos)
                datos = self.datosDocenteInvestigador(datos)
                newPersonal = DocenteInvestigador(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10],datos[11])
            elif op == 4:
                datos = self.datosPersonalApoyo(datos)
                newPersonal = PersonalApoyo(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5])
        return newPersonal

    #--------------------------------------------------#
    #                   Apartado 1                     #
    #--------------------------------------------------#

    def insertarAgente(self,agente):
        if isinstance(agente,Personal):
            posicion = input('Ingrese posicion [0 a {0}]: '.format(self.__personal.len()-1))
            result = self.__personal.insertarElemento(agente,posicion)
            while result == None:
                posicion = input('Ingrese posicion [0 a {0}]: '.format(self.__personal.len()-1))
                result = self.__personal.insertarElemento(agente,posicion)
            print('Agente insertado correctamente en la posicion {}!'.format(posicion))
        else:
            print('Error: No se pudo agregar el agente.')

    #--------------------------------------------------#
    #                   Apartado 2                     #
    #--------------------------------------------------#

    def agregarAgente(self,agente):
        if isinstance(agente,Personal):
            self.__personal.agregarElemento(agente)
            print('Agente agregado correctamente!')
        else:
            print('Error: No se pudo agregar el agente.')  

    #--------------------------------------------------#
    #                   Apartado 3                     #
    #--------------------------------------------------#
    def showTipoAgente(self):
        header = self.__generaHeader('AGENTE ALMACENADO EN UNA POSICION')
        print(' Ingrese posicion [0 a {0}]: '.format(self.__personal.len()-1))
        posicion = input(' --> ')
        agente = self.__personal.mostrarElemento(posicion)
        while agente == None:
            posicion = input(' --> ')
            agente = self.__personal.mostrarElemento(posicion)    
        tipo = agente.getTipo()
        print(header)
        print('| Posicion: {0:39}|'.format(str(posicion)))
        print('| Tipo de agente: {0:33}|'.format(tipo))
        print(header)
    #--------------------------------------------------#
    #                   Apartado 4                     #
    #--------------------------------------------------#

    #Muestro carreras disponibles con Docentes Investigadores para ayudar al usuario
    def showCarreras(self):
        carreras = []
        for agente in self.__personal:
            if isinstance(agente,DocenteInvestigador):
                carrera = agente.getCarrera()
                if carrera not in carreras:
                    carreras.append(carrera)
              
        header = self.__generaHeader('CARRERAS CON DOCENTES INVESTIGADORES')
        for carrera in carreras:
            print('| {0:49}|'.format(carrera))
        print(header)
    
    #Metodo privado para ordenar segun metodo, por nombre o por apellido
    def __ordenar(self,metodo):
        #Ordenar por nombre en orden alfabetico
        cota = self.__personal.len() - 1
        k=1
        while k != -1:
            k = -1
            for i in range(cota):
                agente1 = self.__personal.mostrarElemento(i)
                agente2 = self.__personal.mostrarElemento(i+1)
                if metodo == 'nombre':
                    dato1 = agente1.getNombre()
                    dato2 = agente2.getNombre()
                elif metodo == 'apellido':
                    dato1 = agente1.getApellido()
                    dato2 = agente2.getApellido()

                if dato1 > dato2:
                    self.__personal.cambiarElemento(agente2,i)
                    self.__personal.cambiarElemento(agente1,i+1)
                    k = i
            cota = k

    def listadoPorCarrera(self,carrera):
        #Obtengo Docentes investigadores de la carrera
        self.__ordenar('nombre')
        header = self.__generaHeader('DOCENTES INVESTIGADORES EN {0}'.format(carrera.upper()))
        for agente in self.__personal:
            if isinstance(agente,DocenteInvestigador):
                if carrera.lower() == agente.getCarrera().lower():
                    agente.mostrarDatos()
                    print(header)


    #--------------------------------------------------#
    #                   Apartado 5                     #
    #--------------------------------------------------#

    #Muestro areas disponibles para ayudar al usuario
    def showAreas(self):
        areas = []
        for agente in self.__personal:
            if isinstance(agente,Investigador):
                area = agente.getArea()
                if area not in areas:
                    areas.append(area)
        
        header = self.__generaHeader('AREAS DE INVESTIGACION')
        for area in areas:
            print('| {0:49}|'.format(area))
        print(header)
    
    #Cuento cantidad de docente investigador y de investigador que trabajan en el area
    def contarSegunArea(self,area):
        contDocInv = 0
        contInv = 0
        for agente in self.__personal:
            if isinstance(agente,Investigador):
                if area.lower() == agente.getArea().lower():
                    if isinstance(agente,DocenteInvestigador):
                        contDocInv += 1
                    else:
                        contInv +=1
        
        header = self.__generaHeader('CANTIDAD DE AGENTES')
        print('| Area: {0:43}|'.format(area))
        print(header) 
        print('| Investigador: {0:35}|'.format(str(contInv)))
        print('| Docente Investigador: {0:27}|'.format(str(contDocInv)))
        print(header)

    #--------------------------------------------------#
    #                   Apartado 6                     #
    #--------------------------------------------------#

    def listarTodos(self):
        header = self.__generaHeader('AGENTES DE LA UNIVERSIDAD')
        #Ordeno alfabeticamente por apellido
        self.__ordenar('apellido')
        for agente in self.__personal:
            nombre = agente.getNombre()
            apellido = agente.getApellido()
            tipo = agente.getTipo()
            sueldo = agente.calcSueldo()
            print('| Nombre y apellido: {0:30}|'.format(nombre + ' ' + apellido))
            print('| Tipo: {0:43}|'.format(tipo))
            print('| Sueldo: {0:41}|'.format(str(sueldo)))
            print(header)           

    #--------------------------------------------------#
    #                   Apartado 7                     #
    #--------------------------------------------------#

    def listarPorCategoria(self):
        print('Seleccione una categoria {0}'.format(DocenteInvestigador.categorias))
        miCategoria = input('--> ').upper()
        while miCategoria not in DocenteInvestigador.categorias:
            print('La categoria ingresada no es valida, reintente')
            miCategoria = input('--> ').upper()
        header = self.__generaHeader('DOCENTES INVESTIGADORES CATEGORIA {0}'.format(miCategoria))
        extraTotal = 0
        for agente in self.__personal:
            if isinstance(agente,DocenteInvestigador):
                if miCategoria == agente.getCategoria():
                    apellido = agente.getApellido()
                    nombre = agente.getNombre()
                    extra = agente.getExtra()
                    extraTotal += extra
                    print('| Nombre y apellido: {0:30}|'.format(nombre + ' ' + apellido))
                    print('| Importe por docencia e investigacion [$]: {0:7}|'.format(str(extra)))
                    print(header)
        print('| Total a solicitar al Ministerio [$]: {0:12}|'.format(str(extraTotal)))
        print(header)                  

    #--------------------------------------------------#
    #                   Apartado 8                     #
    #--------------------------------------------------#
    #Retorno una lista con las representaciones diccionario de cada agente
    def guardarJSON(self):
        listaJSON = [agente.toJSON() for agente in self.__personal]
        return listaJSON

    #--------------------------------------------------#
    #                Metodos Auxiliares                #
    #--------------------------------------------------#

    #Genero un encabezado para los distintos apartados
    def __generaHeader(self,titulo):
        header = '+' + '-'*50 + '+'
        print(header)
        print('|{0:^50}|'.format(titulo))
        print(header)
        return header 
    
    #Busco el cuil ingresado, para saber si ya esta en el sistema
    def __buscarCuil(self,cuil):
        esta = False
        i = 0
        while i < self.__personal.len() and not esta:
            agente = self.__personal.mostrarElemento(i)
            if agente.getCuil() == cuil:
                esta = True
            else:
                i+=1
        return esta