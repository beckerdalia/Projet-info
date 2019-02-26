# -*- coding: utf-8 -*-
import sauvegardelecture, moyennes

def calcule_taille(matieres, notes):
    maxnom = len(max(notes.keys(), key=len))+5
    #max des longueurs de noms pour bien aligner l'affichage
    maxmat = len(max(matieres, key=len))+5
    #de même pour les longueurs des matières
    return maxnom, maxmat

def affichage_promo(matieres, notes) :
    # permet d'afficher le tableau avec les moyennes
    maxnom, maxmat = calcule_taille(matieres, notes)
    formatnom = "{:"+str(maxnom)+"s}"
    formatmat = "{:>"+str(maxmat)+"s}"
    formatnote = "{:"+str(maxmat)+".2f}"
    # string pour le format de l'affichage utilisé en-dessous

    print formatnom.format(""),
    # champ de nom vide pour l'affichage des matières
    for i in range(len(matieres)):
        print formatmat.format(matieres[i]),
        # affichage des matières en ligne (avec la virgule) de même longueur
    print ""
    # saut à la ligne
    eleves = sorted(notes.keys())
    #tri des élèves dans l'ordre alphabétique
    for nom in eleves:
        print formatnom.format(nom),
        # affichage du nom
        for i in range(len(matieres)):
            print formatnote.format(notes[nom][i]),
        # affichage da la note
        print ""
    moy = moyennes.calcul_moyennes(notes)
    # affichage des moyennes
    print maxnom*'-'
    print formatnom.format('moyenne'),
    for i in range(len(matieres)):
        print formatnote.format(moy[i]),
    print ""


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
    affichage_promo(matieres, notes)
