# -*- coding: utf-8 -*-

import Tkinter as tk
import tkFileDialog
import tkMessageBox
# https://stackoverflow.com/questions/32019556/matplotlib-crashing-tkinter-application
import matplotlib
matplotlib.use("TkAgg")
import affichage, sauvegardelecture, gestion_etudiants, outils_tk, radar, suppression, modification_coefficient, outils_clavier, saisie_matieres

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

    def affiche_promo(self):
        texte =  affichage.affichage_promo_string(self.matieres, self.coeffs, self.notes)
        self.text.configure(state='normal')
        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, texte)
        self.text.configure(state='disabled')

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
            w = tk.OptionMenu(self.top, self.variable, *sorted(noms))
            self.variable.set(noms[0])
            w.pack(side="top", expand=True, fill=tk.BOTH)
            button = tk.Button(self.top, width=10, text="Fini", command=self.radarbuttonfini)
            button.pack(side="bottom", expand=True, fill=tk.BOTH)

    def lecture(self):
        # https://pythonspot.com/tk-file-dialogs/
        self.filename = tkFileDialog.askopenfilename(title="Choisir le fichier",defaultextension='txt')
        self.matieres, self.coeffs, self.notes = sauvegardelecture.lecture(self.filename)
        self.affiche_promo()
        # self.text.configure(state='normal')
        # self.text.delete('1.0', tk.END)
        # self.text.insert(tk.END, texte)
        # self.text.configure(state='disabled')

    def sauvegarde(self):
        sauvegardelecture.ecrire_dans_fichier(self.matieres, self.coeffs, self.notes, self.filename)

    def sauvegardesous(self):
        filename = tkFileDialog.asksaveasfilename(title="Choisir le fichier", defaultextension='txt')
        if filename:
            sauvegardelecture.ecrire_dans_fichier(self.matieres, self.coeffs, self.notes, filename)


    def suppetudbuttonfini(self):
        choix_etudiant = self.variable.get()
        self.top.destroy()
        self.notes.pop(choix_etudiant)
        self.affiche_promo()
    def supprimer_etudiant(self):
        noms = self.notes.keys()
        self.top = tk.Toplevel()
        self.top.title("Choisir un étudiant")
        self.variable = tk.StringVar(self.top)
        w = tk.OptionMenu(self.top, self.variable, *sorted(noms))
        self.variable.set(noms[0])
        w.pack(side="top", expand=True, fill=tk.BOTH)
        button = tk.Button(self.top, width=10, text="Fini", command=self.suppetudbuttonfini)
        button.pack(side="bottom", expand=True, fill=tk.BOTH)


    def suppmatbuttonfini(self):
        choix_matiere = self.variable.get()
        self.top.destroy()
        self.matieres, self.coeffs, self.notes = suppression.suppression_matiere(choix_matiere, self.matieres, self.coeffs, self.notes)
        self.affiche_promo()
    def supprimer_matiere(self):
        self.top = tk.Toplevel()
        self.top.title("Choisir une matière")
        self.variable = tk.StringVar(self.top)
        w = tk.OptionMenu(self.top, self.variable, *sorted(self.matieres))
        self.variable.set(self.matieres[0])
        w.pack(side="top", expand=True, fill=tk.BOTH)
        button = tk.Button(self.top, width=10, text="Fini", command=self.suppmatbuttonfini)
        button.pack(side="bottom", expand=True, fill=tk.BOTH)


    def modcoefbuttonfini(self):
        choix_matiere = self.variable.get()
        try:
            choix_coef = float(self.variablecoeff.get())
            self.top.destroy()
            self.coeffs = modification_coefficient.modif_coeff_mat(choix_matiere, choix_coef, self.matieres,
                                                                   self.coeffs)
            self.affiche_promo()
        except:
            pass
    def modifier_coeff(self):
        self.top = tk.Toplevel()
        self.top.title("Choisir une matière")
        self.variable = tk.StringVar(self.top)
        w = tk.OptionMenu(self.top, self.variable, *sorted(self.matieres))
        self.variable.set(self.matieres[0])
        w.pack(side="top", expand=True, fill=tk.BOTH)

        self.variablecoeff = tk.StringVar(self.top)
        self.variablecoeff.set(self.coeffs[0])
        entry = tk.Entry(self.top, textvariable=self.variablecoeff)
        entry.pack(side="bottom", expand=True, fill=tk.BOTH)

        button = tk.Button(self.top, width=10, text="Fini", command=self.modcoefbuttonfini)
        button.pack(side="bottom", expand=True, fill=tk.BOTH)

    def ajouetudbuttonfini(self):
        nom = self.variablenom.get()
        message = outils_clavier.tester_nom(nom)
        if message != "":
            tkMessageBox.showinfo("",message)
            return None
        # convertir en notes
        try:
            notes = [float(var.get()) for var in self.vars]
        except:
            tkMessageBox.showinfo("","Je ne peux pas lire les notes")
            return None
        notesok = True
        for note in notes:
            if note<0 or note>20:
                notesok = False
        if not notesok:
            tkMessageBox.showinfo("","Je ne peux pas lire les notes")
            return None
        self.top.destroy()
        noteseleve = []
        for i,matiere in enumerate(self.matieres):
            noteseleve.append(notes[i])
        self.notes[nom] = noteseleve
        self.affiche_promo()
    def ajouter_etudiant(self):
        self.top = tk.Toplevel()
        self.top.title("Ajout d'un étudiant")

        frame1 = tk.Frame(self.top)
        frame1.pack(side="bottom", expand=True, fill=tk.BOTH)
        label = tk.Label(frame1, text="Nom de l'étudiant")
        label.pack(side="left", expand=True, fill=tk.BOTH)
        self.variablenom = tk.StringVar(self.top)
        entry = tk.Entry(frame1, textvariable=self.variablenom)
        entry.pack(side="right", expand=True, fill=tk.BOTH)
        #
        frame2 = tk.Frame(self.top)
        frame2.pack(side="bottom", expand=True, fill=tk.BOTH)
        self.vars = outils_tk.creer(frame2, self.matieres)

        button = tk.Button(self.top, width=10, text="Fini", command=self.ajouetudbuttonfini)
        button.pack(side="bottom", expand=True, fill=tk.BOTH)

    def ajoumatbuttonfini(self):
        matiere = self.variable.get()
        coeff = float(self.variablecoeff.get())
        try:
            notes = [float(var.get()) for var in self.vars]
        except:
            tkMessageBox.showinfo("","Je ne peux pas lire les notes")
            return None
        notesok = True
        for note in notes:
            if note<0 or note>20:
                notesok = False
        if not notesok:
            tkMessageBox.showinfo("","Je ne peux pas lire les notes")
            return None
        self.matieres, self.coeffs, self.notes = saisie_matieres.ajout_matiere(matiere, coeff, notes, self.matieres, self.coeffs, self.notes)
        self.affiche_promo()

    def ajouter_matiere(self):
        self.top = tk.Toplevel()
        self.top.title("Ajout d'une matière")

        frame1 = tk.Frame(self.top)
        frame1.pack(side="bottom", expand=True, fill=tk.BOTH)
        label = tk.Label(frame1, text="Nom de la matière")
        label.pack(side="left", expand=True, fill=tk.BOTH)
        self.variable = tk.StringVar(self.top)
        entry = tk.Entry(frame1, textvariable=self.variable)
        entry.pack(side="right", expand=True, fill=tk.BOTH)

        frame2 = tk.Frame(self.top)
        frame2.pack(side="bottom", expand=True, fill=tk.BOTH)
        label = tk.Label(frame2, text="Coefficient de la matière")
        label.pack(side="left", expand=True, fill=tk.BOTH)
        self.variablecoeff = tk.StringVar(self.top)
        entry = tk.Entry(frame2, textvariable=self.variablecoeff)
        entry.pack(side="right", expand=True, fill=tk.BOTH)
        #
        frame2 = tk.Frame(self.top)
        frame2.pack(side="bottom", expand=True, fill=tk.BOTH)
        self.vars = outils_tk.creer(frame2, self.notes.keys())

        button = tk.Button(self.top, width=10, text="Fini", command=self.ajoumatbuttonfini)
        button.pack(side="bottom", expand=True, fill=tk.BOTH)


    def definir_menu(self):
        frame = tk.Frame(self.root, width=600, height=400, bd=2, relief=tk.SUNKEN)
        frame.pack(expand=True, fill=tk.BOTH)

        self.text = tk.Text(frame, height=20, width=100, font=("Monaco", 16))
        self.text.pack(side="left", expand=True, fill=tk.BOTH)
        self.text.insert(tk.END, "Veuillez charger les notes\n")
        self.text.configure(state='disabled')

        # honteusement copiè de https://www.tutorialspoint.com/python/tk_menu.htm
        menubar = tk.Menu(self.root)


        menu_fichier = tk.Menu(menubar, tearoff=0)
        menu_fichier.add_command(label="Charger", command=self.lecture)
        menu_fichier.add_command(label="Sauvegarder", command=self.sauvegarde)
        menu_fichier.add_command(label="Sauvegarder sous...", command=self.sauvegardesous)
        menu_fichier.add_command(label="Quitter", command=self.quitter)

        menu_affichage = tk.Menu(menubar, tearoff=0)
        menu_affichage.add_command(label="Radar", command=self.radar)


        menu_gestion = tk.Menu(menubar, tearoff=0)
        menu_gestion.add_command(label="Ajouter un étudiant", command=self.ajouter_etudiant)
        menu_gestion.add_command(label="Ajouter une matière", command=self.ajouter_matiere)
        menu_gestion.add_separator()
        menu_gestion.add_command(label="Supprimer un étudiant", command=self.supprimer_etudiant)
        menu_gestion.add_command(label="Supprimer une matière", command=self.supprimer_matiere)
        menu_gestion.add_separator()
        menu_gestion.add_command(label="Modifier un coefficient", command=self.modifier_coeff)

        menubar.add_cascade(label="Fichier", menu=menu_fichier)
        menubar.add_cascade(label="Affichage", menu=menu_affichage)
        menubar.add_cascade(label="Gestion", menu=menu_gestion)

        self.root.config(menu=menubar)

#================================================================#
# programme principal...
root = tk.Tk()
f = Fenetrage(root)
root.mainloop()
