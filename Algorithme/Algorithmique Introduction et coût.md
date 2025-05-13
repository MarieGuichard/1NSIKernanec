## Algorithmique: Introduction et coût. 

#### I. Les algorithmes.

##### 1. Définition. 

Nous prendrons pour définition d'algorithme la définition suivante : 

** Algorithme :nom masculin, ensemble de règles opératoires dont l'application permet de 	résoudre un problème énoncé au moyen d'un nombre fini d'opérations élémentaires . ** 

Exemple 1 : Donner au moins trois exemples d'algorithme que nous utilisons dans la vie 	quotidienne.

##### 2. D'où vient le mot *algorithme* ?

![](/Algorithme/IMG/image_al_khwarizmi.jpg)

Le mot *algorithme* vient du nom du mathématicien persan Al-Khwarizmi, né vers 780 et mort à Bagdad vers 850. 



Al-Khwarizmi est resté célèbre pour deux ouvrages qui ont largement contribué à faire connaître et à vulgariser les chiffres dits « *arabes* » et les méthodes de calcul, ainsi que les procédés algébriques de résolution d’équations, aussi bien dans le monde musulman qu’en Occident chrétien. 

Le premier de ces ouvrages s’intitule : « *Traité de l’addition et de la soustraction d’après le calcul des Indiens* ». L’original de ce traité est malheureusement perdu, mais il en reste plusieurs traductions latines faites à partir du XIIème siècle. C’est le premier livre arabe connu où le système décimal d’écriture des nombres et les méthodes de calcul d’origine indienne font l’objet d’explications détaillées, illustrées par de nombreux exemples. 

Le traité débute ainsi : « *Nous avons décidé d’exposer la manière de calculer des Indiens à l’aide de neuf caractères et de montrer comment, grâce à leur simplicité et leur concision, ces caractères peuvent exprimer tous les nombres.* » Al-Khwarizmi explique ensuite en détail le principe de la numération décimale de position, en signalant l’origine indienne des neuf chiffres et de « *la dixième figure en forme de cercle* » (le zéro), dont il recommande de « *ne pas négliger l’usage afin de ne pas confondre les positions* ». 

Ce livre jouira plus tard dans les pays d’Europe d’une telle renommée que le nom même de son auteur finira par désigner le système de numération décimale : latinisé, le nom d’Al-Khwarizmi deviendra d’abord **Alchoarismi**, puis il se transformera en **Algorismi**, **Algorismus**, **Algorithmus**, et, enfin : **Algorithme**.

##### 3. Cinq caractéristiques importantes d'un algorithme. 

Dans les années 1960, Donald Knuth, un des pionniers en algorithmie, énonce dans l'un de 	ses ouvrages les cinq caractéristiques importantes d'un algorithme :

- Un algorithme doit toujours se terminer après un nombre fini d'étapes.
- Chaque étape d'un algorithme doit être définie précisément, les actions doivent être spécifiées rigoureusement et sans ambiguïté pour chaque cas.  	
- Un algorithme a une ou plusieurs sorties, quantités qui ont une relation spécifiée avec les entrées.  	
- Les instructions doivent être suffisamment basiques pour pouvoir être en principe exécutées de manière exacte et en temps fini par une personne utilisant un papier et un crayon.  	

#### 4.  Le pseudo-code. 



Puisqu'il y a un très grand nombre de langages différents, il est commode d'utiliser une sorte de lingua franca qui permet d'écrire un algorithme dans un langage « universel ». Nous appellerons cela le pseudo-code. 

Il n'y a pas de standard normalisé, il faut juste que cela soit clair et compréhensible par un grand nombre de personnes. 



#### 5. Prenons un exemple.

Lorsque vous étiez en classe de troisième, vous avez du étudier l'algorithme d'Euclide 

Exercice 2: 

​	1. Résoudre le probléme suivant :

​	Un chocolatier a fabriqué 186 pralines et 155 chocolats. 

​	Les colis sont constitués ainsi : 

