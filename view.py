
from tkinter import ttk

class MainView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Fenêtre principale")

        ttk.Label(root, text="Menu principal").pack(pady=10)

        ttk.Button(
            root,
            text="1. Graphiques",
            command=self.controller.open_window1
        ).pack(pady=5)

        ttk.Button(
            root,
            text="2. Prédicteur",
            command=self.controller.open_window3
        ).pack(pady=5)





