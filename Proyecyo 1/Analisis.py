from TE import Token
from TE import Error
import re

global tokens
tokens=[]  
class Analizador():
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        self.estado = 0
        self.i = 0
        
    def imprimirDatos(self):
        print ('**************Lista Tokens************')
        for token in self.listaTokens:
            token.getTok()
    #tengo que crear mi objeto Token first
    def agregar_token(self,caracter,token,linea,columna):
        self.listaTokens.append(Token(caracter,token,linea,columna))
        self.buffer = ''

    #tengo que crear mi objeto Error first
    def agregar_error(self,caracter,linea,columna):
        self.listaErrores.append(Error('Caracter ' + caracter + ' no reconocido.', linea, columna))
        
    
    #Análisis Léxico 
    def AnalisisLexico(self,cadena):
        text = cadena + '$'
        temp = ""
        estado = 0
        option = True
        for caracter in text:
            option = True
            while option:
                if estado == 0:
                    option=False
                    if caracter == '~':
                        self.buffer+=caracter
                        self.columna+=1
                        #acá ya agrego a la lista de tokens y a los tokens, ya en agregar token se reinicia el buffer y mi estado sigue en 0 so ok 
                        self.agregar_token(self.buffer, 'Virgulilla', self.linea, self.columna)
                    elif caracter == '\n':
                        self.linea += 1
                        self.columna = 1
                    elif caracter in ['\t',' ']:
                        self.columna += 1
                    elif caracter == '>':
                        self.buffer+= caracter
                        self.columna+=1
                        self.agregar_token(self.buffer, 'Mayor que', self.linea, self.columna)
                    elif caracter == '<':
                        self.buffer+= caracter
                        self.columna+=1
                        self.agregar_token(self.buffer, 'Menor que', self.linea, self.columna)
                    elif caracter == ',':
                        self.buffer+= caracter
                        self.columna+=1
                        self.agregar_token(self.buffer, 'Coma', self.linea, self.columna)
                    elif caracter == ':':
                        self.buffer+= caracter
                        self.columna+=1
                        self.agregar_token(self.buffer, 'Dos Puntos', self.linea, self.columna)
                    elif caracter == '[':
                        self.buffer+= caracter
                        self.columna+=1
                        self.agregar_token(self.buffer, 'Corchete abre', self.linea, self.columna)
                    elif caracter == ']':
                        self.buffer+= caracter
                        self.columna+=1
                        self.agregar_token(self.buffer, 'Corchete cierra', self.linea, self.columna)
                    elif caracter.isalpha():
                        self.buffer+= caracter
                        self.columna+=1
                        estado = 1
                elif estado== 1:
                    option =False
                    if caracter.isalpha():
                        self.buffer+= caracter
                        self.columna+=1
                    else:
                        if self.buffer == 'formulario':
                            self.agregar_token(self.buffer,'Palabra reservada', self.linea,self.columna)
                            estado = 0
                        elif self.buffer == 'tipo':
                            self.agregar_token(self.buffer,'identificador', self.linea,self.columna)
                            estado = 0
                        elif self.buffer == 'valor':
                            self.agregar_token(self.buffer,'identificador', self.linea,self.columna)
                            estado = 0
                        elif self.buffer == 'fondo':
                            self.agregar_token(self.buffer,'identificador', self.linea,self.columna)
                            estado = 0
                        elif self.buffer == 'valores':
                            self.agregar_token(self.buffer,'identificador', self.linea,self.columna)
                            estado = 0
                        elif self.buffer == 'evento':
                            self.agregar_token(self.buffer,'identificador', self.linea,self.columna)
                            estado = 0
                        self.estado = 0
                        self.columna+=1
                        
                            
                        
                    
                elif estado== 2:
                    option =False
                    if  re.search(r'[0-9]',caracter):
                        temp +=caracter 
                    elif re.search(r'(\.)',caracter):
                        temp+= caracter
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
                    if re.search(r'[a-zA-Z]',caracter):
                        temp+= caracter 
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
                    if  re.search(r'[0-9]',caracter):
                        temp +=caracter 
                        estado = 5 
                elif estado== 5:
                    option =False
                    if  re.search(r'[0-9]',caracter):
                        temp +=caracter 
                    else:
                        temp_token=[]
                        temp_token.append("token_decimal")
                        temp_token.append(temp)
                        tokens.append(temp_token)
                        temp = ""
                        estado = 0
                        option =True
                else:
                    if ord(caracter) == 32 or ord(caracter) == 10 or ord(caracter) == 9 :
                        pass
                    else:   
                        pass     
        #acá en vez de mandarlo a llamar le debe de ingresar un self
        #Analizador_sintactico()
