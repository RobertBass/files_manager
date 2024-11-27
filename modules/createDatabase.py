import os

def createDatabase():

    # Crear carpeta donde se almacenaran las bases de datos
    os.makedirs('db', exist_ok=True)
    os.makedirs('output', exist_ok=True)

    # Crear archivos
    with open('db/Proveedor.txt', 'w+') as p:
        p.write('COD NOMBRE  ESTADO')
        p.write('\n1 MARCELINO JARRIN A')
        p.write('\n2 KARLA MARIDUENA I')
        p.write('\n3 PATRICIO CASTRO A')
        p.close()

    with open('db/Productos.txt', 'w+') as pr:
        pr.write('ID PRODUCTO    ESTADO')
        pr.write('\n1 AZUCAR    A')
        pr.write('\n2 CREMA DE LECHE  I')
        pr.write('\n3 CAFE EN GRANO LOJA A')
        pr.close()

    with open('db/Prod_Proveedor.txt', 'w+') as f:
        f.write('PRV_COD PRO_COD ESTADO')
        f.write('\n1 3 A')
        f.write('\n1 2 A')
        f.write('\n3 1 A')
        f.write('\n2 2 I')
        f.close()

    open('output/resultados.txt', 'w+')

createDatabase()