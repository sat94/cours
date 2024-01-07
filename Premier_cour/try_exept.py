try:
    # Code qui peut générer une erreur
    resultat = 10 / 0


except ZeroDivisionError:
    # Code qui s'exécute en cas d'erreur spécifique (ici, division par zéro)
    print("Division par zéro n'est pas possible.")
