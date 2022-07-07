from Manejador import ManejadorCama
from ManejadorMedicamento import ManejadorMedicamento



if __name__ == '__main__':
    
    ObjM = ManejadorMedicamento()
    ObjC= ManejadorCama()
    ObjM.cargaLista()
    ObjC.CargaArreglo()
    Nombre=input('Ingrese nombre a de paciente: ')
    ObjC.darAlta(Nombre, ObjM)
    diagnostico= input('Ingrese diagnostico :')
    ObjC.MostrarOcupada(diagnostico)