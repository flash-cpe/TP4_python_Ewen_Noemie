"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la class balle
a faire : modifier le deplacement pour respecter la loi de Descartes quand touche la raquette  prendre en compte les rebords, si la balle atteint le fond moins une vie
"""
import random
import math
import tkinter as tk

class balle :
    def __init__(self, rayon, centre,hauteur, largeur) :
        self.rayon = rayon
        self.centre = centre
        self.hauteur = hauteur
        self.largeur = largeur
        self.x = largeur/2
        self.y = hauteur/2
        
        self.vitesse = random(1.8,2)*5
        self.angle= random.uniform(0,2 * math.pi)
        self.DX = self.vitesse*math.cos(self.angle)
        self.DY = self.vitesse*math.sin(self.angle)
#Balle = Canevas.create_oval(X-RAYON,Y-RAYON,X+RAYON,Y+RAYON,width=1,outline='red',fill='blue')
        self.Balle = tk.Canvas.create_oval(self.x-self.rayon, self.y-self.rayon, self.x+self.rayon, self.y+self.rayon, width=1, outline='red', fill='blue')

    def deplacement(self):
        if self.x + self.rayon + self.DX > self.largeur: #rebon a droite
            self.x = 2*(self.largeur- self.rayon)-self.x
            self.DX= -self.DX

        if self.x - self.rayon +self.DX<0: # rebon a gauche
            self.x= 2*(self.rayon-self.rayon)-self.x
            self.DX=-self.DX
        if self.y - self.rayon +self.DY<0: #rebon en haut
            self.y=2*(self.rayon-self.y)
            self.DY =- self.DY
            
        self.x += self.DX
        self.y += self.DY

    
