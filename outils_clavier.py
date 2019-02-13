# -*- coding: utf-8 -*-

def get_nom():
    nom_valide = False
    while not nom_valide:
        nom = raw_input("Donnez le NOM et Prénom de l'élève à ajouter (exemple DUPONT Jean) : ").strip()
        nomsplit = nom.split()
        if len(nomsplit) != 2:
            print "votre choix ('{}') n'est pas sous la forme 'NUM Prénom'. Veuillez ressayer".format(nom)
        else:
            if nomsplit[0] != nomsplit[0].upper():
                print "le nom de faimille de votre choix ('{}') n'est pas en majuscules'. Veuillez ressayer".format(nom)
            else:
                nom_valide = True
        if nom_valide:
            return nom


def affiche_et_choix(choix_possibles):
    n = len(choix_possibles)
    for i, choix in enumerate(choix_possibles):
        if n < 10:
            print "\t({:1d}) {}".format(i+1,choix)
        elif n<100:
            print "\t({:2d}) {}".format(i + 1, choix)
        else:
            raise NotImplementedError
    choix_valide=False
    while not choix_valide:
        choix = raw_input("Donner le votre choix (un chiffre) et valider avec entrée :").strip()
        try:
            choix = int(choix)
            choix_valide = choix in range(1,1+n)
        except:
            pass
        if choix_valide:
            return choix_possibles[choix-1], choix
        else:
            print "votre choix ('{}') n'est pas un chiffre entre 1 et {}. Veuillez ressayer".format(choix,n)


#================================================================#
if __name__ == '__main__':
    nom = get_nom()
    print "nom saisi = ", nom
    choix = affiche_et_choix(['3', '6', 'z', 'a'])
    print "choix saisi = ", choix

