"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la class brique
a faire :  
"""


class brique :
    """
    creer une brique sur le canvas a partir de ses donnees de dimension (de type int),
    de positions (de type int) et de couleur (de type str)
    le canvas sert a creer et supprimer les briques
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
        permet de supprimer une brique a partir de ses donnees
        """
        self.canvas.delete(self.identifiant)
        
    

                