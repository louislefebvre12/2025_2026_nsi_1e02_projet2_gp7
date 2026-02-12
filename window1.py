import tkinter as tk
from tkinter import ttk

class Window1:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Fenêtre 1")
        ttk.Label(self.window, text="Contenu fenêtre 1").pack(padx=40, pady=40)




