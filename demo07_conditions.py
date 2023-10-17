""" LES CONDITIONS """


# LA CONDITION "if"

# Dans une liste,
myList = ["Pomme", 1, True, "Pomme", 4, "Poire"]
# on peut vérifier si un élément existe avec une condition et le mot-clé "in"
if "Poire" in myList:
    print("Oui, Poire est dans la liste. ^^")
if "Banane" not in myList:
    print("Mais, Banane n'y est pas!")
print()

# *** ATTENTION ***
# Python ne demande pas de ";" en fin de bloc ou autres signes particuliers.
# Mais il OBLIGE l'identation!
# On ouvre le bloc avec les ":".
# Ensuite,
# L'espace en début de ligne permet de lui signifier qu'on est dans le bloc de la condition! (ligne 10 et 12)

a = 5
b = 2

if b < a:
    print('"b" est plus petit que "a"')

# Que se passe-t-il si la condition n'est pas vraie?
# En changeant le comparateur par exemple...
if b > a:
    print('"b" est plus grand que "a"')
# Et bien rien du tout!
# Puisque on entre jamais dans le bloc à exécuter,
# vu que la condition n'est pas vraie!
# On doit donc lui dire d'exécuter autre chose si la condition est fausse.


# if ... ELSE
if b > a:
    print('"b" est plus grand que "a"')
else:
    print('"b" N\'est PAS plus grand que "a"')
# Et si les valeurs était égales?
# On entrerait ni dans le "if", ni dans le "else"...
# Comment faire alors?
# En rajoutant un bloc de vérification entre les deux!


# if ... ELIF (else if) ... else
b = 5 # on redéfinit "b" pour l'exemple.
if b > a:
    print('"b" est plus grand que "a"')
elif b == a:
    print('"a" et "b" sont de valeur égale')
else:
    print('"b" N\'est PAS plus grand que "a"')
print()
# On peut rajouter autant de "elif" que nécessaire!

# *** ATTENTION ***
# L'ordre des blocs à de l'importance!!!
b = 2 # on redonne sa valeur à "b"


# SHORTS HAND & TERNAIRE

# Short Hand "if"
# Si on a qu'une seule ligne à exécuter, on peut écrire en inline!
if b < a: print('"b" est plus petit que "a"')
print()

# Short Hand "if ... else"
# Qu'on appelle aussi "ternaire".
print('"a" est plus grand') if a > b else print('"b" est plus grand')
print()

# Avec avec un bloc dans un bloc
# En reprenant l'idée du a == b...
print('"a" est plus grand') if a > b else print('"a" et "b" sont de valeur égale') if a == b else print('"b" est plus grand')
b = 5
print('"a" est plus grand') if a > b else print('"a" et "b" sont de valeur égale') if a == b else print('"b" est plus grand')
b = 10
print('"a" est plus grand') if a > b else print('"a" et "b" sont de valeur égale') if a == b else print('"b" est plus grand')
# On entre bien dans chaque bloc...
