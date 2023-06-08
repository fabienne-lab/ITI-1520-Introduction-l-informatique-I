#SAWADOGO MARIE FABIENNE
#300101795


#annee en secondes lumiere
def anneeEnSecondes(AnneeLumiere):
    "convertit annee siderale en annee lumiere"
    SecondeLumiere = AnneeLumiere * 31558464
    return SecondeLumiere

AnneeLumiere = float(input("Entrez un nombre d’années-lumière: "))
SecondeLumiere = anneeEnSecondes (AnneeLumiere)
print("Le nombre de secondes-lumière est :", SecondeLumiere)

#secondes lumiere en km
def secondesLumiereEnKm(SecondeLumiere):
    "convertit seconde lumiere en km"
    Distance = SecondeLumiere * 300000
    return Distance
Distance = secondesLumiereEnKm(SecondeLumiere)
print("La distance est :", Distance, "Km")


#distance entre deux etoiles
def distanceEntreEtoile (AnneeLumiere1, AnneeLumiere2):
    "converti les annee lumiere en km"
    SecondeLumiere1 =  anneeEnSecondes(AnneeLumiere1)
    SecondeLumiere2 =  anneeEnSecondes(AnneeLumiere2)
    Distance1 = secondesLumiereEnKm(SecondeLumiere1)
    Distance2 = secondesLumiereEnKm(SecondeLumiere2)
    dis = Distance1 + Distance2
    return dis


AnneeLumiere1 = float(input("Entrez la distance de la première étoile, en années-lumière: "))
AnneeLumiere2 = float(input("Entrez la distance de la deuxième étoile, en années-lumière: "))
dis =  distanceEntreEtoile  (AnneeLumiere1, AnneeLumiere2)
print("La distance entre les deux étoiles est : ", dis)
print("thanks for using this systeme")



