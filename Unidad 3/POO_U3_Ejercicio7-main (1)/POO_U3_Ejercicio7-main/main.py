from claseLista import Lista
from claseMenu import Menu
from claseManejadorPersonal import ManejadorPersonal
from claseObjectEncoder import ObjectEncoder

if __name__=='__main__':
    #Cargo los datos del archivo JSON en el manejador
    manejador = ManejadorPersonal()
    encoder = ObjectEncoder()
    archivo = open('personal.json')
    lista = encoder.leerJSONArchivo(archivo)
    manejador.decodificarJSON(lista)

    menu = Menu()
    menu.define_menu('Menu de opciones',[
        '[1]- Insertar a agentes a la colección.',
        '[2]- Agregar agentes a la colección.',
        '[3]- Tipo de agente almacenado en una posición dada.',
        '[4]- Docentes investigadores de una carrera ordenados por nombre.',
        '[5]- Cantidad de Docentes Investigadores e Investigadores según área.',
        '[6]- Listar todos los agentes ordeandos por apellido.',
        '[7]- Listar Docentes Investigadores por categoria.',    
        '[8]- Almacenar los datos de todos los agentes en el archivo "personal.json".',
        '[0]- Salir. '])

    menu.showMenu()
    op = menu.selectOption()
    while op != 0:
        if op == 1:
            newAgente = manejador.crearAgente()
            if newAgente != None:
                manejador.insertarAgente(newAgente)
        elif op == 2:
            newAgente = manejador.crearAgente()
            if newAgente != None:
                manejador.agregarAgente(newAgente)
        elif op == 3:
            manejador.showTipoAgente()
        elif op == 4:
            manejador.showCarreras()
            carrera = input('Ingrese carrera: ')
            manejador.listadoPorCarrera(carrera)
        elif op == 5:
            manejador.showAreas()
            area = input('Ingrese area: ')
            manejador.contarSegunArea(area)
        elif op == 6:
            manejador.listarTodos()
        elif op == 7:
            manejador.listarPorCategoria()
        elif op == 8:
            listaJSON = manejador.guardarJSON()
            encoder.guardarJSONArchivo(listaJSON,'personal.json')
            print('Archivo guardado.\n')
        
        input('Presione ENTER para continuar...')
        menu.showMenu()
        op = menu.selectOption()         