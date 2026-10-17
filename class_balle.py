"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la class balle
a faire : modifier le deplacement pour respecter la loi de Descartes quand touche la raquette  prendre en compte les rebords,
si la balle atteint le fond moins une vie
"""
import random
import math
import tkinter as tk
from time import sleep


class balle :
    """
    creer la balle avec toutes ses inforations de dimension et lui donne une vitesse initiale
    """
    
    def __init__(self, canvas, fenetre, rayon, hauteur, largeur) :
        self.rayon = rayon
        self.hauteur = hauteur
        self.largeur = largeur
        self.x = largeur / 2
        self.y = hauteur / 2
        self.canvas = canvas
        self.fenetre = fenetre

        # creetion de la vitesse
        self.vitesse = 16 #random.uniform(1.8, 2) * 5
        self.angle = random.uniform(0, 2 * math.pi)
        if self.angle < math.pi * (5 / 3) and self.angle > math.pi * (4 / 3) :
            self.angle += (math.pi / 3) * math.copysign(1, self.angle)
            
        self.DX = self.vitesse*math.cos(self.angle)
        self.DY = self.vitesse*math.sin(self.angle)

        # creation de la balle
        self.Balle = self.canvas.create_oval(self.x - self.rayon, self.y - self.rayon, self.x + self.rayon,
                                            self.y + self.rayon, width = 1, outline = 'red', fill = 'blue')

