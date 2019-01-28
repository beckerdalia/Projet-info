# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import math
import matplotlib.pyplot as plt

#----------------------------------
def ecriture(matieres, data, filename='notes.txt'):
    """
    Écriture du fichier contenant les noms des matières et le notes de chaque élève par ligne
    on utilise une virgule pour séparer les données

    matieres: liste des noms des matières
    data: dictionaire nom de l'élève -> liste des notes
    filename: nom du fichier, par défault  'notes.txt'

    retour: rien
    """
    with open(filename,'w') as file:
        file.write(",".join(matieres))
        file.write("\n")
        for nom in data:
            file.write(nom)
            for note in data[nom]:
                file.write(",{}".format(note))
            file.write("\n")

#----------------------------------
def lecture(filename='notes.txt'):
    """
    Lecture du fichier contenant les noms des matières et le notes de chaque élève par ligne
    on suppose que les données sont séparées par une virgule

    filename: nom du fichier, par défault  'notes.txt'

    retour: liste des matières et dictionaire des notes
    """
    data = {}
    with open(filename,'r') as file:
         lines = file.readlines()
         matieres = lines[0].strip().split(',')
         for line in lines[1:]:
             linestrip = line.strip().split(',')
             data[linestrip[0]] = [float(l) for l in linestrip[1:]]
    return matieres, data


def lecture2(fichier) :
    with open ( fichier , "r") as texte:
        data = texte.readlines()
    matieres = data[0].split()
    data.remove(data[0])
    dico_data={}
    for eleve in data :
        eleve.strip(" ").strip("\n")
        L=eleve.split()
        dico_data[L[0]]=L[1:]
    return dico_data , matieres

#================================================================#
if __name__ == '__main__':
    # quelques donnees pour tester
    data={}
    data['justine']=[19, 12,13,14,15]
    data['hela']=[14,12,16, 14,15]
    matieres=["Chimie","Maths","Physique","Biologe","SHS"]

    ecriture(matieres, data)
    matieres2, data2 = lecture()

    if matieres == matieres2:
        print("matieres ok")
    else:
        raise IOError("matieres lu != matieres écrit")
    if data == data2:
        print("data ok")
    else:
        raise IOError("data lu != data écrit")
