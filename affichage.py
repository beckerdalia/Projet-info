# -*- coding: utf-8 -*-
import sauvegardelecture, moyennes

def affichage_promo(matieres, coeffs, notes) :
    # permet d'afficher le tableau avec les moyennes
    eleves = sorted(notes)
    #tri des élèves dans l'ordre alphabétique
    maxnom = len(max(eleves, key=len))+5
    #max des longueurs de noms pour bien aligner l'affichage
    maxmat = len(max(max(matieres, key=len),'moyenne'))+5
    #de même pour les longueurs des matières

    moyennes_eleves = moyennes.calcul_moyennes_eleves(coeffs, notes)

    formatnom = "{:"+str(maxnom)+"s}"
    formatmat = "{:>"+str(maxmat)+"s}"
    formatnote = "{:"+str(maxmat)+".2f}"
    # string pour le format de l'affichage utilisé en-dessous

    print formatnom.format(""),
    # champ de nom vide pour l'affichage des matières
    for i in range(len(matieres)):
        print formatmat.format(matieres[i]),
        # affichage des matières en ligne (avec la virgule) de même longueur
    print formatmat.format("Moyenne")
    # saut à la ligne
    for nom in eleves:
        print formatnom.format(nom),
        # affichage du nom
        for i in range(len(matieres)):
            print formatnote.format(notes[nom][i]),
        # affichage da la note
        print formatnote.format(moyennes_eleves[nom])
    moy = moyennes.calcul_moyennes_matieres(notes)
    moyennes_promo = moyennes.calcul_moyennes_promo(coeffs, moy)
    # affichage des moyennes
    print maxnom*'-'
    print formatnom.format('Moyenne'),
    for i in range(len(matieres)):
        print formatnote.format(moy[i]),
    print formatnote.format(moyennes_promo)


def affichage_etudiant(nom, matieres, notes):
    """
    même chose pour un étudiant
    """
    maxmat = len(max(matieres, key=len))+5
    nmat = len(matieres)
    fmtnom = "{:"+str(len(nom))+"s}"
    fmtmat = "{:^"+str(maxmat)+"s}"

    print fmtnom.format(""),
    for i in range(len(matieres)):
        print fmtmat.format(matieres[i]),
    print ""
    print fmtnom.format(nom),
    for i in range(nmat):
        print fmtmat.format(str(notes[nom][i])),
    print ""

#================================================================#
if __name__ == '__main__':
    (matieres, coeffs, notes) = sauvegardelecture.lecture('notes.txt')
    affichage_promo(matieres, coeffs, notes)
