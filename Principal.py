#practicando para leer un archivo .data en una función e imprimir el contenido 
def LeerArchivoVentas (ruta):
    archivo = open (ruta, 'r')
    contenido = archivo.read()
    #print (contenido)
    archivo.close
    return contenido 

