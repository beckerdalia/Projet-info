# -*- coding: utf-8 -*-
import sauvegardelecture, affichage, gestion_etudiants

def ajout_matiere(matiere, coeff, notesmat, matieres, coeffs, notes):
    """
    modifier la bas de données pour une matière, un coefficient et la liste des notes de cette matière
    """
    matieres.append(matiere)
    coeffs.append(coeff)
    for i,nom in enumerate(notes.keys()):
        notes[nom].append(notesmat[i])
    return matieres, coeffs, notes


def saisie_matiere(matieres, coeffs, notes):
    """
    saisie les informations nécessaires (nom, coefficient, notes) pour une nouvelle matière
    """
    saisieok = False
    while not saisieok:
    # boucle pour s'assurer d'une saisie correcte
        matiere=input("Veuillez donner le nom de la nouvelle matière : ")
        if matiere in matieres :
            print("La matiere existe déjà\n")
        else:
            saisieok = True
    saisieok = False
    while not saisieok:
        coeff=input("Veuillez choisir le coefficient de la matiere : ")
        try:
            coeff = float(coeff)
            if coeff >=0:
                saisieok = True
            else:
                print("Ce n'est pas un nombre positif")
        except:
            print("Ce n'est pas un nombre")
    notesmat = []
    for nom in list(notes.keys()):
        note = gestion_etudiants.saisie_note(matiere, nom)
        notesmat.append(note)
    return ajout_matiere(matiere, coeff, notesmat, matieres, coeffs, notes)


#================================================================#
if __name__ == '__main__':
    (matieres, coeffs, notes) = sauvegardelecture.lecture('notes.txt')
    affichage.affichage_promo(matieres, coeffs, notes)
    (matieres, coeffs, notes) = saisie_matiere(matieres, coeffs, notes)
    affichage.affichage_promo(matieres, coeffs, notes)
