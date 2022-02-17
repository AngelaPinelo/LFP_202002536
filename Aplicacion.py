from prueba import AnalisiLexico 
from tkinter import *
from tkinter import ttk
from tkinter import filedialog 


def LeerArchivoVentas ():
    text =  filedialog.askopenfilename(initialdir="c:/", title="Escoge un archivo", filetypes= (("data files" ,"*.data"),("all files", "*.*")))
    print (text)
    archivo = open (text, 'r')
    global contenido
    contenido = archivo.read()
    print (contenido)
    archivo.close
    return contenido 


class Aplicacion:
    
    def __init__(self):
        self.app()
        
    def app(self):
       while  True:
            res = input('''
1. Cargar Archivo de Ventas
2. Cargar Instrucciones
3. Analizar
4. Generar reportes
5. Salir
Selecciona una opcion: ''')
                #switch
            if res == '1':
                LeerArchivoVentas()
                AnalisiLexico(contenido)
            elif res == '2':
                pass
            elif res == '3':
                pass
            elif res == '4':
                pass
            elif res == '5':
                print("Adios")
                break
           # else:
               # print ("Por favor ingrese una opción valida >:( ")
                
b = Aplicacion()

