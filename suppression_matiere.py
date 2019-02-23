
def suppression_matiere(dico_data, dico_matiere) :
    matiere=raw_input("veuillez choisir une matière :  ")
    while matiere in  dico_matiere == False :
    #tant que la matiere donnee n'est pas trouvable, on demande une nouvelle saisie
        print " vérifiez la cohérence de votre saisie , voici la liste des matières"
        print dico_matiere.keys()
        #on montre les matieres existantes
        matiere=raw_input("veuillez choisir une matière :  ")
    x=dico_matiere.keys().index(matiere)
    #position de la matiere dans le dictionnaire
    del dico_matiere[matiere]
    for nom  in dico_data :
        dico_data[nom].pop(x)
    return None
