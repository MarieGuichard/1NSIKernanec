## Les algorithmes de tris. 



#### I. Introduction.

​	

Un **algorithme de tri** est, en informatique ou en mathématiques, un algorithme qui permet d'organiser une collection d'objets selon un relation d'ordre déterminée. Les objets à trier sont des éléments d'une ensemble muni d'un ordre total. Il est, par exemple, fréquent de trier des entiers selon la relation d'ordre usuelle "est inférieur ou égal à". Les algorithmes de tri sont uilisés dans de très nombreuses situations. Ils sont, en particulier, utiles à de nombreux algorithmes de recherche comme la recherche dichotomique. Il peuvent également servir pour mettre des données sous forme canonique ou les rendre plus lisibles pour l'utilisateur. 

La collection à trier est souvent donnée sous forme de tableau, afin de permettre l'accés direct aux différents éléments de la collection.

Les algorithmes de tri sont souvent étudiés dans les cours d'algorithmique pour introduire des notions comme la complexité algorithmique ou la terminaison.

D'aprés Wikipedia. 





Le problème est donc le suivant : 

Soit un tableau contenant des entiers. 

Nous voulons trouver un algorithme qui prend en paramètre ce tableau et qui renvoie le tableau trié.

Par exemple : Soit t le tableau t= [5;4;8;3;7]. 

L'objectif est d'obtenir ce tableau trié dans l'ordre que nous aurons établi au préalable. 

Nous choisirons l'ordre croissant : nous souhaitons donc obtenir le tableau [3;4;5;7;8]



Il est possible de faire le même travail avec des flottants, des chaînes de caractères (l'ordre est alors l'ordre alphabétique), ou n'importe quel ensemble de données pourvu que l'on puisse établir un ordre dessus. 

 

Nous étudierons cette année deux algorithmes de tris : le tri par insertion, le tri par sélection. Mais il en existe de nombreux. Vous pouvez aller faire un tour rapide sur la page https://fr.wikipedia.org/wiki/Algorithme_de_tri pour vous en convaincre. 

#### II. Le tri par insertion.



##### 1. Observer. 



Allez visionner la vidéo suivante :  https://youtu.be/ROalU379l3U



##### 2. Expérimenter. 



Demander 10 jetons à votre professeur et, en reproduisant la méthode vue dans la vidéo, trier ces jetons dans l'ordre croissant. 



##### 3. Écrire un algorithme. 

Écrire, en pseudo-code, un algorithme de tri par insertion. 

Demander au groupe voisin d'expérimenter cet algorithme  avec des jetons pour vérifier qu'il 	fonctionne correctement. 

Appeler votre professeur.

##### 4. Correction. 
```
VARIABLES:
t: tableau d'entiers
i: nombre entier
j: nombre entier 
k: nombre entier
DEBUT
j <- 2
Tant que j<= longueur(t): 
    j <- j-1
    k <- t[j]
    Tant que i>0 et t[i]>k:
       t[i+1] <- t[i]
       i <-i-1
       Fin Tant que 
    t[i+1] <-k
    j <- j+1
Fin Tant que 
```




Exercice 1: Faitre tourner à la main l'algorithme que nous venons d'écrire avec le tableau suivant1  t=[27 ;10 ;12 ;8 ;11] :

Exercice 2 : Traduire votre algorithme en python et vérifier qu'il fonctionne correctement 	(c'est le moment d'utiliser doctest;-))





##### 5. Vérifions que cela fonctionne.

Exercice 3: 

1. Quel invariant de boucle pouvez vous utiliser ?
2. Vérifiez que votre invariant de boucle est vrai lors de l'initialisation.  		
3. Montrer que si l'invariant de boucle est vérifié à un moment donné, alors, il est toujours vérifié à l'itération suivante.  		



##### f. Complexité. 

Prenons le pire des cas : un tableau rangé dans l'ordre décroissant et comptons le nombre de 	déplacements. 

Soit t=[5,4,3,2,1]

![](/Algorithme/IMG/complexite_tris_insertion.jpg)



Il y a dans ce cas : 

- 1 déplacement pour j = 2
- 2  déplacements pour j=3
- 3 déplacements pour j=4
- 4 déplacements pour j=5

Soit un total de 10 déplacements. 



Si on travaille avec un tableau de longueur n, il y aura :

- 1 déplacement pour j=2
- 2 déplacements pour j=3
- …..
- n-1 déplacements pour j=n

Soit un total de 1+2+....n-1 déplacements. 

​	

Ceux qui suivent la spé maths reconnaissent une somme qu'ils ont vu dans le cours sur les 	suites arithmétiques, pour les autres, voici la formule :

$1+2+...+ n-1 = \frac {n(n-1)}{2}=\frac{n^2}{2}-\frac{n}{2}$

Nous pouvons donc dire que la complexité de l'algorithme de tri par insertion est en $O(n^2) $. 

#### II. Le tri par sélection.

##### 1. Observer. 

Allez visionner la vidéo suivante : https://youtu.be/Ns4TPTC8whw



##### 2. . Expérimenter. 



Demander 10 jetons à votre professeur et, en reproduisant la méthode vue dans la vidéo, trier 	ces jetons dans l'ordre croissant. 



##### 3.  Écrire un algorithme. 

Écrire, en pseudo-code, un algorithme de tri par sélection. 

Demander au groupe voisin d'expérimenter cet algorithme  avec des jetons pour vérifier qu'il 	fonctionne correctement. 

Exercice 4:  Faire tourner l'algorithme sur le tableau t=[12,8,23,10,15]. 



Exercice 5:  Traduire votre algorithme en python et vérifier qu'il fonctionne correctement 	(c'est le moment d'utiliser doctest;-))



##### 4. Vérifier que cela fonctionne. 



- Terminaison.

  Exercice 6: Justifier la terminaison de l'algorithme de tri par sélection.  	



- Correction. 	 	

  Exercice 7 : Trouvez un invariant de boucle pour l'algorithme de tri par sélection. Procédez ensuite à la démonstration en 2 étapes afin de démontrer la correction de l'algorithme de tri par sélection.  	



##### 5. Complexité.

Exercice 8:  Soit t le tableau t = [15, 16, 11, 13, 12] .

1. Compter le nombre de comparaisons effectuées pour trier ce tableau avec l'algorithme du tri 	par sélection.  
2. En déduire la complexité de l'algorithme du tri par sélection.

