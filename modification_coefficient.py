
def modification_coeff( dico_matiere) :
    matiere=raw_input("veuillez choisir une matière :  ")
    while matiere in  dico_matiere == False :
    #on verifie si la matiere est bien saisie par l'utilisateur
        print " vérifiez la cohérence de votre saisie , voici la liste des matières"
        print dico_matiere.keys()
        matiere=raw_input("veuillez choisir une matière :  ")
    coeff=raw_input("veuillez donner le nouveau coefficient de la matière " )
    dico_matiere[matiere]=coeff
    print " Le coefficient a bien été modifié."
    return dico_matiere
    