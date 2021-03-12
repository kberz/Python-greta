note = int(input("ENTREZ une note sur 20: "))

if note <= 10:
    print("Vous n'avez pas eu votre bac :/")

elif note >= 16 and note < 20:
    print("Vous avez eu mention très bien")

elif note >= 12 and note < 14:
    print("Vous avez eu mention assez bien")

elif note >= 14 and note < 16:
    print("Vous avez eu mention bien")

else :
    print("vous essayez de tricher ?")
