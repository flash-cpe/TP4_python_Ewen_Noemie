"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la classe de la fenetre du jeu
a faire : impossibilité de mettre la fonction clavier dans la class barre
car il y un probleme d'importation circulaire

Le jeu devra présenter une implémentation de liste, une de file et une de pile 

fichier readme indiquant les règles du jeu et les spécificités de votre implémentation

"""

from time import sleep
import random
import tkinter as tk
from class_raquette import raquette
from class_balle import balle
from class_gestion_brique import gestion_brique



class fenetre :

    def __init__(self):
        self.raquette_info = raquette(10, 100, "blue")
        
        self.fenetre = tk.Tk()
        self.fenetre.title("Casse Brique")

        self.frame = tk.Frame(self.fenetre)
        self.frame.pack(side = "top")

        self.text_score = tk.Label(self.frame, text = "Score :")
        self.text_score.pack(padx = "200", pady = "5", side ="right")

        self.text_vie = tk.Label(self.frame, text = "Vie :")
        self.text_vie.pack(padx = "5", pady = "5", side ="left")

        self.canvas=tk.Canvas(self.fenetre, width = 650, height = 650, bg = 'black')

        # position initiale de la raquette
        self.PosX = int(self.canvas.cget("width")) / 2 #320
        self.PosY = int(self.canvas.cget("height")) - 30  #620

       
        self.canvas.focus_set()
        self.canvas.bind('<Key>', self.clavier)
        self.canvas.pack()

       

        self.bouton_Jeu = tk.Button(self.fenetre, text = "démarrer une partie", command = self.lancement_jeu)
        self.bouton_Jeu.pack()

        # bouton pour quitter le jeu
        self.bouton_fermer = tk.Button(self.fenetre, text = "quitter le jeu", fg = "red", command = self.fermer)
        self.bouton_fermer.pack(side = "bottom", pady = "5", padx = "5")

        
        
  
    def lancement_jeu(self) :
         # creation des briques
        self.gestion_briques = gestion_brique(self.canvas)
        self.gestion_briques.creer_brique(5, "green", 10, 10)

         # creation de la raquette
        self.raquette = self.canvas.create_rectangle(self.PosX - (self.raquette_info.larguer / 2),
                                                    self.PosY - (self.raquette_info.hauteur / 2),
                                                    self.PosX + (self.raquette_info.larguer / 2),
                                                    self.PosY + (self.raquette_info.hauteur / 2),
                                                    fill= self.raquette_info.couleur
                                                    )

        #creation de la balle
        self.balle_info = balle(self.canvas, self.fenetre, 15, 0, int(self.canvas.cget("height")),
                                int(self.canvas.cget("width")))
        self.deplacement()


    def fermer(self):
        """
        permer de fermer le fenetre principale 
        """
        self.fenetre.destroy()

    def menu(self):
        self.menu_Principal= tk.Menu(self.fenetre)
        self.menu_nondetachable=tk.Menu(self.fenetre, tearoff = 0)
        self.menu_detachable= tk.Menu(self.fenetre, tearoff = 1)
        self.menu_Principal.add_cascade(label = "Menu1", menu = self.menu_nondetachable)
        self.menu_Principal.add_cascade(label = "Menu2", menu = self.menu_detachable)
        self.menu_detachable.add_command(labe = "Quitter", command = self.fermer)


        #self.menu_principal.add_command(label = "quitter", command = self.fermer)



    def clavier(self, event):
                """
                gere le deplacement de la raquette et l'empeche de sortir du canvas
                """
                self.largeur_canvas = self.canvas.winfo_width()
                """ Gestion de l'evenement Appui sur une touche du clavier """
                touche = event.keysym
                
                # deplacement vers la droite
                if touche == "Right" and (self.PosX + 20 + self.raquette_info.larguer / 2) < self.largeur_canvas :
                    self.PosX += 20
                elif touche == "Right" :
                     self.PosX += self.largeur_canvas - (self.PosX + self.raquette_info.larguer / 2)
                
                # deplacement vers la gauche
                if touche == "Left" and (self.PosX - 20 - self.raquette_info.larguer / 2) > 0 :
                    self.PosX -= 20
                elif touche == "Left" :
                    self.PosX -= (self.PosX - self.raquette_info.larguer / 2)
                
                # on dessine le pion a sa nouvelle position
                self.canvas.coords(self.raquette,
                                   self.PosX - (self.raquette_info.larguer / 2),
                                   self.PosY - (self.raquette_info.hauteur / 2),
                                   self.PosX + (self.raquette_info.larguer / 2),
                                   self.PosY + (self.raquette_info.hauteur / 2)
                                   )
                
    def collision_balle(self):
   
            b = self.balle_info
            r = self.raquette_info
           
   
            rx1 = self.PosX - (r.larguer / 2)
            rx2 = self.PosX + (r.larguer / 2)
            ry1 = self.PosY - (r.hauteur / 2)
            ry2 = self.PosY + (r.hauteur / 2)
   
            bx1 = b.x - b.rayon
            bx2 = b.x + b.rayon
            by1 = b.y - b.rayon
            by2 = b.y + b.rayon
   
           
            if bx2 < rx1 or bx1 > rx2 or by2 < ry1 or by1 > ry2:
               return
   
            overlap_x = min(bx2, rx2) - max(bx1, rx1)
            overlap_y = min(by2, ry2) - max(by1, ry1)
   
   
            if overlap_x < overlap_y:
               b.DX = -b.DX
   
               if b.DX > 0:
                   b.x = rx2 + b.rayon
               else:
                   b.x = rx1 - b.rayon
            else:
               b.DY = -b.DY
   
               if b.DY > 0:
                   b.y = ry2 + b.rayon
               else:
                   b.y = ry1 - b.rayon
   
            self.canvas.coords(b.Balle, 
                               b.x - b.rayon,
                               b.y - b.rayon, 
                               b.x + b.rayon, 
                               b.y + b.rayon)



    def deplacement(self):
        print("test")
        print(self.balle_info.x)
        print(self.balle_info.y)
        if self.balle_info.x + self.balle_info.rayon + self.balle_info.DX > self.balle_info.largeur: #rebon a droite
            self.balle_info.x = 2*(self.balle_info.largeur- self.balle_info.rayon)-self.balle_info.x
            self.balle_info.DX= -self.balle_info.DX
    
        if self.balle_info.x - self.balle_info.rayon +self.balle_info.DX<0: # rebon a gauche
            self.balle_info.x= 2*(self.balle_info.rayon-self.balle_info.rayon)-self.x
            self.balle_info.DX=-self.balle_info.DX
        if self.balle_info.y - self.balle_info.rayon +self.balle_info.DY<0: #rebon en haut
            self.balle_info.y=2*(self.rayon-self.y)
            self.balle_info.DY =- self.balle_info.DY
                
        self.balle_info.x += self.balle_info.DX*10
        self.balle_info.y += self.balle_info.DY*10

        self.canvas.coords(self.balle_info.Balle,
                            self.balle_info.x - self.balle_info.rayon,
                            self.balle_info.y - self.balle_info.rayon,
                            self.balle_info.x + self.balle_info.rayon,
                            self.balle_info.y + self.balle_info.rayon)
        print("test 2")
        print(self.balle_info.x)
        print(self.balle_info.y)
        self.fenetre.after(50, self.deplacement)
