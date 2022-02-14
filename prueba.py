import re
from typing import Tuple 
from Principal import LeerArchivoVentas 

if __name__ =='__main__':

 text = LeerArchivoVentas("archivoentrada.txt") 
 
#producto= re.search(r'(\[).*((")[\s\S]*(")).*(\,).*([0-9]+((\.)[0-9]+)?).*(\,).*[0-9]+.*(\])(\;)',text).group()

tokens=[]

temp_anterior="" 
temp = ""
estado = 0
option = True
#token_mes: [a-zA-Z]+
#ANÁLISIS LÉXICO
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
            
print (tokens)

def UbicarToken(texto):
    pass
    
    
def isLetra(txt):
    if((ord(txt) >= 65 and ord(txt) <= 90) or (ord(txt) >= 97 and ord(txt) <= 122) or ord(txt) == 164 or ord(txt) == 165):
        return True
    else:
        return False     