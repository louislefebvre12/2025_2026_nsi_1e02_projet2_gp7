
from tkinter import ttk


class MainView:
    """
    Vue principale : affiche le menu qui permet d'ouvrir
    soit la fenêtre de graphiques, soit la fenêtre de prédiction.
    """

    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Fenêtre principale")

        # Titre du menu
        ttk.Label(root, text="Menu principal").pack(pady=10)

        # Bouton pour ouvrir la fenêtre 1 (visualisation graphique)
        ttk.Button(
            root,
            text="1. Graphiques",
            command=self.controller.open_window1
        ).pack(pady=5)

        # Bouton pour ouvrir la fenêtre 3 (prédicteur de réussite)
        ttk.Button(
            root,
            text="2. Prédicteur",
            command=self.controller.open_window3
        ).pack(pady=5)

