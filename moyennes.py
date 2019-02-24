# -*- coding: utf-8 -*-
from sauvegardelecture import lecture

#----------------------------------
def calcul_moyennes(notes):
    """
    entrée : dico des notes
    retour : liste des moyennes par matières
    """
    nmat = len(notes.values()[0])
    # nmat est le nombre de matières, car values() rend la liste des valeurs d'un dico, ici les listes de notes
    ms = nmat*[0.0]
    for nom in notes:
        notesmat = notes[nom]
        # c'est la liste des notes d'un élève
        if len(notesmat)!=nmat:
            raise ValueError("pas le bon nombre de notes (notesmat={} nmat={})".format(notesmat, nmat))
        for i,note in enumerate(notesmat):
            ms[i] += note
    for i in range(nmat):
        ms[i] /= len(notes)
    return ms


#================================================================#
if __name__ == '__main__':
    (matieres, coeffs, notes) = lecture('notes.txt')
    moyennes = calcul_moyennes(notes)
    print "moyenne", moyennes
