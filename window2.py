import tkinter as tk
from tkinter import ttk

class Window2:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Fenêtre 2")
        ttk.Label(self.window, text="Contenu fenêtre 2").pack(padx=40, pady=40)
