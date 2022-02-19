import re
from tokenize import Double
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
global tokens
tokens=[]  
global encabezado
encabezado=[]
global productos 
productos = [] 
global listax
listax = []
global listay
listay= []
class Analizador1():
    
    def __init__ (self):
        self.texto=""
        self.prod = []
        self.gananciass=[]
        self.encabezados=[]
        
        
   
    def LeerArchivoVentas2 (self):
        text =  filedialog.askopenfilename(initialdir="c:/", title="Escoge un archivo", filetypes= (("data files" ,"*.data"),("all files", "*.*")))
        archivo = open (text, 'r')
        global contenido
        contenido = archivo.read()
        archivo.close
        #print (contenido2)
        #archivo.close
        self.texto = contenido
        #print(self)
    
    #ANÁLISIS LÉXICO
    def AnalisiLexico(self):
        text = self.texto
        temp = ""
        estado = 0
        option = True
        for sonnic in text:
            option = True
            while option:
                if estado == 0:
                    option=False
                    if re.search(r'(\:)',sonnic):
                        temp_token=[]
                        temp_token.append("token_puntos")
                        temp_token.append(sonnic)
                        tokens.append(temp_token)
                        temp = ""
                    elif re.search(r'[=]',sonnic):
                        temp_token=[]
                        temp_token.append("token_eq")
                        temp_token.append(sonnic)
                        tokens.append(temp_token)
                        temp = ""
                    elif re.search(r'[(]',sonnic):
                        temp_token=[]
                        temp_token.append("token_pa")
                        temp_token.append(sonnic)
                        tokens.append(temp_token)
                        temp = ""
                    elif re.search(r'[)]',sonnic):
                        temp_token=[]
                        temp_token.append("token_pc")
                        temp_token.append(sonnic)
                        tokens.append(temp_token)
                        temp = ""
                    elif re.search(r'(\[)',sonnic):
                        temp_token=[]
                        temp_token.append("token_ca")
                        temp_token.append(sonnic)
                        tokens.append(temp_token)
                        temp = ""
                    elif re.search(r'(\,)',sonnic):
                        temp_token=[]
                        temp_token.append("token_coma")
                        temp_token.append(sonnic)
                        tokens.append(temp_token)
                        temp = ""
                    elif re.search(r'(\])',sonnic):
                        temp_token=[]
                        temp_token.append("token_cc")
                        temp_token.append(sonnic)
                        tokens.append(temp_token)
                        temp = ""
                    elif re.search(r'(\;)',sonnic):
                        temp_token=[]
                        temp_token.append("token_semi")
                        temp_token.append(sonnic)
                        tokens.append(temp_token)
                        temp = ""
                    elif re.search(r'(")',sonnic):
                        temp+=sonnic
                        estado =1 
                    elif re.search(r'[0-9]',sonnic):
                        temp+=sonnic
                        estado =2
                    elif re.search(r'[a-zA-Z]',sonnic):
                        temp+=sonnic
                        estado =3
                elif estado== 1:
                    option =False
                    if sonnic != "\"":
                        temp+=sonnic
                    else:
                        temp+=sonnic
                        temp_token=[]
                        temp_token.append("token_producto")
                        temp_token.append(temp)
                        tokens.append(temp_token)
                        temp = ""
                        estado =0
                    
                elif estado== 2:
                    option =False
                    if  re.search(r'[0-9]',sonnic):
                        temp +=sonnic 
                    elif re.search(r'(\.)',sonnic):
                        temp+= sonnic
                        estado =4
                    else:
                        temp_token=[]
                        temp_token.append("token_precent")
                        temp_token.append(temp)
                        tokens.append(temp_token)
                        temp = ""
                        estado=0
                        option =True 
                    
                elif estado== 3:
                    option =False
                    if re.search(r'[a-zA-Z]',sonnic):
                        temp+= sonnic 
                    else:
                        temp_token=[]
                        temp_token.append("token_mes")
                        temp_token.append(temp)
                        tokens.append(temp_token)
                        temp = ""
                        estado=0
                        option =True
                elif estado== 4:
                    option =False
                    if  re.search(r'[0-9]',sonnic):
                        temp +=sonnic 
                        estado = 5 
                elif estado== 5:
                    option =False
                    if  re.search(r'[0-9]',sonnic):
                        temp +=sonnic 
                    else:
                        temp_token=[]
                        temp_token.append("token_decimal")
                        temp_token.append(temp)
                        tokens.append(temp_token)
                        temp = ""
                        estado = 0
                        option =True
                else:
                    if ord(sonnic) == 32 or ord(sonnic) == 10 or ord(sonnic) == 9 :
                        pass
                    else:   
                        pass     
        #acá en vez de mandarlo a llamar le debe de ingresar un self
        #Analizador_sintactico()

 
    
    def Analizador_sintactico(self):
        temp1=[]
        global Nombre_mes
        global year
        #para quitar el "token_mes" y que solo se quede el nombre del mes 
        if(tokens[0][0] == "token_mes"):
            Nombre_mes = tokens[0][1]
            tokens.pop(0)
    #eliminando los dos puntos 
            if(tokens[0][0] == "token_puntos"):
                tokens.pop(0)
    #almacenando el año 
                if(tokens[0][0] == "token_precent"):
                    year= tokens[0][1]
                    tokens.pop(0)
    #eliminando el =
                    if(tokens[0][0] == "token_eq"):
                        tokens.pop(0)
    #eliminando el (
                        if(tokens[0][0] == "token_pa"):
                            tokens.pop(0)
                            temp1.append(Nombre_mes)
                            temp1.append(year)
                            encabezado.append(temp1)
    #ya que se leyó el inicio mandar a llamar a la otra función que nos lee los productos 
                            #Productos(encabezado)
        print (encabezado)
        self.encabezados=encabezado

        '''incio =    productos 
    ptoductos =  proctos'
    productos' = ptoductos  | nada
    '''
              
    
    def Productos(self):
        #porque puede que vengan productos o puede que no venga nada 
        while(True):
            temp2 = []
    #eliminando el [        
            if(tokens[0][0] == "token_ca"):
                tokens.pop(0)
    #agregando los productos y quitando ""
                if(tokens[0][0] == "token_producto"):
                    producto =tokens[0][1].replace('"','')
                    tokens.pop(0)
    #eliminando , 
                    if(tokens[0][0] == "token_coma"):
                        tokens.pop(0)
    #Guardando el precio y casteado a float para después multiplicarlo 
                        if(tokens[0][0] == "token_precent" or tokens[0][0] == "token_decimal"):
                            precio = float(tokens[0][1])
                            tokens.pop(0)

                            if(tokens[0][0] == "token_coma"):
                                tokens.pop(0)

                                if(tokens[0][0] == "token_precent"):
                                    unidades = float(tokens[0][1])
                                    ganancias = precio * unidades
                                    tokens.pop(0)

                                    if(tokens[0][0] == "token_cc"):
                                        tokens.pop(0)

                                        if(tokens[0][0] == "token_semi"):
                                            tokens.pop(0)
                                            temp2.append(producto)
                                            temp2.append(ganancias)
                                            productos.append(temp2)

                                            if(tokens[0][0] == "token_pc"):
                                                break
                                
                                            
    #para que me separe los productos y las ganancias en listas separadas                                        
        print(productos)
        print (ganancias)
    #haciendo referencia a los ejes para las gráficas     
        
        for i in range(0,len(productos)):
            listax.append(productos[i][0])
            listay.append(productos[i][1])

        print("\n\n")
        print(listax)
        print(listay)
        self.prod= productos 
        self.gananciass=ganancias
        
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
                if (sonnic != " " and sonnic != "\n" and sonnic != "\t") or com:
                    delimitadores += sonnic
            elif not com:
                delimitadores += sonnic
                com = True
            else:
                delimitadores += sonnic
                com = False
        #print (contenido2)
        #archivo.close
        print(delimitadores)
        self.texto = delimitadores
        print(self)


        #para analizar mis intrucciones 
    def AnalizarInstrucciones(self):
        cadena = self.texto
        #los primeros 2 caracteres
        ini = cadena[0:2]
        a = len(cadena) - 3 # El tamaño de los datos menos los últimos 3 
        b = len(cadena)
        fin = cadena[a:b]

        caso = 0
        entry = False
        #en aux vamos a guardar las instrucciones como diccionario
        global aux
        aux = {}
        if ini == "<¿" and fin == '\"?>':
            #con esto quito los primero dos caracteres (<¿)
            cadena = cadena[2:]
            #con esto quito los últimos dos caracteres (?>)
            cadena = cadena[:-2]
            #$ me va a servir para saber donde acabo el archivo porque se lo voy agregando al final 
            cadena += "$"
            #la instrucción del lado izquierdo
            comando = ""
            #el nombre de la instrucción del lado derecho 
            nombre = ""
            #sonnic representa a mi variable letra 
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
                #Para cuando entren las comillas almacenarlo en nombre 
                elif entry == True:
                    nombre += sonnic
                #para sustituír en caso se repita la instrucción o $ venga al final que siempre se lo agragamos
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
            #si los comandos nombre y grafica vienen ya almacenados en aux 
            if 'nombre' in aux and 'grafica' in aux:
                self.instr = aux
                print(self.instr)
            else:
                print("Error, no se puede almacenar esta informacion, faltan datos")                    

        else:
            print("Error, no se puede leer este archivo")
    #@property
    '''def get_Instrucciones(self):
        return self.instr'''
    
    '''@Instrucciones.setter
    def Instucciones(self,listaInstrucciones):
        self.instr = listaInstrucciones'''

    def Graficador(self):
        tipo =self.instr
        if tipo.get('grafica') == "barras":
            datos=self.instr
            eje_x =listax  
            eje_y =listay 
            plt.bar(eje_x, eje_y)
            plt.ylabel(datos.get('tituloy'))
            plt.xlabel(datos.get('titulox'))
            plt.title(datos.get('titulo'))
            plt.savefig(datos.get('nombre'))
            plt.show()
        elif tipo.get('grafica') == "líneas":
            datos=self.instr
            eje_x =listax  
            eje_y =listay 
            plt.plot(eje_x, eje_y, marker='o', linestyle='--', color='g', label ='Total de ingresos en el mes')
            plt.ylabel(datos.get('tituloy'))
            plt.xlabel(datos.get('titulox'))
            plt.title(datos.get('titulo'))
            plt.savefig(datos.get('nombre'))
            plt.show()
        elif tipo.get('grafica') == "pie" or tipo.get('grafica') == "pastel":
            datos=self.instr
            eje_y =listax  
            #eje_y =listay
            eje_x= np.array(listay)
            eje_x = eje_x.astype(int)
            #de primero va el dato numérico
            plt.pie(eje_x, labels=eje_y, autopct='%.0f %%')
            plt.ylabel(datos.get('tituloy'))
            plt.xlabel(datos.get('titulox'))
            plt.title(datos.get('titulo'))
            plt.savefig(datos.get('nombre'))
            plt.show()
                                       