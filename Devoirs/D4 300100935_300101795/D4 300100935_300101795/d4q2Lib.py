#Berte Tata 
#300100935
#Sawadogo Marie Fabienne
#300101795
#devoir 4 question 2



def effaceTableau (tab):
   '''
   (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice) 
   en mettant '-' dans tous les elements.
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
    # a completer
    
   for i in range(0,len(tab)):

       for j in range(0,len(tab)):          
          tab[i][j]="-"
          
  
   
  
# retourne rien
   
       
       

      
def verifieGagner(tab):  
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!" 
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''

    # a completer
    resultat=True
    diag=testDiags(tab)
    ligne= testLignes(tab)
    colonne=testCols(tab)
    Match=testMatchNul(tab)
    
    if (ligne=="X") or (colonne == "X")or (diag=="X"):
       resultat=True
       print("Joueur X a gagné!")
       return resultat
       
       
    if(ligne=="O") or (colonne == "O")or (diag=="O") :
       print("Joueur O a gagné!")
       
       resultat=True
       return resultat
    if(ligne=="-") or (colonne == "-")or (diag=="-") :
       resultat=False

    if Match== True:
       print("Match Nul")
       resultat=True
    elif Match==False:
       resultat==False
       
   
       
   




    return resultat # a changer

 
def testLignes(tab):
   ''' (list) ->  str
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer
   comptex =0
   compteo =0
   for lig in tab:
      if lig==['X','X','X']:
          comptex+=1
          
      if lig==['O','O','O']:
          compteo+=1
   if comptex==compteo :
      return '-'
          
   if comptex>=1:
      return "X"
   if compteo>=1:
      return "O"
      
         
      
   
          
        
      
    # pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant 

  
  
def testCols(tab):
   ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer
   gagne = True
   for x in range(len(tab)):
        gagne=True
        
          
        for y in range(len(tab)): 
            if tab[y][x] !="O":
                gagne = False                
                  
        if gagne == True:
            signe = tab[y][x]
            break
   if gagne==False:
      signe="-"
  
  
  
   if signe=="-":
          
        gagne=True    
        for x in range(len(tab)):
            gagne=True
            for y in range(len(tab)): 
                if tab[y][x] !="X": 
                    gagne = False
                
            if gagne == True:
                signe = tab[y][x]
            break
           
        if gagne==False:
            signe="-"
   return signe  

   # pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

   
def testDiags(tab):
   ''' (list) ->  str
   * cherche trois 'X' ou trois 'O' dans une diagonale.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer
   for i in range(0,len(tab)):
      for j in range(0,len(tab)):
         if tab[0][0]==tab[1][1]==tab[2][2]:
            return tab[i][j]
         if tab[0][2]==tab[1][1]==tab[2][0]:
            return tab[0][2]
         else:
            return "-"
      
    
   return '-'   # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

  
  
def testMatchNul(tab):
   ''' (list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
   * Si on ne trouve pas de '-' dans la matrice, retourne True. 
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer
   match =True 
   for i in range (0, len(tab)):
      j =0
      for j in range(0, len(tab)):
         if tab[i][j]=="-":
            match=False
            break
            
         elif tab[i][j]!="-":
            match=True
            
         
      
      
   return match  # a changer

