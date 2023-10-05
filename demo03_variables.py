""" LES VARIABLES """

# *** ATTENTION ***
# Il n'y a pas de constantes en Pyhton!
# Nous utiliserons les convientions légales de programmations pour le "naming" des variables!


# DÉCLARER UNE VARIABLE

# Elles se créent dès lors qu'on leur assigne une valeur.
a = 5
b = "MelYuki"
print("a =", a)
print("b = " + b) # => Concaténation avec l'opérateur "+"

# On peut les réassigner n'importe quand.
a = "reassigned!"
print("a =", a)

# Python n'oblige aucun typage.
# Mais elles en posèdent tout de même un!
a = 10
print(type(a)) # => 'int' = 'integer' = nombre entier
print(type(b)) # => 'str' = 'string' = chaine de caractère

# Caster une variable pour spécifier son type.
c = str(3)
d = int(3)
e = float(3) # => 'float' = 'floating' = nombre décimal
# Afin d'éviter des erreurs d'interprétation lorsqu'on les utilise...


# NAMING

# Règles
# Un nom de variable:
# - DOIT commencer avec une lettre ou un underscore.
# - NE DOIT PAS commencer avec un chiffre.
# - peut UNIQUEMENT contenir des caractères alpha-numeric et des underscores (A-z, 0-9, _)
# - NE PEUT PAS être un mot-clé réservé à Python.
# - EST sensible à la casse. (age et Age sont 2 variables différentes!)
# - DEVRAIT toujours s'écrire en anglais.

# Légal (conventions, bonnes pratiques)
myvar = "MelYuki" # n'est pas très lisible donc ne s'utilise pas!
myVar = "MelYuki" # bonne pratique! => camelCase
my_var = "MelYuki" # bonne pratique! => snake_case
_my_var = "MelYuki" # OK mais peu utilisé à ma connaissance.
myVar2 = "MelYuki" # OK
MYVAR = "MelYuki" # convention utilisée pour déclarer les CONSTANTES et comprise par Python!

# Illégal (commenté car ce sont des erreurs pour l'IDE)
# 2myvar = "MelYuki"
# my-var = "MelYuki"
# my var = "MelYuki"

# Tips
# Camel Case
myVarName = "MelYuki"
# Pascal Case
MyVarName = "MelYuki"
# Snake Case
my_var_name = "MelYuki"


# ASSIGNATION MULTIPLE

# Python permet de déclarer et d'assigner plusieurs variables sur une ligne (inLine).
f, g, h = "Pomme", "poire", "habricot"
print(f, g, h)

# De même, assigner une valeur à plusieurs variables.
f = g = h = "Pomme"
print(f, g, h)

# Unpacking
# Extraire les valeurs d'une collection (liste, tuple, tableau...) dans des variables.
fruits = ["Pomme", "poire", "habricot"]
f, g, h = fruits
print(f, g, h)


# PORTÉE DES VARIABLES (locales et globables)

# Globales
# Ce sont des variables déclarées et assignées en début de code qui seront utilisables par tout le monde.
# (les fonctions seront détaillées plus tard!)
x = "fine"

def myFunction():
    print("I'm " + x)

myFunction()
# La variable globale "x" est utilisable à l'intérieur la fonction "myFunction()" et dans tout le reste du programme.

def myFunction2():
    x = "not ok"
    print("I'm " + x)

myFunction2()
print("I'm", x)
# On a réassigné la variable "x" dans la fonction.
# Mais de retour hors de la fonction, "x" reprend sa valeur globale.

# Locales
# Ces variables ne seront utilisables que dans les blocs dans lesquels elles existent et ont été créées,
# mais pas en dehors.
def myFunction3():
    y = "So that's ok!" # variable locale!
    print(y)

myFunction()
myFunction3()
# print("I'm", x, y) # => NameError: name 'y' is not defined

# Le mot-clé "global"
# Une varibale locale peut devenir globale.
def myFunction4():
    global z
    z = "let's go!"

myFunction4() # l'appelle de la fonction active la variable globalement.

print("I'm ready,", z)
