def question():
    prenom = input("Quel est votre prénom ? ")
    age = input("Quel âge avez-vous ? ")

    try:
        age = int(age)
        if age <= 0 or age > 99:
            print("Vous vous êtes trompé, veuillez retaper un chiffre entre 1 et 99 !")
            age = input("Quel âge avez-vous ? ")
        else:
            print(f"Vous vous appelez {prenom}")
            print(f"Et vous avez {age} ans !")
            if age >= 18:
                print("Vous êtes majeur !")
            else:
                print("Vous êtes mineur !")
    except:
        print("L'âge doit être un nombre.")
