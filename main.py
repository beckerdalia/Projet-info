# -*- coding: utf-8 -*-
import affichage, sauvegardelecture, gestion_etudiants, outils_clavier, quitter, radar, suppression, modification_coefficient

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
if __name__ == '__main__':
    fini = False
    matieres, coeffs, notes = sauvegardelecture.lecture('notes.txt')
    while not fini:
        choix = menu_principal()
        if choix == 1:
            matieres, coeffs, notes = sauvegardelecture.lecture()
        elif choix == 2:
            affichage.affichage_promo(matieres, coeffs, notes)
        elif choix == 3:
            noms = notes.keys()
            nom, numero = outils_clavier.affiche_et_choix(noms)
            affichage.affichage_etudiant(nom, matieres, notes)
            radar.diagramme_radar(nom, matieres, notes)
        elif choix == 4:
            gestion_etudiants.ajout_etudiant(notes, matieres)
        elif choix == 5:
            gestion_etudiants.saisie_etudiant(notes, matieres)
        elif choix == 6:
            noms = notes.keys()
            nom, numero = outils_clavier.affiche_et_choix(noms)
            notes = suppression.supprimer_etudiant(nom, notes)
        elif choix == 7:
            notes = suppression.supprimer_tous(notes)
        elif choix == 8:
            sauvegardelecture.sauvegarde(matieres, coeffs, notes)
        elif choix == 9:
            raise NotImplementedError("???")
        elif choix == 10:
            raise NotImplementedError("???")
        elif choix == 11:
            coeffs = modification_coefficient.modification_coeff(matieres, coeffs)
        elif choix == 12:
            quitter.efface_ecran()
            fini = True
