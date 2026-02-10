
from tkinter import *

class View:
    def __init__ (self, window):
        self.window = window
        self.window.title("Gestion des Noms et Prénoms")
        self.window.geometry("500x400")
        self.window.geometry('600x400')
        self.window.title('Multiple windows')

        self.button1 = Button(window, text = 'Open main window')
        self.button1.pack(expand = True)

        self.button2 = Button(window, text = 'Close main window')
        self.button2.pack(expand = True)

        self.button3 = Button(window, text = 'PRÉDICTION')
        self.button3.pack(expand = True)
        
        self.button4 = Button(window, text = 'QuiT')
        self.button4.pack(expand = True)



