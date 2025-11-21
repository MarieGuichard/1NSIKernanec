# Représentation approximative des nombres réels.



Nous savons représenter en machine un nombre entier si ce nombre est compris entre deux bornes qui dépendent du nombre d'octets utilisés.

 Qu'en est-il pour un nombre réel quelconque ? Ces nombres sont de différents types : entier comme 3, décimal comme -8,75 ou 0,2, rationnel comme $\frac{1}{3}$ ou ${\frac{3}{4}}$ ou  irrationnel comme $\pi$ ou $\sqrt{7}$

Nous savons qu'une donnée, quelle qu’elle soit, sera représentée sous forme binaire au sein de la machine et cela sur un nombre fini d'octets. De ce fait, tous les nombres réels ne pourront pas être représentés (ben oui, il en existe quand même une infinité...). Nous utiliserons donc une représentation approximative des nombres réels pour un certain nombre d'entre eux. 

En informatique, nous ne parlons donc pas de nombre réel mais de nombre flottant. 

#### I. Du décimal au binaire.

​	Partons d'un exemple :

​	Prenons le nombre décimal $x=3.6875_{10}$  et écrivons sa représentation en binaire.

​	Tout d'abord, considérons sa partie entière : 3. $3_{10}$ s'écrit  $11_2$ en binaire. C'est la partie facile:-)

​	Puis, considérons sa partie décimale : 0,6825. 

​	Il s'agit de décomposer 0,6875 en puissance de deux négatives (ce qui n'est pas facile). 

​	Pour cela, nous allons procéder par multiplication successive :

​	$0.6875\times2=0.375+1$

​	$0.375\times2=0.75+0$

​	$0.75\times2=0.5+1$

​	$0.5\times2=0+1$

​	Nous obtenons donc que $0.6875_{10}=0.1011_2$

​	La représentation binaire de $3.6875_{10}$ est $11.1011_2$

La méthode est donc la suivante : 

- séparer la partie entière et la partie décimale.

- Pour la partie entière, procéder comme vu dans le cours sur l'écriture d'un entier positif dans une base b.   	

- Pour la partie décimale,	

  ​		multiplier le nombre par 2.  	

  ​		 tant que la partie décimale du nombre obtenu n'est pas nul,  	

  ​			noter la partie entière du résultat obtenu  		

  ​                        multiplier la partie décimale du résultat par 2



​	Exercice 1 :

​	a. Convertir  $127,75_{10}$ en binaire. 

​	b. Convertir  $101.01_2$ en décimal. 

​	c. Convertir  $0.2_{10}$ en binaire. Que pouvez vous dire ?



Il n'est possible d'écrire sous forme en binaire que les nombres de la forme $\frac{N}{2^n}$ où N est un nombre 	entier, et $n$ un nombre entier relatif.

On ne peut pas écrire, de manière fini, une infinité de  nombres décimaux. Leurs développement en 	binaire est nécessairement tronqué et cela engendrera des erreurs dans les opérations. 



Sous Python, par exemple : 

```python
>>> 0.1+0.2
0.30000000000000000004
```

​	



Une des conséquences de cela est qu'il faut éviter de tester l'égalité de deux flottants, en effet, l'égalité 0,1+0,2 ==0,3 n'est pas vraie. 

```python
>>> 0.1+0.2 == 0.3
False
```

​	



Il s'agit d'y être particulièrement vigilant. En effet, les conséquences peuvent ne pas être 	négligeables....

