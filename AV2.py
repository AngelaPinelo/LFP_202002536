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
global gananciass
gananciass=[]
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
        global unidades2 
        unidades2=[]
        global precios
        precios=[]
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
                            precios.append(precio)
                            tokens.pop(0)

                            if(tokens[0][0] == "token_coma"):
                                tokens.pop(0)

                                if(tokens[0][0] == "token_precent"):
                                    unidades = float(tokens[0][1])
                                    unidades2.append(float(tokens[0][1]))
                                    ganancias = precio * unidades
                                    gananciass.append(ganancias)
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
        #print(productos)
        #print (ganancias)
        #print(unidades2)
        #print(precios)
    #haciendo referencia a los ejes para las gráficas     
        
        for i in range(0,len(productos)):
            listax.append(productos[i][0])
            listay.append(productos[i][1])
            
        print("\n\n")
        print(listax)
        print(listay)
        self.prod= listax 
        self.gananciass=listay
        
    def Ordenar (self):
        global orden
        orden=listay             
        intercambio = True
        while intercambio:
            intercambio=False
            for i in range(len(orden)-1):
                if orden[i] < orden [i+1]:
                    listax[i],listax[i+1]=listax[i+1],listax[i]
                    unidades2[i],unidades2[i+1]=unidades2[i+1],unidades2[i]
                    precios[i],precios[i+1]=precios[i+1],precios[i]
                    orden[i],orden[i+1]=orden[i+1], orden[i]
                    intercambio=True
        print(orden)
        print(listax)
    def Inicializar_reportes(self): 
        global parteInicial
        parteInicial='''<!DOCTYPE html>
<html lang="en">
<head>
	<title>Productos</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->	
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
<!--===============================================================================================-->
</head>
<body>
	<h1>Productos Ordenados de Mayor a Menor Ganancia</h1>
	<div class="limiter">
		<div class="container-table100">
			<div class="wrap-table100">
				<div class="table100 ver1">
					<div class="table100-firstcol">
						<table>
							<thead>
								<tr class="row100 head">
									<th class="cell100 column1">Productos</th>
								</tr>								
							</thead>
							<tbody>'''
        global parteMedia
        parteMedia='''</tbody>
						</table>
					</div>
					
					<div class="wrap-table100-nextcols js-pscroll">
						<div class="table100-nextcols">
							<table>
								<thead>
									<tr class="row100 head">
										<th class="cell100 column2">Precio</th>
										<th class="cell100 column3">Unidades</th>
										<th class="cell100 column4">Ganancia</th>
									</tr>
								</thead>
								<tbody>'''   
        global parteFinal
        parteFinal='''</tbody>
							</table>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>'''
    global parteFinalFinal
    parteFinalFinal='''<br>Reporte generado por: Angela Gabriela Pinelo Flores </br>
		Carnet:202002536
	</p>


<!--===============================================================================================-->	
	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/bootstrap/js/popper.js"></script>
	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/perfect-scrollbar/perfect-scrollbar.min.js"></script>
	<script>
		$('.js-pscroll').each(function(){
			var ps = new PerfectScrollbar(this);

			$(window).on('resize', function(){
				ps.update();
			})

			$(this).on('ps-x-reach-start', function(){
				$(this).parent().find('.table100-firstcol').removeClass('shadow-table100-firstcol');
			});

			$(this).on('ps-scroll-x', function(){
				$(this).parent().find('.table100-firstcol').addClass('shadow-table100-firstcol');
			});

		});

		
		
		
	</script>
<!--===============================================================================================-->
	<script src="js/main.js"></script>

</body>
</html>'''
    def TextoReportes(self):
        global tabla1
        tabla1=""
        for zeus in range(len(productos)-1):
            tabla1+='<tr class="row100 body">\n'
            tabla1+='<td class="cell100 column1">'+str(listax[zeus])+'</td>\n'
            tabla1+='</tr>'
        '''<tr class="row100 body">
				<td class="cell100 column1">Brandon Green</td>
					</tr>'''
        global tabla2
        tabla2=""
        for odin in range(len(productos)-1):
            tabla2+='<tr class="row100 body">\n'
            tabla2+='<td class="cell100 column2">\n'+str(precios[odin])+'</td>\n'
            tabla2+='<td class="cell100 column2">\n'+str(unidades2[odin])+'</td>\n'
            tabla2+='<td class="cell100 column2">\n'+str(orden[odin])+'</td>\n'
            tabla2+='</tr>'
            '''<tr class="row100 body">
                <td class="cell100 column2">CMO</td>
                <td class="cell100 column3">16 Nov 2012</td>
                    <td class="cell100 column4">16 Nov 2017</td>
                </tr>'''
        global pmas
        global pmenos
        intercambio = True
        while intercambio:
            intercambio=False
            for i in range(len(unidades2)-1):
                if unidades2[i] < unidades2 [i+1]:
                    listax[i],listax[i+1]=listax[i+1],listax[i]
                    unidades2[i],unidades2[i+1]=unidades2[i+1],unidades2[i]
                    intercambio=True
        pmas="<h1>"+"Producto m&aacute;s vendido:"+"</h1></br>"
        pmas+="<h1>"+str(listax[0])+" -->"+str(unidades2[0])+"</h1></br>"
        
        intercambio = True
        while intercambio:
            intercambio=False
            for i in range(len(unidades2)-1):
                if unidades2[i] > unidades2 [i+1]:
                    listax[i],listax[i+1]=listax[i+1],listax[i]
                    unidades2[i],unidades2[i+1]=unidades2[i+1],unidades2[i]
                    intercambio=True
        pmenos="<h1>"+"Producto menos vendido:"+"</h1></br>"
        pmenos+="<h1>"+str(listax[0])+"--> "+str(unidades2[0])+"</h1></br>"
    def crearReporte(self):
        try: 
            textoCompleto= parteInicial+tabla1+parteMedia+tabla2+parteFinal+pmas+pmenos+parteFinalFinal
            file= open("./fixed-column-table/Table_Fixed_Column/index.html",'w')
            file.write(textoCompleto)
        except:
            pass
        
