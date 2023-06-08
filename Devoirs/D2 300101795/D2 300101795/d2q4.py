#Sawadogo Marie Fabienne
#300101795


#importation de la fontion random qui permettra de donner des valeurs aleatoires
from random import *
#declaration de la variable choix qui dependra de la fontion random entre 0 et 1
Choix = randint(0, 1)

print("Bienvennue!")
print("Ce logiciel va effectuez un test avec une serie de 10 questions pour evaluez votre niveau avant le devoir.")
print("Pour ce faire, ce systeme n'utilise que des nombres positifs")
print("LES DONNÉE SERONT ALEATOIRES")
 #definition de la fonction effectuerTest qui permettra de poser des question aleqtoires sur la multiplication et l'addition a l'eleve       
def effectuerTest (Choix):
    
    Choix = randint(0, 1)
    '''le cas ou le choix est 0 pour l'addition'''
    
    if Choix == 0 :
        Nombre1 = randint(0, 9)
        Nombre2 = randint(0, 9)
        ''' addition entre deux variable de type int: (int, int)-> int'''
        Resultat = int(Nombre1 + Nombre2)
            
        print(Nombre1, " + ", Nombre2, " = ")
        #l'eleve entre sa reponse
        Reponse = int(input("Reponse : "))
        #on utilise True quand la reponse est varie et False quand elle est fausse 
        #on a deux cas: lorsque l'eleve entre le bon resultat et lorsquil entre le mauvais resutat
        if Reponse != Resultat :
            print("Reponse incorrecte la bonne reponse est", Resultat)
            test = False
        #car si le resultat n'est pas la reponse que l'eleve entre alors ca ne peut etre que Reponse == resultat     
        elif Reponse == Resultat:
            print("Bonne Reponse")
            test = True

#si le choix n'est pas 0 alors il sera forcement 1

    else:
        Nombre1 = randint(0, 9)
        Nombre2 = randint(0, 9)
        ''' addition entre deux variable de type int: (int, int)-> int'''
        Resultat = int(Nombre1 * Nombre2)
            
        print(Nombre1, " * ", Nombre2, " = ")
        Reponse = int(input("Reponse : "))
                
        if Reponse != Resultat :
            print("Reponse incorrecte la bonne reponse est", Resultat)
            test = False
             
        elif Reponse == Resultat:
            print("Bonne reponse")
            test = True
            
#va retourner une valeure booleene 
    return bool(test)
#on utilise une valeur bool qui exprime quand le test est vrai ou faux
 #on utilise maintenat une boucle pour faire tourner la fonction 10 fois correspondand au nombre de questions   
compteur = 0
CompteurVrai = 0
CompteurFaux = 0
#le compteur va incrementer les CompteurVrai et CompteurFaux

while compteur <10:
    Test = effectuerTest (Choix)
    
    if Test:
        CompteurVrai += 1
    else:
        CompteurFaux += 1
        
    compteur += 1
if CompteurVrai >= 6 :
    print("vous avez ", CompteurVrai, "Reponses correctes, felicitation!!!. ")
elif CompteurVrai <6 :
    print("vous avez ", CompteurFaux, "Reponses Incorrecte demander a votre enseignant(e) de vous aidez!!!")

    

        

    

     
    
