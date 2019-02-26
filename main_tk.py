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
        self.root.title('Gestion de notes')
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
        self.filename = tkFileDialog.askopenfilename(title="Choisir le fichier",defaultextension='txt')
        self.matieres, self.coeffs, self.notes = sauvegardelecture.lecture(self.filename)
        texte =  affichage.affichage_promo_string(self.matieres, self.coeffs, self.notes)
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, texte)

    def sauvegarde(self):
        sauvegardelecture.ecrire_dans_fichier(self.matieres, self.coeffs, self.notes, self.filename)

    def sauvegardesous(self):
        filename = tkFileDialog.asksaveasfilename(title="Choisir le fichier", defaultextension='txt')
        if filename:
            sauvegardelecture.ecrire_dans_fichier(self.matieres, self.coeffs, self.notes, filename)


    def definir_menu(self):
        frame = tk.Frame(self.root, width=600, height=400, bd=2, relief=tk.SUNKEN)
        frame.pack(expand=True, fill=tk.BOTH)

        self.text = tk.Text(frame, height=20, width=100)
        self.text.pack(side="left", expand=True, fill=tk.BOTH)
        self.text.insert(tk.END, "Veuillez charger les notes\n")

# honteusement copiè de https://www.tutorialspoint.com/python/tk_menu.htm
        menubar = tk.Menu(self.root)

        menu_fichier = tk.Menu(menubar, tearoff=0)
        menu_fichier.add_command(label="Charger", command=self.lecture)
        menu_fichier.add_command(label="Sauvegarder", command=self.sauvegarde)
        menu_fichier.add_command(label="Sauvegarder sous...", command=self.sauvegardesous)

        # editmenu = tk.Menu(menubar, tearoff=0)
        # editmenu.add_command(label="Undo", command=self.nada)
        # editmenu.add_separator()
        # editmenu.add_command(label="Cut", command=self.nada)
        # editmenu.add_command(label="Copy", command=self.nada)
        # editmenu.add_command(label="Paste", command=self.nada)
        # editmenu.add_command(label="Delete", command=self.nada)
        # editmenu.add_command(label="Select All", command=self.nada)

        # menu_quitter = tk.Menu(menubar, tearoff=0)
        # menu_quitter.add_command(label="Quitter", command=self.quitter)
        # menu_quitter.add_command(label="Radar", command=self.radar)

        # helpmenu = tk.Menu(menubar, tearoff=0)
        # helpmenu.add_command(label="Help Index", command=self.nada)
        # helpmenu.add_command(label="About...", command=self.nada)

        menubar.add_cascade(label="Fichier", menu=menu_fichier)
        # menubar.add_cascade(label="Edit", menu=editmenu)
        # menubar.add_cascade(label="Autres", menu=menu_quitter)
        menubar.add_command(label="Quitter", command=self.quitter)
        menubar.add_command(label="Radar", command=self.radar)
        # menubar.add_cascade(label="Help", menu=helpmenu)

        self.root.config(menu=menubar)

#================================================================#
# programme principal...
root = tk.Tk()
f = Fenetrage(root)
root.mainloop()
