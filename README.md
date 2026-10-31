Répertoire Git du projet : https://github.com/flash-cpe/TP4_python_Ewen_Noemie.git


Règles du jeu :

    Le joueur contrôle une raquette en bas de l'écran pour empêcher la balle de tomber.

    L'objectif est de détruire toutes les briques situées en haut de l'écran.

    Chaque brique détruite rapporte des points. Le joueur dispose d'un nombre de 3 vies.


Spécificités de l'implémentation :

    Déplacement avec les flèches directionnelles.
    La touche espace permet de mettre le jeu en pause.

    Il faut gagnez le niveau pécédent pour débloquer le suivant.

    Le jeu possède 5 niveau de difficulté, d'on le niveau 5 qui fonctionne par dépilement de 2 lignes par 2 lignes de briques de toutes les briques des autres niveaux. 

    Le joueur possède 3 vies.

    Le score, les vies restantes et le temps passé sur le niveau actuel sont affiché dans l'écran de jeu et a la fin de la partie, si le joueur a gagnée.

    Possible retour au menu de sélection des niveaux quand une partie est fini ou a tout moment via le menu en haut de la fenètre.

    Les rebonds entre la balle et la raquette sont calculés avec la 2 loi de Newton.

    On peut quitter le jeu, et donc fermer le programme soit par le menu présent en haut de la fenètre. Soit par un bouton situé en bas de la fenètre.


Emplacement des structures de données demandées :

    File d'attente des niveaux (deque) :

        Implémentée via collections.deque pour gérer l'enchaînement et la navigation rapide (popleft()) entre les différents niveaux du jeu.

        Localisation : fichier class_fenetre.py, initialisation ligne 27 et utiliser ligne 28 et 508 avec un popleft()


    Pile de briques :

        Implémenté pour stocker les briques et permettre de les dépiler au niveau 5.

        Localisation : fichier class_fenetre.py, initialisation ligne 32, empilement entre la ligne 205 et 234, dépilement ligne 443

    liste : 

        Implémenté pour stocké les briques pour verifier les collision et la destruction de briques.

        Localisation : fichier class_gestion_brique.py, initialisation ligne 17, ajout d'éléments dans la liste ligne 36 et parcour de la liste ligne 51