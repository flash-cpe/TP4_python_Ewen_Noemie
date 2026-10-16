"""

prout
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la classe de la fenetre du jeu
a faire : impossibilité de mettre la fonction clavier dans la class barre
car il y un probleme d'importation circulaire

Le jeu devra présenter une implémentation de liste, une de file et une de pile 

fichier readme indiquant les règles du jeu et les spécificités de votre implémentation

a faire finir de modifier les interfaces

probleme de cassage de plusieurs briques en meme temps 

creer une interface pour quand le joueur perd, idée : affiche un message "perdu" et un bouton pour revenir au menu, juste utilise le bouton de demarage de partie

creer differentes briques avec des vies

implementes des niveau a choisir depuis le menu et donc faire un retour au menu
"""

import numpy as np
from time import sleep
import tkinter as tk
from class_raquette import raquette
from class_balle import balle
from class_gestion_brique import gestion_brique



class fenetre :

    def __init__(self) :

        self.raquette_info = raquette(10, 100, "blue")
        self.vie = 1
        self.fenetre = tk.Tk()
        self.fenetre.title("Casse Brique")
        self.menu()

        # ecran d'acceuil
        self.frame_acceuil = tk.Frame(self.fenetre, width = 650, height = 730, bg = '#2a2a2a')
        self.frame_acceuil.pack_propagate(False)
        self.frame_acceuil.pack(side = "top")

        self.bouton_jouer = tk.Button(self.frame_acceuil, text = "jouer", command = self.charger_ecran_jeu,
                                    fg = "#07fa1f", bg = '#1a1a1a', padx = 20, pady = 17, font=("Arial", 20, "bold"))
        self.bouton_jouer.pack(pady = 30)

        # ecran de jeu
        self.frame_jeu = tk.Frame(self.fenetre, bg = '#2a2a2a')
        self.frame_info = tk.Frame(self.fenetre)

        self.frame_bar = tk.Frame(self.frame_jeu, width = 650, height = 50, bg = '#1a1a1a')
        self.frame_bar.pack(side = "top", fill = "x")

        self.text_score = tk.Label(self.frame_bar, text = "Score :", font = ("Helvetica", 12, "bold"))
        self.text_score.pack(padx = 20, pady = 10, side = "right")

        self.text_vie = tk.Label(self.frame_info, text = "Vie :", font = ("Helvetica", 12, "bold"))
        self.text_vie.pack(padx = 20, pady = 10, side = "left")

        self.canvas = tk.Canvas(self.frame_jeu, width = 650, height = 650, bg = 'black')
        self.canvas.pack()


        # position initiale de la raquette
        self.PosX = int(self.canvas.cget("width")) / 2 
        self.PosY = int(self.canvas.cget("height")) - 30  

       
        self.canvas.focus_set()
        self.canvas.bind('<Key>', self.clavier)
        self.canvas.pack()

       
        # bouton de demarage
        self.bouton_Jeu = tk.Button(self.frame_jeu, text = "démarrer une partie", command = self.lancement_jeu)
        self.bouton_Jeu.pack()

        # bouton pour quitter le jeu
        self.bouton_fermer = tk.Button(self.frame_jeu, text = "quitter le jeu", fg = "red", command = self.fermer)
        self.bouton_fermer.pack(side = "bottom", pady = "5", padx = "5")

        
        
    def charger_ecran_jeu(self) :
        """
        lance l'ecran du jeu
        """
        self.frame_acceuil.pack_forget()
        self.frame_jeu.pack(side = "bottom")
        self.frame_info.pack(side = "top")
        self.canvas.focus_set()


    def lancement_jeu(self) :
        """
        creer tous les objets du canvas et initialise les valeurs
        """
        self.canvas.delete("all")

        self.score = 0
        self.text_score.config(text = f"Score : {self.score}")

        self.vie = 3
        self.text_vie.config(text = f"Vie : {self.vie}")

         # creation des briques
        self.gestion_briques = gestion_brique(self.canvas)
        self.gestion_briques.creer_brique(5, "green", 10, 10)

         # creation de la raquette
        self.raquette = self.canvas.create_rectangle(self.PosX - (self.raquette_info.larguer / 2),
                                                    self.PosY - (self.raquette_info.hauteur / 2),
                                                    self.PosX + (self.raquette_info.larguer / 2),
                                                    self.PosY + (self.raquette_info.hauteur / 2),
                                                    fill = self.raquette_info.couleur
                                                    )

        #creation de la balle
        self.balle_info = balle(self.canvas, self.fenetre, 15, int(self.canvas.cget("height")),
                                int(self.canvas.cget("width")))
        
        self.deplacement()


    def fermer(self) :
        """
        permer de fermer le fenetre principale 
        """
        self.fenetre.destroy()

    def menu(self) :
        """
        permet de créer un menu avec différantes options (a determiner)
        """
        self.menu_Principal = tk.Menu(self.fenetre)
        self.menu_nondetachable = tk.Menu(self.fenetre, tearoff = 0)
        self.menu_detachable = tk.Menu(self.fenetre, tearoff = 1)
        self.menu_Principal.add_cascade(label = "Menu1", menu = self.menu_nondetachable)
        self.menu_Principal.add_cascade(label = "Menu2", menu = self.menu_detachable)
        self.menu_detachable.add_command(label = "Quitter", command = self.fermer)
        self.fenetre['menu'] = self.menu_Principal


   



    def clavier(self, event) :
        """
        gere le deplacement de la raquette et l'empeche de sortir du canvas
        """
        self.largeur_canvas = self.canvas.winfo_width()

        # Gestion de l'evenement Appui sur une touche du clavier 
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
                


    def collision(self, objet1, objet2) :
        """
        return True si il y a une collision entre les deux ojets
        """
        x1, y1, x2, y2 = self.canvas.coords(objet1)
        a1, b1, a2, b2 = self.canvas.coords(objet2)

        return (x1 < a2 and x2 > a1 and y1 < b2 and y2 > b1)



    def deplacement(self) :
        """
        gere le deplacement et les collision de la balle
        """
        if self.vie != 0 :
            # verification des collisions avec les briques
            self.gestion_briques.verifier_collision_balle(self.balle_info, self.canvas)

            # si il a une collision avec une brique, le score augmente de 1
            if self.gestion_briques.verifier_collision_balle(self.balle_info, self.canvas) == True :
                self.score += 1
                self.text_score.config(text = f"Score : {self.score}")

            # gestion des collisions avec les murs
            if self.collision(self.balle_info.Balle, self.raquette) != True :

                # rebond a droite
                if self.balle_info.x + self.balle_info.rayon + self.balle_info.DX > self.balle_info.largeur : 
                    self.balle_info.x = 2 * (self.balle_info.largeur - self.balle_info.rayon) - self.balle_info.x
                    self.balle_info.DX = - self.balle_info.DX

                # rebond a gauche
                if self.balle_info.x - self.balle_info.rayon + self.balle_info.DX  < 0 : 
                    self.balle_info.x = 2 * (self.balle_info.rayon - self.balle_info.rayon) - self.balle_info.x
                    self.balle_info.DX = - self.balle_info.DX

                 # rebond en haut
                if self.balle_info.y - self.balle_info.rayon + self.balle_info.DY < 0 :
                    self.balle_info.y = 2 * np.abs((self.balle_info.rayon - self.balle_info.y))
                    self.balle_info.DY = - self.balle_info.DY

                # touche le bas du canvas
                if self.balle_info.y + self.balle_info.rayon >= int(self.canvas.cget("height")) :
                    self.canvas.delete(self.balle_info.Balle)
                    self.vie -= 1
                    self.text_vie.config(text = f"Vie : {self.vie}")
                    self.balle_info = balle(self.canvas, self.fenetre, 15,
                                            int(self.canvas.cget("height")), int(self.canvas.cget("width")))

            # collision avec la raquette
            elif self.collision(self.balle_info.Balle, self.raquette) == True :
                self.balle_info.DY = - self.balle_info.DY

                if self.balle_info.x - self.PosX > self.raquette_info.larguer / 5 :
                    self.balle_info.DX = np.abs(self.balle_info.DX) * (1 + (self.balle_info.x - self.PosX) / (33 * self.balle_info.DX))
                    
                elif self.balle_info.x - self.PosX < - self.raquette_info.larguer / 5 :
                    self.balle_info.DX = - np.abs(self.balle_info.DX) * (1 + (self.PosX - self.balle_info.x) / (33 * self.balle_info.DX))
                    
                    
            # nouvelle vitesse de la balle
            self.balle_info.x += self.balle_info.DX
            self.balle_info.y += self.balle_info.DY

            # nouvelle coordonnees de la balle
            self.canvas.coords(self.balle_info.Balle,
                                self.balle_info.x - self.balle_info.rayon,
                                self.balle_info.y - self.balle_info.rayon,
                                self.balle_info.x + self.balle_info.rayon,
                                self.balle_info.y + self.balle_info.rayon)

            # rafraichissement de la fenetre pour mettre a jour la position et le vitesse
            self.fenetre.after(50, self.deplacement)








