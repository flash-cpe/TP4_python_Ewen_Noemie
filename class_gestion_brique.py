"""
date : 10/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la class brique
a faire : vie des briques en fonction du niveau
"""

from class_brique import brique

class gestion_brique :
    """
    permet de gerer l'ensemble des briques 
    """

    def __init__(self, canvas) :
        self.canvas = canvas
        self.liste_brique = []


    def creer_brique(self, espace, couleur, nb_ligne, nb_colonne) :
        """
        creer les briques et les stock dans une liste.
        La taille des briques s'adapte a la taille du canvas
        """
        hauteur_canvas = int(self.canvas.cget("height"))
        largeur_canvas = int(self.canvas.cget("width"))

        hauteur_brique = (hauteur_canvas / 3) / nb_ligne - espace
        largeur_brique = largeur_canvas / nb_colonne - espace

        for ligne in range(nb_ligne) :
            for colonne in range(nb_colonne) :
                x = espace + colonne * (largeur_brique + espace)                     
                y = espace + ligne * (hauteur_brique + espace)
    
                B = brique(x, y, hauteur_brique, largeur_brique, couleur, self.canvas)
                self.liste_brique.append(B)


    def verifier_collision_balle(self, balle_info, canvas) :
        """
        Vérifie la collision entre la balle et chaque brique.
        Si collision il y a : on détruit la brique, on inverse la direction de la balle et on renvoie True.
        """
        bx1 = balle_info.x - balle_info.rayon
        bx2 = balle_info.x + balle_info.rayon
        by1 = balle_info.y - balle_info.rayon
        by2 = balle_info.y + balle_info.rayon

        for b in self.liste_brique :
            # Récupère les coordonnées actuelles de la brique sur le canvas
            coords = canvas.coords(b.identifiant)
            if not coords:
                continue
            rx1, ry1, rx2, ry2 = coords

            # Test de collision AABB (Box-Box)
            if bx1 < rx2 and bx2 > rx1 and by1 < ry2 and by2 > ry1 :
                # Destruction de la brique
                b.detruire()
                self.liste_brique.remove(b)

                # Inversion de la trajectoire verticale de la balle (rebond)
                balle_info.DY = - balle_info.DY
                return True
        return False
