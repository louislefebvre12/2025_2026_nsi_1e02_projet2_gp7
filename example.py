import tkinter as tk
from tkinter import ttk

# ==========================
# MODEL
# ==========================
class Model:
    def __init__(self):
        self.message = "Application MVC avec 3 fenêtres"



class MainView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Fenêtre principale")

        ttk.Label(root, text="Menu principal").pack(pady=10)

        ttk.Button(
            root,
            text="Ouvrir Fenêtre 1",
            command=self.controller.open_window1
        ).pack(pady=5)

        ttk.Button(
            root,
            text="Ouvrir Fenêtre 2",
            command=self.controller.open_window2
        ).pack(pady=5)

        ttk.Button(
            root,
            text="Ouvrir Fenêtre 3",
            command=self.controller.open_window3
        ).pack(pady=5)


class Window1:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Fenêtre 1")
        ttk.Label(self.window, text="Contenu fenêtre 1").pack(padx=40, pady=40)


class Window2:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Fenêtre 2")
        ttk.Label(self.window, text="Contenu fenêtre 2").pack(padx=40, pady=40)


class Window3:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Fenêtre 3")
        ttk.Label(self.window, text="Contenu fenêtre 3").pack(padx=40, pady=40)



class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = MainView(root, self)

    def open_window1(self):
        Window1()

    def open_window2(self):
        Window2()

    def open_window3(self):
        Window3()


if __name__ == "__main__":
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()