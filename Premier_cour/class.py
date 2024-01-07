class Voiture:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur
        self.vitesse = 0

    def accelerer(self, valeur):
        self.vitesse += valeur

    def afficher_vitesse(self):
        print("La vitesse de la voiture est :", self.vitesse)

# Création d'un objet de la classe Voiture
ma_voiture = Voiture("Peugeot", "rouge")

# Utilisation des méthodes de l'objet
ma_voiture.accelerer(10)
ma_voiture.afficher_vitesse()
