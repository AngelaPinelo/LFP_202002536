from AV2 import Analizador1
from AV2 import Analizador2
from tkinter import *


#op por operación xd 
ap=Analizador1()
op = Analizador2()

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
                ap.LeerArchivoVentas2()
                ap.AnalisiLexico()
                ap.Analizador_sintactico()
                ap.Productos()
            elif res == '2':
                op.LeerArchivoInstrucciones()
                op.AnalizarInstrucciones()
            elif res == '3':
                op.Graficador()
            elif res == '4':
                pass
            elif res == '5':
                print("Adios")
                break
            else:
                
                print ("Por favor ingrese una opción valida >:( ")
                
b = Aplicacion()