class Analizador2():

    def __init__(self):
        #contiene todo el texto de los datos
        self.texto = ""
        #instrucciones almacenadas en un diccionario
        self.instrucciones = {}
        
   
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
        print(delimitadores)
        self.texto = delimitadores
        print(self)


        #para analizar mis intrucciones 
    def AnalizarInstrucciones(self):
        #tal cual las instrucciones que ingresan
        instruccioness = self.texto
        #los primeros 2 caracteres
        ini = instruccioness[0:2]
        a = len(instruccioness) - 3 # El tamaño de los datos menos los últimos 3 dentro del archivo
        b = len(instruccioness)
        fin = instruccioness[a:b]

        caso = 0
        entry = False
        #en aux vamos a guardar las instrucciones como diccionario
        global aux
        aux = {}
        if ini == "<¿" and fin == '\"?>':
            #con esto quito los primero dos caracteres (<¿)
            instruccioness = instruccioness[2:]
            #con esto quito los últimos dos caracteres (?>)
            instruccioness = instruccioness[:-2]
            #$ me va a servir para saber donde acabo el archivo porque se lo voy agregando al final 
            instruccioness += "$"
            #la instrucción del lado izquierdo
            comando = ""
            #el nombre de la instrucción del lado derecho 
            nombre = ""
            #sonnic representa a mi variable letra 
            for sonnic in instruccioness:
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
                self.instrucciones = aux
                print(self.instrucciones)
            else:
                print("Error, no se puede almacenar esta informacion, faltan datos")                    

        else:
            print("Error, no se puede leer este archivo")
    #@property
    '''def get_Instrucciones(self):
        return self.instrucciones'''
    
    '''@Instrucciones.setter
    def Instucciones(self,listaInstrucciones):
        self.instrucciones = listaInstrucciones'''

    def Graficador(self):
        tipo =self.instrucciones
        if tipo.get('grafica') == "barras":
            datos=self.instrucciones
            eje_x =listax  
            eje_y =listay 
            plt.bar(eje_x, eje_y)
            plt.ylabel(datos.get('tituloy'))
            plt.xlabel(datos.get('titulox'))
            plt.title(datos.get('titulo'))
            plt.savefig(datos.get('nombre'))
            plt.show()
        elif tipo.get('grafica') == "líneas" or tipo.get('grafica') == "lineas" or tipo.get('grafica') == "lneas":
            datos=self.instrucciones
            eje_x =listax  
            eje_y =listay 
            plt.plot(eje_x, eje_y, marker='o', linestyle='--', color='g', label ='Total de ingresos en el mes')
            plt.ylabel(datos.get('tituloy'))
            plt.xlabel(datos.get('titulox'))
            plt.title(datos.get('titulo'))
            plt.savefig(datos.get('nombre'))
            plt.show()
        elif tipo.get('grafica') == "pie" or tipo.get('grafica') == "pastel":
            datos=self.instrucciones
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
                                       