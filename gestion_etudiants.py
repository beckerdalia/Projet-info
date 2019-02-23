# -*- coding: utf-8 -*-
import sauvegardelecture, outils_clavier

def get_note(matiere, nom):
    note_valide = False
    while not note_valide:
        note = raw_input("Donnez la note de : '{}' de l'étudiant : '{}': ".format(matiere, nom))
        try:
            note = float(note)
            note_valide = note >= 0 and note <= 20
        except:
            pass
        if note_valide:
            return note


def ajout_etudiant(dico_data, matieres):
    nom = outils_clavier.saisie_nom()
    notes=[]
    for matiere in matieres:
        note = get_note(matiere, nom)
        notes.append(note)
    dico_data[nom]=notes
    return dico_data

def saisie_etudiant(dico_data, matieres):
    nom, numero = outils_clavier.affiche_et_choix(dico_data.keys())
    matiere, numero = outils_clavier.affiche_et_choix(matieres)
    note = get_note(matiere, nom)
    dico_data[nom][numero-1]=note
    return dico_data

#================================================================#
if __name__ == '__main__':
    matieres, data = sauvegardelecture.lecture('notes.txt')
    print "avant data", data
    data2 = ajout_etudiant(data, matieres)
    sauvegardelecture.sauvegarde(matieres, data2)
    print "après data", data
    pass
    
   
