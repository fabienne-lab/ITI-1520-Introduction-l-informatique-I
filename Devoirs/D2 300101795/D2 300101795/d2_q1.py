#Sawadogo Marie Faienne
#300101795

#Ce programme consistera a caluculer l'IMC de lutilisateur en utilisant la formule poid/(taille)**2

#creation de la fontion de bmi qui prend les parametres "taille" et "poids"
#et les retourne en IMC
def bmi(poids, taille):
    '''transforme des poids et taille en IMC, (float)-> float
    '''
    IMC = poids / (taille)**2
    return IMC
#declaration de la variable poids par lutilisateur:
poidS = float(input("SVP entre votre poids en kilogrammes:"))

#declaration de la variabl taille par lutilisateur:
taillE = float(input("SVP entre votre taille en metres:"))

#retour de la valeur de l'IMC apres le calcul
IMC = bmi (poidS, taillE)
print("Votre IMC est: ", IMC)

#creation des condition: IMC<18.5 «maigreur»,  18.5=<IMC<25 «Poids idéal», 25=<IMC<30 «surpoids», IMC>=30 « Obésité »
if IMC < 18.5 :
    print("Maigreur")
elif IMC >= 18.5 and IMC < 25 :
    print ("Poids idéal")
elif IMC >= 25 and IMC < 30 :
    print("surpoids")
else :
    print("Obésité")

print("Merci d'avoir utiliser ce systeme")

