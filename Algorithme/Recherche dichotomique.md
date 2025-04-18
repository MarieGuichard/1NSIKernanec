# Recherche dichotomique. 



Nous avons déjà vu une première méthode permettant de dire si un élément  est contenu dans un tableau. 

Pour cela, nous avons écrit un algorithme qui, dans le pire des cas, énumère toutes les valeurs contenues dans ce tableau. 

Nous allons voir une nouvelle manière de répondre à ce problème qui sera plus efficace. Il s'agit de la recherche dichotomique dans un tableau trié. 

#### I. Principe et premier exemple. 



Soit t un tableau contenant n éléments triés dans l'ordre croissant. 

Le principe est le suivant : 

Sachant que le tableau est trié, nous allons le couper en deux et regarder si la valeur à trouver serait dans la partie gauche ou droite de ce tableau. 

On en extrait donc un sous tableau qui a une taille de $\frac{n}{2}$   (à peu de choses prés, puisque n n'est pas forcément pair). 

On a donc un nouveau tableau que nous allons couper en deux, puis nous allons regarder si la valeur à trouver serait dans la partie gauche ou droite de ce tableau. 

On en extrait un sous tableau.....



et ainsi de suite jusqu'à ce que le sous tableau soit de taille 1 et que la valeur qu'il contient 	soit égal ou non à la valeur que l'on cherche. 



Prenons un exemple : soit t = [1,3,7,9,12,16,18,24,32]

Ce tableau a pour longueur 9. 

Nous cherchons à savoir si 18 est contenu dans ce tableau. 



Étape 1 : t = [1,3,7,9,12,16,18,24,32]

Le tableau n'est pas vide.

Déterminons la valeur du milieu. Le tableau a pour longueur 9, la moitié de 9 vaut 4,5, que nous arrondirons en dessous (ou nous prendrons la partie entiére, c'est-à-dire le nombre sans la partie décimale). 

Donc le milieu est 9. 

Comparons cette valeur avec la valeur cherchée. 

9 n'est pas égal à 18. 

9 est plus petit que 18, donc comme t est rangé dans l'ordre croissant, nous savons que 18, s'il est dans le tableau, sera dans la partie à droite de 9. Donc, nous ne regarderons que dans la partie droite du tableau 

t = [1,3,7,9,<span style="color:pink">12,16,18,24,32]</span>



Étape 2 :t = [1,3,7,9,<span style="color:pink">12,16,18,24,32]</span>

Intéressons nous à la partie que nous avons sélectionné. 

Cette partie n'est pas vide. 

Déterminons la valeur du milieu. La partie du tableau a pour longueur 5, la moitié de 5 vaut 2,5, que nous arrondirons en dessous (ou nous prendrons la partie entiére, c'est-à-dire le nombre sans la partie décimale). 

Donc le milieu est 16. 

Comparons cette valeur avec la valeur cherchée. 

16 n'est pas égal à 18. 

16 est plus petit que 18, donc comme t est rangé dans l'ordre croissant, nous savons que 18, s'il est dans le tableau, sera dans la partie à droite de 16. Donc, nous ne regarderons que dans la partie droite du tableau t = [1,3,7,9,<span style="color:pink">12,16,</span> <span style="color:purple">18,24,32]</span>



Étape 3 : t = t = [1,3,7,9,<span style="color:pink">12,16,</span> <span style="color:purple">18,24,32]</span>

Intéressons nous à la partie que nous avons sélectionné. 

Cette partie n'est pas vide. 

Déterminons la valeur du milieu. La partie du tableau a pour longueur 3, la moitié de 3 vaut 1,5, que nous arrondirons en dessous (ou nous prendrons la partie entière, c'est-à-dire le nombre sans la partie décimale). 

Donc le milieu est 18. 

Comparons cette valeur avec la valeur cherchée. 

18 est égal à 18. C'est fini ! Nous avons trouvé notre valeur. 

​	

Visionnez la vidéo suivante : https://youtu.be/ULr_8ocz0AU



#### II. L'algorithme.	



```
VARIABLE

t : tableau d'entiers trié 

mil : nombre entier 	

fin : nombre entier 

deb : nombre entier 

x : nombre entier // x : l'entier recherché 

tr : booléen 	

DEBUT

tr ← FAUX 

deb ← 1 	

fin ← longueur(t) 	

tant que tr == FAUX et que fin – deb ≥ 0 : 

	mil ← partie_entière((deb+fin)/2) 

	si t[mil] == x : 

		tr = vrai 

	sinon : 

		si x > t[mil] :

			 deb ← mil+1 

		sinon : 

			fin ← mil-1 

		fin si 

	fin si 

fin tant que 

renvoyer la valeur de tr 

FIN


```

​	Faisons fonctionner cet algorithme sur un exemple : 

​	x=35 est-il présent dans le tableau t=[5,7,12,14,23,27,35,40,41,45] ? 

​	

​	Étape 1 :

​	deb=1

​	fin=10

​	tr = Faux

​	fin – deb >= 0  et tr=Faux => on entre dans la boucle

​	mil=5

​	t[5] n'est pas égal à 35 => on entre dans le sinon. 

​	35>t[5] => on entre dans le si

​	deb = mil+1 = 6



​	Etape 2 :

​	deb = 6

​	fin  = 10

​	tr = Faux

​	fin – deb >= 0 et tr= faux => on entre dans le tant que 	

​	mil = 8

​	t[8] n'est pas égal à 35 => on entre dans le sinon

​	35<t[8] => on entre dans le sinon

​	fin = 8-1 = 7



​	Etape 3 :

​	deb = 6

​	fin = 7 

​	tr = Faux

​	fin – deb >= 0 et tr = Faux => on entre dans le tant que

​	mil = 6

​	t[6] n'est pas égal à 35 => on entre dans le sinon

​	35>t[6] => on entre dans le si

​	deb =7



​	Etape 4 :

​	deb = 7

​	fin = 7 

​	tr =Faux

​	fin – deb >= 0 et tr=Faux => on entre dans le tant que

​	mil = 7

​	t[7]=35 => on entre dans le si. 

​	Tr = Vrai

​	

​	Etape 5 :

​	deb = 7

​	fin = 7 

​	tr = Vrai

​	fin – deb >= 0 et tr =Vrai => on n'entre pas dans le tant que

​	renvoyer vrai



On peut résumer le principe de fonctionnement de l'algorithme de recherche dichotomique par le schéma suivant : 

Il est aussi possible de représenter le principe de l'algorithme de recherche dichotomique avec le schéma suivant :

![](/Algorithme/IMG/dichotomie_image1.jpg)

L'idée est donc de définir le milieu du tableau (variable "mil") et de couper le tableau 	en 2, on se retrouve avec 2 tableaux. On garde uniquement le tableau qui peut contenir la 	valeur recherchée. On recommence le processus jusqu'au moment où l'on "tombe" sur la 	valeur recherchée ou que l'on se retrouve avec un tableau contenant un seul élément : si 	l'élément unique du tableau n'est pas l'élément recherché, l'algorithme renvoie FAUX. 

![](/Algorithme/IMG/dichotomie_image2.jpg)

Exercice 1: Représentez le principe de fonctionnement de l'algorithme en utilisant le schéma 2 dans les deux cas suivants :

1. t = [5, 7, 12, 14, 23, 27, 35, 40, 41, 45] et x = 9
2. t = [5, 7, 12, 14, 23, 27, 35, 40, 41, 45] et x = 40  		

​			

#### III. Terminaison.

L'algorithme de dichotomie contenant une boucle non bornée, il est nécessaire de vérifier la 	terminaison de celui-ci. 

Nous allons pour cela utiliser un variant de boucle. 

Définition : Soit une condition permettant de sortir d'une boucle constituée d'une comparaison entre une variable et une constante. La variable est un variant de boucles si :

- elle reste positive tout au long de l'algorithme
- elle décroît strictement à chaque itération de la boucle.  	

​	

Ainsi, après un nombre fini d'itérations, on est sur que la boucle se terminera. 



Remarques :

- un variant de boucle permet de s'assurer qu'une boucle se terminera
- un variant de boucle ne permet pas d'assurer qu'un algorithme fournit la réponse attendue.  	



Soit la variable fin-deb. 

fin-deb reste positive tout au long de l'algorithme (sinon, on sort de la boucle et l'algorithme s'arrête). 

A chaque itération, 

- soit tr= Vrai, et alors on sort de la boucle. 
-  Soit deb = mil+1. Comme mil>deb, on a alors fin-deb qui décroît. 
- Soit fin = mil – 1. Comme mil<fin, on a alors fin-deb qui décroît. 

Donc fin-deb est bien un variant de boucle. Et donc, la boucle s'arrête nécessairement. 

​	

#### III. Complexité.



Pour étudier la complexité, nous allons nous intéresser à la boucle : au niveau de la boucle, combien doit-on effectuer d'itérations pour un tableau de taille n dans le cas le plus défavorable (l'entier x n'est pas dans le tableau t) ? 

Sachant qu'à chaque itération de la boucle on divise le tableau en 2, cela revient donc à se demander combien de fois faut-il diviser le tableau en 2 pour obtenir, à la fin, un tableau comportant un seul entier ? Autrement dit, combien de fois faut-il diviser n par 2 pour obtenir 1 ? 

Mathématiquement cela se traduit par l'équation$\frac{n}{2^a}=1$ avec $ a$ le nombre de fois qu'il faut diviser n par 2 pour obtenir 1. Il faut donc trouver a ! 

A ce stade il est nécessaire d'introduire une nouvelle notion mathématique : le "logarithme  base 2" noté $log_2$ . Par définition $log_2(2^x)=x$ . 

Nous avons donc : 

$\frac{n}{2^a}=1$ => $ n=2^a $ => $ log_2(n)=log_2(2^a)=a$. 

Par conséquent, $a =log_2(n)$ 

Nous pouvons donc dire que la complexité en temps dans le pire des cas de l'algorithme de recherche dichotomique est $O(log_2(n))$. 

Afin de pouvoir comparer l'efficacité des différents algorithmes, voici une représentation graphique des fonctions  (en rouge),  (en bleu) et  (en vert). 

![](/Algorithme/IMG/dichotomie_image3.jpg)

Comme vous pouvez le constater l'algorithme de recherche dichotomique est plus efficace que l'algorithme de recherche qui consiste à parcourir l'ensemble du tableau, car $x>log_2(x)$  quelque soit $x$. Cependant, il ne faut pas perdre de vu que dans le cas de la recherche dichotomique, il est nécessaire d'avoir un tableau trié, si au départ le tableau n'est pas trié, il faut rajouter la durée du tri. 
