# un dictionnaire
{"nom": "Le Docteur", "Origine": "Gallifrey", "Race": "Maître du temps"}

d = {"nom": "Le Docteur", "Origine": "Gallifrey", "Race": "Maître du temps"}
dir(d)

# récupération d'un élément
d["nom"]

# ajout d'un émément
d["Vaisseau"] = "TARDIS"

# suppression d'un élément
del(d["Vaisseau"])

# la liste des clés
d.keys()
list(d.keys())

# la liste des valeurs
list(d.values())
