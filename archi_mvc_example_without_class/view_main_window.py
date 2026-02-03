import tkinter as tk
from tkinter import ttk


def make_main_window():
    """
    Crée et retourne la fenêtre principale avec tous les widgets.
    
    Returns:
        tuple: (root, widgets_dict) où widgets_dict contient tous les widgets nécessaires
    """
    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Gestion des Noms et Prénoms")
    root.geometry("500x400")
    
    # Frame pour la saisie
    frame_saisie = tk.Frame(root)
    frame_saisie.pack(pady=20)
    
    # Label et champ de saisie
    label = tk.Label(frame_saisie, text="nom - prénom:", font=("Arial", 12))
    label.pack(side=tk.LEFT, padx=5)
    
    entry = tk.Entry(frame_saisie, width=30, font=("Arial", 11))
    entry.pack(side=tk.LEFT, padx=5)
    
    # Bouton valider
    bouton_valider = tk.Button(root, text="Valider", font=("Arial", 11))
    bouton_valider.pack(pady=10)
    
    # Label pour afficher le résultat de la validation
    label_resultat = tk.Label(root, text="", font=("Arial", 11), fg="blue")
    label_resultat.pack(pady=5)
    
    # Séparateur
    separator = ttk.Separator(root, orient='horizontal')
    separator.pack(fill='x', pady=10)
    
    # Frame pour la liste des noms-prénoms
    frame_liste = tk.Frame(root)
    frame_liste.pack(pady=10, fill=tk.BOTH, expand=True)
    
    label_liste = tk.Label(frame_liste, text="Liste des noms-prénoms enregistrés:", 
                          font=("Arial", 11, "bold"))
    label_liste.pack(pady=5)
    
    # Listbox avec scrollbar
    frame_listbox = tk.Frame(frame_liste)
    frame_listbox.pack(fill=tk.BOTH, expand=True, padx=20)
    
    scrollbar = tk.Scrollbar(frame_listbox)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    listbox = tk.Listbox(frame_listbox, font=("Arial", 10), 
                        yscrollcommand=scrollbar.set, height=8)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar.config(command=listbox.yview)
    
    # Bouton supprimer
    bouton_supprimer = tk.Button(root, text="Supprimer la sélection", 
                                font=("Arial", 10))
    bouton_supprimer.pack(pady=5)
    
    # Dictionnaire contenant tous les widgets
    widgets = {
        'root': root,
        'entry': entry,
        'bouton_valider': bouton_valider,
        'label_resultat': label_resultat,
        'listbox': listbox,
        'bouton_supprimer': bouton_supprimer
    }
    
    return root, widgets


def afficher_message_validation(label, message, est_valide):
    """
    Affiche un message de validation avec la couleur appropriée.
    
    Args:
        label: Le widget Label où afficher le message
        message (str): Le message à afficher
        est_valide (bool): True si valide (vert), False si invalide (rouge)
    """
    label.config(text=message)
    if est_valide:
        label.config(fg="green")
    else:
        label.config(fg="red")

def actualiser_listbox(listbox, chaines):
    """
    Actualise le contenu de la listbox avec la liste des noms-prénoms.
    
    Args:
        listbox: Le widget Listbox à actualiser
        chaines (list): Liste des noms-prénoms à afficher
    """
    # Vider la listbox
    listbox.delete(0, tk.END)
    
    # Ajouter tous les noms-prénoms
    for chaine in chaines:
        listbox.insert(tk.END, chaine)

def obtenir_selection_listbox(listbox):
    """
    Récupère l'élément sélectionné dans la listbox.
    
    Args:
        listbox: Le widget Listbox
    
    Returns:
        str or None: L'élément sélectionné ou None si aucune sélection
    """
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        return listbox.get(index)
    return None
