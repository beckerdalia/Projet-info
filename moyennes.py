# -*- coding: utf-8 -*-
from sauvegardelecture import lecture
import numpy as np

#----------------------------------
def calcul_moyennes_matieres(matieres, notes):
    """
    entrée : dico des notes
    retour : liste des moyennes par matières
    """
    nmat = len(matieres)
    # nmat est le nombre de matières, car values() rend la liste des valeurs d'un dico, ici les listes de notes
    ms = nmat*[0.0]
    for nom in notes:
        notesmat = notes[nom]
        # c'est la liste des notes d'un élève
        if len(notesmat)!=nmat:
            raise ValueError("pas le bon nombre de notes (notesmat={} nmat={})".format(notesmat, nmat))
        for i,note in enumerate(notesmat):
            ms[i] += note
    if len(notes):
        for i in range(nmat):
            ms[i] /= len(notes)
    return ms


def calcul_moyennes_promo(coeffs, moy):
    return np.average(moy, weights=coeffs)

#----------------------------------
def calcul_moyennes_eleves(matieres, coeffs, notes):
    """
    entrée : dico des notes
    retour : liste des moyennes par élèves
    """
    somme_coeff = np.sum(coeffs)
    nmat = len(matieres)
    neleves = len(notes.keys())
    # nmat est le nombre de matières, car values() rend la liste des valeurs d'un dico, ici les listes de notes
    ms = {}
    for nom in notes:
        ms[nom] = 0.0
    for nom,notesmat in notes.iteritems():
        # c'est la liste des notes d'un élève
        if len(notesmat)!=nmat:
            raise ValueError("pas le bon nombre de notes (notesmat={} nmat={})".format(notesmat, nmat))
        for i,note in enumerate(notesmat):
            ms[nom] += note*coeffs[i]
    for nom in notes:
        ms[nom] /= somme_coeff
    return ms

#================================================================#
if __name__ == '__main__':
    (matieres, coeffs, notes) = lecture('notes.txt')
    moyennes_matieres = calcul_moyennes_matieres(matieres, notes)
    print "moyennes_matieres", moyennes_matieres
    moyennes_eleves = calcul_moyennes_eleves(matieres, coeffs, notes)
    print "moyennes_eleves", moyennes_eleves
