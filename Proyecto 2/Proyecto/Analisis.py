from Token import Token
from Token import Error
from prettytable import PrettyTable


class Analizador():
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        
    
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
        
        estado = 0
        option = True
        for caracter in cadena:            
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
                            self.agregar_error(self.buffer,'Error Lexico',self.linea,self.columna)
                            
                        
                elif estado == 1:
                    option=False
                    if caracter.isupper():
                        self.buffer+=caracter
                    #if caracter != '"':
                    #if caracter.isalpha():
                     #   self.buffer+= caracter                       
                    #if caracter.isdigit():
                     #   self.buffer+=caracter                       
                    #elif caracter== '_' or caracter=='!' or caracter == ' ' or caracter =='¿' or caracter =='?':
                     #   self.buffer+=caracter
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
                
                elif estado == 2:
                    option=False
                    if caracter!='<':                           
                        if caracter.isdigit() :  
                            self.buffer+= caracter
                            if len(self.buffer)== 4:                      
                                self.agregar_token(self.buffer, 'Año 1',self.linea, self.columna )
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
                        
                
                elif estado == 3:                    
                    option=False
                    if caracter=="-":
                        self.buffer+= caracter 
                        if caracter =='f' or caracter == 'n' or caracter == 'j' or caracter.isdigit():
                            self.agregar_token(self.buffer, 'indicacion esp.',self.linea, self.columna )
                        else:
                            self.agregar_error(self.buffer,'Error Lexico',self.linea,self.columna)                        
                            estado=0
                                               
                    else: 
                        self.agregar_token(self.buffer, 'Grupo', self.linea, self.columna)
                        self.columna+=1
                        self.agregar_token("'", 'Comilla simple',self.linea, self.columna )
                        estado=0
                
                elif estado == 4:
                    option=False
                    if caracter!='"':
                        self.buffer+= caracter                        
                    else: 
                        self.agregar_token(self.buffer, 'nombre equipo', self.linea, self.columna)
                        self.columna +=1
                        self.agregar_token('"', 'Comilla Doble',self.linea, self.columna )
                        estado=0
                        
                elif estado == 5:
                    option=False  
                    
                    #print (caracter)                  
                    if caracter.isdigit():
                        self.buffer+= caracter
                        #print(self.buffer)
                        if  len(self.buffer) == 2 :                            
                            self.listaTokens.pop()                           
                            self.agregar_token(self.buffer, 'numero jornada', self.linea, self.columna)                             
                            estado=5   
                        else: 
                            self.agregar_error(self.buffer,'jornada no válida',self.linea,self.columna)                        
                            estado=0  
                        '''elif caracter.isupper():
                         self.agregar_token(self.buffer, 'numero jornada', self.linea, self.columna)
                         estado =1 '''
                    elif  caracter.isupper():
                        self.buffer+= caracter
                        #self.agregar_token(self.buffer, 'numero jornada', self.linea, self.columna) 
                        estado=1 
                    else:
                        self.buffer+=caracter 
                        self.agregar_error(self.buffer,'jornada no válida',self.linea,self.columna)                        
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
    
    #cadena = 'RESULTADO"Real Madrid"VS"Villarreal"TEMPORADA <2019-2020>'
    #AnalisisLexico(cadena)
    #impTokens()

def Pruebita():
        g = Analizador()
        cadena = 'JORNADA888882TEMPORADA<2019-2020>'
        g.AnalisisLexico(cadena)
        #g.AnalisisLexico(cadena)
        g.impTokens()
        #g.imprimirDatos()
        g.impErrores()

Pruebita()
