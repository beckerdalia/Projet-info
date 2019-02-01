# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import math
import matplotlib.pyplot as plt
from ecriturelecture import lecture
from moyennes import calcul_moyennes

#----------------------------------
def diagramme_radar(title, notes, moyennes, matieres):
    if len(notes) != 5: raise ValueError("notes n'est pas de taille 5")
    if len(moyennes) != 5: raise ValueError("moyennes n'est pas de taille 5")
    if len(matieres) != 5: raise ValueError("matieres n'est pas de taille 5")
    dpsc = 2 * math.pi / len(matieres)
    nbmatieres=len(matieres)+1
    notes.append(notes[0])
    moyennes.append(moyennes[0])
    x = [math.cos(k * dpsc) for k in range(nbmatieres)]
    y = [math.sin(k * dpsc) for k in range(nbmatieres)]
    xd = [0.5 * x[k] for k in range(nbmatieres)]
    yd = [0.5 * y[k] for k in range(nbmatieres)]
    xn = [notes[k]/20.0 * x[k] for k in range(nbmatieres)]
    yn = [notes[k]/20.0 * y[k] for k in range(nbmatieres)]
    xm = [moyennes[k]/20.0 * x[k] for k in range(nbmatieres)]
    ym = [moyennes[k]/20.0 * y[k] for k in range(nbmatieres)]

    plt.figure(figsize=(6, 6))
    plt.axis([-1.25, 1.75, -1.5, 1.5])
    plt.title(title, fontweight='bold')
    for k in range(5):
        plt.plot([0, x[k]], [0, y[k]], '-k' )
        plt.plot(x[k], y[k], 'ok')
        va = 'bottom'
        if y[k] < 0: va = 'top'
        plt.annotate("{} ({:2d})".format(matieres[k],int(notes[k])),xy=(x[k]*1.1, y[k]*1.1), ha='center', va=va)
    plt.plot(xm, ym, '-b', label='Classe')
    plt.plot(xn, yn, '-r', linewidth=2.5, label='Etudiant')
    plt.plot(xd, yd, '--k', label='10')
    plt.legend(loc='upper left')
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
    plt.show()

#================================================================#
if __name__ == '__main__':
    matieres, data = lecture('notes.txt')
    moyennes = calcul_moyennes(data)
    diagramme_radar('justine', data['justine'], moyennes, matieres)
