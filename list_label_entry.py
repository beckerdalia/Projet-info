import Tkinter as tk
import sauvegardelecture, affichage

def creer(root, matieres):
    root.geometry("600x200")
    root.grid_columnconfigure((0, 1), weight=1)
    for i,matiere in enumerate(matieres):
        label = tk.Label(root, text=matiere)
        entry = tk.Entry(root, bd=5)
        label.grid(row=i, column=0)
        entry.grid(row=i, column=1)



#================================================================#
if __name__ == '__main__':
    (matieres, coeffs, notes) = sauvegardelecture.lecture('notes.txt')
    root = tk.Tk()
    creer(root, matieres)
    root.mainloop()
