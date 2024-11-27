import time
from modules.services import *

def menuPrincipal():
    while True:
        print(f'\n====MENU PRINCIPAL====')
        print(f'\n1. CONSULTAR PRODUCTOS POR PROVEEDOR')
        print('2. LISTA DE PROVEEDORES')
        print('3. LISTA DE PRODUCTOS')
        print('4. REGISTRAR PROVEEDORES')
        print('5. REGISTRAR PRODUCTOS')
        print('6. ASIGNAR PRODUCTO A PROVEEDOR')
        print(f'7. SALIR DEL SISTEMA\n')

        seleccion = input('ELIGE UNA OPCION DEL MENU: ')

        if seleccion == '1':
            print(f'\n====INFORMACION DE PRODUCTOS POR PROVEEDOR====')
            mostrar(dbProv)
            flag = 0
            while flag == 0:
                codProv = input(f'\nINGRESA EL CODIGO DEL PROVEEDOR: ')
                flag, proveedor = buscarProveedor(codProv)
            print(f'\n')
            time.sleep(1)
            infoPorProveedor(codProv, proveedor)
            time.sleep(2)
            menuSecundario()


        if seleccion == '2':
            print(f'\n====LISTA DE PROVEEDORES====')
            mostrar(dbProv)
            time.sleep(2)
            menuSecundario()


        if seleccion == '3':
            print(f'\n====LISTA DE PRODUCTOS====')
            mostrar(dbProd)
            time.sleep(2)
            menuSecundario()


        if seleccion == '4':
            print(f'\n====REGISTRO DE PROVEEDORES====')
            validacion = 0
            while validacion == 0:
                nombre = input('INGRESA EL NOMBRE DEL PROVEEDOR (UN NOMBRE Y UN APELLIDO): ')
                nombre = nombre.upper()
                validacion = validarProveedor(nombre, 2)
            while validacion == 1:
                estado = input('INGRESA EL ESTADO DEL PROVEEDOR (a/A/i/I): ')
                estado = estado.upper()
                validacion = validarEstado(estado)
            registrar(dbProv, nombre, estado)
            print('PROVEEDOR REGISTRADO EXITOSAMENTE')
            time.sleep(2)
            menuSecundario()


        if seleccion == '5':
            print(f'\n====REGISTRO DE PRODUCTOS====')
            validacion = 0
            limite = 4
            while validacion == 0:
                nombre = input('INGRESA EL NOMBRE DEL PRODUCTO: ')
                nombre = nombre.upper()
                validacion = validarProducto(nombre, limite)
                texto = nombre.split()
                contador = 0
                for palabra in texto:
                    contador += 1
                while contador < limite:
                    nombre += ' '
                    contador += 1
            while validacion == 1:
                estado = input(f'\nINGRESA EL ESTADO DEL PRODUCTO (a/A/i/I): ')
                estado = estado.upper()
                validacion = validarEstado(estado)
            registrar(dbProd, nombre, estado)
            print('PRODUCTO REGISTRADO EXITOSAMENTE')
            time.sleep(2)
            menuSecundario()


        if seleccion == '6':
            print(f'\n====ASIGNACION DE PRODUCTOS A PROVEEDORES====')
            mostrar(dbProv)
            flag = 0
            while flag == 0:
                codProv = input(f'\nINGRESA EL CODIGO DEL PROVEEDOR: ')
                flag, proveedor = buscarProveedor(codProv)
            mostrar(dbProd)
            while flag == 1:
                idProd = input(f'\nINGRESA EL ID DEL PRODUCTO: ')
                flag, producto = buscarProducto(idProd)
            asignarProducto(codProv, idProd, producto)
            print(f'\nREGISTRO COMPLETADO SATISFACTORIAMENTE')
            time.sleep(2)
            menuSecundario()


        if seleccion == '7':
            exit()


def menuSecundario():
    flag = 0
    print('QUE DESEAS REALIZAR A CONTINUACION?')
    print('====OPCIONES====')
    print('1. VOLVER AL MENU PRINCIPAL')
    print('2. SALIR')


    while flag == 0:
        opcion = input(f'\nESCOGE UNA OPCION: ')
        if opcion == '1':
            flag = 1
            menuPrincipal()
        elif opcion == '2':
            print('GRACIAS, VUELVE PRONTO...')
            exit()
        else:
            print(f'OPCION {opcion} NO VALIDA. DEBES INGRESAR 1 o 2')
