# -*- coding: utf-8 -*-
import sauvegardelecture, outils_clavier

def modification_coeff(matieres, coeffs):
    matiere, choix = outils_clavier.affiche_et_choix(matieres)
    saisieOk= False
    while not saisieOk:
    #boucle pour s'assurer d'une saisie correcte
        coeff=raw_input("Veuillez donner le nouveau coefficient de la matière: " )
        try:
            coeff=float(coeff)
            saisieOk=True
        except:
            print "Ce nombre n'est pas bien écrit (mettez un '.' au lieu de ',' ) "
    for i,mat in enumerate(matieres):
        if mat==matiere:
            coeffs[i] = float(coeff)
            break
            # on quitte la boucle
    return coeffs


# ================================================================#
if __name__ == '__main__':
    (matieres, coeffs, notes) = sauvegardelecture.lecture('notes.txt')
    print "avant coeffs", coeffs
    coeffs = modification_coeff(matieres, coeffs)
    print "après coeffs", coeffs


