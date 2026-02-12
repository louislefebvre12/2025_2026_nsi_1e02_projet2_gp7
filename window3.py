import tkinter as tk
from tkinter import ttk

class Window3:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Fenêtre 3")
        ttk.Label(self.window, text="Contenu fenêtre 3").pack(padx=40, pady=40)
