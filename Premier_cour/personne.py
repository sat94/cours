class Personne():
    def __init__(self, prenom, nom):
        self.nom = nom
        self.prenom = prenom
        self.age = 0

    def verification(self):         
        age = int(input("Quel âge avez-vous ? "))
        try:
            if 0 < age <= 99:
                self.age = age                    
            else:
                print("Vous vous êtes trompé, veuillez retaper un chiffre entre 1 et 99 !")
        except:
            print("L'âge doit être un nombre.")

    def majeur(self):
        if self.age >= 18:
            print("Vous êtes majeur !")
        else:
            print("Vous êtes mineur !")

    def afficher_la_personne(self):
        print("Bonjour, vous vous appelez " + self.prenom + self.nom + ".")
        print("Et vous avez " + str(self.age) + " ans !")
