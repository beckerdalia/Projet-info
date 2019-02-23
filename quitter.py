import os
from sys import platform as sys_exploitation

def efface_ecran():
    """
    Permet d'effacer l'ecran en mode console
    """
    if sys_exploitation == "win32" or sys_exploitation == "win64":
        os.system('cls')
    else:
        os.system('clear')
    return None