import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Nom du fichier de données téléchargé depuis data.gouv.fr.
# Il contient, pour chaque combinaison (session, académie, département, voie, genre),
# le nombre de présents, d'admis et le taux de réussite au BAC.
EXCEL_PATH = "fr-en-baccalaureat-par-departement.xlsx"


class Window1:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("1. Graphiques - Résultats au BAC")

        title_label = ttk.Label(
            self.window,
            text="1. Graphiques - Résultats au BAC",
            padding=10
        )
        title_label.config(font=("Courrier", 20, "bold"))
        title_label.pack()

        try:
            self.df = pd.read_excel(EXCEL_PATH)
        except FileNotFoundError:
            self.df = pd.DataFrame()

        if not self.df.empty:
            # On supprime uniquement les lignes entièrement vides
            # (cela peut arriver à la fin du fichier Excel).
            self.df = self.df.dropna(how="all")

        # Figure Matplotlib commune à tous les graphiques de cette fenêtre
        self.fig, self.ax = plt.subplots(figsize=(7, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Frame qui contient les boutons de choix du graphique
        button_frame = ttk.Frame(self.window)
        button_frame.pack(pady=10)

        ttk.Button(
            button_frame,
            text="Taux de réussite par année",
            command=self.plot_taux_par_annee
        ).grid(row=0, column=0, padx=5, pady=5)

        ttk.Button(
            button_frame,
            text="Top 10 académies (taux moyen)",
            command=self.plot_taux_par_academie
        ).grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(
            button_frame,
            text="Nombre de candidats par année",
            command=self.plot_candidats_par_annee
        ).grid(row=0, column=2, padx=5, pady=5)

        ttk.Button(
            button_frame,
            text="Taux par série (moyenne)",
            command=self.plot_taux_par_serie
        ).grid(row=1, column=0, padx=5, pady=5)

        ttk.Button(
            button_frame,
            text="Top 10 séries (candidats)",
            command=self.plot_candidats_par_serie
        ).grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(
            button_frame,
            text="Répartition des candidats par académie",
            command=self.plot_repartition_candidats_academie
        ).grid(row=1, column=2, padx=5, pady=5)

    def _clear_ax(self):
        self.ax.clear()

    def _check_data(self, required_columns):
        if self.df.empty:
            self._clear_ax()
            self.ax.text(
                0.5,
                0.5,
                f"Fichier Excel introuvable :\n{EXCEL_PATH}",
                ha="center",
                va="center",
                fontsize=12,
            )
            self.canvas.draw()
            return False

        missing = [col for col in required_columns if col not in self.df.columns]
        if missing:
            self._clear_ax()
            self.ax.text(
                0.5,
                0.5,
                "Colonnes manquantes dans le fichier :\n" + ", ".join(missing),
                ha="center",
                va="center",
                fontsize=12,
            )
            self.canvas.draw()
            return False

        return True

    def plot_taux_par_annee(self):
        # Session = année, Taux de réussite à l'examen.
        # On calcule ici l'évolution du taux moyen par année.
        taux_col = "Taux de r\u00e9ussite \u00e0 l'examen"
        if not self._check_data(["Session", taux_col]):
            return

        df_group = (
            self.df.groupby("Session")[taux_col]
            .mean()
            .reset_index()
            .sort_values("Session")
        )

        self._clear_ax()
        self.ax.plot(
            df_group["Session"],
            df_group[taux_col],
            marker="o",
            linestyle="-",
            color="tab:blue",
        )
        self.ax.set_xlabel("Session")
        self.ax.set_ylabel("Taux de réussite (%)")
        self.ax.set_title("Taux de réussite moyen par année")
        self.ax.grid(True, alpha=0.3)
        self.fig.tight_layout()
        self.canvas.draw()

    def plot_taux_par_academie(self):
        taux_col = "Taux de r\u00e9ussite \u00e0 l'examen"
        if not self._check_data(["Acad\u00e9mie", taux_col]):
            return

        df_group = (
            self.df.groupby("Acad\u00e9mie")[taux_col]
            .mean()
            .reset_index()
            .sort_values(taux_col, ascending=False)
            .head(10)
        )

        self._clear_ax()
        self.ax.barh(df_group["Acad\u00e9mie"], df_group[taux_col], color="tab:green")
        self.ax.set_xlabel("Taux de réussite moyen (%)")
        self.ax.set_title("Top 10 académies par taux de réussite moyen")
        self.ax.invert_yaxis()
        self.fig.tight_layout()
        self.canvas.draw()

    def plot_candidats_par_annee(self):
        candidats_col = "Nombre de pr\u00e9sents \u00e0 l'examen"
        if not self._check_data(["Session", candidats_col]):
            return

        df_group = (
            self.df.groupby("Session")[candidats_col]
            .sum()
            .reset_index()
            .sort_values("Session")
        )

        self._clear_ax()
        # On place les barres à des positions 0,1,2,... (entiers)
        # et on met les années en étiquettes pour éviter des valeurs
        # numériques étranges sur l'axe des abscisses.
        x = range(len(df_group))
        self.ax.bar(x, df_group[candidats_col], color="tab:orange")
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(df_group["Session"].astype(str))
        self.ax.set_xlabel("Session")
        self.ax.set_ylabel("Nombre de candidats")
        self.ax.set_title("Nombre total de candidats par année")
        self.fig.tight_layout()
        self.canvas.draw()

    def plot_taux_par_serie(self):
        taux_col = "Taux de r\u00e9ussite \u00e0 l'examen"
        if not self._check_data(["Voie", taux_col]):
            return

        df_group = (
            self.df.groupby("Voie")[taux_col]
            .mean()
            .reset_index()
            .sort_values(taux_col, ascending=False)
        )

        self._clear_ax()
        self.ax.barh(df_group["Voie"], df_group[taux_col], color="tab:purple")
        self.ax.set_xlabel("Taux de réussite moyen (%)")
        self.ax.set_title("Taux de réussite moyen par voie")
        self.ax.invert_yaxis()
        self.fig.tight_layout()
        self.canvas.draw()

    def plot_candidats_par_serie(self):
        candidats_col = "Nombre de pr\u00e9sents \u00e0 l'examen"
        if not self._check_data(["Voie", candidats_col]):
            return

        df_group = (
            self.df.groupby("Voie")[candidats_col]
            .sum()
            .reset_index()
            .sort_values(candidats_col, ascending=False)
        )

        self._clear_ax()
        # Graphique horizontal pour éviter le chevauchement des labels de voie
        self.ax.barh(df_group["Voie"], df_group[candidats_col], color="tab:red")
        self.ax.set_ylabel("Voie")
        self.ax.set_xlabel("Nombre de candidats")
        self.ax.set_title("Nombre de candidats par voie")
        self.ax.invert_yaxis()
        self.fig.tight_layout()
        self.canvas.draw()

    def plot_repartition_candidats_academie(self):
        candidats_col = "Nombre de pr\u00e9sents \u00e0 l'examen"
        if not self._check_data(["Acad\u00e9mie", candidats_col]):
            return

        df_group = (
            self.df.groupby("Acad\u00e9mie")[candidats_col]
            .sum()
            .reset_index()
            .sort_values(candidats_col, ascending=False)
        )

        total = df_group[candidats_col].sum()
        df_group = df_group[df_group[candidats_col] / total > 0.01]

        self._clear_ax()
        self.ax.pie(
            df_group[candidats_col],
            labels=df_group["Acad\u00e9mie"],
            autopct="%1.1f%%",
            startangle=90,
        )
        self.ax.set_title("Répartition des candidats par académie")
        self.ax.axis("equal")
        self.fig.tight_layout()
        self.canvas.draw()
