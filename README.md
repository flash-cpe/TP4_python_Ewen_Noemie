Répertoire Git du projet : https://github.com/flash-cpe/TP4_python_Ewen_Noemie.git


Règles du jeu :

    Le joueur contrôle une raquette en bas de l'écran pour empêcher la balle de tomber.

    L'objectif est de détruire toutes les briques situées en haut de l'écran.

    Chaque brique détruite rapporte des points. Le joueur dispose de 3 vies.


Spécificités de l'implémentation :

    Déplacement avec les flèches directionnelles.
    La touche espace permet de mettre le jeu en pause.

    Il faut gagner le niveau pécédent pour débloquer le suivant.

    Le jeu possède 5 niveaux de difficulté, dont le niveau 5 qui fonctionne par dépilement de 2 lignes par 2 lignes de briques de toutes les briques des autres niveaux. 

    Le score, les vies restantes et le temps passé sur le niveau actuel sont affichés dans l'écran de jeu et à la fin de la partie, si le joueur a gagné.

    Possible retour au menu de sélection des niveaux quand une partie est finie ou à tout moment via le menu en haut de la fenêtre.

    Les rebonds entre la balle et la raquette sont calculés avec la 2e loi de Newton.

    On peut quitter le jeu, et donc fermer le programme soit par le menu présent en haut de la fenêtre, soit par un bouton situé en bas de la fenêtre.

    Utilisation des bibliothèques tkinter, random, math et collections 


Emplacement des structures de données demandées :

    File d'attente des niveaux (deque) :

        Implémentée via collections.deque pour gérer l'enchaînement et la navigation rapide (popleft()) entre les différents niveaux du jeu. La fonction deque() permet de réduire les temps de calcul, passage de O(n) à O(1). Dans notre cas pas forcément nécessaire

        Localisation : fichier class_fenetre.py, initialisation ligne 27 et utilisée ligne 28 et 508 avec un popleft()


    Pile de briques :

        Implémentée pour stocker les briques et permettre de les dépiler au niveau 5.

        Localisation : fichier class_fenetre.py, initialisation ligne 32, empilement entre la ligne 205 et 234, dépilement ligne 443

    liste : 

        Implémentée pour stocker les briques pour vérifier les collisions et la destruction de briques.

        Localisation : fichier class_gestion_brique.py, initialisation ligne 17, ajout d'éléments dans la liste ligne 36 et parcours de la liste ligne 51