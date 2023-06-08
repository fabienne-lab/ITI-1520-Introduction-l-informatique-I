def calcule(cote1, cote2, cote3):
  "Calcule la surface d'un traigle."
  note = devoirsMoy*25/100 + partiel*25/100 + examen*50/100
  return note

note_devoirs = int(input('Veuillez entrez la note moyenne des devoirs: '))
note_partiel = int(input('Veuillez entrez la note du partiel: '))
note_examen = int(input('Veuillez entrez la note de l\'examen: '))

note_finale = calcule(note_devoirs, note_partiel, note_examen)
print(note_finale)
