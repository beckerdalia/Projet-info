def sauvegarde_donnees(dico_data, dico_matiere):
    nom_fichier=raw_input("Choisissez le nom du fichier dans lequel vous souhaitez effectuer le sauvegarde : ")
    #pour verifier l'existence du fichier:
    try:
        open(nom_fichier,"r")
        X= True
    except:
        X= False
    print X
    if X==True:
    #si le fichier existe, verifier si l'utilisateur souhaite tout le meme le modifier
        reponse=raw_input("Le fichier existe, etes-vous sur de vouloir le remplacer? Repondez: Oui ou Non :")
        if reponse.upper()=='OUI':    
            with open(nom_fichier,"w") as fichier:
                liste_matiere=[]
                #creer une liste des matieres avec les coeffs pour pouvoir la sauvgarder dans le fichier
                for i in range(len(dico_matiere.keys())):
                    liste_matiere.extend([dico_matiere.keys()[i],dico_matiere.values()[i]])
                fichier.writelines(";".join(liste_matiere)+"\n")
                for i in range(len(dico_data.items())):
                    fichier.writelines(dico_data.items()[i][0]+";"+" ".join(dico_data.items()[i][1])+"\n")
        else:
            print 'pour sauvegarder dans un autre fichier, vous allez etre redirige au menu principal afin de relancer la commande sauvegarde'
            return None
    else:
        with open(nom_fichier,"w") as fichier:
            liste_matiere=[]
            for i in range(len(dico_matiere.keys())):
                liste_matiere.extend([dico_matiere.keys()[i],dico_matiere.values()[i]])
            fichier.writelines(";".join(liste_matiere)+"\n")
            for i in range(len(dico_data.items())):
                fichier.writelines(dico_data.items()[i][0]+";"+" ".join(dico_data.items()[i][1])+"\n")
    return None
