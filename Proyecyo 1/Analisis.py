from TE import Token
from TE import Error
from prettytable import PrettyTable
import webbrowser

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
        for error in self.listaErrores:
            error.getError()
    #tengo que crear mi objeto Token first
    def agregar_token(self,caracter,token,linea,columna):
        self.listaTokens.append(Token(caracter,token,linea,columna))
        self.buffer = ''

    #tengo que crear mi objeto Error first
    def agregar_error(self,caracter,descripcion,linea,columna):
        self.listaErrores.append(Error( caracter, descripcion, linea, columna))
        self.buffer=''
        
    
    #Análisis Léxico 
    def AnalisisLexico(self,cadena):
        text = cadena + '$'
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
                    elif caracter =='$':
                        print("Archivo leído con éxito")
                    elif caracter.isalpha():
                        self.buffer+= caracter
                        self.columna+=1
                        estado = 1
                    elif caracter=='"':
                        self.buffer+= caracter
                        self.columna+=1
                        estado = 2
                    else:
                        self.buffer += caracter
                        self.agregar_error(self.buffer,'Error Lexico',self.linea,self.columna)
                        self.buffer = ''
                        self.columna += 1 
                elif estado== 1:
                    option =False
                    '''if ord (caracter)!=97 and ord (caracter)!=98 and ord (caracter)!=99 and ord (caracter)!=100 and ord (caracter)!=101 and ord (caracter)!=102 and ord (caracter)!=103 and ord (caracter)!=104 and ord (caracter)!=105 and ord (caracter)!=106 and ord (caracter)!=107 and ord (caracter)!=108 and ord (caracter)!=109 and ord (caracter)!=110 and ord (caracter)!=111 and ord (caracter)!=112 and ord (caracter)!=113 and ord (caracter)!=114 and ord (caracter)!=115 and ord (caracter)!=116 and ord (caracter)!=117 and ord (caracter)!=118 and ord (caracter)!=119 and ord (caracter)!=120 and ord (caracter)!=121 and ord (caracter)!=122:
                        self.buffer += caracter
                            self.agregar_error(self.buffer,'Error Lexico',self.linea,self.columna)
                            self.buffer = ''
                            self.columna += 1 
                            self.estado = 0'''
                        
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
                        '''elif  ord (caracter)!=97 and ord (caracter)!=98 and ord (caracter)!=99 and ord (caracter)!=100 and ord (caracter)!=101 and ord (caracter)!=102 and ord (caracter)!=103 and ord (caracter)!=104 and ord (caracter)!=105 and ord (caracter)!=106 and ord (caracter)!=107 and ord (caracter)!=108 and ord (caracter)!=109 and ord (caracter)!=110 and ord (caracter)!=111 and ord (caracter)!=112 and ord (caracter)!=113 and ord (caracter)!=114 and ord (caracter)!=115 and ord (caracter)!=116 and ord (caracter)!=117 and ord (caracter)!=118 and ord (caracter)!=119 and ord (caracter)!=120 and ord (caracter)!=121 and ord (caracter)!=122:                            
                            self.buffer += caracter
                            self.agregar_error(self.buffer,'Error Lexico',self.linea,self.columna)
                            self.buffer = ''
                            self.columna += 1 
                            self.estado = 0'''
                elif estado == 2:
                    option = False
                    if caracter == '"':
                        self.buffer+=caracter
                        self.columna+=1
                    elif caracter.isalpha() or caracter== ':'or caracter== ' 'or caracter== '@'or caracter== '?'or caracter== '¿'or caracter== '*'or caracter== '+'or caracter== '_'or caracter== ','or caracter== '<'or caracter== '>'or caracter== '-'or caracter== '%'or caracter== '!'or caracter== '¡'or caracter== '#':
                        self.buffer+=caracter
                        self.columna+=1
                    else:
                        self.agregar_token(self.buffer,'instruccion', self.linea,self.columna)
                        estado= 0
                        self.columna+=1  
                '''else:
                    self.buffer += caracter
                    self.agregar_error(self.buffer,'Error Lexico',self.linea,self.columna)
                    self.buffer = ''
                    self.columna += 1  '''                                                 
                    
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
        if len(self.listaErrores)==0:
            print('No hay errores')
        else:
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

