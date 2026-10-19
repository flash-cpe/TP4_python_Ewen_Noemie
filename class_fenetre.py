"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la classe de la fenetre du jeu
a faire : impossibilité de mettre la fonction clavier dans la class barre
car il y un probleme d'importation circulaire

Le jeu devra présenter une implémentation de file et une de pile 

fichier readme indiquant les règles du jeu et les spécificités de votre implémentation

a faire finir de modifier les interfaces

possible fusion entre fin_jeu() et gagnez()

ameliorer les rebonds sur la raquette (pouvoir enleve de l'angle pour tirer plus droit)
"""

import numpy as np
import tkinter as tk
from collections import deque

from class_raquette import raquette
from class_balle import balle
from class_gestion_brique import gestion_brique



class fenetre :

    def __init__(self) :
        self.file_niveaux = deque(["niveau_1", "niveau_2", "niveau_3"])

        self.raquette_info = raquette(10, 100, "blue")
        self.vie = 1
        self.fenetre = tk.Tk()
        self.fenetre.title("Casse Brique")
        self.menu()

    # ecran d'acceuil
        # creation d une frame
        self.frame_acceuil = tk.Frame(self.fenetre, width = 650, height = 730, bg = '#2a2a2a')
        self.frame_acceuil.pack_propagate(False)
        self.frame_acceuil.pack(side = "top")

        # creation des boutons pour chaque niveau (de 1 a 4)
        for i in range(1, 5):
            btn = tk.Button(self.frame_acceuil, text = f"Niveau {i}",
                command = lambda niv = i : self.charger_ecran_jeu(niv),
                bg = '#1a1a1a', fg = "#07fa1f", font = ("Arial", 14), padx = 15, pady = 5)
            btn.pack(pady = 10)

        # bouton pour quitter le jeu
        self.bouton_fermer = tk.Button(self.frame_acceuil, text = "quitter le jeu", fg = "red", command = self.fermer)
        self.bouton_fermer.pack(side = "bottom", pady = "5", padx = "5")

    # ecran de jeu
        self.frame_jeu = tk.Frame(self.fenetre, bg = '#2a2a2a')
        self.frame_info = tk.Frame(self.fenetre)

        self.frame_bar = tk.Frame(self.frame_jeu, width = 650, height = 50, bg = '#1a1a1a')

        self.text_niveau = tk.Label(self.frame_info, text = "Niveau :", font = ("Helvetica", 12, "bold"))
        self.text_niveau.pack(padx = 20, pady = 10)

        self.text_score = tk.Label(self.frame_bar, text = "Score :", font = ("Helvetica", 12, "bold"))
        self.text_score.pack(padx = 20, pady = 10, side = "right")

        self.text_vie = tk.Label(self.frame_bar, text = "Vie :", font = ("Helvetica", 12, "bold"))
        self.text_vie.pack(padx = 20, pady = 10, side = "left")

        self.canvas = tk.Canvas(self.frame_jeu, width = 650, height = 650, bg = 'black')
        self.canvas.pack()


        # position initiale de la raquette
        self.PosX = int(self.canvas.cget("width")) / 2 
        self.PosY = int(self.canvas.cget("height")) - 30  

       
        self.canvas.focus_set()
        self.canvas.bind('<Key>', self.clavier)
        self.canvas.pack()

        # boutton pour lancer le jeu
        self.bouton_rejouer = tk.Button(self.canvas, text = "Jouer", command = self.lancement_jeu,
                    bg = "#4CAF50", fg = "white", font = ("Arial", 14, "bold"), padx = 10, pady = 5)
        self.canvas.create_window(325, 300, window = self.bouton_rejouer)

        # boutton pour retourner au menu
        self.bouton_retour = tk.Button(self.canvas, text = "Retour", command = self.ecran_menu,
                    bg = "#333333", fg = "white", font = ("Arial", 14, "bold"), padx = 10, pady = 5)
        self.canvas.create_window(325, 400, window = self.bouton_retour)

        # bouton pour quitter le jeu
        self.bouton_fermer = tk.Button(self.frame_jeu, text = "quitter le jeu", fg = "red", command = self.fermer)
        self.bouton_fermer.pack(side = "bottom", pady = "5", padx = "5")

    def ecran_menu(self) :
        """
        cache la frame du jeu qui contient le canvas et les info du score, vie, niveau.
        Et affiche la frame du menu
        """
        # verifie si le canvas existe
        if hasattr(self, "canvas") :
            self.canvas.delete("fin")

        self.frame_jeu.pack_forget()
        self.frame_bar.pack_forget()
        self.frame_info.pack_forget()

        self.frame_acceuil.pack(side = "top")


    def charger_ecran_jeu(self, niveau) :
        """
        charge l'ecran du jeu et cache la frame du menu
        """
        self.niveau = niveau
        self.text_niveau.config(text = f"Niveau : {self.niveau}")

        self.frame_acceuil.pack_forget()

        self.frame_info.pack(side = "top")
        self.frame_bar.pack(side = "top", fill = "x")
        self.frame_jeu.pack(side = "bottom")

        self.bouton_jouer = tk.Button(self.canvas, text = "Jouer", command = self.lancement_jeu,
                    bg = "#4CAF50", fg = "white", font = ("Arial", 14, "bold"), padx = 10, pady = 5)
        self.canvas.create_window(325, 300, window = self.bouton_jouer)

        self.bouton_retour_menu = tk.Button(self.canvas, text = "Retour", command = self.ecran_menu,
                    bg = "#333333", fg = "white", font = ("Arial", 14, "bold"), padx = 10, pady = 5)
        self.canvas.create_window(325, 400, window = self.bouton_retour_menu)

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

        # creation des briques, creer_brique(espece, couleur, ligne, colonne)
        if self.niveau == 1 : 
            self.gestion_briques = gestion_brique(self.canvas)
            self.gestion_briques.creer_brique(40, "red", 2, 5)
        if self.niveau == 2 :
            self.gestion_briques = gestion_brique(self.canvas)
            self.gestion_briques.creer_brique(20, "red", 4, 5)
        if self.niveau == 3 :
            self.gestion_briques = gestion_brique(self.canvas)
            self.gestion_briques.creer_brique(40, "green", 2, 5)
        if self.niveau == 4 :
            self.gestion_briques = gestion_brique(self.canvas)
            self.gestion_briques.creer_brique(20, "green", 4, 5)

        # creation de la raquette
        self.raquette = self.canvas.create_rectangle(self.PosX - (self.raquette_info.larguer / 2),
                                                    self.PosY - (self.raquette_info.hauteur / 2),
                                                    self.PosX + (self.raquette_info.larguer / 2),
                                                    self.PosY + (self.raquette_info.hauteur / 2),
                                                    fill = self.raquette_info.couleur)

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
                           self.PosY + (self.raquette_info.hauteur / 2))


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
        if self.vie != 0 and len(self.gestion_briques.liste_brique) != 0 :
            # verification des collisions avec les briques
            collision = self.gestion_briques.verifier_collision_balle(self.balle_info, self.canvas)

            # si il a une collision avec une brique, le score augmente de 1
            if collision == True :
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
                    self.balle_info.x = 2 * self.balle_info.rayon - self.balle_info.x
                    self.balle_info.DX = - self.balle_info.DX

                 # rebond en haut
                if self.balle_info.y - self.balle_info.rayon + self.balle_info.DY < 0 :
                    self.balle_info.y = 2 * self.balle_info.rayon - self.balle_info.y
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
                    if self.balle_info.DX > 0 :
                        self.balle_info.DX = np.abs(self.balle_info.DX) * (1 + (self.balle_info.x - self.PosX) / (33 * self.balle_info.DX))
                    else :
                        self.balle_info.DX = np.abs(self.balle_info.DX) * (1 + (self.balle_info.x - self.PosX) / (15 * self.balle_info.DX))


                elif self.balle_info.x - self.PosX < - self.raquette_info.larguer / 5 :
                    if self.balle_info.DX < 0 :
                        self.balle_info.DX = - np.abs(self.balle_info.DX) * (1 + (self.balle_info.x - self.PosX) / (33 * self.balle_info.DX))
                    else :
                        self.balle_info.DX = - np.abs(self.balle_info.DX) * (1 + (self.balle_info.x - self.PosX) / (15 * self.balle_info.DX))
                    
                    
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

        if self.vie == 0 :
            self.fin_jeu()

        if len(self.gestion_briques.liste_brique) == 0 :
            self.canvas.delete(self.balle_info.Balle)
            self.gagnez()
            return



    def fin_jeu(self) :
        """
        affiche un message de fin et les boutons pour rejouer et retourner au menu
        """
        # afficher le texte "Game Over" au centre du canvas
        self.canvas.create_text(325, 250, text = "GAME OVER", fill = "red", font = ("Arial", 32, "bold"), tags = "fin")
        
        # creer un bouton "Rejouer"
        self.bouton_rejouer = tk.Button(self.canvas, text="Rejouer", command = self.lancement_jeu,
            bg = "#4CAF50", fg = "white", font = ("Arial", 14, "bold"), padx = 10, pady = 5)

        # boutton pour retourner au menu
        self.bouton_retour = tk.Button(self.canvas, text = "Retour", command = self.ecran_menu,
                    bg="#333333", fg="white", font=("Arial", 14, "bold"), padx = 10, pady = 5)
        
        
        # incruster des boutons sur le canvas
        self.canvas.create_window(325, 300, window = self.bouton_rejouer, tags = "fin")
        self.canvas.create_window(325, 400, window = self.bouton_retour, tags = "fin")


    def gagnez(self) :
        """
        affiche un message de fin et les boutons pour rejoeur et retourner au menu
        """
        # afficher les statistique du joueur au centre du canvas
        self.canvas.create_text(325, 150, text = "VOUS AVEZ GAGNE", fill = "green", font = ("Arial", 32, "bold"), tags = "fin")
        self.canvas.create_text(325, 250, text = f"statistiques \nvie restante : {self.vie} \nscore : {self.score}",
                                justify = "left", fill = "white", font = ("Arial", 20, "bold"), tags = "fin")
        
        # creer un bouton "Rejouer"
        self.bouton_rejouer = tk.Button(self.canvas, text = "Rejouer", command = self.lancement_jeu,
            bg = "#4CAF50", fg = "white", font = ("Arial", 14, "bold"), padx = 10, pady = 5)

        # boutton pour retourner au menu
        self.bouton_retour = tk.Button(self.canvas, text = "Retour", command = self.ecran_menu,
                    bg="#333333", fg="white", font=("Arial", 14, "bold"), padx = 10, pady = 5)
        
        # incruster ce bouton sur le canvas
        self.canvas.create_window(325, 400, window = self.bouton_rejouer, tags = "fin")
        self.canvas.create_window(325, 500, window = self.bouton_retour, tags = "fin")








