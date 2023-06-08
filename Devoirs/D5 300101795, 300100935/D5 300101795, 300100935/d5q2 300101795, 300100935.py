#Berte Tata Saida
#300100935
#Sawadogo Marie Fabienne
#300101795

#question a il sagit de print des etoiles avec une fontion recrusive
def etoile(nombre,maxi):
     '''prend comme entree (int)->(str)'''
     #maxi sera le nombre entree par lutilisateur fois -1
     #le nombre doit etre different de 0 parce quon ne veut pas afficher de ligne
     #vide
     
     if nombre>=maxi and nombre!=0:
         print(abs(nombre)*"*")
         #pour appeler la fonction de facon recrusive
         etoile(nombre-1, maxi)
     if nombre==0:
         etoile(nombre-1, maxi)
print("cette fonction dessine des etoiles")
nombre=int(input("entrez un entier strictement positif svp : "))
while True:
     if nombre>0:
          break
     if nombre<=0:
         nombre=int(input(" erreur, entrez un entier strictement positif svp : "))
     
maxi=-1*nombre
etoile(nombre, maxi)

#question numero b
def sommeliste_rec(l, n):
     '''prend comme entree une (liste)->(int)''' 
     #la deuxieme fonction additionne les nombre positifs dans une liste

     s=0
     #on trie la liste pour faciliter les calculer la somme 
     l.sort()
     if n==1and l[n-1]>0:
          #il faut que les nombre soient positifs
          s=l[0]
     elif n==1 and l[n-1]<0:
         s=0
     if l[n-1]<=0:
             pass
     
     elif  l[n-1]>=0:
          #pour appeler la fontion de facon recrusive 
         somme_part=sommeliste_rec(l, n-1)
         s = somme_part +l[n-1]
     
         
    
     return s
print("la deuxieme fonction additionne les nombre positifs dans une liste")
#on va prendre la liste entree avec lutilisateur
n=int(input("Entrez combien vous voulez de valeurs dans votre liste : "))
L=[]
for i in range(0,n):
     x=int(input("Entrez une valeur : "))
     L.append(x)
print("votre liste est ", L)
print("la somme des entiers positifs de votre liste est ", sommeliste_rec(L, len(L)))              

