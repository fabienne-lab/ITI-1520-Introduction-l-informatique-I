#sawadogo Marie Fabienne
#300101795
#prend une liste et retourne le nombre delement positif
ch=input("Veuillez entrer une liste de valeurs séparées par des virgules:")
L = list(eval(ch))
def compte_pos(L):
    '''(list)->(int)'''
    pos = 0
    #pour incrementer le nombre des positifs a chaque boucle
   
    for elt in L:
        '''pour chaque element dans l on comptes tout les positifs'''
        if elt>0:
            pos+=1
    print(pos)
    return pos

compte_pos(L)