​	• Le nombre de pralines est le même dans chaque colis. 

​	• Le nombre de chocolats est le même dans chaque colis. 	

​	• Tous les chocolats et toutes les pralines sont utilisés.

​		 a) Quel nombre maximal de colis pourra-t-il réaliser ?

​		 b) Combien y aura-t-il de chocolats et de pralines dans chaque colis ? 

​	2. Rédiger en pseudo-code l'algorithme d'Euclide. 

​	3. Donner l'algorithme à votre voisin et demander lui de le tester sans réfléchir avec les nombres 133 	et 209. 

​	Corriger votre travail si besoin. 

**En conclusion, un algorithme, c'est comme un programme, mais sans la notion de langage, il vous faut juste utiliser un papier et un crayon (comme vous le demande depuis le début de l'année votre prof préférée....) pour réfléchir à la question posée.** 



#### 6. Exercices. 



Exercice 3 : 

​	On considère l'algorithme suivant



​	Afficher « Saisisser un nombre entier N : »

​	

```
Saisir N

S ← 1

Pour i allant de 1 jusqu'à N

	S ← S*i 

Fin Pour

Afficher S
```



1. Tester cet algorithme pour N=5 en donnant les résultats à chaque itération.
2. Que se passe-t-il si on retire la ligne S reçoit la valeur 1 ?  		

​	

Exercice 4: 

​	On considère l'algorithme suivant :



```
Entrer un entier naturel N

Tant que N>1 faire :

	Si N est pair, 

		 N ← N/2

	Sinon

		N ← 3N+1

Fin Tant Que

Afficher N
```



1. Tester cet algorithme avec les entiers N=6, N=7 et N=16.

   Que constatez vous ?  		

2. Modifier l'algorithme pour qu'il affiche toutes les valeurs successives de N .  		

3. Modifier 	l'algorithme pour qu'il affiche le nombre de tests effectués.  		

4. Modifier l'algorithme pour qu'il affiche la valeur maximale de N atteinte.  		





#### 7. Les algorigrammes. 



Il peut être commode de représenter des algorithmes sous forme d'organigrammes : nous appellerons cela un algorigramme. 



Pour savoir de quoi il s'agit, rendez vous sur la page suivante :

​	https://troumad.developpez.com/C/algorigrammes/



​	

#### II. Vérifier que cela fonctionne !



Lorsqu'on écrit un algorithme, il est impératif de vérifier que cet algorithme va produire un résultat en un temps fini et que ce résultat sera correct dans le sens où il sera conforme à une spécification précise. Nous dirons alors que l'algorithme est valide. 



Nous nous concentrerons sur la validité des boucles tant que, qui sont les seules pouvant mener à des boucles infinies. 



##### 1. Les invariants de boucle. 



**Définition : Un invariant d'une boucle est une propriété qui est vérifiée avant l'entrée dans une boucle, à chaque passage dans cette boucle et à la sortie de cette boucle.**

Exercice 4: 

​	Voici un algorithme :

​	

```
Saisir a 

Saisir b

m ← 0

p ← 0

Tant que m<a

	m ← m+1

	p ← p+b

Fin Tant que

afficher p


```



1. Tester cet algorithme avec a = 4 et b = 3, puis avec a = 6 et b = 4.

2. Que renvoie cet algorithme ?  		

3. L'objectif de cette question est de montrer que $p = m\times b$ est un invariant de la boucle Tant que.  		

   a. Vérifier que  $p=m\times b$est vrai avant le premier passage dans la boucle.  		

   b. Supposons qu'à un moment donné, on ait $p = m\times b$ , montrer qu'aprés un passage dans la boucle, cette égalité est toujours vraie.  		

   c. Conclure.  		



##### 2. Variant de boucles. 



** Définition : On appelle variant d'une boucle une expression dont la valeur varie à chacune 	des itération de la boucle. **	



Un variant de boucle permet de prouver qu'une boucle Tant Que se termine. 



Exercice 5: Voici un algorithme. 

