# -*- coding: utf-8 -*-
import sauvegardelecture, affichage, gestion_etudiants

def saisie_matiere(matieres, coeffs, notes):
    saisieok = False
    while not saisieok:
    # boucle pour s'assurer d'une saisie correcte
        matiere=raw_input("Veuillez donner le nom de la nouvelle matière : ")
        if matiere in matieres :
            print "La matiere existe déjà\n"
        else:
            saisieok = True
    saisieok = False
    while not saisieok:
        coeff=raw_input("Veuillez choisir le coefficient de la matiere : ")
        try:
            coeff = float(coeff)
            if coeff >=0:
                saisieok = True
            else:
                print "Ce n'est pas un nombre positif"
        except:
            print "Ce n'est pas un nombre"
    matieres.append(matiere)
    coeffs.append(coeff)
    for nom in notes.keys():
        note = gestion_etudiants.saisie_note(matiere, nom)
        # on utilise notre fonction pour la saise d'une note pour nom et matière donnés
        notes[nom].append(note)
    return matieres, coeffs, notes


#================================================================#
if __name__ == '__main__':
    (matieres, coeffs, notes) = sauvegardelecture.lecture('notes.txt')
    affichage.affichage_promo(matieres, coeffs, notes)
    (matieres, coeffs, notes) = saisie_matiere(matieres, coeffs, notes)
    affichage.affichage_promo(matieres, coeffs, notes)
