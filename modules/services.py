import pandas as pd
import string
from unidecode import unidecode

dbPP = 'db/Prod_Proveedor.txt'
dbProv = 'db/Proveedor.txt'
dbProd = 'db/Productos.txt'
output = 'output/resultados.txt'

db1 = pd.read_csv(dbPP, sep=' ', skiprows=0)
db2 = pd.read_csv(dbProv, sep=' ', skiprows=0)
db3 = pd.read_csv(dbProd, sep=' ', skiprows=0)


# FUNCION PARA MOSTRAR CONTENIDO DE LOS ARCHIVOS
def mostrar(db):
    with open(db, 'r') as f:
        print(f.read())


# FUNCION PARA REGISTRAR NUEVOS PROVEEDORES Y PRODUCTOS
def registrar(db, descripcion, estado):
    data = pd.read_csv(db, sep=' ', skiprows=0)
    cod = str(data.__len__() + 1)
    with open(db, 'a') as f:
        f.write(f'\n{cod} {descripcion} {estado}')
        f.close()


def buscarProveedor(codProv):
    db2 = pd.read_csv(dbProv, sep=' ', skiprows=0)
    proveedor = db2[db2['COD'] == int(codProv)]
    if proveedor.__len__() == 0:
        print(f'PROVEEDOR CON EL CODIGO {codProv} NO SE ENCUENTRA EN LA BASE DE DATOS, INTENTALO DE NUEVO')
        return 0, proveedor
    else:
        return 1, proveedor


def buscarProducto(idProd):
    db3 = pd.read_csv(dbProd, sep=' ', skiprows=0)
    producto = db3[db3['ID'] == int(idProd)]
    if producto.__len__() == 0:
        print(f'PRODUCTO CON EL CODIGO {idProd} NO SE ENCUENTRA EN LA BASE DE DATOS')
        return 1, producto
    else:
        return 0, producto


# FUNCION PARA ASIGNAR PRODUCTOS A LOS PROVEEDORES
def asignarProducto(codProv, idProd, producto):
    index = 0
    for i in producto.index:
        index = i
    estadoProd = producto.loc[index,'ESTADO']
    with open(dbPP, 'a') as f:
        f.write(f'\n{codProv} {idProd} {estadoProd}')
        f.close()



# FUNCION PARA VALIDAR TEXTO INGRESADO PARA REGISTRAR PRODUCTOS
# CONDICION: MAXIMO 4 PALABRAS
def validarProveedor(valor, limite):
    # DAMOS FORMATO AL TEXTO
    texto = valor.upper()
    texto = texto.translate(str.maketrans('','',string.punctuation + '¿¡'))
    texto = unidecode(texto)
    # CONTAMOS LAS PALABRAS INGRESAMOS
    palabras = texto.split()
    contador = 0
    for palabra in palabras:
        contador += 1
    if contador > limite:
        print(f'LA CANTIDAD DE PALABRAS INGRESADAS ({contador}) SUPERA EL LIMITE ESTABLECIDO')
        return 0
    elif contador < limite:
        print(f'AL MENOS DEBES INGRESAR {limite} PALABRAS -> (UN NOMBRE Y UN APELLIDO)')
        return 0
    else:
        return 1


def validarProducto(valor, limite):
    # DAMOS FORMATO AL TEXTO
    texto = valor.upper()
    texto = texto.translate(str.maketrans('', '', string.punctuation + '¿¡'))
    texto = unidecode(texto)
    # CONTAMOS LAS PALABRAS INGRESAMOS
    palabras = texto.split()
    contador = 0
    for palabra in palabras:
        contador += 1
    if contador > limite:
        print(f'LA CANTIDAD DE PALABRAS INGRESADAS ({contador}) SUPERA EL LIMITE ESTABLECIDO')
        return 0
    else:
        return 1


def validarEstado(valor):
    valor = valor.upper()
    if valor == 'A' or valor == 'I':
        return 0
    else:
        print(f'EL ESTADO {valor} NO ES VALIDO, VUELVE A INTENTARLO')
        return 1


# FUNCION PARA MOSTRAR CONSULTAS DE PROVEEDORES CON SUS PRODUCTOS
'''
RECIBE COMO PARAMETROS EL CODIGO INGRESADO POR EL USUARIO, LOS ARCHIVOS DE BASES DE DATOS Y
LA UBICACION DEL ARCHIVO PIVOT DE SALIDA
'''
def infoPorProveedor(codProv, proveedor):
    db1 = pd.read_csv(dbPP, sep=' ', skiprows=0)
    db3 = pd.read_csv(dbProd, sep=' ', skiprows=0)
    # INICIALIZAMOS VARIABLES
    codes = []
    # EXTRAEMOS LOS DATOS DEL PROVEEDOR PARA ALMACENARLAS EN EL ARCHIVO PIVOT DE SALIDA
    for i in proveedor.index:
        index = i
    nombre = str(proveedor.loc[index, 'NOMBRE'] + ' ' + proveedor.loc[index, 'Unnamed: 2'])
    estado = str(proveedor.loc[index, 'ESTADO'])
    with open(output, 'w') as f:
        f.write(f'Proveedor: {nombre}\n')
        f.write(f'Estado: {estado}\n')
        f.write(f'ID        PRODUCTO        ESTADO\n')
        f.close()
    # FILTRAMOS LOS PRODUCTOS RELACIONADOS CON EL PROVEEDOR DE LA BASE RELACIONANTE
    items = db1[db1['PRV_COD'] == int(codProv)]
    #RECORREMOS EL DATAFRAME EN BUSCA DE LOS INDICES
    for i in items.index:
        codigo = int(db1.loc[i,'PRO_COD'])
        codes.append(codigo)
    # RECORREMOS LA BASE EN BUSCA DE LOS PRODUCTOS CON EL ID Y LO ALMACENAMOS EN EL ARCHIVO PIVOT DE SALIDA
    for i in codes:
        producto = db3[db3['ID'] == i]
        producto.to_csv(output, mode='a', index=False, header=False, sep='\t')
    # MOSTRAMOS EN PANTALLA EL RESULTADO DE LA INFORMACION SOLICITADA POR EL USUARIO
    print('***RESULTADO DE LA BUSQUEDA***')
    mostrar(output)