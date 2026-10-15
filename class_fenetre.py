"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la classe de la fenetre du jeu
a faire : impossibilité de mettre la fonction clavier dans la class barre
car il y un probleme d'importation circulaire

Le jeu devra présenter une implémentation de liste, une de file et une de pile 

fichier readme indiquant les règles du jeu et les spécificités de votre implémentation

probleme, le balle s'arrete sur les briques
"""

import numpy as np

import tkinter as tk
from class_raquette import raquette
from class_balle import balle
from class_gestion_brique import gestion_brique



class fenetre :

    def __init__(self):
        self.raquette_info = raquette(10, 100, "blue")
        
        self.fenetre = tk.Tk()
        self.fenetre.title("Casse Brique")
        self.menu()
#Ecran principal

        self.frame_acceuil =tk.Frame(self.fenetre,width=650, height=730, bg='#2a2a2a')
        self.frame_acceuil.pack_propagate(False)
        self.frame_acceuil.pack(side="top")

        self.bouton_jouer=tk.Button(self.frame_acceuil,text="jouer", command= self.charger_ecran_jeu)
        self.bouton_jouer.pack(pady=20)

#ecran de jeu

        self.frame_jeu = tk.Frame(self.fenetre)


        self.text_score = tk.Label(self.frame_jeu, text = "Score :")
        self.text_score.pack(padx = "200", pady = "5", side ="right")

        self.text_vie = tk.Label(self.frame_jeu, text = "Vie :")
        self.text_vie.pack(padx = "5", pady = "5", side ="left")

        self.canvas=tk.Canvas(self.frame_jeu, width = 650, height = 650, bg = 'black')

        # position initiale de la raquette
        self.PosX = int(self.canvas.cget("width")) / 2 #320
        self.PosY = int(self.canvas.cget("height")) - 30  #620

       
        self.canvas.focus_set()
        self.canvas.bind('<Key>', self.clavier)
        self.canvas.pack()

       

        self.bouton_Jeu = tk.Button(self.frame_jeu, text = "démarrer une partie", command = self.lancement_jeu)
        self.bouton_Jeu.pack()

        # bouton pour quitter le jeu
        self.bouton_fermer = tk.Button(self.frame_jeu, text = "quitter le jeu", fg = "red", command = self.fermer)
        self.bouton_fermer.pack(side = "bottom", pady = "5", padx = "5")

        
        
    def charger_ecran_jeu(self):
        self.frame_acceuil.pack_forget()
        self.frame_jeu.pack()
        self.canvas.focus_set()

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
        """permet de créer un menu avec différantes options (a determiner)"""
        self.menu_Principal = tk.Menu(self.fenetre)
        self.menu_nondetachable = tk.Menu(self.fenetre, tearoff = 0)
        self.menu_detachable = tk.Menu(self.fenetre, tearoff = 1)
        self.menu_Principal.add_cascade(label = "Menu1", menu = self.menu_nondetachable)
        self.menu_Principal.add_cascade(label = "Menu2", menu = self.menu_detachable)
        self.menu_detachable.add_command(label = "Quitter", command = self.fermer)
        self.fenetre['menu'] = self.menu_Principal


   



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


    def collision(self, objet1, objet2):
        x1, y1, x2, y2 = self.canvas.coords(objet1)
        a1, b1, a2, b2 = self.canvas.coords(objet2)

        return (x1 < a2 and x2 > a1 and y1 < b2 and y2 > b1)



    def deplacement(self):
        # 1. Vérification des collisions avec les briques
        self.gestion_briques.verifier_collision_balle(self.balle_info, self.canvas)

        # 2. Gestion des collisions avec la raquette
        if self.collision(self.balle_info.Balle, self.raquette) != True :

            if self.balle_info.x + self.balle_info.rayon + self.balle_info.DX > self.balle_info.largeur : # rebond a droite
                self.balle_info.x = 2 * (self.balle_info.largeur - self.balle_info.rayon) - self.balle_info.x
                self.balle_info.DX = - self.balle_info.DX
            
            if self.balle_info.x - self.balle_info.rayon + self.balle_info.DX  < 0 : # rebond a gauche
                self.balle_info.x = 2 * (self.balle_info.rayon - self.balle_info.rayon) - self.balle_info.x
                self.balle_info.DX = - self.balle_info.DX

            if self.balle_info.y - self.balle_info.rayon + self.balle_info.DY < 0 : # rebond en haut
                self.balle_info.y = 2 * np.abs((self.balle_info.rayon - self.balle_info.y))
                self.balle_info.DY = - self.balle_info.DY
                        
        elif self.collision(self.balle_info.Balle, self.raquette) == True :
            self.balle_info.DY = - self.balle_info.DY

        self.balle_info.x += self.balle_info.DX
        self.balle_info.y += self.balle_info.DY

        self.canvas.coords(self.balle_info.Balle,
                            self.balle_info.x - self.balle_info.rayon,
                            self.balle_info.y - self.balle_info.rayon,
                            self.balle_info.x + self.balle_info.rayon,
                            self.balle_info.y + self.balle_info.rayon)
        
        self.fenetre.after(50, self.deplacement)