Voici deux exemples de désastres causés par une mauvaise gestion des erreurs d'arrondi :

 1. Le 25 février 1991, pendant la Guerre du Golfe, une batterie américaine de missiles Patriot, à Dharan (Arabie Saoudite), a échoué dans l'interception d'un missile Scud irakien. Le Scud a frappé un baraquement de l'armée américaine et a tué 28 soldats. La commission d'enquête a conclu à un calcul incorrect du temps de parcours, dû à un problème d'arrondi. Les nombres étaient représentés en virgule fixe sur 24 bits. Le temps était compté par l'horloge interne du système en 1/10 de seconde. Malheureusement, 1/10 n'a pas d'écriture finie dans le système binaire : 

    1/10 = $0,1_{10}$ = $0,0001100110011001100110011..._2$

    L'ordinateur de bord arrondissait 1/10 à 24 chiffres, d'où une petite erreur dans le décompte du temps pour chaque 1/10 de seconde. Au moment de l'attaque, la batterie de missile Patriot était allumée depuis environ 100 heures, ce qui avait entraîné une accumulation des erreurs d'arrondi de 0,34 s. 	Pendant ce temps, un missile Scud parcourt environ 500 m, ce qui explique que le Patriot soit passé à côté de sa cible.



​	2. Le 4 juin 1996, une fusée Ariane 5 a explosé 40 secondes après l'allumage. La fusée et son 		 	chargement avaient coûté 500 millions de dollars. La commission d'enquête a rendu son rapport au 	bout de deux semaines. Il s'agissait d'une erreur de programmation dans le système inertiel de 	  	référence. À un moment donné, un nombre codé en virgule flottante sur 64 bits (qui représentait la 	vitesse horizontale de la fusée par rapport à la plate-forme de tir) était converti en un entier sur 16 	bits. Malheureusement, le nombre en question était plus grand que 32768, le plus grand entier que 	l'on peut coder sur 16 bits, et la conversion a été incorrecte.

#### II. La norme IEEE-754.

​	La représentation des nombres flottants et les opérations arithmétiques qui les accompagnent 	  	ont été définies dans la norme internationale IEEE 754. C'est la norme la plus couramment utilisée 	dans les ordinateurs.

​	Selon la précision ou l'intervalle de représentation souhaité, la norme définit un format de 		 	données sur 32 bits, appelé simple précision, et un autre sur 64 bits, appelé double précision. 		  	Dans les deux cas, la représentation d'un nombre flottant est similaire à l'écriture scientifique d'un 	nombre décimal, à savoir une décomposition en trois parties : un signe s, une mantisse m et un 	 	exposant n . 

​	De manière général, un nombre flottant a la forme suivante : 

​	Cela ressemble à l'écriture scientifique mais :

	- la base choisie est une base 2 et non une base 10
	- la mantisse appartient à l'intervalle [1;2[

- l'exposant n est décalé (ou biaisé) d'une valeur d qui dépend du format choisi (32 ou 64 bits).



​	Travaillons avec le format 32 bits 

​	![](/RepresentationsDonnees/IMG/normeIEEE754.jpg)



-  Le bit de poid fort est utilisé pour représenter le signe : 0 pour le signe + et 1 pour le signe -
- Les 8 bits suivants sont réservés pour stocker la valeur de l'exposant. Dans le cas d'un codage sur 32 bits, le décalage est de 127.
- Les 23 derniers bits servent à décrire la mantisse : la mantisse étant toujours comprise dans l'intervalle [1;2[, elle représente un nombre de la forme 1,xxxxxx, c'est à dire un nombre commençant 	nécessairement par le chiffre 1. Par conséquent, pour gagner 1 bit de précision, les 23 bits dédiés à la mantisse sont uniquement utilisés pour représenter les chiffres après la virgule, qu'on appelle la fraction.  	



​	 Prenons un exemple :

​	     Soit le mot de 32 bits suivants :

​	    1 10000110 10101101100000000000000



​	     1 représente le signe, cela signifie que le nombre est négatif.

​	     10000110 représente l'exposant, soit 134. Il faut tenir compte du décalage. L'exposant est donc de 		134-127, soit 7

​	     10101101100000000000000 représente la mantisse. En ajoutant le 1, on obtient le calcul 	      		       suivant : 

​	     $1+2^{-1}+2^{-3}+2^ {-5}+2^{-8}+2^{-9}=1.6677734375$

​	      Soit au final, le nombre décimal suivant : $-1.77734375\times2^7=-271.75$



​		

