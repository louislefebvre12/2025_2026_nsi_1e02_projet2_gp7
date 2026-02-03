import tkinter as tk
from tkinter import ttk

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Noms et Prénoms")
        self.root.geometry("500x400")

        # Frame pour la saisie
        self.frame_saisie = tk.Frame(root)
        self.frame_saisie.pack(pady=20)

        # Label et champ de saisie
        self.label = tk.Label(self.frame_saisie, text="nom - prénom:", font=("Arial", 12))
        self.label.pack(side=tk.LEFT, padx=5)

        self.entry = tk.Entry(self.frame_saisie, width=30, font=("Arial", 11))
        self.entry.pack(side=tk.LEFT, padx=5)

        # Boutons
        self.bouton_valider = tk.Button(root, text="Valider", font=("Arial", 11))
        self.bouton_valider.pack(pady=10)

        self.bouton_supprimer = tk.Button(root, text="Supprimer", font=("Arial", 11))
        self.bouton_supprimer.pack(pady=5)

        # Label pour afficher le résultat de la validation
        self.label_resultat = tk.Label(root, text="", font=("Arial", 11), fg="blue")
        self.label_resultat.pack(pady=5)

        # Séparateur
        self.separator = ttk.Separator(root, orient='horizontal')
        self.separator.pack(fill='x', pady=10)

        # Frame pour la liste des noms-prénoms
        self.frame_liste = tk.Frame(root)
        self.frame_liste.pack(pady=10)

        self.scrollbar = tk.Scrollbar(self.frame_liste)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(
            self.frame_liste,
            yscrollcommand=self.scrollbar.set,
            width=50,
            height=10,
            font=("Arial", 11)
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.config(command=self.listbox.yview)

    def afficher_message_validation(self, message, est_valide):
        couleur = "green" if est_valide else "red"
        self.label_resultat.config(text=message, fg=couleur)

    def obtenir_selection_listbox(self):
        selection = self.listbox.curselection()
        if selection:
            return self.listbox.get(selection[0])
        return None

    def actualiser_listbox(self, chaines):
        self.listbox.delete(0, tk.END)
        for chaine in chaines:
            self.listbox.insert(tk.END, chaine)
