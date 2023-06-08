#Sawadogo Marie Fabienne
#300101795
#Devoir1 question 3


print("Bonjour")

#fonction 1
def lb_en_kg(lb) :
    "convertir lb en killo"
    kg = lb * 0.4536
    return kg

lb = float(input("entrez le nombre de livres svp : "))
n_lb = lb_en_kg(lb)

#fonction2
def oz_en_kg(oz) :
    "convertir oz en killo"
    kg = oz / 35.274
    return kg

oz = float(input("entrez le nombre de onces svp : "))
n_oz = oz_en_kg(oz)
ValeurKg = n_lb + n_oz
print(lb, "livres et", oz, "onces",  " équivalent à :", ValeurKg, "killogrammes")
