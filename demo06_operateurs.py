""" LES OPÉRATEURS """

# À retenir:
# PEMDAS: (), **, *, / ou //, +, -
# Ceci nous donne l'ordre dans lequel le programme effectuera les opérations!


# MATHÉMATIQUES

a = 5
b = 2

# Les classiques (+ - * /)
addition = a + b # => 7
substraction = a - b # => 3
multiplication = a * b # => 10
division = a / b # => ?
print(division)
print(type(division))
# La division classique donnera une division "complète",
# et modifiera le type de la variable qui contient le résultat!

# La division entière (//)
floor_division = a // b # => ?
print(floor_division)
print(type(floor_division))
# La division entière arrondira le résultat à l'entier inférieur,
# et NE modifiera donc PAS le type de la variable qui contient le résultat!

# Le modulo (%)
modulo = a % b # => ?
print(modulo)
# Il donnera comme résultat, ce qui reste de la division entière.
# Très pratique pour savoir si un nombre est divisible par un autre.
# (pair/impair, multiple de 3, etc...)

# Exposant (**)
exponentiation = a ** b
print(exponentiation)


# D'AFFECTATION

# Combiner un "=" avec un opérateur,
# pour factoriser le code.
c = 3
# Au lieu d'écrire,
# c = c + b
# On écrit,
c += b
print(c) # => 5
# On réaffecte donc une nouvelle valeur à la variable "c",
# en utilisant sa valeur première et en effectuant une opération dessus.
c -= b # => ?
c *= b # => ?
c /= b # => ?

# Ceux ci-dessus sont les classiques.
# Mais cela fonctionne avec tous les autres opérateurs.


# LOGIQUES (and, or, not) et de COMPARAISON (==, !=, <, >, <=, >=)

# Avec les opérateurs d'affectation,
# on les utilisera dans les "conditions" et les "boucles".
# *** ATTENTION ***
# Une comparaison retournera TOUJOURS un boolean! (True ou False)
print(a == b) # égale, => ?
print(a != b) # différent, => ?
print(a < b) # plus petit que, => ?
print(a > b) # plus grand que, => ?
print(a <= b) # plus petit ou égale, => ?
print(a >= b) # plus grand ou égale, => ?

print(a < 10 and a > 3)
# Retournera,
# "True" si le résultat de chaque comparaison est égale.
# "False" si les résultats sont différents.
print(b > 5 or b < 10)
#  Retournera,
# "True" si AU MOINS UNE des comparaisons est vraie.
# "False" si AUCUNE n'est vraie.
print(not(a < 10 and a > 3))
# Retourne le résultat inverse!
