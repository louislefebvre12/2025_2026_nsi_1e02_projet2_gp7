from model import Model
from view import View

class Controller:
    def __init__(self, root, model, view):
       
        self.model = model
        self.view = view

        chaines = self.model.charger_chaines()
        self.view.actualiser_listbox(chaines)

    def valider_chaine(self, chaine):
        
    def action_valider(self):
        

    def action_supprimer(self):
        self.window.quit()