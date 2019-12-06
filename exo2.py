def rankInside(list, element):
    # Début de ton code
    # Dans le fichier **exo2.py**, tu dois écrire une fonction qui trouve à quelle place d'une liste se trouve un élément.
     
    joueurs = ( "messi", "ronaldo")
    return joueurs [1]

    # Fin de ton code



# Pas touche!
tests = (
    ([1, 2, 3], 2, 1),
    ([1, 2, 3], -1, None),
    (["pomme", "banane", "orange"], "pomme", 0),
    (["pomme", "banane", "orange"], "cerise", None),
)

for test in tests:
    print(f"L'appel  rankInside({test[0]}, {test[1]})  renvoie: {rankInside(test[0], test[1])} (résultat attendu: {test[2]})")
