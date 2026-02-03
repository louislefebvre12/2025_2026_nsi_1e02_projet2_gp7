from model import Model
from view import View

class Controller:
    def __init__(self, root):
        """
        Initialise le contrôleur, la vue et le modèle.
        """
        self.model = Model()
        self.view = View(root)

        # Charger les données initiales
        chaines = self.model.charger_chaines()
        self.view.actualiser_listbox(chaines)

        # Lier les événements aux boutons
        self.view.bouton_valider.config(command=self.action_valider)
        self.view.bouton_supprimer.config(command=self.action_supprimer)

        # Permettre la validation avec la touche Entrée
        self.view.entry.bind('<Return>', lambda event: self.action_valider())

    def valider_chaine(self, chaine):
        """
        Valide que la chaîne ne contient pas de chiffres.

        Args:
            chaine (str): Chaîne à valider

        Returns:
            tuple: (bool, str) - (True, "") si valide, (False, message) sinon
        """
        if any(c.isdigit() for c in chaine):
            return False, "La chaîne ne doit pas contenir de chiffres."
        return True, ""

    def action_valider(self):
        """
        Action déclenchée par le bouton Valider.
        """
        chaine = self.view.entry.get().strip()
        if not chaine:
            self.view.afficher_message_validation("Veuillez entrer un nom et un prénom", False)
            return

        est_valide, message = self.valider_chaine(chaine)
        self.view.afficher_message_validation(message, est_valide)

        if est_valide:
            self.model.sauvegarder_chaine(chaine)
            chaines = self.model.charger_chaines()
            self.view.actualiser_listbox(chaines)
            self.view.entry.delete(0, 'end')

    def action_supprimer(self):
        """
        Action déclenchée par le bouton Supprimer.
        """
        selection = self.view.obtenir_selection_listbox()
        if selection:
            self.model.supprimer_chaine(selection)
            chaines = self.model.charger_chaines()
            self.view.actualiser_listbox(chaines)
            self.view.afficher_message_validation(f"'{selection}' a été supprimé", True)
        else:
            self.view.afficher_message_validation("Veuillez sélectionner un élément à supprimer", False)
