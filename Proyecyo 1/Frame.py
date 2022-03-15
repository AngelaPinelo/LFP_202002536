from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox



def leerArchivo():
    Tk().withdraw()
    entrada = filedialog.askopenfilename(initialdir="c:/LFP", title="Escoge un archivo", filetypes= (("form files" ,"*.form"),("all files", "*.*")))
    archivo = open(entrada, 'r')
    global contenido
    contenido = archivo.read()
    analizarTexto.insert(1.0,contenido)
    #entrada.set(contenido)
    archivo.close()
    return contenido

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
#miFrame.pack()
miFrame.config(bg="light pink")

#entrada=StringVar()

botonCargar=Button(root,text="Cargar archivo",command = lambda: leerArchivo())
botonCargar.grid(row=0, column=0,padx=1,pady=1)
botonAnalizar=Button(root,text="Analizar archivo")
botonAnalizar.grid(row=1, column=0,padx=1,pady=2)
#botonCargar.pack()

analizarTexto=Text(root,width=70, height=30)
#analizarTexto.insert(INSERT,entrada)
analizarTexto.grid(row=3, column=8)
scrollTexto=Scrollbar(root, command=analizarTexto.yview)
scrollTexto.grid(row=3,column=9, sticky="nsew")
#scrollTexto.config(yscrollcommand=scrollTexto.set)
#analizarTexto.pack()

reportesMenu=Menubutton(root, text="Reportes", relief=RAISED)
reportesMenu.grid(row=2, column=0,padx=1,pady=2)
reportesMenu.menu =  Menu ( reportesMenu, tearoff = 0 )
reportesMenu["menu"] =  reportesMenu.menu

repTokens = IntVar()
repErrores = IntVar()

reportesMenu.menu.add_checkbutton ( label="Tokens",
                          variable=repTokens, command=lambda: leerArchivo())
reportesMenu.menu.add_checkbutton ( label="Errores",
                          variable=repErrores )




root.mainloop()