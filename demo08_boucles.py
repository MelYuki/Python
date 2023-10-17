""" LES BOUCLES """

# "while" & "for"
# Elles permettent:
# - de continuer de faire tourner un programme tant que la condition est vraie,
# jusqu'à une limite définie ou jusqu'à ce que l'utilisateur décide de l'arrêter.
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

# Pour parcourir et afficher tous les éléments d'une liste,
# il va falloir créer une boucle (for) qui va lire chaque élément, pour ensuite l'afficher.
myList = ["Pomme", 1, True, "Pomme", 4, "Poire"]
for element in myList:
    print(element)
# On dit au programme,
# "pour" chaque "élément" "dans" "ma liste": "affiche"("l'élément")

# On peut également faire tout cela via les index,
# avec pour "range" la "longueur" de la liste.
# Habituellement on utilise "i" pour les itérations.
for i in range(len(myList)):
    print() # un simple saut de ligne pour la clareté.
    print(i) # en faisant cela, nous affichons l'index des éléments!
    print(myList[i]) # ici nous affichons bien l'élément de la liste, récupéré à l'index!

