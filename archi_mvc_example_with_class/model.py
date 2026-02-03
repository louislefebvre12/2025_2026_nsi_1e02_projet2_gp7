import json

class Model:
    def __init__(self, fichier_donnees="data.json"):
        self.fichier_donnees = fichier_donnees

    def charger_chaines(self):
        try:
            with open(self.fichier_donnees, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def sauvegarder_chaines(self, chaines):
        with open(self.fichier_donnees, 'w') as f:
            json.dump(chaines, f, indent=4)

    def sauvegarder_chaine(self, chaine):
        chaines = self.charger_chaines()
        chaines.append(chaine)
        self.sauvegarder_chaines(chaines)

    def supprimer_chaine(self, chaine):
        chaines = self.charger_chaines()
        if chaine in chaines:
            chaines.remove(chaine)
            self.sauvegarder_chaines(chaines)
