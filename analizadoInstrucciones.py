class Simbolo:

    def __init__(self, token, lexema, linea, columna):
        self.token = token
        self.lexema = lexema
        self.linea = linea
        self.columna = columna


class Instruccion:
    def __init__(self,nombre,valor):
        self.nombre = nombre 
        self.valor = valor




#se almacenan los símbolos objetos 
tablaSimbolos = []
#se almacenan las intrucciones
listaInstrucciones = []
listaErrores = []
fila = 0
columna = 0
flagExpresionId = False
flagExpresionCadena = False
valor = ""
estado = 0


flagAutomataInicio = False
nombreTemporal = ""

#para mostrar errores 
def mostrarError(simbolo, expectativa, linea, columna):
    global listaErrores
    msgError = "Error, no se reconoce el simbolo: " + simbolo + ", se esperaba: " +  expectativa + " linea: " + str(linea) + ", columna: " + str(columna)
    print(msgError)
    listaErrores.append(msgError)


def isLetter(c):
    return (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122)


def isNumber(c):
    return (ord(c) >= 48 and ord(c) <= 57)


def expresionRegularId(c):
    #valor como string, columna = 0, fila =0, flagExpresionId bool
    global valor, columna, fila, flagExpresionId

    if isLetter(c) or isNumber(c):
        valor += c
        columna += 1
        return;
    elif ord(c) == 32:
        valor += c
        columna += 1
        tablaSimbolos.append(
            Simbolo("ID", valor, fila, (columna - 1 - len(valor))))
        valor = ""
        flagExpresionId = False
    elif ord(c) == 61:
        tablaSimbolos.append(
            Simbolo("ID", valor, fila, (columna - len(valor))))
        columna += 1
        tablaSimbolos.append(
            Simbolo("simbolo_igual", "=", fila, (columna - 2)))
        valor = ""
        flagExpresionId = False
    elif ord(c) == 58:
        tablaSimbolos.append(
            Simbolo("ID", valor, fila, (columna - len(valor))))
        columna += 1
        tablaSimbolos.append(
            Simbolo("simbolo_dos_puntos", ":", fila, (columna - 2)))
        valor = ""
        flagExpresionId = False
    else:
        mostrarError(c, "", fila, columna)
print (tablaSimbolos)


def expresionRegularCadena(c):
    global valor, columna, fila, flagExpresionCadena

    if ord(c) == 34:
        columna += 1
        valor += c
        tablaSimbolos.append(
            Simbolo("CADENA", valor, fila, (columna - 1 - len(valor))))
        valor = ""
        flagExpresionCadena = False
        return;

    columna += 1
    valor += c


def analizadorLexico(c):
    global fila, columna, flagExpresionId, valor, flagExpresionCadena, valor
    if flagExpresionId:
        expresionRegularId(c)
    elif flagExpresionCadena:
        expresionRegularCadena(c)
    elif isLetter(c):
        columna += 1
        flagExpresionId = True
        valor = c
    elif ord(c) == 34:  # ""
        flagExpresionCadena = True
        valor = c
        columna += 1
    elif ord(c) == 60:  # <
        columna += 1
        valor = c
        tablaSimbolos.append(
            Simbolo("simbolo_menor_que", c, fila, (columna - 2)))
        valor = ""
    elif ord(c) == 62:  # >
        columna += 1
        valor = c
        tablaSimbolos.append(
            Simbolo("simbolo_mayor_que", c, fila, (columna - 2)))
        valor = ""
    elif ord(c) == 168 or ord(c) == 191: #¿
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_pregunta_abre",c,fila,(columna - 2)))
        valor = ""
    elif ord(c) == 63: #?
        columna += 1
        valor = c
        tablaSimbolos.append(Simbolo("simbolo_pregunta_cierra",c,fila,(columna - 2)))
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
    global tablaAtributos,estado,flagAutomataInicio,nombreTemporal,listaInstrucciones
    
    if estado == 1:
        if s.token == "simbolo_pregunta_abre" :
            listaInstrucciones = []
            estado = 2 
        else :
            estado = -1
            flagAutomataInicio = False
            mostrarError(s.lexema,"¿",s.linea,s.columna)

    elif estado == 2:
        if s.token == "ID":
            nombreTemporal = s.lexema
            estado = 3
        else :
            estado = -1
            flagAutomataInicio = False
            mostrarError(s.lexema,"ID",s.linea,s.columna)
    
    elif estado == 3:
        if s.token == "simbolo_dos_puntos":
            estado = 4
        else :
            estado = -1
            flagAutomataInicio = False
            mostrarError(s.lexema,":",s.linea,s.columna)

    elif estado == 4: 
        if s.token == "CADENA" :
            estado = 5
            listaInstrucciones.append(Instruccion(nombreTemporal,s.lexema))
        else :
            estado = -1
            flagAutomataInicio = False
            mostrarError(s.lexema,"CADENA",s.linea,s.columna) 
    elif estado == 5:
        if s.token == "simbolo_coma" : 
            estado = 2 
        elif s.token == "simbolo_pregunta_cierra": 
            estado = 6
        else :
            estado = -1
            flagAutomataInicio = False
            mostrarError(s.lexema,", o ?",s.linea,s.columna) 
    elif estado == 6:
        if s.token == "simbolo_mayor_que": 
            estado = -1 
            flagAutomataInicio = False 
        else :
            estado = -1
            flagAutomataInicio = False
            mostrarError(s.lexema,">",s.linea,s.columna) 
      




def analizarInstruccion(cadena):
    global tablaAtributos,estado,flagAutomataInicio,listaErrores,tablaSimbolos,fila,columna,listaInstrucciones
    tablaSimbolos = []
    fila = 0
    columna = 0
    listaErrores = []

    caracteres = list(cadena)
    for c in caracteres:
        analizadorLexico(c)

    #for s in tablaSimbolos:
    #    print(s.token + ": " + s.lexema)

    
    for s in tablaSimbolos:
        if flagAutomataInicio:
            automataInicio(s)
        elif s.token == "simbolo_menor_que":
            estado = 1 
            flagAutomataInicio = True
        else:
            mostrarError(s.lexema,"<",s.linea,s.columna)

    #for a in listaInstrucciones:
        #print(a.nombre,a.valor)

    return {"data":listaInstrucciones,"errores":listaErrores}


