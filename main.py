from analizadoInstrucciones import analizarInstruccion 
from analizadorData import analizarData

cadena1 = "<¿ Nombre: \"A\", Apellido: \"B\" ?>"
cadena2 = "Enero: 2020 = {[\"a\",2,2,2,2],[\"b\",2.2,1.2,3,5]}"
print(analizarInstruccion(cadena1))
#print(analizarData(cadena2))