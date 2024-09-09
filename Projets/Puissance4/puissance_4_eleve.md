#  Puissance 4 #

L’objectif de ce TP est de simuler un jeu de puissance 4 à deux joueurs. 
Les joueurs porteront les numéros 1 et 2. 
Le joueur numéro 1 mettra des X dans la grille et le joueur 2 des O.

**Etape 1:** Création du plateau de jeu. 

Ecrire une fonction `installation_jeu()`
qui renverra une matrice de 6 lignes et de 7 colonnes ne contenant que des zéros.  Pour cela, vous ferez une liste de liste. Cela simulera les 7 colonnes de 6 lignes de votre jeu de puissance 4. 
    
![40% center](installation_jeu.jpg)

**Etape2:** Affichage du plateau de jeu. 

Ecrire une fonction `affichage_plateau()` qui prend en paramétre le plateau de jeu et qui l’affiche. 
Les 0 matérialisant les cases vides seront représentés par un espace, les 1 représentant les pions mis par le joueur 1 seront représentés par des X, et les 2 par des O. 

![50% center](grille_de_jeu.jpg)
![50% center](jeu_en_cours.jpg)



**Etape 3:** Choix du premier joueur

Ecrire une fonction `premier_joueur()` qui choisit au hasard le numéro du joueur qui débutera la partie. 


**Etape 4:** changement de joueur

Ecrire une fonction `changement_de_joueur()` qui prend le paramétre le numéro du joueur qui vient de jouer et qui renvoit le numéro de l’autre joueur. 

**Etape 5:** Le jeu est-il fini? 

Pour que le jeu soit fini, il y a deux possibilités, soit un des joueurs a gagné, soit la grille est pleine. 

Il s’agit donc de tester ces deux possibilités.

 1. Pour qu’un joueur ait gagné, il faut qu’il ait alignés 4 pions soit de manière horizontale, soit de manière verticale, soit en diagonale. 
Pour cela, vous allez écrire quatre fonctions `_4_pions_en_ligne()`,` _4_pions_en_colonne()`, `_4_pions_en_diagonale_mont()`,` _4_pions_en_diagonale_desc()` prenant en paramétre le plateau, testant s’il existe dans le plateau 4 pions alignés respectivement horizontalement, verticalement, en diagonale montante et en diagonale descendante. Ces fonctions retourneront 0 si ça n’est pas le cas, 1 si c’est le joueur 1 qui a aligné 4 pions et 2 si c’est le joueur 2. 

2.  A l’aide des fonctions précédentes, écrire une fonction `_y_a_t_il_un_gagnant()`  prenant en paramétre le plateau et renvoyant True si l’un des joueurs a gagné la partie et False sinon.

3. Ecrire une fonction `est_fini()` prenant le plateau en paramétre et renvoyant True si le jeu est fini et False sinon. Cette fonction testera si l’un des joueurs a gagné la partie ou si le plateau de jeu est complet.

**Etape 6:** Liste des coups possibles. 

Ecrire une fonction `coups_possibles()` qui prend en paramétres le plateau de jeu et qui retourne, sous forme d’une liste, la liste des colonnes dans lesquelles il est encore possible de jouer. 

**Etape 7:** Affichage du joueur courant ainsi que de la liste des coups qu’il peut faire. 

Ecrire une fonction `affiche_coups()` prenant pour paramétres la liste des coups possibles ainsi que le joueur courant. Elle affichera un message indiquant le joueur qui doit jouer ainsi que la liste des colonnes dans lesquelles il est encore possible de jouer. 


**Etape 8:** Le choix du joueur.

Ecrire une fonction `coup_choisi()` prenant en paramétre la liste des coups possibles, demandant au joueur quelle est la colonne qu’il choisit et qui retourne ce numéro de colonne. 
Vous veillerez à ce que le joueur ne puisse donner qu’un numéro de colonne valide. 

**Etape 9:** Mise à jour du plateau. 

Ecrire une fonction `mise_a_jour_plateau()` prenant en paramétres le coup choisi par le joueur, le numéro du joueur ainsi que le plateau courant. Cette fonction retournera le plateau modifié après le coup du joueur. 

![40% center](coup_joueur.jpg)

**Etape 10:** Le résultat du jeu.

Ecrire une fonction resultat_jeu() qui prend en paramétre le plateau et qui retourne le numéro du joueur gagnant et 0 si le match est nul. 

**Etape 11:** Affichage des résultats.

Ecrire une fonction` afficher_gagnant()` qui prend en paramètre le joueur gagnant s’il existe et  0 sinon, et qui affiche soit le nom du gagnant, soit le “le match est nul” si c’est le cas. 

![40% center](victoire.jpg)

**Etape 12:** Jouons !

Ecrire une fonction `jouer()` ne prenant aucun paramètre et faisant en sorte que les deux joueurs puissent jouer l’un contre l’autre et affichant, s’il existe, le nom du gagnant à la fin de la partie. 
