""" LES STRINGS """

# Les "strings" sont des chaînes de caractères.
# Il y a plusieurs façon de les déclarer, les assembler et les manipuler.
# Nous pouvons également les considérer comme des collections. (plus avancé)


# DÉCLARATION

# Nous utilisons des "double quotes"
greet1 = "Hello 1"

# Mais aussi des 'simple quotes'
greet2 = 'Hello 2'

# On peut écrire sur plusieurs lignes,
# avec des """ """
greet3 = """Hello
World 3 ! """
# ou des ''' '''
greet4 = '''
Hello
World 4 ! '''
# Les décalages ont leur importance!

print(greet1)
print(greet2)
print(greet3)
print(greet4)
print()

# Si je veux afficher => Il y a de "pires" languages!
# Je ne pourrai pas utiliser les "" dans le string,
# si je déclare mon string avec des ""
# Exemple:
# message = "Il y a de "pires" languages!" # => SyntaxError: invalid syntax
    # "pires" se retrouve hors de la chaîne de caractère!
# Je devrai alors utiliser les ''
message1 = 'Il y a de "pires" languages!'
print(message1) # Et ici tout va bien!

# De même,
# Si je veux afficher => Bienvenue à l'école!
# Je ne pourrai pas utiliser les ''
message2 = "Bienvenue à l'école!"
print(message2)

# MAIS,
# Il y a tout de même un moyen "d'échapper" les symboles qui posent problèmes.
# Grâce au backslash (\), à insérer avant le symbole qu'on veut échapper!
# Si on reprend l'exemple ci-dessus...
message = "Il y a de \"pires\" languages!"
print(message)
print()


# CONCATÉNATION

# En utilisant l'opérateur "+"
firstname = "Mel"
lastname = "Yuki"
age = 340
birthYear = 1683
fullname = firstname + " " + lastname
print("Vous vous appelez " + fullname + " !")

# Concaténation ou opération ??
# Il faut ABSOLUMENT faire attention aux types des variables à concaténer !!!
# text = "Je suis " + firstname + " et j'ai " + age + "ans."
# print(text) # => TypeError: can only concatenate str (not "int") to str
text1 = "Je suis " + firstname + " et j'ai " + str(age) + " ans."
print(text1) # nous avons du retyper la variable "age" au format str.
print()
# Si le programme voit un opérateur comme "+" et un int comme "age" il va vouloir faire une opération,
# alors qu'on veut faire de la concaténation!

# Tips
# On peut aussi utiliser des ","
print("Je m'appelle", firstname, lastname)
print("Je m'appelle", fullname, "!")
# Cela évite de devoir rajouter des espaces partout...

text2 = "Je suis", firstname, "et j'ai", age, "ans."
print(text2) # ATTENTION, nous avons créé une liste d'éléments!
# Les "," vont s'utiliser dans la méthode "print()"
print("Je suis", firstname, "et j'ai", age, "ans.") # pas besoin de retyper ici...
print()


# FORMATER

# La méthode format()
text3 = "Je suis " + firstname + " et j'ai {} ans."
print(text3.format(age))

# Avec plusieurs valeurs,
# Les paramètres doivent être dans l'ordre!
text4 = """
Je suis {} et j'ai {} ans.
Je suis né en {}!"""
print(text4.format(firstname, age, birthYear))

# On pourra changer l'ordre,
# mais il faudra donner l'index dans les {}
text5 = """
Je suis {1} et j'ai {0} ans.
Je suis né en {2}!"""
print(text5.format(age, firstname, birthYear))

# Personnellement,
# j'utilise cette manière de faire!
print(f"""
Je suis {firstname} et j'ai {age} ans.
Je suis né en {birthYear}!""")
# Il y a avant les """, un petit "f" qui signifie qu'il faudra formater les variables entre {} dans le string!
# Ceci ne se trouve pas dans les livres! ;)
print()


# MANIPULATION

# Comme dit plus haut,
# il faut voir les strings comme des collections.

greeting = "Hello world!"
print(greeting)
print(len(greeting)) # => 12, la longueur du string
print(greeting[0]) # => H, le caractère à l'index O
print(greeting[3:9]) # => lo wor, les caractères de l'index 3 inclu à l'index 9 exclu
# etc...

# Plusieurs méthodes de modifications...

# La méthode upper()
# Transforme les caractères en majuscule.
print(greeting.upper())

# La méthode lower()
# Transforme les caractères en minuscule.
print(greeting.lower())

# La méthode capitalize()
# Converti le premier caractère en majuscule.
print(greeting.capitalize())

# Il y a bien d'autres méthodes intéressantes à voir qui s'appliquent également aux collections!


# Pour rire...
reverseGreet = ""
for char in greeting:
    reverseGreet = char + reverseGreet
print("reverseGreet =", reverseGreet)
