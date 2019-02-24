# -*- coding: utf-8 -*-
import sauvegardelecture

def supprimer_etudiant(nom, notes):
    """
    supprime un étudiant
    """
    del notes[nom]
    return notes


def supprimer_tous(notes):
    # Cette fonction permet de supprimer tous les étudiants
    x = raw_input("Voulez-vous vraiment supprimer tous les étudiants? Répondez par Oui ou Non\n")
    # on demande si l'utilisateur est sûr de lui
    while x.upper() != "OUI" and x.upper() != "NON":
        # tant qu'il n'a pas bien écrit la réponse, on le sollicite à recommencer
        x = raw_input("Réessayez: voulez-vous vraiment supprimer tous les étudiants? Répondez par Oui ou Non\n")
    if x.upper()=="OUI":
        notes = {}
    return notes

def suppression_matiere(notes, dico_matiere) :
    matiere=raw_input("veuillez choisir une matière :  ")
    while matiere in  dico_matiere == False :
    #tant que la matiere donnee n'est pas trouvable, on demande une nouvelle saisie
        print " vérifiez la cohérence de votre saisie , voici la liste des matières"
        print dico_matiere.keys()
        #on montre les matieres existantes
        matiere=raw_input("veuillez choisir une matière :  ")
    x=dico_matiere.keys().index(matiere)
    #position de la matiere dans le dictionnaire
    del dico_matiere[matiere]
    for nom  in notes :
        notes[nom].pop(x)
    return None

#================================================================#
if __name__ == '__main__':
    (matieres, coeffs, notes) = sauvegardelecture.lecture('notes.txt')
    notes = supprimer_etudiant(notes.keys()[0], notes)
    print "notes après suppresion du premier élève", notes
    notes = supprimer_tous(notes)
    print "notes après suppresion de tous les élèves", notes
    # affichage_promo(matieres, notes)
