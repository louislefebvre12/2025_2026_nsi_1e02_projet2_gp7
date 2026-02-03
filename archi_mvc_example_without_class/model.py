import json
import os


def make_model():
    """
    Lit le fichier data.json et retourne une liste de messages formatés.
    
    Returns:
        list: Liste de messages formatés "votre nom et prénom : ..."
    """
    fichier_json = "data.json"
    
    # Si le fichier n'existe pas, retourner une liste vide
    if not os.path.exists(fichier_json):
        return []
    
    try:
        # Lire le fichier JSON
        with open(fichier_json, 'r', encoding='utf-8') as f:
            chaines = json.load(f)
        
        # Créer la liste de messages
        messages = []
        for chaine in chaines:
            message = f"votre nom et prénom : {chaine}"
            messages.append(message)
        
        return messages
    
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return []


def sauvegarder_chaine(chaine):
    """
    Ajoute un nom-prénom valide au fichier data.json.
    
    Args:
        chaine (str): Le nom-prénom à sauvegarder
    
    Returns:
        bool: True si la sauvegarde a réussi, False sinon
    """
    fichier_json = "data.json"
    
    try:
        # Lire les données existantes
        if os.path.exists(fichier_json):
            with open(fichier_json, 'r', encoding='utf-8') as f:
                donnees = json.load(f)
        else:
            donnees = []
        
        # Ajouter le nouveau nom-prénom s'il n'existe pas déjà
        if chaine not in donnees:
            donnees.append(chaine)
            
            # Sauvegarder dans le fichier
            with open(fichier_json, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, ensure_ascii=False, indent=2)
            
            return True
        return False
    
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")
        return False


def charger_chaines():
    """
    Charge la liste brute des noms-prénoms depuis le fichier JSON.
    
    Returns:
        list: Liste des noms-prénoms
    """
    fichier_json = "data.json"
    
    if not os.path.exists(fichier_json):
        return []
    
    try:
        with open(fichier_json, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
        return []


def supprimer_chaine(chaine):
    """
    Supprime un nom-prénom du fichier data.json.
    
    Args:
        chaine (str): Le nom-prénom à supprimer
    
    Returns:
        bool: True si la suppression a réussi, False sinon
    """
    fichier_json = "data.json"
    
    try:
        donnees = charger_chaines()
        
        if chaine in donnees:
            donnees.remove(chaine)
            
            with open(fichier_json, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, ensure_ascii=False, indent=2)
            
            return True
        return False
    
    except Exception as e:
        print(f"Erreur lors de la suppression : {e}")
        return False

