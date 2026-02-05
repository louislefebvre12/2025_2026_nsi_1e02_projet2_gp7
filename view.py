
from tkinter import *

class View:
    def __init__ (self, window):
        self.window = window
        self.window.title("Gestion des Noms et Prénoms")
        self.window.geometry("500x400")
        self.window.geometry('600x400')
        self.window.title('Multiple windows')

        self.button1 = Button(window, text = 'Open main window', command = plot_window(self))
        self.button1.pack(expand = True)

        self.button2 = Button(window, text = 'Close main window', command = ranking_window(self))
        self.button2.pack(expand = True)

        self.button3 = Button(window, text = 'PRÉDICTION', command = prediction_window)
        self.button3.pack(expand = True)
        
        self.button4 = Button(window, text = 'QuiT', command = close_window)
        self.button4.pack(expand = True)

        def close_window() :
            window.destroy()








