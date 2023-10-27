""" LES FONCTIONS """

# Une fonction:
# - C'est un bloc de code qui sera exécuter quand il sera appelé.
# - On peut lui passer des données, arguments(args), paramétres.
# - Elle peut retourner une donnée comme résultat.


# CRÉATION DE LA FONCTION
# On la définit(def) en utitilisant le mot-clé "def".
def myFunc1():
    print("\nHello World!")
# APPEL DE LA FONCTION
myFunc1()


# PARAMÈTRES & ARGUMENTS

def myFunc2(name):
    print("\nHello", name)

myFunc2("MelYuki")

# Pour la compréhension:
# - Un paramètre est une variable listée entre parenthèses à la définition de la fonction.
# - Un argument est une valeur envoyée à la fonction lorsqu'on l'appelle.
# On peut insérer autant de paramétres que l'on souhaite.
# Par défaut,
# une fonction DOIT être appelée avec le même nombre d'arguments qu'elle a de paramètres!
def myFunc3(fName, lName):
    print(f"\nHello {fName}, your family name is {lName}.")

# myFunc3() => ERROR! car on a donné aucun argument!
# myFunc3("MelYuki") => ERROR! car on a donné un seul argument!
myFunc3("Mel", "Yuki")

# *** ATTENTION ***
# La fonction comprendra les paramètres grâce l'ordre des arguments donnés!
# Si on veut entrer les arguments dans le désordre,
# On fera ceci:
myFunc3(lName= "Yuki", fName= "Mel")


# ARGUMENTS ARBITRAIRES

# Si on ne connait pas le nombre d'arguments qu'on recevra,
# on ajouter "*" devant le paramètre!
# La fonction recevra alors un tuple d'arguments auquel elle aura accès.
def myFunc4(*names):
    print("\nHere is the students's name:")
    for name in names:
        print("-", name)

myFunc4("Sacha", "Naomi")
myFunc4("Pierre", "Paul", "Jacques")


# PARAMÈTRE PAR DÉFAUT

def myFunc5(toGreet= "World"):
    print("\nHello", toGreet)

myFunc5()
myFunc5("MelYuki")


# RETURN

def myFunc6(x):
    return 10 * x

print()
print(myFunc6(2))
print(myFunc6(5))


# RECURSIVE

# Une fonction récursive est une fonction qui s'appelle elle-même.
# Si c'est un joli procédé mathématique,
# il est facile de faire des grosses erreurs !!!
# *** ATTENTION *** 
# Ne pas créer de récursive infinie!
# Gare à l'utilisation excessive de la mémoire du processeur!
def myFunc7(num):
    if num > 0:
        result = num + myFunc7(num - 1)
        print(result)
    else:
        result = 0
    return result

print()
myFunc7(10)
