def saisie_note(dico_data, dico_matiere):
    nom_eleve=raw_input("veuillez choisir un nom d'élève (exemple DUPONT Jean) :  ")
    while nom_eleve in  dico_data == False :
    #gestion des erreurs de saisie
        print " vérifiez l'orthographe du nom saisi "
        nom_eleve=raw_input("veuillez choisir un nom d'élève (exemple DUPONT Jean) :  ")
    matiere=raw_input("veuillez choisir une matière :  ")
    while matiere in  dico_matiere == False :
    #gestion des erreurs de saisie
        print " vérifiez la cohérence de votre saisie , voici la liste des matières"
        print dico_matiere.keys()
        matiere=raw_input("veuillez choisir une matière :  ")
    note=raw_input("saisissez la note "+matiere+" de l'élève : "+nom_eleve+" ")
    dico_data[nom_eleve][dico_matiere.keys().index(matiere)]=note
    #place la note de l'eleve dans sa liste de note à la position correspondant à la matiere
    return dico_data
