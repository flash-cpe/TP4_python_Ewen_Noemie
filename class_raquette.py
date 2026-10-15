"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la class barre
a faire :
"""

class raquette :
    def __init__(self, hauteur, largeur, couleur) :
        """
        creation de la classe barre, qui permet d'avoir les information de dimension (de type int) et
        de couleur de la barre (de type str)
        """
        self.hauteur = hauteur
        self.larguer = largeur
        self.couleur = couleur

