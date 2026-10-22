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
        self.hauteur_brique = 40
        self.largeur_brique = 90

    def creer_brique(self, espace, couleur, nb_ligne, nb_colonne, saut_colonne, ligne_debut) :
        """
        creer les briques et les stock dans une liste.
        La taille des briques s'adapte a la taille du canvas
        """
    

        for ligne in range(nb_ligne) :
            for colonne in range(int(nb_colonne / (1 + saut_colonne))) :
                x = espace / 2 + colonne * (1 + saut_colonne) * (self.largeur_brique + espace)                     
                y = ligne_debut * (self.hauteur_brique + espace) + espace + ligne * (self.hauteur_brique + espace)
    
                B = brique(x, y, self.hauteur_brique, self.largeur_brique, couleur, self.canvas)
                self.liste_brique.append(B)


    def verifier_collision_balle(self, balle_info, canvas) :
        """
        verifie la collision entre la balle et chaque brique (dessus/dessous et cotes).
        si collision il y a : on détruit la brique, on inverse la bonne direction de la balle et on renvoie True.
        """
        b = balle_info
        bx1 = b.x - b.rayon
        bx2 = b.x + b.rayon
        by1 = b.y - b.rayon
        by2 = b.y + b.rayon

        for brique_obj in self.liste_brique :
            # recupere les coordonnees actuelles de la brique sur le canvas
            coords = canvas.coords(brique_obj.identifiant)
            if not coords:
                continue
            rx1, ry1, rx2, ry2 = coords

            # test de collision AABB (Box-Box)
            if bx1 < rx2 and bx2 > rx1 and by1 < ry2 and by2 > ry1 :
                # calcul de la profondeur du chevauchement pour savoir si on tape par le cote ou par le haut/bas
                overlap_x = min(bx2, rx2) - max(bx1, rx1)
                overlap_y = min(by2, ry2) - max(by1, ry1)

                # destruction de la brique
                if self.canvas.itemcget(brique_obj.identifiant, "fill") == "green" :
                    self.canvas.itemconfig(brique_obj.identifiant, fill = "red")

                elif self.canvas.itemcget(brique_obj.identifiant, "fill") == "red" :
                    brique_obj.detruire()
                    self.liste_brique.remove(brique_obj)

                # si le chevauchement en X est plus petit, c est un rebond sur le cote (gauche ou droite)
                if overlap_x < overlap_y:
                    b.DX = -b.DX
                    # repositionnement pour eviter que la balle ne reste bloquee dans la brique
                    if b.DX > 0 :
                        b.x = rx2 + b.rayon
                    else :
                        b.x = rx1 - b.rayon
                # sinon, c est un rebond vertical (haut ou bas)
                else :
                    b.DY = -b.DY
                    if b.DY > 0 :
                        b.y = ry2 + b.rayon
                    else :
                        b.y = ry1 - b.rayon

                return True
        return False