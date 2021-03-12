from math import pi


#Perimettre de l'aire d'un cercle Perimettre = 2 x Pi x R
r = float(input("Inserre le rayon ici: "))

perimettre_du_cercle = r * 2 * pi

aire_du_cercle = pi * r * r

print("Voici le perimettre: ", perimettre_du_cercle)
print("Voici l'aire: ", aire_du_cercle)





#Perimettre et aire d'un triangle
a = float(input("Inserre le premier coté du triangle: "))
b = float(input("Inserre le deuxième coté du triangle: "))
c = float(input("Inserre le troisième coté du triangle: "))

perimettre_du_triangle = a + b + c

dp = (a + b + c) / 2

aire_du_triangle = (dp * (dp -a) * (dp - b) * (dp -c))** 0.5

print("L'aire du triangle est: ", aire_du_triangle)





#Convertion du degrès en fereninght
degres = float(input("Insère ici les degrès en c°"))

convertioncf = (degres * 1.8) + 32

print("La conversion en fanhrenheit: ", convertioncf)





#Convertion heures minutes seconde
secondes = float(input("insère ici les secondes que tu veux calculer en heures: "))

minutes =  secondes % 3600 // 60

heures = secondes // 3600

secondes = secondes % 3600 % 60

print(" Le resultat est ", heures,"H", minutes,"m", secondes, "secondes") 
