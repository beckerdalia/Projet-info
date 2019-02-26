# -*- coding: utf-8 -*-

import Tkinter as tk
import tkFileDialog
# https://stackoverflow.com/questions/32019556/matplotlib-crashing-tkinter-application
import matplotlib
matplotlib.use("TkAgg")
import affichage, sauvegardelecture, gestion_etudiants, outils_clavier, quitter, radar, suppression
# import affichage, sauvegardelecture

class Fenetrage:
    """
    Pour tk, c'est bien de regrouper toutes les info dans une classe
    """
    def __init__(self, root):
        self.root = root
        self.root.title('Notes')
        self.definir_menu()
        self.matieres = None
        self.coeffs = None
        self.notes = None

    def quitter(self):
        self.root.destroy()

    def nada(self):
        pass

    def radarbuttonfini(self):
        choix_etudiant = self.variable.get()
        print "choix_etudiant", choix_etudiant
        self.top.destroy()
        radar.diagramme_radar(choix_etudiant, self.matieres, self.notes)

    def radar(self):
        # http://effbot.org/tkinterbook/toplevel.htm
        if self.notes is None:
            top = tk.Toplevel()
            top.title("Choisir un étudiant")
            msg = tk.Message(top, width=500, text="Il faut d'abord charger un fichier")
            msg.pack(side="left", expand=True, fill=tk.BOTH)
            button = tk.Button(top, width=10, text="Fini", command=top.destroy)
            button.pack(side="left", expand=True, fill=tk.BOTH)
        else:
            noms = self.notes.keys()
            self.top = tk.Toplevel()
            self.top.title("Choisir un étudiant")
            self.variable = tk.StringVar(self.top)
            w = tk.OptionMenu(self.top, self.variable, *noms)
            self.variable.set(noms[0])
            w.pack(side="top", expand=True, fill=tk.BOTH)
            button = tk.Button(self.top, width=100, text="Fini", command=self.radarbuttonfini)
            button.pack(side="bottom", expand=True, fill=tk.BOTH)

    def lecture(self):
        # https://pythonspot.com/tk-file-dialogs/
        self.filename = tkFileDialog.askopenfilename(initialdir=".", title="Choisir le fichier",
                                                     filetypes=(("fichiers txt", "*.txt"), ("all files", "*.*")))
        self.matieres, self.coeffs, self.notes = sauvegardelecture.lecture(self.filename)
        self.creerGrille()

    def sauvegarde(self):
        pass

    def configCanvas(self, event):
        x, y, self.cancas_w, self.canvas_h = event.x, event.y, event.width, event.height

    def creerGrille(self):
        canvas = self.canvas
        w, h = self.cancas_w, self.canvas_h
        maxnom, maxmat = affichage.calcule_taille(self.matieres, self.notes)
        noms = sorted(self.notes.keys())
        nmat = len(self.matieres)
        nnoms = len(noms)
        mat = self.matieres
        # par ligne il nous faut maxnom+maxmat*nmat
        # il nous faut 2+nnoms colonnes
        canvas.delete('grid_line')
        canvas.delete('grid_index')
        print "h={} w={}".format(h, w)
        nw = w / float(maxnom+maxmat*nmat)
        nh = h / float(2+nnoms)
        print "nw", nw, "nh", nh
        canvas.create_line([(nw*maxnom, nh), (nw*maxnom, h - nh)], tag='grid_line')
        for i in range(1,nmat):
            x = nw*maxnom+ i*nw*maxmat
            canvas.create_line([(x, nh), (x, h - nh)], tag='grid_line')
        for i in range(nmat):
            x = nw*maxnom+ i*nw*maxmat
            y = 0.5 * nh
            canvas.create_text((x,y), text="{}".format(mat[i]), tag='grid_index')
        for i in range(nnoms):
            x = 0.5*nw
            y = nh + i*nh
            canvas.create_text((x,y), text="{}".format(noms[i]), tag='grid_index')
        #
        # for i in range(1, 12):
        #     canvas.create_line([(i * nw, nh), (i * nw, h - nh)], tag='grid_line')
        # for i in range(1, 12):
        #     canvas.create_line([(nw, i * nh), (w - nw, i * nh)], tag='grid_line')
        # for i in range(10):
        #     canvas.create_text((1.5 * nw + i * nw, 0.5 * nh), text="{}".format(i), tag='grid_index')
        # for i in range(10):
        #     canvas.create_text((0.5 * nw, 1.5 * nh + i * nh), text="{}".format(unichr(97 + i)), tag='grid_index')

    def definir_menu(self):
        size = (600,400)
        self.frame = tk.Frame(self.root, width=size[0], height=size[1], bd=2, relief=tk.SUNKEN)
        self.frame.pack(expand=True, fill=tk.BOTH)
        self.canvas= tk.Canvas(self.frame, width=size[0], height=size[1], background='light green')
        self.canvas.pack(side="left", expand=True, fill=tk.BOTH)
        self.canvas.bind('<Configure>', self.configCanvas)

# honteusement copiè de https://www.tutorialspoint.com/python/tk_menu.htm
        menubar = tk.Menu(self.root)

        menu_fichier = tk.Menu(menubar, tearoff=0)
        menu_fichier.add_command(label="Lecture", command=self.lecture)
        menu_fichier.add_command(label="Save", command=self.nada)
        menu_fichier.add_command(label="Save as...", command=self.nada)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.nada)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.nada)
        editmenu.add_command(label="Copy", command=self.nada)
        editmenu.add_command(label="Paste", command=self.nada)
        editmenu.add_command(label="Delete", command=self.nada)
        editmenu.add_command(label="Select All", command=self.nada)

        menu_quitter = tk.Menu(menubar, tearoff=0)
        menu_quitter.add_command(label="Quitter", command=self.quitter)
        menu_quitter.add_command(label="Radar", command=self.radar)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.nada)
        helpmenu.add_command(label="About...", command=self.nada)

        menubar.add_cascade(label="Fichier", menu=menu_fichier)
        menubar.add_cascade(label="Edit", menu=editmenu)
        menubar.add_cascade(label="Autres", menu=menu_quitter)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.root.config(menu=menubar)

#================================================================#
# programme principal...
root = tk.Tk()
f = Fenetrage(root)
root.mainloop()