```
Saisir n

p ← 1

Tant que p<n faire

	p ← 2p

Fin TantQue

Afficher p


```



1. Tester cet algorithme avec n=4 et n=7.

2. Que fait cet algorithme ?  		

3. Justifier le fait que p peut être considéré comme un variant de boucle.  		

   Expliquer pourquoi cela permet de dire que cet algorithme se termine.  		



##### 3. Exercices. 



Exercice 6 : 

​	Voici un algorithme qui permet de tester si une chaîne de caractères m est un palindrome. 

​	

​	

```
Saisir m

i ← 0

j ← longueur(m) -1

Tant que i<=j faire :

	si m[i]=m[j], alors

		i ← i+1

		j ← j-1

	sinon

	    renvoyer Faux

	FinSi

FinTantQue

Renvoyer Vrai


```



1. Décrire au moyen d’un tableau indiquant l’ évolution des valeurs des variables le fonctionnement de l’algorithme précédent pour la chaîne de caractères ”sauras” puis pour la chaîne de caractères ”radar”.
2. Montrer que d=i-j est un variant de la boucle TantQue
3. En déduire que la boucle TantQue se termine.  		



Exercice 7 : On considère l'algorithme suivant qui permet de calculer le quotient et le reste de la division euclidienne d’un entier positif par un entier strictement positif : 

​	



```
Saisir a 

Saisir b

q ← 0

r ← a

Tant que r>=b faire

	q ← q+1

	r ← r-b

FinTantQue

Renvoyer q,r
```



1. Décrire le fonctionnement de l’algorithme pour l’entrée (a = 17, b = 5) au moyen d’un tableau indiquant l’évolution des valeurs des variables au fil des itérations.
2. Montrer que la boucle TantQue se termine en utilisant un variant de boucle.
3. Montrer que la propriété a = bq+r est un invariant de la boucle TantQue, en déduire que l’algorithme produit le résultat attendu.  		



#### III. Combien ça coûte ?

##### 1. Complexité. 

