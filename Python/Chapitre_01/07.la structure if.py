# on recrée un dictionnaire
d = {'Race': 'Maître du temps', 'Vaisseau': 'TARDIS', 'nom': 'Le Docteur', 'Origine': 'Gallifrey'}

# on le test dans une structure if
if d["nom"] == "Le Docteur":
	print("Sauvé ! c'est le docteur !")

# un test de différence, pour voir
if d["nom"] != "Le Docteur":
	print("Sauvé ! c'est le docteur !")

# avec un else pour tester le cas vrai et le cas faux	
if d["nom"] == "Le Docteur":
	print("Sauvé ! c'est le docteur !")
else:
	print("Perdu ! ce n'est pas le docteur !")

# on modifie le nom pour voir si le else s'exécute
d["nom"] = "Dalek"

if d["nom"] == "Le Docteur":
	print("Sauvé ! c'est le docteur !")
else:
	print("Perdu ! ce n'est pas le docteur !")