import re
tokens=[]

#ANÁLISIS LÉXICO
def AnalisiLexico(text):
    temp_anterior="" 
    temp = ""
    estado = 0
    option = True
    for sonnic in text:
        option = True
        while option:
            if estado == 0:
                option=False
                if re.search(r'(\:)',sonnic):
                    temp_token=[]
                    temp_token.append("token_puntos")
                    temp_token.append(sonnic)
                    tokens.append(temp_token)
                    temp = ""
                elif re.search(r'[=]',sonnic):
                    temp_token=[]
                    temp_token.append("token_eq")
                    temp_token.append(sonnic)
                    tokens.append(temp_token)
                    temp = ""
                elif re.search(r'[(]',sonnic):
                    temp_token=[]
                    temp_token.append("token_pa")
                    temp_token.append(sonnic)
                    tokens.append(temp_token)
                    temp = ""
                elif re.search(r'[)]',sonnic):
                    temp_token=[]
                    temp_token.append("token_pc")
                    temp_token.append(sonnic)
                    tokens.append(temp_token)
                    temp = ""
                elif re.search(r'(\[)',sonnic):
                    temp_token=[]
                    temp_token.append("token_ca")
                    temp_token.append(sonnic)
                    tokens.append(temp_token)
                    temp = ""
                elif re.search(r'(\,)',sonnic):
                    temp_token=[]
                    temp_token.append("token_coma")
                    temp_token.append(sonnic)
                    tokens.append(temp_token)
                    temp = ""
                elif re.search(r'(\])',sonnic):
                    temp_token=[]
                    temp_token.append("token_cc")
                    temp_token.append(sonnic)
                    tokens.append(temp_token)
                    temp = ""
                elif re.search(r'(\;)',sonnic):
                    temp_token=[]
                    temp_token.append("token_semi")
                    temp_token.append(sonnic)
                    tokens.append(temp_token)
                    temp = ""
                elif re.search(r'(")',sonnic):
                    temp+=sonnic
                    estado =1 
                elif re.search(r'[0-9]',sonnic):
                    temp+=sonnic
                    estado =2
                elif re.search(r'[a-zA-Z]',sonnic):
                    temp+=sonnic
                    estado =3
            elif estado== 1:
                option =False
                if sonnic != "\"":
                    temp+=sonnic
                else:
                    temp+=sonnic
                    temp_token=[]
                    temp_token.append("token_producto")
                    temp_token.append(temp)
                    tokens.append(temp_token)
                    temp = ""
                    estado =0
                
            elif estado== 2:
                option =False
                if  re.search(r'[0-9]',sonnic):
                    temp +=sonnic 
                elif re.search(r'(\.)',sonnic):
                    temp+= sonnic
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
                if re.search(r'[a-zA-Z]',sonnic):
                    temp+= sonnic 
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
                if  re.search(r'[0-9]',sonnic):
                    temp +=sonnic 
                    estado = 5 
            elif estado== 5:
                option =False
                if  re.search(r'[0-9]',sonnic):
                    temp +=sonnic 
                else:
                    temp_token=[]
                    temp_token.append("token_decimal")
                    temp_token.append(temp)
                    tokens.append(temp_token)
                    temp = ""
                    estado = 0
                    option =True
            else:
                if ord(sonnic) == 32 or ord(sonnic) == 10 or ord(sonnic) == 9 :
                    pass
                else:   
                    pass     
    
    Analizador_sintactico()
'''incio = Token_mes Token_pts Token_precent Token_eq Token_pa productos token_pc
ptoductos = token_ca token_profucto token_coma num token_coma token_precent token_cc token_semi proctos'
productos' = ptoductos  | nada
num = token_precent | token_decimal'''
 


def Analizador_sintactico():
    global Nombre_mes
    global year
    
    if(tokens[0][0] == "token_mes"):
        Nombre_mes = tokens[0][1]
        tokens.pop(0)

        if(tokens[0][0] == "token_pts"):
            tokens.pop(0)

            if(tokens[0][0] == "token_precent"):
                year= tokens[0][1]
                tokens.pop(0)

                if(tokens[0][0] == "token_eq"):
                    tokens.pop(0)

                    if(tokens[0][0] == "token_pa"):
                        tokens.pop(0)
                        productos()

        '''incio =    productos 
ptoductos =  proctos'
productos' = ptoductos  | nada
'''
              
productos = []
def productos():
    producto
    precio
    unidades
    ganancias
 
    while(True):
        temp = []
        if(tokens[0][0] == "token_ca"):
            tokens.pop(0)

            if(tokens[0][0] == "token_profucto"):
                producto =[0][1]
                tokens.pop(0)

                if(tokens[0][0] == "token_coma"):
                    tokens.pop(0)

                    if(tokens[0][0] == "token_precent"):
                        precio = tokens[0][1]
                        tokens.pop(0)

                    elif(tokens[0][0] == "token_decimal"):
                        precio = tokens[0][1]
                        tokens.pop(0)

                        if(tokens[0][0] == "token_pa"):
                            tokens.pop(0)

                            if(tokens[0][0] == "token_coma"):
                                tokens.pop(0)

                                if(tokens[0][0] == "token_precent"):
                                    unidades = tokens[0][1]
                                    ganancias = precio * unidades
                                    tokens.pop(0)

                                    if(tokens[0][0] == "token_cc"):
                                        tokens.pop(0)

                                        if(tokens[0][0] == "token_semi"):
                                            tokens.pop(0)
                                            temp.append(producto)
                                            temp.append(ganancias)
                                            productos.append(temp)

                                            if(tokens[0][0] == "token_pc"):
                                                break
    print(productos)
                                            
                                            

                                    


                                          



                     


      

def UbicarToken(texto):
    pass
    
    
def isLetra(txt):
    if((ord(txt) >= 65 and ord(txt) <= 90) or (ord(txt) >= 97 and ord(txt) <= 122) or ord(txt) == 164 or ord(txt) == 165):
        return True
    else:
        return False     