from AV import AnalisiLexico 
from AI import Analizador2
from tkinter import *
from tkinter import ttk
from tkinter import filedialog 

op = Analizador2()
def LeerArchivoVentas ():
    text =  filedialog.askopenfilename(initialdir="c:/", title="Escoge un archivo", filetypes= (("data files" ,"*.data"),("all files", "*.*")))
    archivo = open (text, 'r')
    global contenido
    contenido = archivo.read()
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
                op.LeerArchivoInstrucciones()
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

