class Leer():
    def leer (ruta):
        with open(ruta, encoding='utf-8') as archivo:
            global contenido
            contenido = archivo.read()              
            return contenido


    contenido2 = leer('LaLigaBot-LFP.csv')
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
    print (objPartidos)
    
   