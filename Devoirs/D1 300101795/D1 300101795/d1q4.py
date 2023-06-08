#Sawadogo Marie Fabienne
#300101795
#devoir1 qestion 4


def numMonnaie(Montant):
    "convertir Montant en MonnaieTotale"
    ValeurArgent = 100 * Montant
    Monnaie25 = ValeurArgent // 25
    Reste1 = ValeurArgent % 25  
    Monnaie10 = Reste1 // 10
    Reste2 = Reste1 % 10
    Monnaie5 = Reste2 // 5
    Reste3 = Reste2 % 5
    Monnaie1 = Reste3 // 1
    Reste4 = Reste3 % 1
    MonnaieTotale = Monnaie25 + Monnaie10 +Monnaie5 + Monnaie1
    return MonnaieTotale

Montant = float(input("Entrez le montant en dollars: "))
MonnaieTotale = numMonnaie(Montant)
print("Le nombre minimal de pièces que le caissier peut rendre est: ", MonnaieTotale)
