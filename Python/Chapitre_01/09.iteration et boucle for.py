# on recrée le dictionnaire
d = {'Race': 'Maître du temps', 'Vaisseau': 'TARDIS', 'nom': 'Le Docteur', 'Origine': 'Gallifrey'}

# la boucle for permet de parcourir les clés du dictionnaire
for x in d:
	print(x)

# on pourrait retrouver les valeurs ainsi
for x in d:
	print(d[x])

# même chose en formatant un petit peu
for x in d:
	print(x, ":", d[x])

# que puis-je faire avec un dictionnaire
dir(d)

# essayons l'itération sur les valeurs
for x in d.values():
	print(x)

d.values()
list(d.values())

# et les paires clé-valeur ?
d.items()

# itération sur items
for x, v in d.items():
	print(x, v)

# avec un peu de formatage
for x, v in d.items():
	print(x, '\t:\t', v)

# itération sur une liste
for x in [1,2,3,4]:
	print(x)

# utilisons la fonction range pour créer un itérable à la volée
for x in range(10):
	print(x)

# pour avoir les nombres de 1 à 10
for x in range(1, 11):
	print(x)
