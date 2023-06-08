#Sawadogo Marie Fabienne
#300101795

#Importation de la fonction random qui va donner des valeurs aleatoires de a et b

from random import *

#Definition de la Fonction effectuerTest 
def effectuerTest (Choix):
    '''la fonction prend le choix de l'eleve et lui pose les questions correspondant 0 pour l'adition et 1 pour la multiplication'''
    #on defini le compteur a zero et la reponse correcte aussi a zero puisquelle sera compter au fur et a mesure
    #NB: les entrees sont toutes en int car on ne travail qu'avec des nombres entiers.
    #on defini le compteur a 0 et ReponseCorrecte a 0 pour incrementer la valeur de ReponseCorrecte pour compter le vombre de reponse positive

    Compteur = 0
    ReponseCorrecte = 0
    #premier cas le choix = 0 pour l'addition
    if Choix == 0:
        #on utilise une boucle while qui execute les conditions ci dessous tant que Compteur<10
        while Compteur < 10 :#pour sarreter a 10 car on ne doit posser que 10 questions
            Nombre1 = randint(0, 9)
            Nombre2 = randint(0, 9)
            ''' addition entre deux variable de type int: (int, int)-> int'''
            Resultat = int(Nombre1 + Nombre2)
            
            print(Nombre1, " + ", Nombre2, " = ")
            Reponse = int(input("Reponse : "))
            '''on a deux cas: lorsque leleve entre le bon resultat et lorsqu'il entre le mauvais resutat'''
            if Reponse != Resultat :
                print("Reponse incorrecte la bonne reponse est", Resultat)
             
            elif Reponse == Resultat:
                print("Bonne Reponse")
                ReponseCorrecte += 1
              
            Compteur += 1
        ''' quand le nombre de  reponse correcte est plus grand que 6 il a reusi sinon il doit voir le prof on utilise alors if et else'''
        if ReponseCorrecte >= 6:
             print("vous avez", ReponseCorrecte, "Reponses correctes, GOOD JOB")
             print("Felicitation et a la prochaine.")
        else :
             ReponseIncorrecte = 10 - int(ReponseCorrecte) 
             print("vous avez", ReponseIncorrecte, "Reponses Incorrectes, Demandez à votre enseignant(e) de vous aider. ")

    # deuxieme cas: le choix est 1 pour la multiplication
   

    elif Choix == 1:
        #on utilise une boucle while qui execute les conditions ci dessous tant que Compteur<10
         while Compteur < 10 :
             #la fonction random qui va permettre de generer des nombre alatoires
            Nombre1 = randint(0, 9)
            Nombre2 = randint(0, 9)
            ''' addition entre deux variable de type int: (int, int)-> int'''
            Resultat = int(Nombre1 * Nombre2)
            
            print(Nombre1, " * ", Nombre2, " = ")
            Reponse = int(input("Reponse : "))

            '''on a deux cas lorsque le resultat est correcte et lorqu'il ne l'est pas'''
                
            if Reponse != Resultat :
                print("Reponse incorrecte la bonne reponse est", Resultat)
             
            elif Reponse == Resultat:
                print("Bonne reponse")
                ReponseCorrecte += 1
              
            Compteur += 1
         if ReponseCorrecte >= 6:
             print("vous avez", ReponseCorrecte, "Reponses correctes,GOOD JOB")
             print("Félicitation!!!")
         else :
             ReponseIncorrecte = 10 - int(ReponseCorrecte) 
             print("vous avez", ReponseIncorrecte, "Reponses Incorrectes, Demandez à votre enseignant(e) de vous aider. ")
    #la fonction ne retourne rien car elle pour proprieter dafficher un certain nombre de donneee
    return


print("Bienvennue!")
print("Ce logiciel va effectuez un test avec une serie de 10 questions pour evaluez votre niveau avant le devoir.")
print("Pour ce faire, ce systeme n'utilise que des nombres positifs")
print("SVP choisissez entre le chiffre 0 pour l'addition et 1 pour la multiplicaton")

#creation de la variable ChoixEleve entree par l'utilisateur        
ChoixEleve = int(input("choisir 0 pour laddition et 1 pour la multiplication: "))
effectuerTest(ChoixEleve)
     
    
