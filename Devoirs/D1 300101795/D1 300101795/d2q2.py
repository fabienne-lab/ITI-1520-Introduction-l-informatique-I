#Sawadogo Marie Fabienne
#300101795
#Devoir 2 question 2

print("bonjour")

#montant d'argent
Montant = float(input("Entrez le montant en dollars svp : "))
ValeurArgent = 100 * Montant

#monnaie 25
Monnaie25 = ValeurArgent // 25
Reste1 = ValeurArgent % 25

#monnaie 10    
Monnaie10 = Reste1 // 10
Reste2 = Reste1 % 10

#monnaie 5
Monnaie5 = Reste2 // 5
Reste3 = Reste2 % 5

#monnaie 1
Monnaie1 = Reste3 // 1
Reste4 = Reste3 % 1

#Monnaie Totale
MonnaieTotale = Monnaie25 + Monnaie10 +Monnaie5 + Monnaie1
print("Le nombre minimal de pièces que le caissier peut rendre est : " , MonnaieTotale)
print("Thanks for using this System")





