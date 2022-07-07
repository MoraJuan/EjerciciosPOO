from claseProvincia import Provincia

from claseManejadorProvincias import ManejadorProvincias

from claseObjectEncoder import ObjectEncoder

from vistaProvincias import ProvinciasView

from claseControladorProvincias import ControladorProvincias

from claseRepositorioProvinciasJSON import RespositorioProvincias

def testprovincias(unManejadorProvincias):
    #modificar
    provincias=[Provincia('Buenos Aires','La Plata','17.541.141','135'),Provincia('Catamarca','Catamarca','415.438','16'),
    Provincia('Chaco','Resistencia','1.204.541','25'),Provincia('Chubut','Rawson','618.994','15'),
    Provincia('Córdoba','Córdoba','3.760.450','26'),Provincia('Corrientes','Corrientes','1.120.801','25'),
    Provincia('Entre Ríos','Paraná','1.385.961','17'),Provincia('Formosa','Formosa','605.193','9'),
    Provincia('Jujuy','San Salvador de Jujuy','770.881','16'),Provincia('La Pampa','Santa Rosa','358.428','22'),
    Provincia('La Rioja','La Rioja','393.531','18'),Provincia('Mendoza','Mendoza','1.990.338','18'),
    Provincia('Misiones','Posadas','1.261.294','17'),Provincia('Neuquén','Neuquén','664.057','16'),
    Provincia('Río Negro','Viedma','747.610','13'),Provincia('Salta','Salta','1.424.397','23'),
    Provincia('San Juan','San Juan','738.959','19'),Provincia('San Luis','San Luis','508.328','9'),
    Provincia('Santa Cruz','Río Gallegos','365.698','7'),Provincia('Santa Fe','Santa Fe','3.536.418','19'),
    Provincia('Santiago del Estero','Santiago del Estero','173.432','27'),Provincia('Tierra del Fuego','173.432','Ushuaia','4'),
    Provincia('Tucumán','San Miguel de Tucumán','1.694.656','17')]

    for provincia in provincias:
        unManejadorProvincias.agregarProvincia(provincia)

def main():
    conn=ObjectEncoder('datos.json')
    repo=RespositorioProvincias(conn)
    vista=ProvinciasView()
    ctrl=ControladorProvincias(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()


if __name__=='__main__':
    jF = ObjectEncoder('datos.json')
    objManejador=ManejadorProvincias()
    
    #Para generar el archivo json con los datos de los provincias usamos:
    #testprovincias(manejador)
    #diccionarioManejador=manejador.toJSON()
    #jF.guardarJSONArchivo(diccionarioManejador)

    #Cuando ya se encuentre cargado el json, usamos
    diccionario=jF.leerJSONArchivo()
    objManejador=jF.decodificarDiccionario(diccionario)
    main()
