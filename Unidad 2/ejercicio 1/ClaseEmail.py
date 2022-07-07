class Email:
    __idcuenta = ''
    __dominio= ''
    __tipodominio= ''
    __contraseña=''

    def __init__(self, idcuenta= '', dominio= '', tipodominio='', contraseña=''):
        self.__tipodominio = tipodominio
        self.__dominio=dominio
        self.__idcuenta=idcuenta
        self.__contraseña=contraseña
    def retornaEmail(self):
        return self.__idcuenta + '@' + self.__dominio + '.' + self.__tipodominio
   
    def getDominio(self):
        return self.__dominio
    def getContrasena(self):
        return self.__contraseña
    def setContraseña(self, nueva):
        
        if self.__contraseña == nueva:
            contra = input('Ingrese nueva contraseña')
            self.__contraseña = contra
        else:
            print('ERRONEO')
        return contra
            
    def crearCuenta(self,email):

        email=email.split('@')
        print(email)
        self.__idcuenta= email[0]
        dominio=email[1].split('.')
        print(dominio)
    def ContMail(self, archivo, idcuenta):
        repetidos = {}
        
        with open(archivo, 'r') as f:
            xmail = f.readline()
            
            while xmail:
                xmail = xmail.strip()
                if xmail == idcuenta:
                    repetidos[xmail] =+ 1
                else:
                    repetidos[xmail] = 1
                    
                xmail = f.readline()
        return repetidos
           
                
        
    



