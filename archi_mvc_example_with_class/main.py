#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Application de gestion de noms et prénoms
Architecture MVC (Modèle-Vue-Contrôleur)
"""

from controler import Controller
import tkinter as tk

def main():
    """
    Point d'entrée principal de l'application.
    """
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()

if __name__ == "__main__":
    main()
