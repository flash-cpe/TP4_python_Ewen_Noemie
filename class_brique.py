"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la class brique
a faire : utiliser soit une pile soit une file si possible 
"""


class brique :
    """
    creer une brique sur le canvas a partir de ses donnees de dimension, de positions et de couleur
    """

    def __init__(self, posX, posY, hauteur, largeur, couleur, canvas) :
        self.hauteur = hauteur
        self.largeur = largeur
        self.couleur = couleur
        self.canvas = canvas
        self.x = posX
        self.y = posY

        # creation de la brique
        self.identifiant = canvas.create_rectangle(self.x, self.y, self.x + self.largeur,
                                                   self.y + self.hauteur, fill = self.couleur)


    def detruire(self) :
        """
        permet de suprimer une brique a partir de ses donnees
        """
        self.canvas.delete(self.identifiant)
        
    

                