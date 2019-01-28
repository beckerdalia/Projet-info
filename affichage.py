from ecriturelecture import lecture

def affichage(matieres, data) :
    eleves = sorted(data)
    maxname = len(max(eleves, key=len))+5
    maxmat = len(max(matieres, key=len))+5
    nmat = len(matieres)

    fmtname = "{:>"+str(maxname)+"s}"
    fmtmat = "{:^"+str(maxmat)+"s}"

    print fmtname.format(""),
    for i in range(len(matieres)):
        print fmtmat.format(matieres[i]),
    print ""
    for nom in eleves:
        print fmtname.format(nom),
        for i in range(nmat):
            print fmtmat.format(str(data[nom][i])),
        print ""

#================================================================#
if __name__ == '__main__':
    matieres, data = lecture('notes.txt')
    affichage(matieres, data)