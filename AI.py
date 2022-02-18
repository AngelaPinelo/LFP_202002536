from fileinput import filename
from tkinter import Tk
from tkinter import filedialog


class Analizador2():

    def __init__(self):
        #contiene todo el texto de los datos
        self.texto = ""
        self.id_instr = 1
        #instrucciones
        self.instr = {}
        
   
    #para leer los archivos .lfp
    def LeerArchivoInstrucciones (self):
        delimitadores=""
        text2 =  filedialog.askopenfilename(initialdir="c:/", title="Escoge un archivo", filetypes= (("data files" ,"*.data"),("all files", "*.*")))
        with open(text2, encoding='utf-8') as archivo:
            #archivo = open (text2, 'r')
        #global contenido2
            contenido2 = archivo.read().strip()
        #para pasar todo a lower 
        contenido2=contenido2.lower()
        #talking about comillas xd 
        com = False
        #para quitar todos los espacios, tabulaciones y saltos de linea en el archivo
        #sonnic representa mi índice que recorre el archivo
        for sonnic in contenido2:
            if sonnic != '"':
                if (sonnic != " " and sonnic != "\n" and sonnic != "\t") or com:
                    delimitadores += sonnic
            elif not com:
                delimitadores += sonnic
                com = True
            else:
                delimitadores += sonnic
                com = False
        print (contenido2)
        #archivo.close
        print(delimitadores)
        self.texto = delimitadores


        #para analizar mis intrucciones 
    def AnalizarInstrucciones(self):
        cadena = self.texto
        ini = cadena[0:2]
        a = len(cadena) - 3 # El tamanio de la lista (numero de datos)
        b = len(cadena)
        fin = cadena[a:b]

        caso = 0
        entry = False
        
        aux = {}
        if ini == "<¿" and fin == '"?>':
            cadena = cadena[2:]
            cadena = cadena[:-2]
            #$ me va a servir para saber donde acabo el archivo 
            cadena += "$"
            comando = ""
            nombre = ""

            for sonnic in cadena:
                if sonnic != ":" and caso == 0:
                    comando += sonnic
                elif sonnic == ":":
                    caso = 1
                elif sonnic == '"':
                    if entry:
                        entry = False
                    else:
                        entry = True
                elif entry == True:
                    nombre += sonnic
                elif (sonnic == "," and caso == 1) or sonnic == "$":
                    if comando == 'nombre':
                        aux[comando] = nombre  # {'nombre': "cambio1"}
                    elif comando == 'grafica':
                        aux[comando] = nombre
                    elif comando == 'titulo':
                        aux[comando] = nombre
                    elif comando == 'titulox':
                        aux[comando] = nombre
                    elif comando == 'tituloy':
                        aux[comando] = nombre
                    else:
                        print("Error, no se reconoce este comando")
                        aux = {}
                        break
                    nombre = ""
                    comando = ""
                    caso = 0
                else:
                    print("Error, no se puede leer este archivo")
                    aux = {}
                    break
            #porque nombre y gráfica son obligatorios
            if 'nombre' in aux and 'grafica' in aux:
                self.instr[self.id_instr] = aux
                self.id_instr += 1
                print(self.instr)
            else:
                print("Error, no se puede almacenar esta informacion, faltan datos")                    

        else:
            print("Error, no se puede leer este archivo")