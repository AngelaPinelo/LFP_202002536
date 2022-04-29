from tokenize import Double
from tkinter import filedialog
from tkinter import Tk


def LeerArchivoInstrucciones ():
        delimitadores=""
        text2 =  filedialog.askopenfilename(initialdir="c:/", title="Escoge un archivo", filetypes= (("data files" ,"*.data"),("all files", "*.*")))
        print(text2)
        with open(text2, encoding='utf-8') as archivo:
            #archivo = open (text2, 'r')
            global contenido2
            contenido2 = archivo.read().strip()
        #para pasar todo a lower 
        contenido2=contenido2.lower()
        #talking about comillas xd 
        com = False
        #para quitar todos los espacios, tabulaciones y saltos de linea en el archivo
        #sonnic representa mi índice que recorre el archivo
        for sonnic in contenido2:
            if sonnic != '"':
                if ( sonnic != "\n" and sonnic != "\t" and sonnic != " ") or com:
                    delimitadores += sonnic
            elif not com:
                delimitadores += sonnic
                com = True
            else:
                delimitadores += sonnic
                com = False
        #print (contenido2)
        #archivo.close
        #print(delimitadores)
        #self.texto = delimitadores
        #rint(self)
#LeerArchivoInstrucciones()


def leerArchivo():
    Tk().withdraw()
    entrada = filedialog.askopenfilename(initialdir="c:/", title="Escoge un archivo", filetypes= (("data files" ,"*.data"),("all files", "*.*")))
    print(entrada)
    with open(entrada, encoding='utf-8') as archivo:
                global contenido
                contenido = archivo.read()              
                return contenido
leerArchivo()
