import tkinter as tk
from tkinter import ttk
import pandas as pd


EXCEL_PATH = "fr-en-baccalaureat-par-departement.xlsx"


class Window3:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("2. Prédicteur - Estimation de réussite au BAC")

        try:
            self.df = pd.read_excel(EXCEL_PATH)
        except FileNotFoundError:
            self.df = pd.DataFrame()

        if not self.df.empty:
            self.df = self.df.dropna(how="all")

        self.taux_col = "Taux de réussite à l'examen"

        title = ttk.Label(
            self.window,
            text="2. Prédicteur - Calcule ta probabilité de réussite au BAC",
            padding=10,
        )
        title.config(font=("Courrier", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        row = 1

        ttk.Label(self.window, text="Académie :").grid(row=row, column=0, sticky="e", padx=5, pady=5)
        self.academie_var = tk.StringVar()
        self.academie_cb = ttk.Combobox(self.window, textvariable=self.academie_var, state="readonly")
        self.academie_cb.grid(row=row, column=1, sticky="w", padx=5, pady=5)
        row += 1

        ttk.Label(self.window, text="Département :").grid(row=row, column=0, sticky="e", padx=5, pady=5)
        self.departement_var = tk.StringVar()
        self.departement_cb = ttk.Combobox(self.window, textvariable=self.departement_var, state="readonly")
        self.departement_cb.grid(row=row, column=1, sticky="w", padx=5, pady=5)
        row += 1

        ttk.Label(self.window, text="Voie (générale / techno / pro) :").grid(row=row, column=0, sticky="e", padx=5, pady=5)
        self.voie_var = tk.StringVar()
        self.voie_cb = ttk.Combobox(self.window, textvariable=self.voie_var, state="readonly")
        self.voie_cb.grid(row=row, column=1, sticky="w", padx=5, pady=5)
        row += 1

        ttk.Label(self.window, text="Genre :").grid(row=row, column=0, sticky="e", padx=5, pady=5)
        self.genre_var = tk.StringVar()
        self.genre_cb = ttk.Combobox(self.window, textvariable=self.genre_var, state="readonly")
        self.genre_cb.grid(row=row, column=1, sticky="w", padx=5, pady=5)
        row += 1

        ttk.Button(
            self.window,
            text="Calculer ma chance de réussite",
            command=self.calculer_chance,
        ).grid(row=row, column=0, columnspan=2, pady=15)
        row += 1

        self.result_label = ttk.Label(self.window, text="", justify="center")
        self.result_label.grid(row=row, column=0, columnspan=2, pady=(10, 15))

        self.window.columnconfigure(0, weight=0)
        self.window.columnconfigure(1, weight=1)

        self._remplir_listes()

    def _remplir_listes(self):
        if self.df.empty:
            self.result_label.config(text=f"Fichier Excel introuvable : {EXCEL_PATH}")
            return

        def uniques(col):
            if col not in self.df.columns:
                return []
            return sorted(self.df[col].dropna().astype(str).unique())

        self.academie_cb["values"] = ["(toutes)"] + uniques("Académie")
        self.academie_cb.current(0)

        self.departement_cb["values"] = ["(tous)"] + uniques("Département")
        self.departement_cb.current(0)

        self.voie_cb["values"] = ["(toutes)"] + uniques("Voie")
        self.voie_cb.current(0)

        self.genre_cb["values"] = ["(tous)"] + uniques("Genre")
        self.genre_cb.current(0)

    def calculer_chance(self):
        if self.df.empty or self.taux_col not in self.df.columns:
            self.result_label.config(text="Impossible de calculer : données manquantes.")
            return

        df = self.df.copy()

        if self.academie_var.get() and self.academie_var.get() != "(toutes)":
            df = df[df["Académie"].astype(str) == self.academie_var.get()]

        if self.departement_var.get() and self.departement_var.get() != "(tous)":
            df = df[df["Département"].astype(str) == self.departement_var.get()]

        if self.voie_var.get() and self.voie_var.get() != "(toutes)":
            df = df[df["Voie"].astype(str) == self.voie_var.get()]

        if self.genre_var.get() and self.genre_var.get() != "(tous)":
            df = df[df["Genre"].astype(str) == self.genre_var.get()]

        if df.empty:
            self.result_label.config(
                text="Aucune donnée ne correspond à ces critères.\nEssaye en enlevant un filtre."
            )
            return

        taux_moyen = df[self.taux_col].mean()
    
        self.result_label.config(text=f"{taux_moyen:.1f} %")

