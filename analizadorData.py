import matplotlib
import matplotlib.pyplot as plt
class Simbolo:

    def __init__(self,token,lexema,linea,columna):
        self.token = token 
        self.lexema = lexema 
        self.linea = linea
        self.columna = columna 

class Producto:
    nombre = ""
    valores = []

class Mes:
    nombre = ""
    anio = 0
    productos = []



tablaSimbolos = []
fila = 0
columna = 0
flagExpresionId = False
flagExpresionCadena = False
flagExpresionNumero = False
valor = ""
estado = 0
listaErrores = []


flagAutomataInicio = False#booleano
flagAutomataProducto = False
mesTemporal = Mes()#tupla
productoTemporal = Producto()#tupla

def mostrarError(simbolo, expectativa, linea, columna):
    global listaErrores
    msgError = "Error, no se reconoce el simbolo: " + simbolo + ", se esperaba: " +  expectativa + " linea: " + str(linea) + ", columna: " + str(columna)
    print(msgError)
    listaErrores.append(msgError)

def isLetter(c):
    return (ord(c) >= 65 and ord(c) <= 90) or  (ord(c) >= 97 and ord(c) <= 122)

def isNumber(c):
    return (ord(c) >= 48 and ord(c) <= 57)

def expresionRegularId(c):
    global valor,columna,fila,flagExpresionId
    
    if isLetter(c) or isNumber(c):
        valor += c
        columna += 1
        return;
    elif ord(c) == 32:
        valor += c
        columna += 1
        tablaSimbolos.append(Simbolo("ID",valor,fila,(columna - 1 - len(valor))))
        valor = ""
        flagExpresionId = False
    elif ord(c) == 61:
        tablaSimbolos.append(Simbolo("ID",valor,fila,(columna  - len(valor))))
        columna += 1
        tablaSimbolos.append(Simbolo("simbolo_igual","=",fila,(columna - 2)))
        valor = ""
        flagExpresionId = False
    elif ord(c) == 58:
        tablaSimbolos.append(Simbolo("ID",valor,fila,(columna  - len(valor))))
        columna += 1
        tablaSimbolos.append(Simbolo("simbolo_dos_puntos",":",fila,(columna - 2)))
        valor = ""
        flagExpresionId = False
    else:
        mostrarError(c,"",fila,columna)

def expresionRegularCadena(c):
    global valor,columna,fila,flagExpresionCadena 

    if ord(c) == 34:
        columna += 1
        valor += c 
        tablaSimbolos.append(Simbolo("CADENA",valor,fila,(columna - 1 - len(valor))))
        valor = ""
        flagExpresionCadena = False
        return; 
    
    columna += 1
    valor += c

def expresionRegularNumero(c):
    global columna,fila,flagExpresionNumero,valor
    if isNumber(c) or c == '.':
        columna += 1
        valor += c
        return 

    columna += 1
    tablaSimbolos.append(Simbolo("NUMERO",valor,fila,(columna - 1 - len(valor))))
    valor = ""
    flagExpresionNumero = False
    if ord(c) == 44: #,
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_coma",c,fila,(columna - 2)))
        valor = ""
    elif ord(c) == 93: #]
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_corchete_cierra",c,fila,(columna - 2)))
        valor = ""


def analizadorLexico(c):
    global fila,columna,flagExpresionId,valor,flagExpresionCadena,flagExpresionNumero,valor
    if flagExpresionId:
        expresionRegularId(c)
    elif flagExpresionCadena:
        expresionRegularCadena(c)
    elif flagExpresionNumero:
        expresionRegularNumero(c)
    elif isLetter(c):
        columna += 1
        flagExpresionId = True
        valor = c
    elif isNumber(c):
        columna += 1 
        valor = c
        flagExpresionNumero = True
    elif ord(c) == 61: #=
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_igual","=",fila,(columna - 2)))
        valor = ""
    elif ord(c) == 34: #""
        flagExpresionCadena = True 
        valor = c
        columna += 1
    elif ord(c) == 91: #[
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_corchete_abre",c,fila,(columna - 2)))
        valor = ""
    elif ord(c) == 93: #]
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_corchete_cierra",c,fila,(columna - 2)))
        valor = ""
    elif ord(c) == 123: #{
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_llave_abre",c,fila,(columna - 2)))
        valor = ""
    elif ord(c) == 125: #}
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_llave_cierra",c,fila,(columna - 2)))
        valor = ""
    elif ord(c) == 44: #,
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_coma",c,fila,(columna - 2)))
        valor = ""
    elif ord(c) == 58: # :
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_dos_puntos",c,fila,(columna - 2)))
        valor = ""
    elif ord(c) == 59: #,
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_punto_coma",c,fila,(columna - 2)))
        valor = ""
    elif ord(c) == 10: #salto de linea
        fila += 1
        columna = 0
        valor = ""
    elif ord(c) == 32: #espacio
        columna += 1
        valor = ""
    else: 
        mostrarError(c,"",fila,columna)

