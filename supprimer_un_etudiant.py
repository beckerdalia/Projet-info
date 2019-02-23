def supprimer(dico_data):
    print " la liste des élèves : "
    for Nom in dico_data.keys():
        print Nom+" ; ",
    print "\n"
    Nom=raw_input(" Veuillez choisir un nom d'élève existant dans la liste : ")
    while (Nom in dico_data) == False :
    #tant que le nom donne n'est pas trouvable dans le dictionnaire, il faut refaire
        print " Veuillez vérifier que vous avez bien écrit le nom d'élève (exemple : DUPONT Jean) : "
        Nom=raw_input(" Veuillez choisir un nom d'élève existant dans la liste ")
    del dico_data[Nom]
    return dico_data
        
