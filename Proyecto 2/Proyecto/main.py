import threading
from tkinter import *
from tkinter import font
from tkinter import ttk
from Analisis import Analizador
import webbrowser
from io import open
import sys

FORMAT = "utf-8"
a=Analizador()

class GUI:
    #file = open("Manual usuario LFP P2.pdf",'r')
    
    # constructor method
    def __init__(self):
       
        # chat window which is currently hidden
        self.Window = Tk()
        self.Window.withdraw()
         
        # login window
        self.login = Toplevel()
        # set the title        
        self.login.title("Login")
        self.login.resizable(width = False,
                             height = False)
        self.login.configure(width = 400,
                             height = 300)       
        # create a Label
        self.pls = Label(self.login,
                       text = "Bienvenid@ a La Liga Bot",
                       justify = CENTER,
                       font = "Helvetica 14 bold")
        
         
        self.pls.place(relheight = 0.05,
                       relx = 0.2,
                       rely = 0.07)
        # create a Label
        self.labelName = Label(self.login,
                               text = "Introduce tu nombre: ",
                               font = "Helvetica 12")
         
        self.labelName.place(relheight = 0.05,
                             relx = 0.01,
                             rely = 0.3)
         
        # create a entry box for
        # tyoing the message
        self.entryName = Entry(self.login,
                             font = "Helvetica 14")
         
        self.entryName.place(relwidth = 0.4,
                             relheight = 0.08,
                             relx = 0.4,
                             rely = 0.28)
         
        # set the focus of the cursor
        self.entryName.focus()
         
        # create a Continue Button
        # along with action
        self.go = Button(self.login,
                         text = "CONTINUAR",
                         font = "Helvetica 14 bold",
                         command = lambda: self.goAhead(self.entryName.get()))
         
        self.go.place(relx = 0.3,
                      rely = 0.55)
        self.Window.mainloop()
 
    def goAhead(self, name):
        self.login.destroy()
        self.layout(name)
         
 
    # The main layout of the chat
    def layout(self,name):
       
        self.name = name
        # to show chat window        
        self.Window.deiconify()
        self.Window.title("CHAT")
        self.Window.resizable(width = True,
                              height = True)
        self.Window.configure(width = 800,
                              height = 600,
                              bg = "#17202A")
        self.labelHead = Label(self.Window,
                             bg = "#ADF80B",
                              fg = "#FFFFFF",
                              text = self.name ,
                               font = "Helvetica 14 bold",
                               pady = 5)
         
        self.labelHead.place(relwidth = 1)
        self.line = Label(self.Window,
                          width = 450,
                          bg = "#ABB2B9")
         
        self.line.place(relwidth = 1,
                        rely = 0.07,
                        relheight = 0.012)
         
        self.textCons = Text(self.Window,
                             width = 20,
                             height = 2,
                             bg = "#5EACAB",
                             fg = "#EAECEE",
                             font = "Helvetica 14",
                             padx = 5,
                             pady = 5)
        
        msgBienvenida = ("Botcito: Hola, bienvenido a La Liga Bot \n puedes escribir el comando que necesites, \n recuerda que puedes encontrar los comandos dando click en\n el boton de Manual de usuario")
        self.textCons.insert(END, msgBienvenida+ "\n\n")
        
        
        self.textCons.place(relheight = 0.745,
                            relwidth = 1,
                            rely = 0.08)
         
        self.labelBottom = Label(self.Window,
                                 bg = "#ADF80B",
                                 height = 80)
         
        self.labelBottom.place(relheight = 0.745,relwidth = 1,
                               rely = 0.825)
                
        
        self.entryMsg = Entry(self.labelBottom,
                              bg = "#2C3E50",
                              fg = "#EAECEE",
                              font = "Helvetica 13")
         
        # place the given widget
        # into the gui window
        self.entryMsg.place(relwidth = 0.74,
                            relheight = 0.08,
                            rely = 0.008,
                            relx = 0.011)
         
        self.entryMsg.focus()
         
        # create a Send Button
        self.buttonMsg = Button(self.labelBottom,
                                text = "Enviar",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#CD41FB",
                                command = lambda : self.sendButton(self.entryMsg.get()))
         
        self.buttonMsg.place(relx = 0.77,
                             rely = 0.008,
                             relheight = 0.06,
                             relwidth = 0.22)
         
        self.textCons.config(cursor = "arrow")
        
        
        # create a  Button Errores
        self.buttonErr = Button(self.labelBottom,
                                text = "Reporte Errores",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#CD41FB",
                                command = lambda : self.repErr(self.msg))
        self.buttonErr.place(relx = 0,
                             rely = 0.099,
                             relheight = 0.06,
                             relwidth = 0.15)
         
        self.textCons.config(cursor = "arrow")
        
        #Limpiar log
        self.cleanLog = Button(self.labelBottom,
                                text = "Limpiar Errores",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#CD41FB",
                                command = lambda : self.cleanErr())
         
        self.cleanLog.place(relx = 0.16,
                             rely = 0.099,
                             relheight = 0.06,
                             relwidth = 0.15)
         
        self.textCons.config(cursor = "arrow")
        
        #Boton Tokens
        self.Tokens = Button(self.labelBottom,
                                text = "Reporte tokens",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#CD41FB",
                                command = lambda : self.repTok(self.msg))
         
        self.Tokens.place(relx = 0.32,
                             rely = 0.099,
                             relheight = 0.06,
                             relwidth = 0.15)
        self.textCons.config(cursor = "arrow")
        
        #Limpiar log Tokens
        self.cleanLogTok = Button(self.labelBottom,
                                text = "Limpiar Tokens",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#CD41FB",
                                command = lambda : self.cleanTok())
         
        self.cleanLogTok.place(relx = 0.48,
                             rely = 0.099,
                             relheight = 0.06,
                             relwidth = 0.15)
         
        self.textCons.config(cursor = "arrow")
        
       #Boton Manual U
        self.ManualUser = Button(self.labelBottom,
                                text = "Manual de Usuario",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#CD41FB",
                                command = lambda : webbrowser.open('Manual usuario LFP P2.pdf'))
         
        self.ManualUser.place(relx = 0.64,
                             rely = 0.099,
                             relheight = 0.06,
                             relwidth = 0.17)
         
        self.textCons.config(cursor = "arrow")
        
      
        #Boton Manual Tec
        self.ManualTec = Button(self.labelBottom,
                                text = "Manual Tecnico",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#CD41FB",
                                command = lambda: webbrowser.open('Manuel T??cnico LFP Proyecto2.pdf'))
         
        self.ManualTec.place(relx = 0.82,
                             rely = 0.099,
                             relheight = 0.06,
                             relwidth = 0.15)
         
        self.textCons.config(cursor = "arrow")
        
         
        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)
         
        # place the scroll bar
        # into the gui window
        scrollbar.place(relheight = 1,
                        relx = 0.974)
         
        scrollbar.config(command = self.textCons.yview)
         
        self.textCons.config(state = DISABLED)
 
    # function to basically start the thread for sending messages
    def sendButton(self, msg):
        self.textCons.config(state = DISABLED)
        self.msg=msg
        self.entryMsg.delete(0, END)
        snd= threading.Thread(target = self.sendMessage)
        snd.start()
 
    
         
    # function to send messages
    def sendMessage(self):
        self.textCons.config(state=DISABLED)
        while True:
            global message
            message = (f"{self.name}: {self.msg}")
            self.textCons.config(state = NORMAL)
            self.textCons.insert(END, message+ "\n\n")  
            cadena=self.msg
            #self.pruebita(cadena)
            #self.textCons.insert(END,)
            if message == (f"{self.name}: ADIOS"):
                respuesta = 'Botcito: Adi??s'
                self.textCons.config(state = NORMAL)
                self.textCons.insert(END, respuesta+ "\n\n")
                self.salir()
            else:
                 self.pruebita(self.msg)                 
            
            break   

    def pruebita (self,cadena):              
        a.AnalisisLexico(cadena)
        a.AnalizadorSintactico()
        print(a.resultado)
        self.textCons.insert(END,a.resultado+ "\n\n")

    def repTok (self,cadena):
        #a.AnalisisLexico(cadena)
        #a.imprimirDatos()
        #a.impTokens()
        a.reporteTokens()

    def repErr (self,cadena):
        #a.AnalisisLexico(cadena)
        #a.imprimirDatos()
        #a.impErrores()
        a.reporteErrores()

    def cleanTok(self):
        a.listaTokens =[]
    
    def cleanErr(self):
        a.listaErrores=[]

    def salir(self):
        self.Window.destroy()
    def ManualUser(self):
        webbrowser.open('Manual usuario LFP P2.pdf')
    def ManualTec(self):
        webbrowser.open('Manuel T??cnico LFP Proyecto2.pdf')
    


g = GUI()