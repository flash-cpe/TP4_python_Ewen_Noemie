"""
date : 10/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la class brique
a faire : 
"""

from class_brique import brique

class gestion_brique :

    def __init__(self, canvas) :
        self.canvas = canvas
        self.liste_brique = []



    def creer_brique (self, espace, couleur, nb_ligne, nb_colonne) :
        hauteur_canvas = int(self.canvas.cget("height"))
        largeur_canvas = int(self.canvas.cget("width"))

        hauteur_brique = (hauteur_canvas / 3) / nb_ligne - espace
        largeur_brique = largeur_canvas / nb_colonne - espace

        for ligne in range(nb_ligne) :
            for colonne in range(nb_colonne) :
                x = espace + colonne * (largeur_brique + espace)                    
                y = espace + ligne * (hauteur_brique + espace)
    
                self.canvas.create_rectangle(x, y, x + largeur_brique, 
                                             y + hauteur_brique, fill = couleur)

                Brique = brique(x, y, hauteur_brique, largeur_brique, couleur, self.canvas)
                self.liste_brique.append(Brique)