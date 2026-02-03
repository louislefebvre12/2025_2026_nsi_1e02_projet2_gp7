#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Application de gestion de noms et prénoms
Architecture MVC (Modèle-Vue-Contrôleur)
"""

import controler_view_main_window


def main():
    """
    Point d'entrée principal de l'application.
    """
    # Initialiser l'application via le contrôleur
    main_window = controler_view_main_window.initialiser_application()
    
    # Lancer la boucle principale
    main_window.mainloop()


if __name__ == "__main__":
    main()
