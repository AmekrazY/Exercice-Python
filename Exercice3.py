max = 0       # declaration de la variable max
# Saisie des trois entiers a, b, c
a = int(input("Entrer la valeur de a : \n "))
b = int(input("Entrer la valeur de b : \n "))
c = int(input("Entrer la valeur de c : \n "))
if a > b:
    max = a
elif b > c:
    max = b
else:
    max = c
print(f"le maximum de { a },{ b } et{ c } est : { max }")   # Affichage du maximum