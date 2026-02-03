import model
import view_main_window


def verifier_chaine (chain):
    """
    Vérifie si la chaîne contient un chiffre et renvoie un message approprié.
    
    Args:
        chain (str): La chaîne à vérifier
    
    Returns:
        tuple: (message, est_valide) où message est le texte et est_valide est un booléen
    """
    # Vérifier si la chaîne contient au moins un chiffre
    if any(char.isdigit() for char in chain):
        return (f"{chain} ne peut pas être un nom - prénom !", False)
    else:
        return (f"votre nom et prénom : {chain}", True)

# Configurer les événements
def action_valider(widgets):
    """Action déclenchée par le bouton Valider"""
    chaine = widgets['entry'].get().strip()
    
    # Vérifier que le champ n'est pas vide
    if not chaine:
        view_main_window.afficher_message_validation(
            widgets['label_resultat'],
            "Veuillez saisir un nom et prénom !",
            False
        )
        return
    
    # Vérifier la validité du nom-prénom
    message, est_valide = verifier_chaine(chaine)
    view_main_window.afficher_message_validation(
        widgets['label_resultat'],
        message,
        est_valide
    )
    
    # Si valide, sauvegarder et actualiser la liste
    if est_valide:
        model.sauvegarder_chaine(chaine)
        chaines = model.charger_chaines()
        view_main_window.actualiser_listbox(widgets['listbox'], chaines)
        
        # Vider le champ de saisie
        widgets['entry'].delete(0, 'end')

def action_supprimer(widgets):
    """Action déclenchée par le bouton Supprimer"""
    selection = view_main_window.obtenir_selection_listbox(widgets['listbox'])

    if selection:
        # Supprimer du modèle
        model.supprimer_chaine(selection)
        
        # Actualiser la vue
        chaines = model.charger_chaines()
        view_main_window.actualiser_listbox(widgets['listbox'], chaines)
        
        # Afficher un message de confirmation
        view_main_window.afficher_message_validation(
            widgets['label_resultat'],
            f"'{selection}' a été supprimé",
            True
        )
    else:
        # Aucune sélection
        view_main_window.afficher_message_validation(
            widgets['label_resultat'],
            "Veuillez sélectionner un élément à supprimer",
            False
        )

def initialiser_application():
    """
    Initialise l'application en créant la vue et en configurant le contrôleur.
    
    Returns:
        tk.Tk: La fenêtre principale
    """
    # Créer la vue
    root, widgets = view_main_window.make_main_window()
    
    # Charger les données initiales
    chaines = model.charger_chaines()
    view_main_window.actualiser_listbox(widgets['listbox'], chaines)
    
    # Lier les événements aux boutons
    widgets['bouton_valider'].config(command=lambda: action_valider(widgets))
    widgets['bouton_supprimer'].config(command=lambda: action_supprimer(widgets))
    
    # Permettre la validation avec la touche Entrée
    widgets['entry'].bind('<Return>', lambda event: action_valider(widgets))
    
    return root
