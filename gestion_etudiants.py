# -*- coding: utf-8 -*-
import sauvegardelecture, outils_clavier

def saisie_note(matiere, nom):
    note_valide = False
    while not note_valide:
        note = raw_input("Donnez la note de : '{}' de l'étudiant : '{}': ".format(matiere, nom))
        try:
            note = float(note)
            if note >= 0 and note <= 20:
               note_valide = True
            else:
                print "mauvaise note '{}'".format(note)
        except:
            print "mauvaise saisie '{}'".format(note)
        if note_valide:
            return note

def ajout_etudiant(notes, matieres):
    nom = outils_clavier.saisie_nom()
    while nom in notes:
        print("Étudiant déjà existant")
        nom = outils_clavier.saisie_nom()
    noteseleve=[]
    for matiere in matieres:
        note = saisie_note(matiere, nom)
        noteseleve.append(note)
    notes[nom]=noteseleve
    return notes

def saisie_etudiant(notes, matieres):
    nom, numero = outils_clavier.affiche_et_choix(notes.keys())
    matiere, numero = outils_clavier.affiche_et_choix(matieres)
    note = saisie_note(matiere, nom)
    notes[nom][numero-1]=note
    return notes

#================================================================#
if __name__ == '__main__':
    (matieres, coeffs, notes) = sauvegardelecture.lecture('notes.txt')
    print "avant notes", notes
    notes = ajout_etudiant(notes, matieres)
    print "après notes", notes

   
