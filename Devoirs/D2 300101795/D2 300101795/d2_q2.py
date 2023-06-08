#SAWADOGO MARIE FABIENNE
#300101795
#ce programme permet de prendre des entree de l'utilisateur et les afficher sucesivement en ajoutant tout le temps 1
#Creation des variables a et b et leur entree par lutilisateur
#la contrainte est que a et doivent etre des entier positif
a =  int(input("SVP donner la valeur de a: "))
b = int(input("SVP donner la valeur de b: "))
#definition de la fonction affiche qui prend comme entier a et retourne tous les entiers compris entre a et b

def affiche(a, b):
   '''on utulise une boucle avec a comme compteur qui prend (int)->(int)
   '''
   while a <= b:
      print(a)
      a += 1
   return #retourne rien parceque la fonction a pour proprieter d'afficher

affiche(a, b)


