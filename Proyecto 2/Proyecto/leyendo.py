class Leer():
    def leer (ruta):
        with open(ruta, encoding='utf-8') as archivo:
            global contenido
            contenido = archivo.read()              
            return contenido

    
    
    
    file = open("Manual usuario LFP P2.pdf",'r')
        
     
    
    
    contenido2 = leer(r'LaLigaBot-LFP.csv')
    partidos = contenido2.split('\n')

    objPartidos = []
    for partido in partidos: 
        datos = partido.split(',')
        p={
        'fecha': datos [0],
        'temporada': datos [1],
        'jornada': datos [2],
        'equipo1': datos [3],
        'equipo2': datos [4],
        'goles1': datos [5],
        'goles2': datos [6]
        }
        objPartidos.append(p)
    #print (objPartidos[2])
    gg='jornada'
    for partido in objPartidos:
        if partido[gg] == '37':
            if partido['equipo1']=='Valencia':
                if partido['equipo2']=='Betis':
                    print ('El Valencia anotó '+partido['goles1']+' Goles')
    
file = open("Manual usuario LFP P2.pdf",'r')