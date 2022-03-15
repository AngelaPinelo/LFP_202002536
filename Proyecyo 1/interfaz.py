import tkinter
from tkinter import *
import sys
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox

#ventana y botones-------------------------------

ventana = tkinter.Tk()
ventana.title('Formularios')
ventana.geometry("900x620")
ventana.config(bg="sky blue")
ventana.iconbitmap("corazon.ico")

boton1 = tkinter.Button(ventana, text = "Cargar",  command = lambda: leerArchivo())
boton2 = tkinter.Button(ventana, text = "Analizar")
boton3 = tkinter.Button(ventana, text = "Imagenes y reportes")

boton5 = tkinter.Button(ventana, text = "Original")
boton6 = tkinter.Button(ventana, text = "Mirror X")
boton7 = tkinter.Button(ventana, text = "Mirror Y")
boton8 = tkinter.Button(ventana, text = "Double Mirror")
boton4 = tkinter.Button(ventana, text = "Salir")

boton1.pack()
#boton1.place(height=100, width=250, x = 0, y = 0)
boton2.pack()
#boton2.place(height=100, width=250, x = 5, y = 0)
boton3.pack()
#boton3.place(height=100, width=250, x = 10, y = 0)

#boton4.place(height=100, width=250,x = 15, y = 0)
boton5.pack()
boton6.pack()
boton7.pack()
boton8.pack()
boton4.pack()
boton5.place(height=100, width=250, x = 20, y = 0)


#área de Texto 
areaText=Text(ventana, text="Información")


diccionario = {}
#funciones---------------------------------------
def leerArchivo():
    Tk().withdraw()
    entrada = askopenfilename(filetypes=[("Archivos PXLA", "*.pxla"), ("All Files", "*.*")])
    archivo = open(entrada, 'r')
    global contenido
    contenido = archivo.read()
    archivo.close()
    return contenido

ventana.mainloop()

