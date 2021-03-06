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
                        self.agregar_token(self.buffer, 'Instrucci??n', self.linea, self.columna)
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
      <INPUT type="radio" name="sexo" value="Var??n"> Var??n<BR>
      <INPUT type="radio" name="sexo" value="Mujer"> Mujer<BR>
    </fieldset>
    <fieldset>
      <p>

        Pa??s:
      
        <select>
      
          <optgroup label="pa??s">
      
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
        
    #Pseudo Ananlizador Sint??ctico
    def creacionFormulario(self):
        global copiaTok
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
                             
                            self.estadoRecursivo()
                            
    def estadoRecursivo(self):
        
        if copiaTok[0].lexema == '<':
            copiaTok.pop(0) 
            if copiaTok[0].lexema == 'tipo':
                copiaTok.pop(0)
                if copiaTok[0].lexema == 'etiqueta'or  copiaTok[0].lexema == 'label':
                    copiaTok.pop(0)
                    if copiaTok[0].lexema==',':                    
                        copiaTok.pop(0)
                        self.opEtiqueta(copiaTok)
                elif copiaTok[0].lexema == 'texto' or copiaTok[0].lexema == 'input':
                    copiaTok.pop(0)                   
                    if copiaTok[0].lexema==',':
                        copiaTok.pop(0)  
                        self.opInput()                
                elif copiaTok[0].lexema == 'grupo-radio' or copiaTok[0].lexema == 'grupo de  input  de  tipo  radio':
                    copiaTok.pop(0)                    
                    if copiaTok[0].lexema==',':
                        copiaTok.pop(0)
                        self.opRadio()
                elif copiaTok[0].lexema == 'grupo-option' or copiaTok[0].lexema == 'select  con  respectivos  option':
                    copiaTok.pop(0)
                    if copiaTok[0].lexema==',':                        
                        copiaTok.pop(0)
                        self.opOption(copiaTok)
                elif copiaTok[0].lexema == 'boton' or copiaTok[0].lexema == 'button':
                    copiaTok.pop(0)
                    if copiaTok[0].lexema==',':
                        copiaTok.pop(0)  
                        self.opBoton()
                if copiaTok[0].lexema == '>':
                    copiaTok.pop(0)
                    if copiaTok[0].lexema==',':
                        copiaTok.pop(0)
                        self.estadoRecursivo()
                    elif copiaTok[0].lexema == ']':
                        print("Terminado")
                            
                        
                
    def opEtiqueta(self,copiaTok):
        '''<fieldset>
      <label for ="nombre">Nombre:</label>
      <input placeholder="Ingresa tu nombre" type="text" tabindex="1" required autofocus>
    </fieldset>'''
        
        global formularioIntermedio
        formularioIntermedio += """ 
        <fieldset>
        <label for ="nombre">       
        """
        if copiaTok[0].lexema =='valor':
            copiaTok.pop(0)
            if copiaTok[0].tipo =='Instrucci??n':                
                formularioIntermedio+= copiaTok[0].lexema + "\n" +"</label></fieldset> \n" 
                copiaTok.pop(0)

    def opInput(self):
        '''<fieldset>
      <label for ="nombre">Nombre:</label>
      <input placeholder="Ingresa tu nombre" type="text" tabindex="1" required autofocus>
    </fieldset>'''
        
        global formularioIntermedio
        formularioIntermedio += """ 
        <fieldset>
        <label for ="nombre">     
        """
        if copiaTok[0].lexema =='valor':
            copiaTok.pop(0)
            if copiaTok[0].tipo =='Instrucci??n':
                formularioIntermedio+= copiaTok[0].lexema + "\n" +"</label></fieldset> \n" 
                copiaTok.pop(0)
                if copiaTok[0].lexema==',':
                    copiaTok.pop(0)
                    if copiaTok[0].lexema =='fondo':
                        #global formularioIntermedio
                        formularioIntermedio += """ 
                        <fieldset>
                        <input placeholder="     
                        """      
                        copiaTok.pop(0)
                        if copiaTok[0].tipo =='Instrucci??n':            
                            formularioIntermedio+= copiaTok[0].lexema + "\n" +'" type="text" tabindex="1" required autofocus></fieldset> \n'
                            copiaTok.pop(0)   
        elif copiaTok[0].lexema =='fondo':
            #global formularioIntermedio
            formularioIntermedio += """ 
            <fieldset>
            <input placeholder="     
            """      
            copiaTok.pop(0)
            if copiaTok[0].tipo =='Instrucci??n':            
                formularioIntermedio+= copiaTok[0].lexema + "\n" +'" type="text" tabindex="1" required autofocus></fieldset> \n'
                copiaTok.pop(0)   
                       
    
    def opRadio(self):
        '''<fieldset>
      <label for ="nombre">Sexo:</label><br>
      <INPUT type="radio" name="sexo" value="Var??n"> Var??n<BR>
      <INPUT type="radio" name="sexo" value="Mujer"> Mujer<BR>
    </fieldset>'''
        global formularioIntermedio
        formularioIntermedio += """ 
        <fieldset>
        <label for ="nombre">       
        """
        if copiaTok[0].lexema =='nombre':
            copiaTok.pop(0)
            if copiaTok[0].tipo =='Instrucci??n':
                formularioIntermedio+= copiaTok[0].lexema + "\n" +"</label><br> \n" 
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
                                    formularioIntermedio+= '<INPUT type="radio" name="sexo" value="Var??n">'+ copiaTok[0].lexema+'<BR> \n'
                                    copiaTok.pop(0)
                                    if copiaTok[0].lexema ==',':
                                        copiaTok.pop(0)
                                    else: 
                                        validacion=False 
                            if copiaTok[0].lexema ==']':
                                formularioIntermedio+="""
                                      </fieldset>"""
                                copiaTok.pop(0)                                
                                pass               
    def opOption(self,copiaTok):
        '''<fieldset>
      <p>

        Pa??s:
      
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
            if copiaTok[0].tipo =='Instrucci??n':
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
                                      </fieldset>"""
                                copiaTok.pop(0)                                
                                pass

    def opBoton(self):
        '''<fieldset>
      <button name="submit" type="submit" id="contact-submit" data-submit="...Sending">Valor</button>
    </fieldset>'''
        
        global formularioIntermedio
        
        if copiaTok[0].lexema =='valor':
            copiaTok.pop(0)
            if copiaTok[0].tipo =='Instrucci??n':
                print('Hola')
                #formularioIntermedio+=  
                #copiaTok.pop(0)
                if copiaTok[1].lexema == ',':
                    copiaTok.pop(1)
                    if copiaTok[1].lexema == 'evento':
                        copiaTok.pop(1)
                        if copiaTok[1].lexema == 'entrada':
                            formularioIntermedio += """ 
                            <fieldset>
                            
                            <button name="submit" type="submit" id="contact-submit" data-submit="...Sending" >     
                            """
                            formularioIntermedio+= copiaTok[0].lexema + "\n" +"</button></fieldset> \n" 
                            formularioIntermedio += """ 
                            <fieldset>
                            <div class="container"> 
                            <iframe class="responsive-iframe" src="https://www.youtube.com/embed/tgbNymZ7vqY"></iframe>
                            </div>   
                                """
                        elif copiaTok[1].lexema != 'entrada':
                            formularioIntermedio += """ 
                            <fieldset>
                            
                            <button name="submit" type="submit" id="contact-submit" data-submit="...Sending" >     
                            """
                            formularioIntermedio+= copiaTok[0].lexema + "\n" +"</button></fieldset> \n" 
                            copiaTok.pop(1)
                            copiaTok.pop(0)
                
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
        
        <style>
        @import url(https://fonts.googleapis.com/css?family=Open+Sans:400italic,400,300,600);

        * {
                margin:0;
                padding:0;
                box-sizing:border-box;
                -webkit-box-sizing:border-box;
                -moz-box-sizing:border-box;
                -webkit-font-smoothing:antialiased;
                -moz-font-smoothing:antialiased;
                -o-font-smoothing:antialiased;
                font-smoothing:antialiased;
                text-rendering:optimizeLegibility;
        }
        
        body {
                font-family:"Open Sans", Helvetica, Arial, sans-serif;
                font-weight:300;
                font-size: 12px;
                line-height:30px;
                color:#000000;
                background:#C0C0C0;
        }
        
        .container {
                max-width:400px;
                width:100%;
                margin:0 auto;
                position:relative;
        }
        
        #contact input[type="text"], #contact input[type="email"], #contact input[type="tel"], #contact input[type="url"], #contact textarea, #contact button[type="submit"] { font:400 12px/16px "Open Sans", Helvetica, Arial, sans-serif; }
        
        #contact {
                background:#eeb0e9;
                padding:25px;
                margin:50px 0;
        }
        
        #contact h3 {
                color: #F96;
                display: block;
                font-size: 30px;
                font-weight: 400;
        }
        
        #contact h4 {
                margin:5px 0 15px;
                display:block;
                font-size:13px;
        }
        
        fieldset {
                border: medium none !important;
                margin: 0 0 10px;
                min-width: 100%;
                padding: 0;
                width: 100%;
        }
        
        #contact input[type="text"], #contact input[type="email"], #contact input[type="tel"], #contact input[type="url"], #contact textarea {
                width:100%;
                border:1px solid #CCC;
                background:#FFF;
                margin:0 0 5px;
                padding:10px;
        }
        
        #contact input[type="text"]:hover, #contact input[type="email"]:hover, #contact input[type="tel"]:hover, #contact input[type="url"]:hover, #contact textarea:hover {
                -webkit-transition:border-color 0.3s ease-in-out;
                -moz-transition:border-color 0.3s ease-in-out;
                transition:border-color 0.3s ease-in-out;
                border:1px solid #AAA;
        }
        
        #contact textarea {
                height:100px;
                max-width:100%;
                resize:none;
        }
        
        #contact button[type="submit"] {
                cursor:pointer;
                width:100%;
                border:none;
                background:#0CF;
                color:#FFF;
                margin:0 0 5px;
                padding:10px;
                font-size:15px;
        }
        
        #contact button[type="submit"]:hover {
                background:rgb(16, 146, 16);
                -webkit-transition:background 0.3s ease-in-out;
                -moz-transition:background 0.3s ease-in-out;
                transition:background-color 0.3s ease-in-out;
        }
        
        #contact button[type="submit"]:active { box-shadow:inset 0 1px 3px rgba(0, 0, 0, 0.5); }
        
        #contact input:focus, #contact textarea:focus {
                outline:0;
                border:1px solid #999;
        }
        ::-webkit-input-placeholder {
            color:#888;
        }
        :-moz-placeholder {
            color:#888;
        }
        ::-moz-placeholder {
            color:#888;
        }
        :-ms-input-placeholder {
            color:#888;
        }
    </style>
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