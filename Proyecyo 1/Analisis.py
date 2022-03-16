
class Analizador():
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 1
        self.buffer = ''
        self.estado = 0
        self.i = 0
        
    #tengo que crear mi objeto Token first
    def agregar_token(self,caracter,token,linea,columna):
        self.listaTokens.append(Token(caracter,token,linea,columna))
        self.buffer = ''

    #tengo que crear mi objeto Error first
    def agregar_error(self,caracter,linea,columna):
        self.listaErrores.append(Error('Caracter ' + caracter + ' no reconocido.', linea, columna))
        
    
    #Análisis Léxico 
    def AnalisisLexico(self,cadena):
        text = cadena 
        temp = ""
        estado = 0
        option = True