def automataInicio(s):
    global tablaAtributos,estado,flagAutomataInicio,mesTemporal,flagAutomataProducto
    
    if estado == 1:
        if s.token == "simbolo_dos_puntos" :
            estado = 2 
        else :
            estado = -1
            flagAutomataInicio = False
            mostrarError(s.lexema,":",s.linea,s.columna)

    elif estado == 2:
        if s.token == "NUMERO":
            mesTemporal.anio = s.lexema
            estado = 3
        else :
            estado = -1
            flagAutomataInicio = False
            mostrarError(s.lexema,"Numero",s.linea,s.columna)
    
    elif estado == 3:
        if s.token == "simbolo_igual":
            estado = 4
        else :
            estado = -1
            flagAutomataInicio = False
            mostrarError(s.lexema,"=",s.linea,s.columna)

    elif estado == 4: 
        if s.token == "simbolo_llave_abre" :
            estado = 0
            flagAutomataProducto = True
            flagAutomataInicio = False
        else :
            estado = -1
            flagAutomataInicio = False
            mostrarError(s.lexema,"{",s.linea,s.columna) 
        
def automataProducto(s):    
    global tablaAtributos,estado,flagAutomataInicio,mesTemporal,flagAutomataProducto
    
    if estado == 0:
        if s.token == "simbolo_corchete_abre" :
            estado = 1
        elif s.token == "simbolo_llave_cierra" :
            estado = -1 
            flagAutomataProducto = False
        else :
            estado = -1
            flagAutomataProducto = False
            mostrarError(s.lexema,"[ o }",s.linea,s.columna)
    
    elif estado == 1:
        if s.token == "CADENA":
            estado = 2 
            productoTemporal.nombre = s.lexema 
            productoTemporal.valores = []
        else :
            estado = -1
            flagAutomataProducto = False
            mostrarError(s.lexema,"cadena",s.linea,s.columna)
    
    elif estado == 2:
        if s.token == "simbolo_coma":
            estado = 3 
        elif s.token == "simbolo_corchete_cierra" :
            estado = 4
        else :
            estado = -1
            flagAutomataInicio = False
            mostrarError(s.lexema,", o ]",s.linea,s.columna)
    
    elif estado == 3:
        if s.token == "NUMERO" :
            estado = 2 
            productoTemporal.valores.append(s.lexema)
        else :
            estado = -1
            flagAutomataInicio = False
            mostrarError(s.lexema,"NUMERO",s.linea,s.columna)
    elif estado == 4:
        if s.token == "simbolo_coma":
            prod = Producto()
            prod.nombre = productoTemporal.nombre
            prod.valores = productoTemporal.valores
            mesTemporal.productos.append(prod)
            estado = 0 
        elif s.token == "simbolo_llave_cierra" :
            prod = Producto()
            prod.nombre = productoTemporal.nombre
            prod.valores = productoTemporal.valores
            mesTemporal.productos.append(prod)
            estado = -1 
            flagAutomataProducto = False
        else :
            estado = -1
            flagAutomataProducto = False
            mostrarError(s.lexema,", o }",s.linea,s.columna)
        

def analizarData(cadena):
    global tablaAtributos,estado,flagAutomataInicio,listaErrores,tablaSimbolos,fila,columna,mesTemporal
    tablaSimbolos = []
    fila = 0
    columna = 0
    listaErrores = []

    caracteres = list(cadena)

    for c in caracteres:
        analizadorLexico(c)

    #for s in tablaSimbolos:
        #print(s.token + ": " + s.lexema)

    for s in tablaSimbolos:
        
        if flagAutomataInicio:
            automataInicio(s)
        elif flagAutomataProducto:
            automataProducto(s)
        elif s.token == "ID":
            mesTemporal.nombre = s.lexema
            estado = 1 
            flagAutomataInicio = True
        else:
            mostrarError(s.lexema,"[",s.linea,s.columna)

    

    #print(mesTemporal.anio,mesTemporal.nombre)
    #for p in mesTemporal.productos:
       #print(p.nombre)
        #for v in p.valores: 
            #print(v)

    return {"data":mesTemporal,"errores":listaErrores}
