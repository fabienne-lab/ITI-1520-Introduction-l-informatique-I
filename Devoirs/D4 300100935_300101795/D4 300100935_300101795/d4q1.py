#Berte Tata 
#300100935
#Sawadogo Marie Fabienne
#300101795
#devoir 4 question 2

#La fonction ajoute prend chaque element de la matrice entree par lutilisateur et ajoute 1 a
#chaque element de la liste . La fontion ajoute_V2 cree une nouvelle matrice avec les meme elements
#mais incrementer avec 1 et retourne une matrice identique a celle obtenue dans la fonction ajoute   

def ajoute(mat):
      "la fonction prend (liste)->(liste)incrementee avec plus un"
      
      i=0
      mat1=[]
      while i<len(mat):
            j=0
            mat1.append ( [] )
            while j <len (mat [i]):
                        mat1[i].append(1+mat[i][j])
                        j=j+1
            i=i+1
      return mat1




m= int(input("Entrez le nombre de rangees: "))
mat= []
x = 0
while (x < m):
      print("Entrez la rangee", x, 
      "(les entiers separes par des espaces)")
      rangee = [int(val) for val in input().split()]
      mat.append(rangee)
      x = x + 1
print("la matrice est:", mat)

mat1=ajoute(mat)
print("Apres execution de la fonction ajoute la matrice est :", mat1)
def ajoute_V2(mat2):
      """La fontion ajoute_V2 cree une nouvelle matrice avec les meme elements
      mais incrementer avec 1 et retourne une matrice identique a celle obtenue dans
      la fonction ajoute """ 


      mat2=ajoute(mat1)
      print("Une nouvelle matrice cree avec ajoute_V2", mat2)
      p=0
      mat3=[]
      i=-1
      
      while p<len (mat2):
            mat3.append([])
            i+=1
            j=-1
            q=0
           
            while q< len(mat2[p]):
                  j+=1
                  
                  
                  mat3[p].append(mat1[i][j])
                  q=q+1
            p=p+1
            
      return mat3
mat3=ajoute_V2(mat1)
print("Apres execution de la fonction ajoute_V2 la matrice initiale est:", mat3)

