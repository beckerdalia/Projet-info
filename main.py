# -*- coding: utf-8 -*-
import affichage, sauvegardelecture, gestion_etudiants, outils_clavier, quitter, radar, suppression, modification_coefficient, saisie_matieres


"""
Nous utilisons trois champs pour représenter les donnée:
    matieres: liste de str
    coeffs:   liste de float (de même longuer que matieres)
    notes:    dictionnaire nom --> list de notes (de même longuer que matieres)
"""

def menu_principal():
    choix_possibles = []
    choix_possibles.append("Charger en mémoire le fichier de notes.")
    choix_possibles.append("Afficher la promotion.")
    choix_possibles.append("Afficher les résultats d’un étudiant.")
    choix_possibles.append("Ajouter un étudiant.")
    choix_possibles.append("Saisie ou modification d’une note pour un étudiant.")
    choix_possibles.append("Suppression d'un étudiant.")
    choix_possibles.append("Suppression de tous les étudiants.")
    choix_possibles.append("Sauvegarder les données.")
    choix_possibles.append("Saisie d'une matière.")
    choix_possibles.append("Supression d'une matière.")
    choix_possibles.append("Modification du coefficient d'une matière.")
    choix_possibles.append("Quitter l'application.")

    choix, numero = outils_clavier.affiche_et_choix(choix_possibles)
    return numero


#================================================================#
fini = False
# matieres, coeffs, notes = sauvegardelecture.lecture('notes.txt')
matieres, coeffs, notes = None, None, None
# pour traiter le cas où on n'a pas encore chargé un fichier
while not fini:
    choix = menu_principal()
    if choix == 1:
        matieres, coeffs, notes = sauvegardelecture.lecture()
    elif choix == 2:
        if matieres is None:
            print "Il faut d'abord charger les notes"
        else:
            affichage.affichage_promo(matieres, coeffs, notes)
    elif choix == 3:
        if matieres is None or len(notes.keys())==0:
            print "Il n'y a aucun étudiant !"
        else:
            nom, numero = outils_clavier.affiche_et_choix(notes.keys())
            affichage.affichage_etudiant(nom, matieres, notes)
            radar.diagramme_radar(nom, matieres, notes)
    elif choix == 4:
        if matieres is None:
            print "Il faut d'abord charger les notes"
        else:
            gestion_etudiants.ajout_etudiant(notes, matieres)
    elif choix == 5:
        if matieres is None:
            print "Il faut d'abord charger les notes"
        else:
            gestion_etudiants.saisie_etudiant(notes, matieres)
    elif choix == 6:
        if matieres is None:
            print "Il faut d'abord charger les notes"
        else:
            noms = notes.keys()
            nom, numero = outils_clavier.affiche_et_choix(noms)
            notes = suppression.supprimer_etudiant(nom, notes)
    elif choix == 7:
        if matieres is None:
            print "Il faut d'abord charger les notes"
        else:
            notes = suppression.supprimer_tous(notes)
    elif choix == 8:
        if matieres is None:
            print "Il faut d'abord charger les notes"
        else:
            sauvegardelecture.sauvegarde(matieres, coeffs, notes)
    elif choix == 9:
        if matieres is None:
            print "Il faut d'abord charger les notes"
        else:
            (matieres, coeffs, notes) = saisie_matieres.saisie_matiere(matieres, coeffs, notes)
    elif choix == 10:
        if matieres is None:
            print "Il faut d'abord charger les notes"
        else:
            matsup, numero = outils_clavier.affiche_et_choix(matieres)
            matieres, coeffs, notes = suppression.suppression_matiere(matsup, matieres, coeffs, notes)
    elif choix == 11:
        if matieres is None:
            print "Il faut d'abord charger les notes"
        else:
            coeffs = modification_coefficient.modification_coeff(matieres, coeffs)
    elif choix == 12:
        quitter.efface_ecran()
        fini = True

