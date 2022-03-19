from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from Analisis import Analizador
from Analisis2 import Analizador2
import sys



def leerArchivo():
    Tk().withdraw()
    entrada = filedialog.askopenfilename(initialdir="c:/", title="Escoge un archivo", filetypes= (("form files" ,"*.form"),("all files", "*.*")))
    with open(entrada, encoding='utf-8') as archivo:
        global contenido
        contenido = archivo.read().strip()
        analizarTexto.insert(1.0,contenido)
    contenido=contenido.lower()
    print(contenido)
  

# con esta funcion modificamos el texto desde el text() de la interfaz
def modifica_texto():
    f = open ('fichero_prueba.txt','a')
    f.write(analizarTexto.get(1.0,END))
    f.close()

root=Tk()
root.title("Creador de Formularios")
root.iconbitmap("corazon.ico")
root.config(bg="sky blue")

miFrame=Frame(root, width=500, height=400)
miFrame.config(bg="light pink")



botonCargar=Button(root,text="Cargar archivo",command = lambda: leerArchivo())
botonCargar.grid(row=0, column=0,padx=1,pady=1)
botonAnalizar=Button(root,text="Analizar archivo",command = lambda: analizar())
botonAnalizar.grid(row=1, column=0,padx=1,pady=2)
botonSalir=Button(root,text="Salir",command = lambda: salir())
botonSalir.grid(row=3,column=0,padx=1,pady=2)
botonFormulario=Button(root,text="Crear Formulario",command = lambda: formulario())
botonFormulario.grid(row=5,column=0,padx=1,pady=2)


analizarTexto=Text(root,width=70, height=30)
analizarTexto.grid(row=3, column=8)
scrollTexto=Scrollbar(root, command=analizarTexto.yview)
scrollTexto.grid(row=3,column=9, sticky="nsew")


reportesMenu=Menubutton(root, text="Reportes", relief=RAISED)
reportesMenu.grid(row=2, column=0,padx=1,pady=2)
reportesMenu.menu =  Menu ( reportesMenu, tearoff = 0 )
reportesMenu["menu"] =  reportesMenu.menu

repTokens = IntVar()
repErrores = IntVar()

reportesMenu.menu.add_checkbutton ( label="Tokens",
                          variable=repTokens, command=lambda: reportarTokens())
reportesMenu.menu.add_checkbutton ( label="Errores",
                          variable=repErrores, command=lambda: reportarErrores())


def analizar ():
    scanner = Analizador2()
    textanalizar=analizarTexto.get(1.0,END)
    textanalizar=textanalizar.lower()
    scanner.AnalisisLexico(textanalizar)
    scanner.imprimirDatos()
    scanner.impTokens()
    scanner.impErrores()
    scanner.creacionFormulario()

def reportarTokens():
    textanalizar=analizarTexto.get(1.0,END)
    textanalizar=textanalizar.lower()
    fabricador=Analizador2()
    fabricador.AnalisisLexico(textanalizar)
    fabricador.reporteTokens()

def reportarErrores():
    textanalizar=analizarTexto.get(1.0,END)
    textanalizar=textanalizar.lower()
    fabricador=Analizador2()
    fabricador.AnalisisLexico(textanalizar)
    fabricador.reporteErrores()
def formulario():
    textanalizar=analizarTexto.get(1.0,END)
    textanalizar=textanalizar.lower()
    fabricador=Analizador2()
    fabricador.AnalisisLexico(textanalizar)
    #print(fabricador.listaTokens)
    fabricador.creacionFormulario()
    fabricador.crearReporte()
    #fabricador.reporteFormulario()
def salir():
    sys.exit()
root.mainloop()