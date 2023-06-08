import math

def calculeSurface(cote1, cote2, cote3):
  "Calcul de la surface du triangle."
  p = cote1 + cote2 + cote3
  s = math.sqrt(p * (p - 2 * cote1) * (p - 2 * cote2) * (p - 2 * cote3)) / 4    
  return s


surface = calculeSurface(20, 30, 40)
print("La surface est ", surface)
