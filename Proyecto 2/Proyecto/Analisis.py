from Token import Token
from Token import Error
from prettytable import PrettyTable

import webbrowser
import copy


class Analizador():
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        self.resultado=''
        
    def leer (ruta):
        with open(ruta, encoding='utf-8') as archivo:
            global contenido
            contenido = archivo.read()              
            return contenido


    contenido2 = leer(r'LaLigaBot-LFP.csv')
    partidos = contenido2.split('\n')

    global objPartidos
    objPartidos = []
    for partido in partidos: 
        datos = partido.split(',')
        p={
        'fecha': datos [0],
        'temporada': datos [1],
        'jornada': datos [2],
        'equipo1': datos [3],
        'equipo2': datos [4],
        'goles1': datos [5],
        'goles2': datos [6]
        }
        objPartidos.append(p)

    def imprimirDatos(self):
        print ('**************Lista Tokens************')
        for token in self.listaTokens:
            token.getTok()
        for error in self.listaErrores:
            error.getError()
    
    def agregar_token(self,caracter,token,linea,columna):
        self.listaTokens.append(Token(caracter,token,linea,columna))
        self.buffer = ''
    
    def agregar_jornada(self,caracter,token,linea,columna):
        self.listaTokens.append(Token(caracter,token,linea,columna))
        
    def agregar_error(self,caracter,descripcion,linea,columna):
        self.listaErrores.append(Error( caracter, descripcion, linea, columna))
        self.buffer=''
        
        
    def AnalisisLexico(self,cadena):
        text = cadena + '$'
        estado = 0
        option = True
        for caracter in text:            
            self.columna+=1
            option = True
            while option:
                if estado == 0:
                    option=False
                    if caracter.isupper():                        
                        self.buffer+=caracter   
                        #print(self.buffer)                                            
                        estado= 1
                    elif caracter =='<':
                        self.buffer+=caracter                                           
                        self.agregar_token(self.buffer, 'menor que', self.linea, self.columna)
                        estado= 2
                    elif caracter =='>':
                        self.buffer+=caracter                                           
                        self.agregar_token(self.buffer, 'mayor que', self.linea, self.columna)
                    elif caracter =='-':
                        self.buffer+=caracter                                           
                        #self.agregar_token(self.buffer, 'guion', self.linea, self.columna)
                        estado= 3                   
                    elif caracter.isdigit():
                        self.buffer+= caracter                      
                        self.agregar_jornada(self.buffer, 'jornada singular', self.linea, self.columna)
                        estado = 5
                    elif caracter == '"':
                        self.buffer+= caracter                
                        self.agregar_token(self.buffer, 'Comilla Doble', self.linea, self.columna)
                        estado = 4                    
                    else: 
                        if caracter =='\n':
                            self.linea+=1
                            self.columna =0
                        elif caracter == '\r':
                            self.columna =0
                            self.linea +=1
                        elif caracter == ' ':
                            pass
                        else: 
                            self.buffer += caracter
                            self.agregar_error(self.buffer,'Error Lexico og',self.linea,self.columna)
                            
                #Para las Palabras reservadas
                elif estado == 1:
                    option=False
                    if caracter.isupper():
                        self.buffer+=caracter                    
                        if self.buffer == 'RESULTADO':                                                   
                            self.agregar_token(self.buffer, 'PR RESULTADO', self.linea, self.columna)
                            estado=0
                        elif self.buffer =='TEMPORADA':
                            self.agregar_token(self.buffer, 'PR TEMPORADA', self.linea, self.columna)
                            estado=0
                        elif self.buffer =='VS':
                            self.agregar_token(self.buffer, 'PR VS', self.linea, self.columna)
                            estado=0
                        elif self.buffer =='JORNADA':
                            self.agregar_token(self.buffer, 'PR JORNADA', self.linea, self.columna)
                            estado=0   
                        elif self.buffer =='GOLES':
                            self.agregar_token(self.buffer, 'PR GOLES', self.linea, self.columna)
                            estado=0 
                        elif self.buffer =='TOTAL':
                            self.agregar_token(self.buffer, 'PR TOTAL', self.linea, self.columna)
                            estado=0   
                        elif self.buffer =='LOCAL':
                            self.agregar_token(self.buffer, 'PR LOCAL', self.linea, self.columna)
                            estado=0  
                        elif self.buffer =='VISITANTE':
                            self.agregar_token(self.buffer, 'PR VISITANTE', self.linea, self.columna)
                            estado=0        
                        elif self.buffer =='TABLA':
                            self.agregar_token(self.buffer, 'PR TABLA', self.linea, self.columna)
                            estado=0       
                        elif self.buffer =='PARTIDOS':
                            self.agregar_token(self.buffer, 'PR PARTIDOS', self.linea, self.columna)
                            estado=0       
                        elif self.buffer =='TOP':
                            self.agregar_token(self.buffer, 'PR TOP', self.linea, self.columna)
                            estado=0 
                        elif self.buffer =='INFERIOR':
                            self.agregar_token(self.buffer, 'PR INFERIOR', self.linea, self.columna)
                            estado=0 
                        elif self.buffer =='SUPERIOR':
                            self.agregar_token(self.buffer, 'PR SUPERIOR', self.linea, self.columna)
                            estado=0 
                        elif self.buffer =='ADIOS':
                            self.agregar_token(self.buffer, 'PR ADIOS', self.linea, self.columna)
                            estado=0 
                    else: 
                        self.buffer += caracter
                        self.agregar_error(self.buffer,'Error LexicoS',self.linea,self.columna)
                        #option=True
                        estado = 0
                
                #para los años adentro de los <>
                elif estado == 2:
                    option=False
                    if caracter!='<':                           
                        if caracter.isdigit() :  
                            self.buffer+= caracter
                            if len(self.buffer)== 4:                      
                                self.agregar_token(self.buffer, 'Año',self.linea, self.columna )
                                estado = 2
                            elif len(self.buffer)>4:
                                self.buffer += caracter
                                self.agregar_error(self.buffer,'Error Lexico',self.linea,self.columna) 
                                estado=0
                        elif caracter =='-':
                                self.buffer += caracter
                                self.agregar_token(self.buffer, 'Guión',self.linea, self.columna )
                                estado=2
                                                    
                                                          
                        elif caracter == '>': 
                            self.buffer += caracter
                            self.agregar_token(self.buffer,'Mayor que',self.linea,self.columna)                        
                            estado=0
                    else: 
                            self.buffer += caracter
                            self.agregar_error(self.buffer,'Error Lexico',self.linea,self.columna)                        
                            estado=0
                        
                #para lo que viene luego de los -
                elif estado == 3:                    
                    option=False
                    if caracter!='-':                                            
                        if caracter =='f':
                            self.buffer+= caracter 
                            self.agregar_token(self.buffer, 'inst. nombre',self.linea, self.columna )  
                            estado=6    
                        elif  caracter =='n':
                            self.buffer+= caracter 
                            self.agregar_token(self.buffer, 'inst. top',self.linea, self.columna )  
                            estado=6  
                        elif  caracter =='j':                            
                            self.buffer+= caracter 
                            self.agregar_token(self.buffer, 'inst. desde',self.linea, self.columna )  
                            estado=6                     
                        else:
                            self.agregar_error(self.buffer,'Error Lexico',self.linea,self.columna)
                            estado=0
                    else:
                        estado=0                                                                   

                #para almacenar lo que viene despues de los -f -ji -jf -n                            
                elif estado ==6:
                    option=False 
                    if caracter!="-":
                        self.buffer+= caracter                  
                    else:                                                                          
                        self.agregar_token(self.buffer, 'nombre doc',self.linea, self.columna)                            
                        self.buffer+= caracter
                        estado=3

                #para lo que viene en comillas
                elif estado == 4:
                    option=False
                    if caracter!='"':
                        self.buffer+= caracter                        
                    else: 
                        self.agregar_token(self.buffer, 'nombre equipo', self.linea, self.columna)
                        self.columna +=1
                        self.agregar_token('"', 'Comilla Doble',self.linea, self.columna )
                        estado=0

                #Para las jornadas        
                elif estado == 5:
                    option=False                                                            
                    if caracter.isdigit():
                        self.buffer+= caracter                    
                        if  len(self.buffer) == 2 : 
                            #para eliminar la "jornada singular" que creamos antes con el primer digito
                            self.listaTokens.pop()                           
                            self.agregar_token(self.buffer, 'numero jornada', self.linea, self.columna)                             
                            estado=0
                        else: 
                            self.agregar_error(self.buffer,'jornada no válida',self.linea,self.columna)                        
                            estado=0                          
                    elif  caracter.isupper() :
                        #porque sigue almacenado en el buffer lo que no borramos de la jornada singular
                        self.buffer=''
                        self.buffer+= caracter                         
                        estado=5
                    else:    
                        self.buffer=''                    
                        self.buffer+=caracter 
                        self.agregar_error(self.buffer,'Error Léxico',self.linea,self.columna)                        
                        estado=0
                        
    
    def impTokens(self):
        print("TABLA TOKENS")
        x = PrettyTable()
        x.field_names = ["Lexema", "Token", "Fila", "Columna"]
        for i in self.listaTokens:
            x.add_row(i.enviarDataTok())
        print(x)
        
    def impErrores(self):
        print("TABLA ERRORES")
        x = PrettyTable()
        x.field_names = ["lexema","Descripcion", "Fila", "Columna"]
        if len(self.listaErrores)==0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                x.add_row(i.enviarDataError())
            print(x)

    def reporteTokens(self):
        x = PrettyTable()
        x.field_names = ["Lexema", "Token", "Fila", "Columna"]
        for i in self.listaTokens:
            x.add_row(i.enviarDataTok())
        cadenatokens = x.get_html_string()
        cadenatokensform = "{}".format(cadenatokens)
        plantilla1 = """
        <html lang="es">
                <head>
                <!-- Required meta tags -->
                <meta charset="utf-8">
                <!-- <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> -->
                <!-- <meta name="viewport" content="width=device-width, initial-scale=1"> -->
                <!-- Bootstrap CSS -->
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
                <title>Reporte de Tokens</title>                
                </head>
                <body>
                <h3>Tokens</h3>
                {cadenatokensform}
                <!-- Optional JavaScript; choose one of the two! -->
                <!-- Option 1: Bootstrap Bundle with Popper -->
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
                <!-- Option 2: Separate Popper and Bootstrap JS -->
                <!--
                <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js" integrity="sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/" crossorigin="anonymous"></script>
                -->
                </body>
                </html>
                """.format(**locals())
        file1= open("reporteTokens.html","w")
        file1.write(plantilla1)
        file1.close()
        webbrowser.open('reporteTokens.html')
    
    def reporteErrores(self):
        x = PrettyTable()
        x.field_names = ["Caracter","Descripcion", "Fila", "Columna"]
    
        for i in self.listaErrores:
            x.add_row(i.enviarDataError())
        cadenaerrores = x.get_html_string()
        cadenaerroresform = "{}".format(cadenaerrores)
        plantilla2 = """
        <html lang="es">
                <head>
                <!-- Required meta tags -->
                <meta charset="utf-8">
                <!-- <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> -->
                <!-- <meta name="viewport" content="width=device-width, initial-scale=1"> -->
                <!-- Bootstrap CSS -->
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
                <title>Reporte de Errores</title>
                </head>
                <body>
                <h3>Errores</h3>
                {cadenaerroresform}
                <!-- Optional JavaScript; choose one of the two! -->
                <!-- Option 1: Bootstrap Bundle with Popper -->
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
                <!-- Option 2: Separate Popper and Bootstrap JS -->
                <!--
                <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js" integrity="sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/" crossorigin="anonymous"></script>
                -->
                </body>
                </html>
                """.format(**locals())
        file1= open("reporteErrores.html","w")
        file1.write(plantilla2)
        file1.close()
        webbrowser.open('reporteErrores.html')
    
    #Ananlizador Sintáctico
    def AnalizadorSintactico(self):
        global copiaTok
        copiaTok=copy.deepcopy(self.listaTokens)
        contador=0
        for a in copiaTok:
            if a.lexema == '"' or a.lexema =="'" :
                copiaTok.pop(contador)
            contador +=1
        contador =0
        for a in copiaTok:            
            if a.lexema == ':':
                copiaTok.pop(contador)
            contador +=1
       
        if copiaTok[0].tipo == 'PR RESULTADO' or copiaTok[0].tipo == 'PR JORNADA' or copiaTok[0].tipo == 'PR GOLES' or copiaTok[0].tipo == 'PR TABLA' or copiaTok[0].tipo == 'PR PARTIDOS' or copiaTok[0].tipo == 'PR TOP':            
              self.estadoRecursivo()
        else:
            self.agregar_error(copiaTok[0].lexema,'Error Sintactico',self.linea,1)

    def estadoRecursivo(self):        
        if copiaTok[0].lexema == 'RESULTADO':
            copiaTok.pop(0) 
            self.Op1()
        elif copiaTok[0].lexema == 'GOLES':
            copiaTok.pop(0) 
            self.Op2() 


    def Op1(self):
        if copiaTok[0].tipo =='nombre equipo':
            global equipo1name
            equipo1name=copiaTok[0].lexema                      
            copiaTok.pop(0)        
            if copiaTok[0].lexema =='VS':
                copiaTok.pop(0)
                if copiaTok[0].tipo =='nombre equipo':
                    global equipo2name
                    equipo2name=copiaTok[0].lexema
                    copiaTok.pop(0)
                    if copiaTok[0].lexema =='TEMPORADA':
                        copiaTok.pop(0)
                        if copiaTok[0].lexema =='<':
                            copiaTok.pop(0)
                            if copiaTok[0].tipo =='Año':
                                global year1
                                year1=copiaTok[0].lexema
                                copiaTok.pop(0)
                                if copiaTok[0].lexema =='-':
                                    copiaTok.pop(0)
                                    if copiaTok[0].tipo =='Año':
                                        global year2
                                        year2=copiaTok[0].lexema
                                        copiaTok.pop(0)
                                        if copiaTok[0].lexema =='>':
                                            copiaTok.pop(0)
                                            global resultado
                                            resultado = self.resultados(equipo1name, equipo2name, year1, year2)  
                                            self.resultado=resultado                                          
                                                                                      
                                        elif copiaTok[0].lexema !='>':
                                            self.agregar_error(copiaTok[0].lexema,'Error Sintactico',self.linea,1)
                                            mensaje='No incluíste >'  
                                    elif copiaTok[0].tipo !='Año':
                                        self.agregar_error(copiaTok[0].lexema,'Error Sintactico',self.linea,1)
                                        mensaje='Te faltó el año' 
                                elif copiaTok[0].lexema !='-':
                                    self.agregar_error(copiaTok[0].lexema,'Error Sintactico',self.linea,1)
                                    mensaje='Te faltó el guión -'
                            elif copiaTok[0].tipo !='Año':
                                self.agregar_error(copiaTok[0].lexema,'Error Sintactico',self.linea,1)
                                mensaje='Te faltó el año' 
                        elif  copiaTok[0].lexema !='<':   
                            self.agregar_error(copiaTok[0].lexema,'Error Sintactico',self.linea,1)
                            mensaje='No incluíste <'              
                    elif  copiaTok[0].lexema !='TEMPORADA':
                         self.agregar_error(copiaTok[0].lexema,'Error Sintactico',self.linea,1)
                         mensaje='No incluíste TEMPORADA'
                elif copiaTok[0].tipo !='nombre equipo':
                    self.agregar_error(copiaTok[0].lexema,'Error Sintactico',self.linea,1)
                    mensaje='Te faltó el nombre del equipo Unu'
            elif  copiaTok[0].lexema !='VS':  
                self.agregar_error(copiaTok[0].lexema,'Error Sintactico',self.linea,1)
                mensaje='No incluíste el VS'  
                print(mensaje)                                                                      
        elif copiaTok[0].tipo !='nombre equipo':
            self.agregar_error(copiaTok[0].lexema,'Error Sintactico',self.linea,1)
            mensaje='Te faltó el nombre del equipo Unu'
    
    def Op2(self):
        if copiaTok[0].lexema =='TOTAL' or copiaTok[0].lexema =='LOCAL' or copiaTok[0].lexema =='VISITANTE':            
            copiaTok.pop(0) 
            if copiaTok[0].tipo =='nombre equipo':
                global nombrEquipo
                nombrEquipo=copiaTok[0].lexema
                copiaTok.pop(0)
                if copiaTok[0].lexema =='TEMPORADA':
                    copiaTok.pop(0) 
                    if copiaTok[0].lexema =='<':
                            copiaTok.pop(0)
                            if copiaTok[0].tipo =='Año':
                                global year1
                                year1=copiaTok[0].lexema
                                copiaTok.pop(0)
                                if copiaTok[0].lexema =='-':
                                    copiaTok.pop(0)
                                    if copiaTok[0].tipo =='Año':
                                        global year2
                                        year2=copiaTok[0].lexema
                                        copiaTok.pop(0)
                                        if copiaTok[0].lexema =='>':
                                            copiaTok.pop(0)
                                            cantgoles = self.goles(nombrEquipo, year1, year2)  
                                            self.resultado='Botcito: Goles:' + cantgoles
                                            print(cantgoles)
        
    def resultados(self, nomequipo1,nomequipo2,year1,year2): 
        temporada = str(year1) + '-' + str(year2)
        for partido in objPartidos:
            if partido['temporada'] == temporada:
                if partido['equipo1']==nomequipo1:
                    if partido['equipo2']==nomequipo2:
                        resultado = 'El resultado de este partido fue: '+nomequipo1+': '+ partido['goles1']+' - '+nomequipo2+': '+partido['goles2'] 
                        return resultado
        return 'No existe el resultado'
    
    def goles (self, equipo1, year1,year2):
        temporada = str(year1) + '-' + str(year2)
        for partido in objPartidos:
            if partido['temporada'] == temporada:
                if partido['equipo1']== equipo1:
                        cantgoles= partido['goles1']
                        #resultado = 'El resultado de este partido fue: '+nomequipo1+': '+ partido['goles1']+' - '+nomequipo2+': '+partido['goles2'] 
                        return cantgoles
        return 'No existe el resultado'

def Pruebita():
        g = Analizador()
        #cadena = 'JORNADA82TEMPORADA<2019-2020>'
        #g.AnalisisLexico(cadena)
        cadena ='GOLESTOTAL"Real Madrid"TEMPORADA<1998-1999>'
        g.AnalisisLexico(cadena)
        g.AnalizadorSintactico()
        g.impTokens()
        #g.reporteErrores()
        #g.imprimirDatos()
        g.impErrores()
        

#Pruebita()
