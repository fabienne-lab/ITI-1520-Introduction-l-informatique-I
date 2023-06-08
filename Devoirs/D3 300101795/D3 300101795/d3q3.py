#Sawadogo Marie Fabienne
#300101795
#cette fonction prend une liste et retourne le nombre de la  longueur de la plus longue séquence d’éléments consécutifs égaux
def sequence_max(l):
    #on cree un tableau vide pour a chaque fois incrementer le nombre de sequence de nombre
    #consecutif
    '''(liste)->int'''
    x=len(l)
    i=0
    TableauValeur = []
    Valeur = 0
    
    while i < x-1:
        a=l[i]
        b=l[i+1]
 
        if a==b:
            Valeur+=1
            
        elif a != b :
            TableauValeur.append(Valeur)
            Valeur = 0
            
        
        i +=1
    if a==l[x-1]:
        TableauValeur.append(Valeur)
    #on use max pour avoir la plus longue chaine
        


    MaximumTableau = max(TableauValeur) +1
    if MaximumTableau==0:
        print("1")

            
    
            
                          

    print(MaximumTableau)
    return MaximumTableau


ch=input("Veuillez entrer une liste de valeurs séparées par des virgules:")
l=list(eval(ch))
sequence_max(l)
