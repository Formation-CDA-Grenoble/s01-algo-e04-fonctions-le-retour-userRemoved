def concatenate(list):
    # Début de ton code
    # Dans le fichier **exo3.py**, tu dois écrire une fonction qui concatène tous les éléments d'une liste.


    return list.join(list) 
    # Fin de ton code

    

# Pas touche!
tests = (
    (["a", "b", "c"], "abc"),
    (["pomme", "banane", "orange"], "pommebananeorange"),
    ([1, 2, 3], "123"),
    (["a", "b", "c", 1, 2, 3], "abc123"),
)

for test in tests:
    print(f"L'appel  concatenate({test[0]})  renvoie: {concatenate(test[0])} (résultat attendu: {test[1]})")
