# -*- coding: utf-8 -*-
import affichage, ecriturelecture, gestion_etudiants, outils_clavier

def menu_principal():
    choix_possibles = []
    choix_possibles.append('Charger en mémoire le fichier de notes.')
    choix_possibles.append('Afficher la promotion.')
    choix_possibles.append('Afficher les résultats d’un étudiant.')
    choix_possibles.append('Ajouter un étudiant.')
    choix_possibles.append('Saisie ou modification d’une note pour un étudiant.')
    choix_possibles.append('Suppression d’un étudiant.')
    choix_possibles.append('Suppression de tous les étudiants.')
    choix_possibles.append('Sauvegarder les données.')
    choix_possibles.append('Quitter l’application.')

    choix, numero = outils_clavier.affiche_et_choix(choix_possibles)
    return numero


#================================================================#
if __name__ == '__main__':
    fini = False
    while not fini:
        choix = menu_principal()
        if choix == 1:
            matieres, data = ecriturelecture.lecture('notes.txt')
        elif choix == 2:
            affichage.affichage_promo(matieres, data)
        elif choix == 3:
            noms = data.keys()
            nom, numero = outils_clavier.affiche_et_choix(noms)
            affichage.affichage_etudiant(nom, matieres, data)
        elif choix == 4:
            gestion_etudiants.ajout_etudiant(data, matieres)
        elif choix == 5:
            gestion_etudiants.saisie_etudiant(data, matieres)
        elif choix == 6:
            raise NotImplementedError("reste à faire")
        elif choix == 7:
            raise NotImplementedError("reste à faire")
        elif choix == 8:
            ecriturelecture.ecriture(matieres, data, 'notes.txt')
        else:
            fini = True
