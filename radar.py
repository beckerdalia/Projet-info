# -*- coding: utf-8 -*-
import math, copy
import matplotlib.pyplot as plt
from sauvegardelecture import lecture
from moyennes import calcul_moyennes_matieres

#----------------------------------
def diagramme_radar(nom, matieres, notes):
    """
    Affichage de type radar des résultats de l'élève nom
    """
    moyennes = calcul_moyennes_matieres(matieres, notes)
    noteseleve = copy.deepcopy(notes[nom])
    deuxpisurn = 2 * math.pi / len(matieres)
    nbmatieres=len(matieres)+1
    noteseleve.append(noteseleve[0])
    # on rajoute la première note à la fin pour finir le dessin de la boucle en matplotlib
    moyennes.append(moyennes[0])
    # de même pour les moyennes
    x = [math.cos(k * deuxpisurn) for k in xrange(nbmatieres)]
    y = [math.sin(k * deuxpisurn) for k in xrange(nbmatieres)]
    # coordonnées polaires pour le calcul des positions
    xd = [0.5 * x[k] for k in xrange(nbmatieres)]
    yd = [0.5 * y[k] for k in xrange(nbmatieres)]
    # moyenne à 10
    xn = [noteseleve[k]/20.0 * x[k] for k in xrange(nbmatieres)]
    yn = [noteseleve[k]/20.0 * y[k] for k in xrange(nbmatieres)]
    # moyenne élève
    xm = [moyennes[k]/20.0 * x[k] for k in xrange(nbmatieres)]
    ym = [moyennes[k]/20.0 * y[k] for k in xrange(nbmatieres)]
    # moyenne promo

    plt.figure(figsize=(6, 6))
    plt.axis([-1.25, 1.75, -1.5, 1.5])
    plt.title(nom, fontweight='bold')
    for k in xrange(len(matieres)):
        plt.plot([0, x[k]], [0, y[k]], '-k' )
        plt.plot(x[k], y[k], 'ok')
        va = 'bottom'
        if y[k] < 0: va = 'top'
        # va est l'alignement vertical et ha horozontal
        plt.annotate("{} ({:2d})".format(matieres[k],int(noteseleve[k])),xy=(x[k]*1.1, y[k]*1.1), ha='center', va=va)
    plt.plot(xm, ym, '-b', label='Classe')
    plt.plot(xn, yn, '-r', linewidth=2.5, label='Etudiant')
    plt.plot(xd, yd, '--k', label='10')
    plt.legend(loc='upper left')
    plt.xticks([])
    plt.yticks([])
    # on enlève les graduations (ticks)
    plt.show()

#================================================================#
if __name__ == '__main__':
    (matieres, coeffs, notes) = lecture('notes.txt')
    nom = notes.keys()[0]
    diagramme_radar(nom, matieres, notes)