L’analyse de la complexité d'un algorithme consiste en l'étude formelle de la quantité de ressources (par exemple de temps ou d'espace) nécessaire à l’exécution de cet algorithme. 

Nous nous restreindrons à l'étude du temps mis pour effectuer un algorithme et négligerons la quantité d'espace. 

La notion de complexité algorithmique ou encore de coût est essentiel. 

Il s'agit de pouvoir comparer l'efficacité d'algorithmes résolvant le même problème afin de choisir le plus rapide.  Ce type de question est primordial, en effet, lorsque les données sont volumineuses, la différence d' exécution de deux algorithmes peut être de l'ordre de plusieurs heures, voir de plusieurs jours.



**Définition : Le coût (en temps) d'un algorithme est l'ordre de grandeur  du nombre d'opérations élémentaires effectué par un algorithme. Cette estimation dépend du nombre de ses entrées et de leur dimension. Une opération élémentaire est une affectation, un calcul, une comparaison.**



Exercice 8 : 

1. Exécutez le fichier python vitesse. 
2. Qu'affiche ce programme ?  		
3. Que pouvez vous en déduire pour les fonctions somme et double_somme ?  		
4. Écrire une fonction element_in_tab qui prend en paramètre un tableau et un nombre, et qui renvoie True si le nombre est dans le tableau et False sinon.  		
5. Afficher la courbe de temps d'exécution de cette fonction.  		
6. Que constatez vous ? 					



##### 2. Calculons. 



Le principe est simple : il s'agit de compter chaque opération faite dans un algorithme, puis de mettre le nombre trouvé en rapport avec le nombre de données fournies. 

Afin de ne pas fausser la réponse trouvée, nous essayons de nous placer dans le pire des cas.

Exercice 9 : 

Voici un algorithme qui prend en entrée un nombre entier t représentant un nombre de secondes et qui le convertit en un temps en heure, minute, seconde. 

​	

```
Saisir t

h ← t // 3600

m ← (t-3600*h)//60

s = t%60

afficher h,m,s
```



​	1. Combien d’opérations sont effectuées ? Nous ne compterons ni la première ligne, ni la dernière. 



​	2. A votre avis, quel est le coût de cet algorithme ? 



Exercice 10 : L'algorithme suivant indique si une année est bissextile ou non en renvoyant un Vrai ou Faux. 

​	

​	

```
Saisir année

si année % 400 =0 :

	res ← Vrai

Sinon si année % 100 = 0

	res ← Faux

Sinon si annee % 4 = 0

	res ← Vrai

Sinon 

	res ← Faux

afficher respectivement
```

​	

1. Quel est le coût lorsque la fonction prend en argument une année multiple de 400 comme 2000 ? 
2. Quel est le coût lorsque la fonction prend comme argument une année multiple de 100 sans l'être de 400 comme 2100 ?
3. Quel est le coût lorsque la fonction prend comme argument une année multiple de 4 sans l'être de 100 ni de 400 comme 2020 ?  		
4. Quel est le coût lorsque la fonction prend comme argument une année non multiple de 4 comme 2021 ?  		
5. Quel est le coût dans le pire des cas, c'est-à-dire dans le cas où le coût d'exécution est le plus grand
6. Quel est le coût dans le meilleur des cas ?  		



​	

Dans ces deux exemples, nous sommes face à des algorithmes ayant des coûts constants. 

​	

**Définition : Soit n la taille d'une donnée, si le nombre d'opérations à effectuer dans le pire des cas est de la forme a où a est un nombre réel positif, on dit que la complexité de cet algorithme est constante. **



Notation : Lorsque la complexité d'un algorithme est linéaire, on la note $O(1)$

*Remarque complétement hors sujet : cette notation est appelée une notation de Landau, tu auras l'occasion de la retrouver si tu fais des maths ou de l'informatique pendant tes études supérieures.* 



Exercice 11:

Cet algorithme calcule la somme des n premiers entiers. 

​	

```
Saisir n

Somme = 0

Pour i allant de 1 à n :

	somme = somme + i

Fin Pour

afficher somme
```



1. Combien d'opérations élémentaires effectue cet algorithme ?
2. A votre avis, comment qualifierait-on le coût de cet algorithme ?  		



​	Définition : Soit n la taille d'une donnée, si le nombre d'opérations à effectuer dans le pire 	des cas est de la forme $a\times n+b$ où a et b sont des nombres réels, , on dit que la 	complexité de cet algorithme est linéaire. 



​	Notation : Lorsque la complexité d'un algorithme est linéaire, on la note $O(n)$.



​	Exemple 12 : Un réseau social contient n membres. L'entreprise gérant ce réseau stocke dans 	un tableau noté tab de taille , le nombre de messages envoyés entre chacun des 	membres du réseau. La case tab[i][j] comptabilise le nombre de messages envoyés du 	membre référencé par le numéro i vers le membre référencé par le numéro j. 

​	L'entreprise veut connaître le nombre de messages déjà envoyés sur son réseau social en utilisant les données de son tableau. 

​	Voici l'algorithme proposé.
```
​	Saisir tab

​	somme ← 0

​	Pour i allant de 1 à n :

​		Pour j allant de 1 à n :

​			somme ← somme + tab[i][j]

​		Fin Pour

​	Fin Pour 

​	Afficher somme. 

```

1. Pour une valeur de i fixée, déterminer le coût des deux lignes suivantes, en admettant que le coût d’accès à tab[i][j] est de 1.

   Pour j allant de 1 à n :

   ​somme ← somme + tab[i][j]

2. Déterminer la complexité de cet algorithme sachant que le nombre de membres est $n$.  		



​	

​Définition : Soit n la taille d'une donnée, si le nombre d'opérations à effectuer dans le pire 	des cas est de la forme  $a\times n^{2}+b\times n +c$où a, b et c sont des nombres réels, , on dit que la 	complexité de cet algorithme est quadratique. 



​	Notation : Lorsque la complexité d'un algorithme est quadratique, on la note $O(n^{2})$



​	
