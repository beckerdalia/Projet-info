# -*- coding: utf-8 -*-

def saisie_nom():
    """
    saisir le nom d'un étudiant
    verifie si le nom est au bon format: NOM Prénom
    et continue de demander si ce n'est la cas
    retour: nom de l'étudiant
    """
    nom_valide = False
    while not nom_valide:
        nom = raw_input("Donnez le NOM et Prénom de l'élève à ajouter (exemple DUPONT Jean) : ").strip()
        nomsplit = nom.split()
        if len(nomsplit) != 2:
            print "votre choix ('{}') n'est pas sous la forme 'NOM Prénom'. Veuillez ressayer".format(nom)
        else:
            if nomsplit[0] != nomsplit[0].upper():
                print "le nom de faimille de votre choix ('{}') n'est pas en majuscules'. Veuillez ressayer".format(nom)
            else:
                nom_valide = True
        if nom_valide:
            return nom


def affiche_et_choix(choix_possibles):
    """
    fonction utilitaire
    saisie d'un choix de l'utilisateur
    entree: choix_possibles: list de string, par exemple liste des matieres
    retour: choix (string)
    """
    n = len(choix_possibles)
    for (i, choix) in enumerate(choix_possibles):
        if n < 10:
            print "\t({:1d}) {}".format(i+1,choix)
            # formatage 1d: entier de 1 caractère (on commence par 1 au lieu de 0)
        elif n<100:
            print "\t({:02d}) {}".format(i + 1, choix)
            # si plus de 9 choix
        else:
            raise NotImplementedError("trop de choix ({})".format(n))
    choix_valide=False
    while not choix_valide:
        choix = raw_input("Donner votre choix (un chiffre) et valider avec entrée :").strip()
        try:
            choix = int(choix)
            choix_valide = choix in range(1,1+n)
        except:
            pass
        if choix_valide:
            return choix_possibles[choix-1], choix
        else:
            print "\nVotre choix ('{}') n'est pas un nombre entre 1 et {}.Veuillez réessayer".format(choix,n)


#================================================================#
if __name__ == '__main__':
    # test de la saisie de nom
    nom = saisie_nom()
    print "nom saisi = ", nom
    # test de la saisie d'un choix
    choix = affiche_et_choix(['math', 'phys', 'svt', 'sport'])
    print "choix saisi = ", choix

