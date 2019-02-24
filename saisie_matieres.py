def saisie_matiere(matieres, notes):
    matiere=raw_input("veuillez donner le nom de la nouvelle matière : ")
    if matiere in dico _matiere :
        print " la matiere existe déjà "
        matiere=raw_input("veuillez donner un nouveau non : ")
    coeff=raw_input("veuillez choisir le coefficient de la matiere : ")
    matieres[matiere]=coeff
    for nom in range(notes):
       note=raw_input("veuillez choisir la note de l'élève : "+nom+" (si il n'a pas de note veuillez entrer '_') ")
       notes_eleve=notes[nom]
       notes[nom]=notes_eleve.append(note)
    return None
