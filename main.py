
"""
Point d'entrée de l'application.
On crée la fenêtre principale Tkinter puis on délègue la suite
au contrôleur (architecture de type MVC : Model / View / Controller).
"""

import tkinter as tk
from controller import Controller


if __name__ == "__main__":
    # Création de la fenêtre principale Tkinter
    root = tk.Tk()

    # Instanciation du contrôleur qui va construire la vue principale
    # et gérer l'ouverture des autres fenêtres.
    app = Controller(root)

    # Boucle principale : l'application attend les interactions utilisateur.
    root.mainloop()






