""" LES LISTES [] """

# Elles permettent de ranger plusieurs éléments de types différents dans une variable.
# Elles sont ordonnées, mutables et acceptent la duplication de valeurs!


# CRÉATION DE LA LISTE

myList = ["Pomme", 1, True, "Pomme", 3, "Poire"]
print(myList)

# On peut mesurer leur longueur - len()
print(len(myList)) # => 6, car 6 éléments dans la liste


# ACCÉDER AUX ÉLÉMENTS

# Les éléments de la liste sont indexés en commençant par 0
print(myList[0]) # à l'index [0], se trouve l'élément 1, qui a pour valeur "Pomme"

# Ils ont également un deuxième index négatif en commençant par la fin avec -1
print(myList[-1]) # à l'index [-1], se trouve le dernier élément
print(myList[-2]) # à l'index [-2], se trouve l'avant-dernier élément

# Accéder à plusieurs valeurs en spécifiant un "range"
print(myList[2:5]) # => [True, 'Pomme', 3], car 2 est inclusif et 5 est exclusif!
print(myList[:4]) # => depuis le premier index (0), jusqu'à l'index 4 exclu!
print(myList[2:]) # => depuis l'index 2 inclus, jusqu'au dernier élément!

# De même avec les index négatifs
print(myList[-4:-1]) # du -4 inclu, jusqu'au -1 exclu!

# Vérifier si un élément existe avec une condition et le mot-clé "in"
if "Poire" in myList:
    print("Oui, Poire est dans la liste! ^^")


# MODIFIER

# un élément
myList[1] = "un"
print(myList)

# un range d'éléments
myList[1:3] = [1, False]
print(myList)

# Si on insert PLUS d'éléments à remplacer,
# ils seront ajouter après le dernier remplacer.
myList[1:2] = ["un", "PLUS"]
print(myList)

# Si on insert MOINS d'éléments à remplacer,
# cela aura un effet de suppression.
myList[1:3] = ["MOINS"]
print(myList)

# La méthode insert()
# Elle permet d'insérer un élément, à un index précis, sans remplacer les valeurs existantes.
myList.insert(2, "Insert")
print(myList)

# Ces modifications (insert) auront pour conséquences de modifier l'ordre et la longueur de la liste!


# AJOUTER

# La méthode append()
myList.append("Ajout ordonné") # ajoutera à la fin ( liste ordonnée)
print(myList)

# La méthode extend()
# Permet d'ajouter les éléments d'une "collection" dans une autre.
noms = ["Pierre", "Paul", "Jacques"]
myList.extend(noms)
print(myList)


# SUPPRIMER

# La méthode remove()
myList.remove("Jacques")
print(myList)

# Si la valeur existe en double dans la liste,
# cela supprime uniquement la première occurence.
myList.remove("Pomme")
print(myList)

# La méthode pop()
# Permet de supprimer un élément à l'index précisé.
myList.pop(2)
print(myList)

# Si on ne spécifie pas d'index,
# cela supprime le dernier élément.
myList.pop()
print(myList)

# Le mot-clé "del" pour delete
# Permet également de supprimer un élément à l'index précisé.
del myList[2]
print(myList)

# Mais aussi de supprimer la liste entière, jusqu'à la variable, si on ne précise pas d'index!
del myList
# print(myList) # => NameError: name 'myList' is not defined

# La méthode clear()
# Permet d'éffacer le contenu de la liste, de la vider.
# Mais ici, la variable et la liste existe toujours.
myList = ["Pomme", 1, True, "Pomme", 3, "Poire"]
myList.clear()
print(myList)
