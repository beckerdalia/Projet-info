def supp_tout(dico_data):
#Cette fonction permet de supprimer tous les étudiants
    x=raw-imput("Voulez-vous vraiment supprimer tous les étudiants? Répondez par Oui ou Non")
    #on demande si l'utilisateur est sur de lui
    while x.upper()!="OUI" or x.upper()!="NON":
    #tant qu'il n'a pas bien écrit la réponse, on le sollicite à recommencer
        print "Réessayez"
        x=raw_imput("Voulez-vous vraiment supprimer tous les étudiants? Répondez par Oui ou Non")
    if x.upper()="OUI"
        dico.data={}
        return dico.data
    elif x.upper()="NON"
        return None
    
