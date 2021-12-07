# on recrée le dictionnaire, au cas où
d = {'Race': 'Maître du temps', 'Vaisseau': 'TARDIS', 'nom': 'Dalek', 'Origine': 'Gallifrey'}

# on essaie d'interpoler
if d["nom"] == "Le Docteur":
	print("Sauvé ! c'est le docteur !")
else:
	print("Perdu ! ce n'est pas le docteur ! Qui est cet inconnu nommé d['nom'] ?" )
	
# est-ce que ça marche ? -- Non

# on peut faire comme ceci 
if d["nom"] == "Le Docteur":
	print("Sauvé ! c'est le docteur !")
else:
	print("Perdu ! ce n'est pas le docteur ! Qui est cet inconnu nommé", d["nom"], "?" )

# mais on peut aussi interpoler, de cette façon : 
"qui est l'inconnu nommé %s ?" % d["nom"]
"qui est l'inconnu nommé %(nom)s ?" % d
"qui est l'inconnu nommé {0} ?".format(d['nom'])

# ce qui nous donne
if d["nom"] == "Le Docteur":
	print("Sauvé ! c'est le docteur !")
else:
	print("Perdu ! ce n'est pas le docteur ! Qui est cet inconnu nommé %s ?" % d['nom'] )

# ou aussi
if d["nom"] == "Le Docteur":
	print("Sauvé ! c'est le docteur !")
else:
	print("Perdu ! ce n'est pas le docteur ! Qui est cet inconnu nommé {0} ?".format(d['nom']) )
	
# ou aussi
if d["nom"] == "Le Docteur":
	print("Sauvé ! c'est le docteur !")
else:
	print("Perdu ! ce n'est pas le docteur ! Qui est cet inconnu nommé %(nom)s ?" % d )

# et avec un elif pour traiter un autre cas connu
if d["nom"] == "Le Docteur":
	print("Sauvé ! c'est le docteur !")
elif d["nom"] == "Dalek":
	print("Perdu ! c'est un Dalek !")
else:
	print("Mon Dieu ! ce n'est pas le docteur ! Qui est cet inconnu nommé %(nom)s ?" % d )

# changeons le nom pour faire le test
d["nom"] = "Cyberman"

if d["nom"] == "Le Docteur":
	print("Sauvé ! c'est le docteur !")
elif d["nom"] == "Dalek":
	print("Perdu ! c'est un Dalek !")
else:
	print("Mon Dieu ! ce n'est pas le docteur ! Qui est cet inconnu nommé %(nom)s ?" % d )