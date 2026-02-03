#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Application de gestion de noms et prénoms
Architecture MVC (Modèle-Vue-Contrôleur)
"""

from model import Model
from view import View
from controler import Controller
import tkinter as tk

def main():
    """
    Point d'entrée principal de l'application.
    """
    main_window = tk.Tk()
    model = Model ()
    view = View(main_window, model)
    app = Controller(main_window, model, view)
    main_window.mainloop()

if __name__ == "__main__":
    main()
