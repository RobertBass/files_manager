'''
MODULO DE IMPLEMENTACION DEL LOS SERVICIOS Y CREACION DE INTERACCION CON EL USUARIO
'''


from modules.createDatabase import *
from modules.interaction import *


def exe():
    createDatabase()

    print('***********************************************************************')
    print('      BIENVENIDO AL SISTEMA DE CONTROL DE PRODUCTOS POR PROVEEDOR      ')
    print('***********************************************************************')

    menuPrincipal()



