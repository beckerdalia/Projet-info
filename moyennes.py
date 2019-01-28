# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
from ecriturelecture import lecture

#----------------------------------
def calcul_moyennes(data):
    ms = [0.0, 0.0, 0.0, 0.0, 0.0]
    for nom in data:
        notes = data[nom]
        assert len(notes)==5
        for i,note in enumerate(notes):
            ms[i] += note
    for i in range(5):
        ms[i] /= len(data)
    return ms


#================================================================#
if __name__ == '__main__':
    matieres, data = lecture('notes.txt')
    moyennes = calcul_moyennes(data)
    print("moyenne", moyennes)
