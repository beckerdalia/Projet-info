# -*- coding: utf-8 -*-
import sauvegardelecture, outils_clavier


def modif_coeff_mat(matiere, coeff, matieres, coeffs):
    # modification pour une matière et un coefficient donnés
    for i,mat in enumerate(matieres):
        if mat==matiere:
            coeffs[i] = float(coeff)
            break
            # on quitte la boucle
    return coeffs


def modification_coeff(matieres, coeffs):
    matiere, choix = outils_clavier.affiche_et_choix(matieres)
    saisieOk= False
    while not saisieOk:
    #boucle pour s'assurer d'une saisie correcte
        coeff=input("Veuillez donner le nouveau coefficient de la matière: " )
        try:
            coeff=float(coeff)
            saisieOk=True
        except:
            print("Ce nombre n'est pas bien écrit (mettez un '.' au lieu de ',' ) ")
    return modif_coeff_mat(matiere, coeff, matieres, coeffs)
    # for i,mat in enumerate(matieres):
    #     if mat==matiere:
    #         coeffs[i] = float(coeff)
    #         break
    #         # on quitte la boucle
    # return coeffs


# ================================================================#
if __name__ == '__main__':
    (matieres, coeffs, notes) = sauvegardelecture.lecture('notes.txt')
    print("avant coeffs", coeffs)
    coeffs = modification_coeff(matieres, coeffs)
    print("après coeffs", coeffs)


