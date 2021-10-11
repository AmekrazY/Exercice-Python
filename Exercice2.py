temp = 0   # declaration d'une variable temporaire pour l'echange
a = int(input("Entrer la premiere valeur : \n "))    # Saisir le premier entier
# Saisir l'entier
b = int(input("Entrer la deuxieme valeur : \n "))     # Saisir le deuxieme entier
print(f"Avant l'echange,le 1er entier = {a} ,et le 2ème = {b} ")
temp = a      # L'echange des entiers
a = b
b = temp
print(f"Apres l'echange,le 1er entier = {a} ,et le 2ème = {b} ")   # On affiche les entiers