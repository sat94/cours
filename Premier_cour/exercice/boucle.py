from fonction_question import question


# pour crée un dictionnaire

personne = {} # Initialisation d'un dictionnaire vide
for i in range(1,5):
    personne[i]=question()


#pour crée une liste
    
personnes =  [] # Initialisation d'une liste vide
for i in range(1, 5):
    reponse = question()
    personnes.append(reponse)



