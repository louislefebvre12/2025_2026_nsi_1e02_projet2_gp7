# Application de Gestion des Noms et Prénoms

## Architecture MVC

Cette application suit le pattern **Modèle-Vue-Contrôleur (MVC)** pour une séparation claire des responsabilités.

### Structure des fichiers

```
.
├── main.py          # Point d'entrée de l'application
├── controler.py     # Logique de contrôle (Contrôleur)
├── view.py          # Interface graphique (Vue)
├── model.py         # Gestion des données (Modèle)
├── data.json        # Stockage des données
└── README.md        # Documentation
```

## Description des fichiers

### 1. **main.py** - Point d'entrée
- Lance l'application
- Initialise le contrôleur
- Démarre la boucle principale tkinter

### 2. **model.py** - Modèle (Données)
Gère la persistance des données dans `data.json`.

**Fonctions:**
- `make_model()` : Lit data.json et retourne une liste de messages formatés
- `sauvegarder_chaine(chaine)` : Ajoute un nom-prénom au fichier
- `charger_chaines()` : Charge la liste brute des noms-prénoms
- `supprimer_chaine(chaine)` : Supprime un nom-prénom

### 3. **view.py** - Vue (Interface)
Gère l'affichage et les widgets tkinter.

**Fonctions:**
- `make_screen()` : Crée la fenêtre et tous les widgets
- `afficher_message_validation(label, message, est_valide)` : Affiche un message coloré
- `actualiser_listbox(listbox, chaines)` : Met à jour la liste affichée
- `obtenir_selection_listbox(listbox)` : Récupère l'élément sélectionné

### 4. **controler.py** - Contrôleur (Logique)
Coordonne le modèle et la vue, gère les événements.

**Fonctions:**
- `verifier_chaine(chain)` : Vérifie qu'un nom ne contient pas de chiffres
- `initialiser_application()` : Configure l'application et les événements
- `action_valider()` : Gère l'ajout d'un nom-prénom
- `action_supprimer()` : Gère la suppression d'un nom-prénom

### 5. **data.json** - Données
Fichier JSON contenant la liste des noms-prénoms enregistrés.

Format:
```json
[
  "Jean Dupont",
  "Marie Martin",
  "Pierre Durant"
]
```

## Fonctionnalités

### 1. Validation de nom-prénom
- Saisir un nom et prénom dans le champ
- Cliquer sur "Valider" (ou appuyer sur Entrée)
- Le système vérifie qu'il ne contient pas de chiffres
- Si valide : sauvegarde et ajout à la liste
- Si invalide : affichage d'un message d'erreur en rouge

### 2. Affichage de la liste
- Tous les noms-prénoms enregistrés sont affichés dans une listbox
- La liste se met à jour automatiquement après chaque ajout/suppression

### 3. Suppression
- Sélectionner un nom-prénom dans la liste
- Cliquer sur "Supprimer la sélection"
- L'élément est supprimé du fichier et de l'affichage

## Utilisation

### Lancer l'application
```bash
python main.py
```

### Exemple d'utilisation
1. Lancer l'application
2. Saisir "Jean Dupont" → Message vert : "votre nom et prénom : Jean Dupont"
3. Saisir "Marie123" → Message rouge : "Marie123 ne peut pas être un nom - prénom !"
4. Sélectionner "Jean Dupont" dans la liste
5. Cliquer sur "Supprimer la sélection"

## Avantages de l'architecture MVC

- **Séparation des responsabilités** : chaque fichier a un rôle précis
- **Maintenabilité** : facile de modifier l'interface sans toucher aux données
- **Testabilité** : chaque composant peut être testé indépendamment
- **Réutilisabilité** : le modèle peut être utilisé dans une autre interface
- **Évolutivité** : facile d'ajouter de nouvelles fonctionnalités
