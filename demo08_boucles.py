""" LES BOUCLES """

# "while" & "for"
# Elles permettent:
# - de continuer de faire tourner un programme tant que la condition est vraie,
#   jusqu'à une limite définie ou jusqu'à ce que l'utilisateur décide de l'arrêter.
# - d'afficher les éléments d'une collection.



# LA BOUCLE "while"

i = 1
while i <= 5:
    print(i)
    i += 1
print()
# On déclare une variable d'incrémentation à afficher (i).
# On lui donne une condition d'arrêt de boucle.
# Dans le bloc:
# - une expression à exécuter
# - Sans oublier d'incrémenter i à chaque fin de boucle!

# *** ATTENTION ***
# Si on n'incrémente pas "i" avec "i += 1",
# On créera une boucle INFINIE !!!
# Ce qui peut être plutôt dangereux pour la machine!


# Le "break"
# Permet de stopper la boucle, même si la condition est toujours vraie.
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
print()


# Le "continue"
# Permet de stopper l'itéraction actuelle et de passer à la suivante.
i = 0
while i <= 5:
    i += 1
    if i == 3:
        continue
    print(i)
print()


# Le "else"
# Permet d'exécuter un dernier bloc de code une fois la boucle terminée.
# C'est à dire, lorsque la condition n'est plus vraie.
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print('"i" est maintenant plus grand que 5!')
print()



# LA BOUCLE "for"

# Parcourir et afficher tous les éléments d'une liste,
# il va falloir créer une boucle (for) qui va lire chaque élément, pour ensuite l'afficher.
myList = ["Pomme", 1, True, "Pomme", 4, "Poire"]
for element in myList:
    print(element)
# On dit au programme,
# "pour" chaque "élément" "dans" "ma liste": "affiche"("l'élément")

# Parcourir une chaîne de caractères.
for char in myList[0]:
    print(char)
print()


# Le "break"
for element in myList:
    print(element)
    if element == 4:
        break
print()
# Si on met le "print(element)" après la condition:
for element in myList:
    if element == 4:
        break
    print(element)
print()


# Le "continue"
for element in myList:
    if element == 4:
        continue
    print(element)
print()


# La fonction "range()"
# Elle retourne une séquence de nombres,
# commençant par 0 par défaut,
# s'incrémentant de 1 par défaut,
# et fini à un nombre spécifié.
for i in range(10):
    print(i)
print()
# On remarque ici qu'on obtient bien 6 valeurs, en commençant par 0!
# Le 6 est donc exclusif!

# Et donc dans une liste via les index...
for i in range(len(myList)):
    print()
    print(i) # en faisant cela, nous affichons l'index des éléments!
    print(myList[i]) # ici nous affichons bien l'élément de la liste, récupéré à l'index!
print()

# Si le premier paramètre donné est la limite,
# On peut en rajouter un pour modifier la valeur par défaut de commencement.
for i in range(2, 10):
    print(i)
print()
# La valeur de début est inclusive!

# On peut en rajouter encore un autre pour modifier la valeur par défaut de l'incrément.
for i in range(2, 10, 2):
    print(i)
print()

# Le "else"
for i in range(10):
    print(i)
else:
    print("Boucle terminée!")
print()

# *** ATTENTION ***
# Si un "break" se trouve dans la boucle,
# le bloc "else" ne s'exécutera pas !!!
for i in range(10):
    print(i)
    if i == 5: break
else:
    print("Boucle terminée!")
print()


# Les boucles imbriquées (Nested For Loops)
integers = [1, 2, 3, 4, 5]
strings = ["un", "deux", "trois", "quatre", "cinq"]

for num in integers:
    print("Première boucle à l'élément :", num)
    for string in strings:
        print("Seconde boucle...", string)
    print()
# Ce concept d'imbrication existe aussi avec les conditions (Nested If)!