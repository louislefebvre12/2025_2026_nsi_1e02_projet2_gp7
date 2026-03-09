
"""
Contrôleur de l'application (C de MVC).
Il fait le lien entre :
- le modèle (données, logique générale),
- la vue principale (menu),
- et les fenêtres secondaires (graphes, prédicteur).
"""

from model import Model
from view import MainView
from window1 import Window1
from window3 import Window3


class Controller:
    def __init__(self, root):
        # Création du modèle (pour l'instant très simple)
        self.model = Model()

        # Création de la vue principale (menu),
        # à laquelle on passe le contrôleur pour que les boutons
        # puissent appeler open_window1 / open_window3.
        self.view = MainView(root, self)

    def open_window1(self):
        """Ouvre la fenêtre 1 : visualisation graphique des données."""
        Window1()

    def open_window3(self):
        """Ouvre la fenêtre 3 : prédicteur de réussite au BAC."""
        Window3()

