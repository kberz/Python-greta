#Test de pureté
print("Bonjour bienvenue sur le best jeu ever been created by the K-Corp")

def reponse_question (question)
    reponse = "0"
    while (reponse != "Oui") and (reponse != "Non"):
        reponse = input(question "(Oui ou Non)")
    return reponse

x = reponse_question
