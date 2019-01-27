# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import math
import matplotlib.pyplot as plt


#----------------------------------
def ecriture(data, filename='notes.txt'):
    with open(filename,'w') as file:
        for nom in data:
            file.write(nom)
            for note in data[nom]:
                file.write(",{}".format(note))
            file.write("\n")

#----------------------------------
def lecture(filename='notes.txt'):
	data = {}
	with open(filename,'r') as file:
         lines = file.readlines()
         for line in lines:
             linestrip = line.strip().split(',')
             print('linestrip[0] =', linestrip[0])
             print('linestrip[1] =', linestrip[1:])
             data[linestrip[0]] = [float(l) for l in linestrip[1:]]
	return data

#----------------------------------
def moyenne(data):
    ms = [0.0, 0.0, 0.0, 0.0, 0.0]
    for nom in data:
        notes = data[nom]
        assert len(notes)==5
        for i,note in enumerate(notes):
            ms[i] += note
    for i in range(5):
        ms[i] /= len(data)
    return ms


#----------------------------------
def diagramme_radar(title, notes, moyennes, matieres):
    if len(notes) != 5: raise ValueError("notes n'est pas de taille 5")
    if len(moyennes) != 5: raise ValueError("moyennes n'est pas de taille 5")
    if len(matieres) != 5: raise ValueError("matieres n'est pas de taille 5")
    dpsc = 2 * math.pi / 5.
    notes.append(notes[0])
    moyennes.append(moyennes[0])
    x = [math.cos(k * dpsc) for k in range(6)]
    y = [math.sin(k * dpsc) for k in range(6)]
    xd = [0.5 * x[k] for k in range(6)]
    yd = [0.5 * y[k] for k in range(6)]
    xn = [notes[k]/20.0 * x[k] for k in range(6)]
    yn = [notes[k]/20.0 * y[k] for k in range(6)]
    xm = [moyennes[k]/20.0 * x[k] for k in range(6)]
    ym = [moyennes[k]/20.0 * y[k] for k in range(6)]

    plt.figure(figsize=(6, 6))
    plt.axis([-1.25, 1.75, -1.5, 1.5])
    plt.title(title, fontweight='bold')
    for k in range(5):
        plt.plot([0, x[k]], [0, y[k]], '-k' )
        plt.plot(x[k], y[k], 'ok')
        va = 'bottom'
        if y[k] < 0: va = 'top'
        plt.annotate("{} ({:2d})".format(matieres[k],notes[k]),xy=(x[k]*1.1, y[k]*1.1), ha='center', va=va)
    plt.plot(xm, ym, '-b', label='Classe')
    plt.plot(xn, yn, '-r', label='Etudiant')
    plt.plot(xd, yd, '--k', label='10')
    plt.legend(loc='upper left')
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
    plt.show()

#================================================================#
if __name__ == '__main__':
    # quelques donnees pour tester
    data={}
    data['justine']=[19, 12,13,14,15]
    data['hela']=[14,12,16, 14,15]

    ecriture(data)
    data2 = lecture()

    print("data", data)
    print("data2", data2)
    print("data == data 2 ? ", data == data2)
    moyennes = moyenne(data)
    print("moyenne", moyennes)

    matieres=["Chimie","Maths","Physique","Biologe","SHS"]
    diagramme_radar('justine', data['justine'], moyennes, matieres)
