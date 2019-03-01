import Tkinter as tk
import sauvegardelecture, affichage

def creer(root, matieres):
    root.grid_columnconfigure((0, 1), weight=1)
    vars = []
    for i,matiere in enumerate(matieres):
        var = tk.StringVar(root)
        label = tk.Label(root, text=matiere)
        entry = tk.Entry(root, bd=5, textvariable=var)
        label.grid(row=i, column=0)
        entry.grid(row=i, column=1)
        vars.append(var)
    return vars



#================================================================#
if __name__ == '__main__':
    (matieres, coeffs, notes) = sauvegardelecture.lecture('notes.txt')
    root = tk.Tk()
    root.geometry("600x200")
    creer(root, matieres)
    root.mainloop()
