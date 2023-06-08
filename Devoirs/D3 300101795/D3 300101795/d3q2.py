#Sawadogo Marie Fabienne
#300101795

ch=input("Veuillez entrer une liste de valeurs séparées par des virgules:")
l=list(eval(ch))
#cette fontion retourne  True s’il y a au moins une séquence de deux éléments consécutifs égaux, et
#false dans le cas contraire
def sequenceDesDeux (l):
    '''(liste)->(bool)'''
    sequence =False
    x=len(l)
    for i in range (0, x-1):
        a=l[i]
        b=l[i+1]
        if a==b and i<=x:
            sequence = True
    print(sequence)
       
            
    return sequence
sequenceDesDeux(l)

            
