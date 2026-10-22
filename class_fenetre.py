"""
date : 8/10/2026
auteur : Ewen MORIETTE , Noemie DETOT
fonction : contient la classe de la fenetre du jeu
a faire : impossibilité de mettre la fonction clavier dans la class barre
car il y un probleme d'importation circulaire

Le jeu devra présenter une implémentation de pile 

fichier readme indiquant les règles du jeu et les spécificités de votre implémentation

a faire finir de modifier les interfaces

possible fusion entre fin_jeu() et gagnez()
"""

import numpy as np
import tkinter as tk
from collections import deque

from class_raquette import raquette
from class_balle import balle
from class_gestion_brique import gestion_brique



class fenetre :

    def __init__(self) :
        self.liste_niveau = [1, 2, 3, 4, 5]
        self.file_niveaux = deque([1, 2, 3, 4, 5])
        self.prochain_niveau = self.file_niveaux.popleft()

        self.boutons_menu = []

        self.pile_niveau_5 = []

        self.touches = {"Left": False, "Right": False}

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

        self.titre_menu = tk.Label(self.frame_acceuil, text="Casse Brique", font=("Helvetica", 45, "bold"), bg='#2a2a2a', fg='white')
        self.titre_menu.pack(pady=(150, 50))
        

        # creation des boutons pour chaque niveau
        btn = tk.Button(self.frame_acceuil, text = f"Niveau {self.prochain_niveau}",
            command = lambda niv = self.prochain_niveau : self.charger_ecran_jeu(niv),
            bg = '#1a1a1a', fg = "#07fa1f", font = ("Helvetica", 14))
        btn.pack(expand = 1)

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
        self.canvas.bind("<KeyPress>", self.appuyer_touche)
        self.canvas.bind("<KeyRelease>", self.relacher_touche)
        self.canvas.pack()

        # boutton pour lancer le jeu
        self.bouton_rejouer = tk.Button(self.canvas, text = "Jouer", command = self.lancement_jeu,
                    bg = "#4CAF50", fg = "white", font = ("Helvetica", 14, "bold"), padx = 10, pady = 5)
        self.canvas.create_window(325, 300, window = self.bouton_rejouer)

        # boutton pour retourner au menu
        self.bouton_retour = tk.Button(self.canvas, text = "Retour", command = self.ecran_menu,
                    bg = "#333333", fg = "white", font = ("Helvetica", 14, "bold"), padx = 10, pady = 5)
        self.canvas.create_window(325, 400, window = self.bouton_retour)

        # bouton pour quitter le jeu
        self.bouton_fermer = tk.Button(self.frame_jeu, text = "quitter le jeu", fg = "red", command = self.fermer)
        self.bouton_fermer.pack(side = "bottom", pady = "5", padx = "5")

        #mise en pause
        self.pause= False
        self.fenetre.bind('<space>', self.mise_en_pause)


    def ecran_menu(self) :
        """
        cache la frame du jeu qui contient le canvas et les info du score, vie, niveau.
        Et affiche la frame du menu
        """
        # verifie si le canvas existe
        if hasattr(self, "canvas") :
            self.canvas.delete("fin")

        # Pour tous les supprimer d'un coup :
        for btn in self.boutons_menu:
            btn.destroy()
        self.boutons_menu.clear() # On vide la liste


        self.frame_jeu.pack_forget()
        self.frame_bar.pack_forget()
        self.frame_info.pack_forget()
        print("test")
        self.frame_acceuil.pack(side = "top")
        print("pack")

        for i in range(4 - len(self.file_niveaux)) :
            print("passage", i)
            btn = tk.Button(self.frame_acceuil, text = f"Niveau {self.liste_niveau[i + 1]}",
                command = lambda niv = self.liste_niveau[i + 1] : self.charger_ecran_jeu(niv),
                bg = '#1a1a1a', fg = "#07fa1f", font = ("Arial", 14), padx = 15, pady = 5)
            btn.pack(pady = 10)
            self.boutons_menu.append(btn) # Tu l'ajoutes à ta liste


    def charger_ecran_jeu(self, niveau) :
        """
        charge l'ecran du jeu et cache la frame du menu
        """
        if hasattr(self, "canvas") :
            self.canvas.delete("fin")

        self.niveau = niveau
        self.text_niveau.config(text = f"Niveau : {self.niveau}")

        self.frame_acceuil.pack_forget()

        self.frame_info.pack(side = "top")
        self.frame_bar.pack(side = "top", fill = "x")
        self.frame_jeu.pack(side = "bottom")

        self.bouton_jouer = tk.Button(self.canvas, text = "Jouer", command = self.lancement_jeu,
                    bg = "#4CAF50", fg = "white", font = ("Helvetica", 14, "bold"), padx = 10, pady = 5)
        self.canvas.create_window(325, 300, window = self.bouton_jouer)

        self.bouton_retour_menu = tk.Button(self.canvas, text = "Retour", command = self.ecran_menu,
                    bg = "#333333", fg = "white", font = ("Helvetica", 14, "bold"), padx = 10, pady = 5)
        self.canvas.create_window(325, 400, window = self.bouton_retour_menu)

        self.canvas.focus_set()        


    def lancement_jeu(self) :
        """
        creer tous les objets du canvas et initialise les valeurs
        """
        self.canvas.delete("all")
        self.pause= False

        self.score = 0
        self.text_score.config(text = f"Score : {self.score}")

        self.vie = 3
        self.text_vie.config(text = f"Vie : {self.vie}")

        # creation des briques, creer_brique(espece, couleur, ligne, colonne, saut_colonne, ligne_depart)
        if self.niveau == 1 : 
            self.gestion_briques = gestion_brique(self.canvas)
            self.gestion_briques.creer_brique(35, "red", 1, 5, 0, 0)
            self.gestion_briques.creer_brique(35, "red", 1, 6, 1, 1)

            self.pile_niveau_5.append((35, "red", 1, 5, 0, 0))
            self.pile_niveau_5.append((35, "red", 1, 6, 1, 1))

        if self.niveau == 2 :
            self.gestion_briques = gestion_brique(self.canvas)
            self.gestion_briques.creer_brique(35, "red", 1, 5, 0, 0)
            self.gestion_briques.creer_brique(35, "red", 1, 6, 1, 1)
            self.gestion_briques.creer_brique(35, "red", 1, 5, 0, 2)

            self.pile_niveau_5.append((35, "red", 1, 5, 0, 0))
            self.pile_niveau_5.append((35, "red", 1, 6, 1, 1))
            self.pile_niveau_5.append((35, "red", 1, 5, 0, 2))

        if self.niveau == 3 :
            self.gestion_briques = gestion_brique(self.canvas)
            self.gestion_briques.creer_brique(35, "green", 1, 5, 0, 0)
            self.gestion_briques.creer_brique(35, "green", 1, 6, 1, 1)

            self.pile_niveau_5.append((35, "green", 1, 5, 0, 0))
            self.pile_niveau_5.append((35, "green", 1, 6, 1, 1))

        if self.niveau == 4 :
            self.gestion_briques = gestion_brique(self.canvas)
            self.gestion_briques.creer_brique(35, "green", 1, 5, 0, 0)
            self.gestion_briques.creer_brique(35, "green", 1, 6, 1, 1)
            self.gestion_briques.creer_brique(35, "green", 1, 5, 0, 2)

            self.pile_niveau_5.append((35, "green", 1, 5, 0, 0))
            self.pile_niveau_5.append((35, "green", 1, 6, 1, 1))
            self.pile_niveau_5.append((35, "green", 1, 5, 0, 2))

        if self.niveau == 5 :
            self.gestion_briques = gestion_brique(self.canvas)
            self.pile_brique = self.pile_niveau_5
            for i in range (2) :
                args = list(self.pile_brique.pop())
                args[-1] = i
                self.gestion_briques.creer_brique(*args)
                


        # creation de la raquette
        self.raquette = self.canvas.create_rectangle(self.PosX - (self.raquette_info.larguer / 2),
                                                    self.PosY - (self.raquette_info.hauteur / 2),
                                                    self.PosX + (self.raquette_info.larguer / 2),
                                                    self.PosY + (self.raquette_info.hauteur / 2),
                                                    fill = self.raquette_info.couleur)

        #creation de la balle
        self.balle_info = balle(self.canvas, self.fenetre, 15, int(self.canvas.cget("height")),
                                int(self.canvas.cget("width")))

        self.texte_pause = self.canvas.create_text(325, 325, text="PAUSE", font=("Helvetica", 40, "bold"), fill="white", state='hidden')
        
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
        self.menu_nondetachable1 = tk.Menu(self.fenetre, tearoff = 0)
        self.menu_nondetachable2 = tk.Menu(self.fenetre, tearoff = 0)

        self.menu_Principal.add_cascade(label = "Parametre :", menu = self.menu_nondetachable)
        self.menu_Principal.add_cascade(label="restaurer le niveau", menu = self.menu_nondetachable1) 
        self.menu_Principal.add_cascade(label="Quitter", menu = self.menu_nondetachable2)
        self.menu_nondetachable1.add_command(label="restaurer le niveau", command=self.ecran_menu)
        self.menu_nondetachable2.add_command(label = "Quitter", command = self.fermer)

        self.fenetre['menu'] = self.menu_Principal


    def appuyer_touche(self, event):
        if event.keysym in self.touches:
            self.touches[event.keysym] = True

    def relacher_touche(self, event):
        if event.keysym in self.touches:
            self.touches[event.keysym] = False

    def mise_en_pause(self,event=None):
        """
        permet de mettre en pause le jeu
        """
        self.pause = not self.pause

        if hasattr(self,'texte_pause'):
            if self.pause :
                self.canvas.itemconfig(self.texte_pause, state='normal')
            else:
                self.canvas.itemconfig(self.texte_pause, state='hidden')


           
    def collision(self, objet1, objet2) :
        """
        return True si il y a une collision entre les deux ojets
        """
        x1, y1, x2, y2 = self.canvas.coords(objet1)
        a1, b1, a2, b2 = self.canvas.coords(objet2)

        return (x1 < a2 and x2 > a1 and y1 < b2 and y2 > b1)


    def deplacement(self) :
        """
        gere le deplacement et les collision de la balle + met en pause le jeu
        """
        if self.vie != 0 and len(self.gestion_briques.liste_brique) != 0 :

            # Vitesse de déplacement de la raquette (en pixels par frame)
            vitesse_raquette = 14  

            # Si la touche Gauche est enfoncée et qu'on ne sort pas de l'écran
            if self.touches["Left"] and self.PosX - self.raquette_info.larguer / 2 > 0 :
                self.PosX -= vitesse_raquette
                self.canvas.move(self.raquette, -vitesse_raquette, 0)

            # Si la touche Droite est enfoncée et qu'on ne sort pas de l'écran
            if self.touches["Right"] and self.PosX < (650 - self.raquette_info.larguer / 2) :
                self.PosX += vitesse_raquette
                self.canvas.move(self.raquette, vitesse_raquette, 0)


            # verification des collisions avec les briques

            if not self.pause:

                collision= self.gestion_briques.verifier_collision_balle(self.balle_info,self.canvas)

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
                elif self.collision(self.balle_info.Balle, self.raquette) == True:
                    masse_balle = 1.0 
                    
                    self.balle_info.DY = -self.balle_info.DY
                    # L'écart par rapport au centre de la raquette crée une force de rappel latérale F_x
                    offset = self.balle_info.x - self.PosX
                    seuil = self.raquette_info.larguer / 5

                    if abs(offset) > seuil:
                        k_force = 0.3 
                        
                        # Force exercée par la raquette : force_x proportionnelle à l'offset
                        force_x = k_force * offset
                        
                        acceleration_x = force_x / masse_balle
                        self.balle_info.DX += acceleration_x
                  
                    
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
            self.fenetre.after(32, self.deplacement)

        if self.niveau != 5 :
            if self.vie == 0 :
                self.fin_jeu()

            if len(self.gestion_briques.liste_brique) == 0 :
                self.canvas.delete(self.balle_info.Balle)
                self.gagnez()
                return



        if self.niveau == 5 :
            if len(self.gestion_briques.liste_brique) == 0 and len(self.pile_brique) != 0 :
                if self.balle_info.y - self.balle_info.rayon > 300 :
                    for i in range (2) :
                        args = list(self.pile_brique.pop())
                        args[-1] = i
                        self.gestion_briques.creer_brique(*args)
                
                self.fenetre.after(32, self.deplacement)
                            
            

            if len(self.gestion_briques.liste_brique) == 0 and len(self.pile_brique) == 0 :
                self.canvas.delete(self.balle_info.Balle)
                self.gagnez()
                return



    def fin_jeu(self) :
        """
        affiche un message de fin et les boutons pour rejouer et retourner au menu
        """
        # afficher le texte "Game Over" au centre du canvas
        self.canvas.create_text(325, 250, text = "GAME OVER", fill = "red", font = ("Helvetica", 32, "bold"), tags = "fin")
        
        # creer un bouton "Rejouer"
        self.bouton_rejouer = tk.Button(self.canvas, text="Rejouer", command = self.lancement_jeu,
            bg = "#4CAF50", fg = "white", font = ("Helvetica", 14, "bold"), padx = 10, pady = 5)

        # boutton pour retourner au menu
        self.bouton_retour = tk.Button(self.canvas, text = "Retour", command = self.ecran_menu,
                    bg="#333333", fg="white", font=("Helvetica", 14, "bold"), padx = 10, pady = 5)
        
        
        # incruster des boutons sur le canvas
        self.canvas.create_window(325, 300, window = self.bouton_rejouer, tags = "fin")
        self.canvas.create_window(325, 400, window = self.bouton_retour, tags = "fin")


    def gagnez(self) :
        """
        affiche un message de fin et les boutons pour rejoeur et retourner au menu
        """
        # afficher les statistique du joueur au centre du canvas
        self.canvas.create_text(325, 150, text = "VOUS AVEZ GAGNE", fill = "green", font = ("Helvetica", 32, "bold"), tags = "fin")
        self.canvas.create_text(325, 250, text = f"statistiques \nvie restante : {self.vie} \nscore : {self.score}",
                                justify = "left", fill = "white", font = ("Helvetica", 20, "bold"), tags = "fin")

        # creer un bouton "jouer"
        if len(self.file_niveaux) != 0 :
            self.bouton_jouer = tk.Button(self.canvas, text = "prochain niveau", command = lambda: self.charger_ecran_jeu(self.file_niveaux.popleft()),
                bg = "#4CAF50", fg = "white", font = ("Helvetica", 14, "bold"), padx = 10, pady = 5)
            self.canvas.create_window(325, 350, window = self.bouton_jouer, tags = "fin")
        
        # creer un bouton "Rejouer"
        self.bouton_rejouer = tk.Button(self.canvas, text = "Rejouer", command = self.lancement_jeu,
            bg = "#4CAF50", fg = "white", font = ("Helvetica", 14, "bold"), padx = 10, pady = 5)

        # boutton pour retourner au menu
        self.bouton_retour = tk.Button(self.canvas, text = "Retour", command = self.ecran_menu,
                    bg="#333333", fg="white", font=("Helvetica", 14, "bold"), padx = 10, pady = 5)
        
        # incruster les boutons sur le canvas
        self.canvas.create_window(325, 400, window = self.bouton_rejouer, tags = "fin")
        self.canvas.create_window(325, 450, window = self.bouton_retour, tags = "fin")
