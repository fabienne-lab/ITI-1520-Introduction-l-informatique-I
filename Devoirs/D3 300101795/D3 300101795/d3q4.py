﻿#Sawadogo Marie Fabienne
#300101795

 # Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet


def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)


def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
   
     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     x=len(p)
     i=0
     donneur, autre = [], []
     while i < x :
          a=p[i]
          if i%2==0:
              autre.append(a)
          else:
              donneur.append(a)
          i+=1

     
       
     


     
     return (donneur, autre)
  

def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢'] 

    '''
    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    #on utilise sort pour trier  la liste et comparer chaque element avec le plus proche dans la liste
    l.sort()
    i=0
    Loop =  True
    x=len(l)
    s1 = l[i]
    s2 = l[i+1]
    s3=l[len(l)-1]
    
    while Loop == True :
        
        while Loop == True:
            
            if i+1 >= len(l):
                Loop = False
                
            else:
                s1=l[i]
                s2=l[i+1]
            
                if s1[0]==s2[0]:
                    l.remove(s1)
                    l.remove(s2)
               
                i += 1

    l.sort()
    i = 0
                
    Loop = True
    
    while Loop == True :
        
        while Loop == True:
            
            if i+1 >= len(l):
                Loop = False
                
            else:
                s1=l[i]
                s2=l[i+1]
            
                if s1[0]==s2[0]:
                    l.remove(s1)
                    l.remove(s2)
                  
                    
                i += 1

    #on utilise deux boucle pour sasurer que toutes les paires soient defausser
    resultat = l
    random.shuffle(resultat)
    return resultat

def enleve_cartes(n):
    elimine_paires(n)
    return n


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    print(p)
    

def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
     '''

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     
     lengh = len(n)
     print("jai", len(n), "cartes.Si 1 est la position de ma premiere carte et ", len(n), "la position de ma derniere carte la quelle vouvez vous")

     print("entree un nombre entier valide entre 1 et", lengh)
     a = int(input(" : "))
     
     if a>lengh or a < 1:
         while a > lengh or a < 1:
             print("Position invalide. SVP entrez un entier :")


             a = int(input(""))

     return a


def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]
     

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     
     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICi
     
     
     jouer = True
     JeuHumain = elimine_paires(humain)
     JeuRobot = elimine_paires(donneur)
     
     
     while jouer:

        print("votre tour")
        print("Votre main est")
        affiche_cartes(JeuHumain)
        a = entrez_position_valide(JeuRobot)

#position valide humain        
        print("vous avez demandez ma carte numero", a)
        print("la voici, cest un", JeuRobot[a-1])
        JeuHumain.append(JeuRobot[a-1])

        print("Avec", JeuRobot[a-1], "ajouté, votre main est:")
        affiche_cartes(JeuHumain)
        JeuRobot.remove(JeuRobot[a-1])
#Fin 
         
        
        JeuHumain = elimine_paires(JeuHumain)
        print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est: ")
        affiche_cartes(JeuHumain)

        attend_le_joueur()
        print("***********************************************************")

        print("Mon tour")

#position Valide Robot
        
        choix_robot=random.randint(0, len(JeuHumain))
        print("jai pris votre", choix_robot)
        JeuRobot.append(JeuHumain[choix_robot-1])
        JeuHumain.remove(JeuHumain[choix_robot-1])
#fIN
        
        JeuRobot = elimine_paires(JeuRobot)
        attend_le_joueur()
        print("***********************************************************")

        if len(JeuHumain) <= 1:
            print("J'ai terminé toutes les cartes.")
            print("Félicitations! Vous, Humain, vous avez gagné.")
            jouer = False

        elif len(JeuRobot) <= 1:
            print("J'ai terminé toutes les cartes.")
            print("Vous avez perdu! Moi, Robot, j'ai gagné.")
                 
            jouer = False

        else:
            Jouer = True

        
         

         
         
# programme principale
joue()
prepare_paquet()

