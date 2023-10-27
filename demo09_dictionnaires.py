""" LES DICTIONNAIRES {key : value}"""

# Les dictionnaires sont utilisés pour ranger des données.
# Ce sont des collections, modifiables, n'acceptant pas la duplication.
# Depuis Python 3.7,
# les dictionnaires sont également ordonnés!
# Les éléments peuvent être de n'importe quel type.


# DÉCLARATION

# On initialisera un dictionnaire avec des {}.
# Dans les {} on y introduira la "clé" d'une donné et la "valeur" de la donnée.
myFavCar = {
    "name" : "Eleanor",
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1967,
}
print(myFavCar)
print(len(myFavCar))
print(type(myFavCar))
print()


# ACCÉDER AUX ÉLÉMENTS

# Obtenir une valeur,
# comme avec les listes et index
print(myFavCar["name"])
# ou via la méthode "get()"
print(myFavCar.get("name"))
print()

# Obtenir les clés,
# avec la méthode "keys()"
print(myFavCar.keys())
print()
# Retournera une liste!

# Obtenir les valeurs,
# avec la méthode "values()"
print(myFavCar.values())
print()
# Retournera une liste!

# Obtenir les clés:valeurs,
# avec la méthode "items()"
print(myFavCar.items())
print()
# Retournera une liste[] de tuples()!
# Les tuples sont des collections NON-modifiables!


# MODIFIER

# On accède simplement à l'élément via la clé,
# et on lui donne une nouvelle valeur
myFavCar["year"] = 1964
print(myFavCar)
print()

# Ou via la méthode "update()"
myFavCar.update({"year" : 1967})
print(myFavCar)
print()


# AJOUTER

# Il n'y a pas de méthode d'ajout pour les dictionnaires en Python!
# On déclarera simplement une nouvellle clé au dictionnaire en initialisant une valeur.
myFavCar["colors"] = ["black", "white"]
print(myFavCar)
print()

# On peut ici encore, utiliser la méthode "update()"
myFavCar.update({"electric" : False})
print(myFavCar)
print()


# SUPPRIMER

# La méthode "pop()"
# Supprimera l'élément dont la clé est donnée en paramètre
myFavCar.pop("electric")
print(myFavCar)
print()

# La méthode "popitem()"
# Depuis Python 3.7,
# le dernier élément inséré est supprimé.
# Avant,
# Cela supprimait un élémént aléatoirement.

# Le mot-clé "del"
# Pareil que pour les collections de type liste.
del myFavCar["name"]
print(myFavCar)
print()
# *** ATTENTION ***
# Si on ne précise pas de clé,
# => del myFavCar
# cela éffacera le dictionnaire et le supprimera!
# => print(myFavCar), ceci donnera donc une erreur puisque le dictionnaire n'existera plus!

# La méthode "clear()"
# Éffacera simplement le dictionnaire.
# Il existera toujours mais sera vide!
myFavCar.clear()
print(myFavCar)


# On pourra aussi:
# - Boucler
# - Copier
# - Imbriquer
