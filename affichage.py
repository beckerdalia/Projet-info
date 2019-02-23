# -*- coding: utf-8 -*-
import sauvegardelecture

def affichage_etudiant(nom, matieres, data):
    maxmat = len(max(matieres, key=len))+5
    nmat = len(matieres)
    fmtname = "{:"+str(len(nom))+"s}"
    fmtmat = "{:^"+str(maxmat)+"s}"

    print fmtname.format(""),
    for i in range(len(matieres)):
        print fmtmat.format(matieres.keys()[i]),
    print ""
    print fmtname.format(nom),
    for i in range(nmat):
        print fmtmat.format(str(data[nom][i])),
    print ""

def affichage_promo(matieres, data) :
    # permet d'afficher le tableau avec les moyennes)
    eleves = sorted(data)
    #tri des élèves dans l'ordre alphabétique
    maxname = len(max(eleves, key=len))+5
    maxmat = len(max(matieres, key=len))+5
    nmat = len(matieres)

    fmtname = "{:"+str(maxname)+"s}"
    fmtmat = "{:^"+str(maxmat)+"s}"

    print fmtname.format(""),
    for i in range(len(matieres)):
        print fmtmat.format(matieres.keys()[i]),
    print ""
    for nom in eleves:
        print fmtname.format(nom),
        for i in range(nmat):
            print fmtmat.format(str(data[nom][i])),
        print ""

#================================================================#
if __name__ == '__main__':
    matieres, data = sauvegardelecture.lecture('notes.txt')
    affichage_promo(matieres, data)
