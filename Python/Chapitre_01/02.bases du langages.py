print("coucou")
print("coucou", 2 + 2)

# les opérateurs
2 + 2	# addition
8 / 3	# division
8 // 3	# division entière
8 % 3	# modulo
8**2	# élévation à la puissance

# les variables
variable = 1	# ceci est une assignation
variable == 1	# ceci est une comparaison qui renvoie un résultat booléen
variable != 1	# comparaison d'inégalité

# Python est sensible à la casse
I = "3"
type(I)	#<class 'str'>
type(i)	#<class 'int'>

"cou" + "cou"	# concaténation
2 + 2			# addition

i + I		# pas possible, types différents
i + int(I)	# ok en faisant une conversion
str(i) + I	# conversion dans l'autre sens
