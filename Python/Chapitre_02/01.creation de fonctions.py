# création de fonction
def cree_liste(taille):
	list(range(taille))

# appel de fonction
cree_liste(12)
cree_liste(taille=12)
print(cree_liste(12))

# cela nousq retourne None. Pourquoi ? J'ai oublié de faire un return !	

def cree_liste(taille):
	return list(range(taille))

# maintenant cela me restourne qqch
cree_liste(12)
cree_liste(taille=12)
	
# la fonction peut être appelée partout où je peux utiliser le type de données résultant
for x in cree_liste(12):
	print(x)

# paes paramètres sont requis
cree_liste()

# Créons un paramètre optionnel avec une valeur par défaut
def cree_liste(taille=10):
	return list(range(taille))
	
# créons un paramètre dictionnaire "libre"
def cree_liste(taille=10, **d):
	return d

cree_liste(taille=3)
cree_liste(taille=10, nom="Les Docteur", Vaisseau="TARDIS")