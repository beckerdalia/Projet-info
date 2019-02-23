# -*- coding: utf-8 -*-
import os.path
# module qui permet de verifier si un fichier existe

#----------------------------------
def sauvegarde(matieres, coeffs, notes, nom_fichier=''):
    """
    Écriture du fichier contenant les noms des matières et le notes de chaque élève par ligne
    on utilise une virgule pour séparer les données
    Si le nom du fichier n'est pas donné, on demande à l'utilisateur

    matieres: liste des noms des matières
    coeff: liste des coefficients
    notes: dictionaire nom de l'élève -> liste des notes

    retour: rien
    """
    if nom_fichier == "":
        nom_fichier = raw_input("Choisissez le nom du fichier dans lequel vous souhaitez effectuer le sauvegarde : ").strip()
        if os.path.isfile(nom_fichier):
            reponse = raw_input("Le fichier existe, etes-vous sur de vouloir le remplacer? Repondez: Oui ou Non :")
            if reponse == "Non":
                while os.path.isfile(nom_fichier):
                    # boucle jusqu'à ce qu'un nom d'un fichier inexistant soit trouvé
                    nom_fichier = raw_input("Choisissez le nom du fichier a écrire : ").strip()

    with open(nom_fichier,'w') as file:
        file.write(",".join(matieres))
        # on assemble la liste des matières en un string en séparant par des virgules
        file.write("\n")
        file.write(",".join([str(c) for c in coeffs]))
        # même chose pour les coeffs, mais il faut les convirtir en string d'abord
        file.write("\n")
        for nom in sorted(notes):
            file.write(nom)
            for note in notes[nom]:
                file.write(",{}".format(note))
            file.write("\n")

#----------------------------------
def lecture(nom_fichier=""):
    """
    Lecture du fichier contenant les noms des matières et le notes de chaque élève par ligne
    on suppose que les données sont séparées par une virgule
    Si le nom du fichier n'est pas donné, on demande à l'utilisateur

    retour: liste des matières, liste des coefficients et dictionaire des notes
    """
    if nom_fichier == "":
        while not os.path.isfile(nom_fichier):
            nom_fichier=raw_input("Choisissez le nom du fichier a lire : ").strip()
    notes = {}
    # dictionnaire vide
    with open(nom_fichier,'r') as file:
         lines = file.readlines()
         matieres = lines[0].strip().split(',')
         # première ligne du fichier
         coeffs = [float(l) for l in lines[1].strip().split(',')]
         # deuxième ligne du fichier
         for line in lines[2:]:
             # à partir de la troisième ligne du fichier
             linestrip = line.strip().split(',')
             # convertir le string en une liste en séparant au niveau des virgules
             notes[linestrip[0]] = [float(l) for l in linestrip[1:]]
             # remplir le dico par des floats
    return matieres, coeffs, notes


#================================================================#
if __name__ == '__main__':
    (matieres, coeffs, notes) = lecture("notes.txt")
    sauvegarde(matieres, coeffs, notes)
    (matieres2, coeffs2, notes2) = lecture("notes.txt")

    if matieres == matieres2:
        # test si on retrouve les matières
        print "matieres ok"
    else:
        raise IOError("matieres lu != matieres écrit")
        # emettre une erreur entree-sortie (IO)
    if coeffs == coeffs2:
        print "coeffs ok"
    else:
        raise IOError("coeffs lu != coeffs écrit")
    if notes == notes2:
        print "notes ok"
    else:
        raise IOError("notes lu != notes écrit")
