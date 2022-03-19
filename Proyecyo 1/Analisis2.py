from TE import Token
from TE import Error
from prettytable import PrettyTable
import webbrowser
import copy

global formularioinicio
formularioinicio=""""""
global formularioIntermedio
formularioIntermedio=""""""
global formularioFinal
formularioFinal=""""""
global copiaTok
copiaTok=[]  

class Analizador2():
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
        
    def agregar_error(self,caracter,descripcion,linea,columna):
        self.listaErrores.append(Error( caracter, descripcion, linea, columna))
        self.buffer=''
        
        
    def AnalisisLexico(self,cadena):
        text = cadena + '$'
        print (text)
        estado = 0
        option = True
        for caracter in text:
            #print (caracter)
            self.columna+=1
            option = True
            while option:
                if estado == 0:
                    option=False
                    if caracter == '~':
                        self.buffer+=caracter
                        #self.columna+=1                        
                        self.agregar_token(self.buffer, 'Virgulilla', self.linea, self.columna)
                    elif caracter =='<':
                        self.buffer+=caracter
                        #self.columna+=1                    
                        self.agregar_token(self.buffer, 'Menor que', self.linea, self.columna)
                    elif caracter =='>':
                        self.buffer+=caracter
                        #self.columna+=1                    
                        self.agregar_token(self.buffer, 'Mayor que', self.linea, self.columna)
                    elif caracter =='[':
                        self.buffer+=caracter
                        #self.columna+=1                    
                        self.agregar_token(self.buffer, 'Corchete que abre', self.linea, self.columna)
                    elif caracter ==':':
                        self.buffer+=caracter
                        #self.columna+=1                    
                        self.agregar_token(self.buffer, 'Dos puntos', self.linea, self.columna)
                    elif caracter ==']':
                        self.buffer+=caracter                                           
                        self.agregar_token(self.buffer, 'Corchete que cierra', self.linea, self.columna)
                    elif caracter ==',':
                        self.buffer+=caracter                                          
                        self.agregar_token(self.buffer, 'Coma', self.linea, self.columna)
                    elif caracter.isalpha():
                        self.buffer+= caracter                      
                        estado = 1
                    elif caracter == '"':
                        self.buffer+= caracter                
                        self.agregar_token(self.buffer, 'Comilla Doble', self.linea, self.columna)
                        estado = 2
                    elif caracter == "'":
                        self.buffer+= caracter
                        self.agregar_token(self.buffer, 'Comilla simple', self.linea, self.columna)                
                        estado = 3
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
                    if caracter.isalpha():
                        self.buffer+= caracter                       
                    elif caracter.isdigit():
                        self.buffer+=caracter                       
                    elif caracter== '_':
                        self.buffer+=caracter
                    else: 
                        self.agregar_token(self.buffer, 'Identificador', self.linea, self.columna)
                        estado=0
                        option=True
                
                elif estado == 2:
                    option=False
                    if caracter!='"':
                        self.buffer+= caracter                        
                    else: 
                        self.agregar_token(self.buffer, 'Instrucción', self.linea, self.columna)
                        self.columna +=1
                        self.agregar_token('"', 'Comilla Doble',self.linea, self.columna )
                        estado=0
                        
                
                elif estado == 3:
                    option=False
                    if caracter!="'":
                        self.buffer+= caracter                        
                    else: 
                        self.agregar_token(self.buffer, 'Grupo', self.linea, self.columna)
                        self.columna+=1
                        self.agregar_token("'", 'Comilla simple',self.linea, self.columna )
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
    
    def reporteFormulario(self):
        plantilla3 ="""
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Formulario LFP</title>
  <link rel="stylesheet" href="./style.css">

</head>
<body>
<!-- partial:index.partial.html -->
<div class="container">  
  <form id="contact" action="" method="post">
    <h3>Formulario</h3>
    <fieldset>
      <label for ="nombre">Nombre:</label>
      <input placeholder="Ingresa tu nombre" type="text" tabindex="1" required autofocus>
    </fieldset>
    <fieldset>
      <label for ="nombre">Sexo:</label><br>
      <INPUT type="radio" name="sexo" value="Varón"> Varón<BR>
      <INPUT type="radio" name="sexo" value="Mujer"> Mujer<BR>
    </fieldset>
    <fieldset>
      <p>

        País:
      
        <select>
      
          <optgroup label="país">
      
            <option>Guatema</option>
      
            <option>Honduras</option>
      
            <option>Costa Rica</option>
      
            <option>Panama</option>      
        </select>
      
      </p>
    </fieldset>
    <fieldset>
      <button name="submit" type="submit" id="contact-submit" data-submit="...Sending">Valor</button>
    </fieldset>
  </form>
 
  
</div>
</body>
</html>
        
        """
        file1= open("Formulario.html","w")
        file1.write(plantilla3)
        file1.close()
        webbrowser.open('Formulario.html')
        
    #Pseudo Ananlizador Sintáctico
    def creacionFormulario(self):
        copiaTok=copy.deepcopy(self.listaTokens)
        contador=0
        for a in copiaTok:
            if a.lexema == '"' or a.lexema =="'":
                copiaTok.pop(contador)
            contador +=1
        contador =0
        for a in copiaTok:            
            if a.lexema == ':':
                copiaTok.pop(contador)
            contador +=1
        #print('Verificando si quita comillas y dos puntos')
        #for i in copiaTok:
         #   print(i.lexema)
        
        if copiaTok[0].lexema == 'formulario':
            copiaTok.pop(0)
            if copiaTok[0].lexema == '~':
                copiaTok.pop(0)
                if copiaTok[0].lexema == '>':
                    copiaTok.pop(0)
                    if copiaTok[0].lexema == '>':
                        copiaTok.pop(0)
                        if copiaTok[0].lexema == '[':
                            copiaTok.pop(0)   
                             
                            self.estadoRecursivo(copiaTok)
                            
    def estadoRecursivo(self,copiaTok):
        #for i in copiaTok:
           # print(i.lexema)
        
        if copiaTok[0].lexema == '<':
            copiaTok.pop(0) 
            if copiaTok[0].lexema == 'tipo':
                copiaTok.pop(0)
                #print('********************')
                #for i in copiaTok:
                 #   print(i.lexema)
                if copiaTok[0].lexema == '"etiqueta"'or  copiaTok[0].lexema == '"label"':
                    copiaTok.pop(0)
                   
                    if copiaTok[0].lexema==',':
                        copiaTok.pop(0)
                        
                        #self.opEtiqueta()
                elif copiaTok[0].lexema == '"texto"' or copiaTok[0].lexema == '"input"':
                    copiaTok.pop(0)
                   
                    if copiaTok[0].lexema==',':
                        copiaTok.pop(0)  
                        #self.opinput()                
                elif copiaTok[0].lexema == '"grupo-radio"' or copiaTok[0].lexema == '"grupo de  input  de  tipo  radio"':
                    copiaTok.pop(0)
                    
                    if copiaTok[0].lexema==',':
                        copiaTok.pop(0)
                        #self.opOption()
                elif copiaTok[0].lexema == 'grupo-option' or copiaTok[0].lexema == 'select  con  respectivos  option':
                    copiaTok.pop(0)
                    #for i in copiaTok:
                     #   print(i.lexema, '\n')
                    if copiaTok[0].lexema==',':                        
                        copiaTok.pop(0)
                        self.opOption(copiaTok)
                elif copiaTok[0].lexema == '"boton"' or copiaTok[0].lexema == '"button"':
                    copiaTok.pop(0)
                    if copiaTok[0].lexema==',':
                        copiaTok.pop(0)  
                if copiaTok[0].lexema == '>':
                    copiaTok.pop(0)
                    if copiaTok[0].lexema==',':
                        copiaTok.pop(0)
                        self.estadoRecursivo()
                    elif copiaTok[0].lexema == ']':
                        print("Terminado")
                            
                        
                
    def opEtiqueta(self):
        if copiaTok[0].lexema =='valor':
            copiaTok.pop(0)
            if copiaTok[0].tipo =='instruccion':
                copiaTok.pop(0)
                
    def opOption(self,copiaTok):
        '''<fieldset>
      <p>

        País:
      
        <select>
      
            <option>Guatema</option>
      
            <option>Honduras</option>
      
            <option>Costa Rica</option>
      
            <option>Panama</option>      
        </select>
      
      </p>
    </fieldset>'''
        global formularioIntermedio
        formularioIntermedio += """ 
        <fieldset>
        <p>        
        """
        if copiaTok[0].lexema =='nombre':
            copiaTok.pop(0)
            if copiaTok[0].tipo =='Instrucción':
                formularioIntermedio+= copiaTok[0].lexema + "\n" +"<select> \n" 
                copiaTok.pop(0)
                if copiaTok[0].lexema==',':
                    copiaTok.pop(0)
                    if copiaTok[0].lexema=='valores':
                        copiaTok.pop(0)
                        if copiaTok[0].lexema =='[':
                            copiaTok.pop(0)
                            validacion=True
                            while validacion:                                
                                if copiaTok[0].tipo =='Grupo':
                                    formularioIntermedio+= "<option>"+ copiaTok[0].lexema+"</option> \n"
                                    copiaTok.pop(0)
                                    if copiaTok[0].lexema ==',':
                                        copiaTok.pop(0)
                                    else: 
                                        validacion=False 
                            if copiaTok[0].lexema ==']':
                                formularioIntermedio+="""</select>
      
                                                    </p>
                                                    </fieldset>"""
                                copiaTok.pop(0)                                
                                pass
                            
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
                            
                    
                    
    def crearReporte(self):
        try: 
            textoCompleto= formularioinicio+formularioIntermedio+formularioFinal
            file= open("Formulario.html",'w')
            file.write(textoCompleto)
            webbrowser.open('Formulario.html')
        except:
            pass     

formularioinicio="""
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Formulario LFP</title>
  <link rel="stylesheet" href="./style.css">

</head>
<body>
<!-- partial:index.partial.html -->
<div class="container">  
  <form id="contact" action="" method="post">
  <h3>Formulario</h3>
"""

formularioFinal="""
</form>
</div>
</body>
</html>

"""
