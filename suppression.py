# -*- coding: utf-8 -*-
import sauvegardelecture, affichage, outils_clavier

def supprimer_etudiant(nom, notes):
    """
    supprime un étudiant
    """
    del notes[nom]
    return notes


def supprimer_tous(notes):
    # Cette fonction permet de supprimer tous les étudiants
    x = input("Voulez-vous vraiment supprimer tous les étudiants? Répondez par Oui ou Non\n")
    # on demande si l'utilisateur est sûr de lui
    while x.upper() != "OUI" and x.upper() != "NON":
        # tant qu'il n'a pas bien écrit la réponse, on le sollicite à recommencer
        x = input("Réessayez: voulez-vous vraiment supprimer tous les étudiants? Répondez par Oui ou Non\n")
    if x.upper()=="OUI":
        notes = {}
    return notes

def suppression_matiere(matsup, matieres, coeffs, notes):
    x=matieres.index(matsup)
    #position de la matiere dans le dictionnaire
    matieres.remove(matsup)
    #effacer un élément d'une liste par valeur
    coeffs.pop(x)
    #effacer un élément d'une liste par indice
    for nom  in list(notes.keys()):
        notes[nom].pop(x)
    return matieres, coeffs, notes

#================================================================#
if __name__ == '__main__':
    (matieres, coeffs, notes) = sauvegardelecture.lecture('notes.txt')
    notes = supprimer_etudiant(list(notes.keys())[0], notes)
    print("notes après suppresion du premier élève", notes)
    affichage.affichage_promo(matieres, coeffs, notes)
    matieres, coeffs, notes = suppression_matiere(matieres[0], matieres, coeffs, notes)
    affichage.affichage_promo(matieres, coeffs, notes)
    notes = supprimer_tous(notes)
    print("notes après suppresion de tous les élèves", notes)
