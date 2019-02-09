# -*- coding: utf-8 -*-
import ecriturelecture

def ajout_etudiant(dico_data, matieres):
    nom_etudiant = raw_input("Donnez le NOM et Prénom de l'élève à ajouter (exemple DUPONT Jean) : ").strip()
    nomsplit = nom_etudiant.split()
    if len(nomsplit)!=2:
        # il ne suffirait pas de relancer 'raw_input', car il n'y aurait plus de test
        # si l'on veut faire ça, il faudrait faire une boucle....
        raise IOError("Réessayez svp, il faut nom et prénom !")
    if nomsplit[0]!=nomsplit[0].upper():
        raise IOError("Réessayez svp, le nom de famille doit etre en majuscules !")
    notes=[]
    for matiere in matieres:
        note_etudiant = raw_input("Donnez la note de : ' "+matiere+" ' de l'étudiant : " + nom_etudiant+": ")
        if note_etudiant not in range(0,21):
            raise IOError("la note doit être entre 0 et 20 !")
        # ça marche pas si une matiere manque !
        # note_etudiant = raw_input("Donnez la note de : ' "+matiere+" ' de l'étudiant : " + nom_etudiant+" (s'il n'a pas de notes, rentrez un '_') : ")
        # if note_etudiant!='_':
        #     notes.append(note_etudiant)
    dico_data[nom_etudiant]=notes
    return dico_data
  
#================================================================#
if __name__ == '__main__':
    matieres, data = ecriturelecture.lecture('notes.txt')
    print "data", data
    data2 = ajout_etudiant(data, matieres)
    ecriturelecture.ecriture(matieres, data2)
    print "data", data
    pass
    
   
