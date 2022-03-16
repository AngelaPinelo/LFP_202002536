class Token:
    def __init__ (self,lexema,tipo,linea,columna):
        self.lexema = lexema
        self.linea = linea
        self.columna = columna
        self.tipo = tipo
        
    def enviarDataTok(self):
        return [self.lexema, self.tipo, self.linea, self.columna]
    
    def getTok(self):
        
        print('\n *****************')
        print('Tipo:', self.tipo)
        print('Lexena:', self.lexema)
        print('Linea:', self.linea)
        print('Columna:', self.columna)
        
class Error :
    def __init__ (self,tipo,descripcion, linea,columna):
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna
        self.tipo = tipo
        
    def enviarDataError(self):
        return [self.descripcion, self.tipo, self.linea, self.columna]
    
    def getTok(self):
        
        print('\n *****************')
        print('Tipo:', self.tipo)
        print('Descripcion:', self.descripcion)
        print('Linea:', self.linea)
        print('Columna:', self.columna)
                                