# Algorithme: introduction et complexité. 

Depuis la classe de petite section en maternelle à cette année, nous avons déjà utilisé, complété, corrigé et conçu un grand nombre d'algorithmes. Nous allons maintenant étudier cette notion plus en détail. 

### I. D'où vient le mot *algorithme* ?

![](E:\lycee\NSI\Algorithme\image_al_khwarizmi.jpg)

Le mot *algorithme* vient du nom du mathématicien persan Al-Khwarizmi, né vers 780 et mort à Bagdad vers 850. 

Al-Khwarizmi est resté célèbre pour deux ouvrages qui ont largement contribué à faire connaître et à vulgariser les chiffres dits « *arabes* » et les méthodes de calcul, ainsi que les procédés algébriques de résolution d’équations, aussi bien dans le monde musulman qu’en Occident chrétien. 

Le premier de ces ouvrages s’intitule : « *Traité de l’addition et de la soustraction d’après le calcul des Indiens* ». L’original de ce traité est malheureusement perdu, mais il en reste plusieurs traductions latines faites à partir du XIIème siècle. C’est le premier livre arabe connu où le système décimal d’écriture des nombres et les méthodes de calcul d’origine indienne font l’objet d’explications détaillées, illustrées par de nombreux exemples. 

Le traité débute ainsi : « *Nous avons décidé d’exposer la manière de calculer des Indiens à l’aide de neuf caractères et de montrer comment, grâce à leur simplicité et leur concision, ces caractères peuvent exprimer tous les nombres.* » Al-Khwarizmi explique ensuite en détail le principe de la numération décimale de position, en signalant l’origine indienne des neuf chiffres et de « *la dixième figure en forme de cercle* » (le zéro), dont il recommande de « *ne pas négliger l’usage afin de ne pas confondre les positions* ». 

Ce livre jouira plus tard dans les pays d’Europe d’une telle renommée que le nom même de son auteur finira par désigner le système de numération décimale : latinisé, le nom d’Al-Khwarizmi deviendra d’abord **Alchoarismi**, puis il se transformera en **Algorismi**, **Algorismus**, **Algorithmus**, et, enfin : **Algorithme**.

Aujourd’hui, le mot algorithme signifie : *enchaînement d’actions permettant l’accomplissement d’une tâche*.

Quant à l’algorithmique, il s’agit de la science qui étudie l’application des algorithmes à l’informatique.

Remarque : la notion d'algorithme est très antérieure à la création du premier ordinateur. 

### II. Qu'est ce qu'un algorithme ?

​	

Nous avons la définition suivante:

**Algorithme :nom masculin, ensemble de règles opératoires dont l'application permet de résoudre un problème énoncé au moyen d'un nombre fini d'opérations élémentaires .**

De plus, un algorithme peut être traduit grâce à un langage de programmation, en un programme exécutable par un ordinateur. 



Qu'est ce qu'une opération élémentaire :

définir "opération élémentaire" n'est pas chose aisée ! On peut tout de même dire qu'une "opération élémentaire" est une action simple, qui doit être facilement compréhensible pour la personne chargée d'effectuer cette action. 

L'action "Peser 100 g de farine" peut être considérée comme une "opération élémentaire", en effet, tout le monde est capable de comprendre ce que cela signifie et la réalisation de cette opération ne prête ni à interprétation, ni à confusion.  En revanche "Prendre de la farine, des oeufs, du sucre et du chocolat afin de faire un gâteau au chocolat" n'est clairement pas une "opération élémentaire", car l'action décrite ici manque de précision, c'est une opération complexe (même si dans la pratique il n'est pas très difficile de faire un gâteau au chocolat, ce n'est pas évident pour quelqu'un qui n'a pas l'habitude). La frontière entre "opération élémentaire" et "opération complexe" n'est pas toujours évidente, en effet, l'opération "Peser 100 g de farine" pourrait être encore plus précise : "mettre la balance à zéro (faire la tare), verser ensuite de la farine sur le plateau de la balance jusqu'à ce que le nombre 100 soit affiché sur l'écran de la balance" 

On pourrait donc résumer ce qu'est un algorithme par le schéma suivant :

![](E:\lycee\NSI\Algorithme\schéma_algo_1.jpg)

 Donald Knuth a énoncé quelques régles dans un ouvrage monumental, The Art of Computer Programming, dont l'écriture a commencé en 1962 et la publication du premier volume date de 1968. L'ouvrage commence par un algorithme décrivant la manière de lire le premier volume de cet ensemble puis de lire les différents volumes ! 

Nous pouvons en extraire cinq caractéristiques importantes d'un algorithme :

- ​	Un algorithme doit toujours se terminer après un nombre fini d'étapes.
- ​	Chaque étape d'un algorithme doit être définie précisément, les actions à mener doivent être spécifiées rigoureusement, et sans ambiguïté pour chaque cas.  
- ​	Un algorithme a des entrées, zéro ou plus, quantités qui lui sont données avant ou pendant son exécution.  
- ​	Un algorithme a une ou plusieurs sorties, quantités qui ont relation spécifiée avec les entrées.  
- ​	Les instructions doivent être suffisamment basiques pour pouvoir être en principe exécutées de manière exacte et en un temps fini par une personne utilisant un papier et un crayon.  

### III. Un premier exemple. 

Prenons un exemple concret : 

Nous allons étudier cette année, ainsi que l'année prochaine, des algorithmes de tri pour les tableaux (un tableau ressemble beaucoup à une liste en Python, même si ce n'est pas exactement la même chose). Nous avons en entrée un tableau non trié et nous obtenons en sortie un tableau trié : 

![](E:\lycee\NSI\Algorithme\schéma_algo_tri1.jpg)

La "valeur de sortie" n'est pas obligatoirement du même type que la "valeur d'entrée". Prenons l'exemple d'un algorithme qui prend en entrée un tableau t d'entiers et un entier x, et qui "répond" par "oui" ou par "non" à la question "x est-il présent dans le tableau t ?". Dans ce cas, la "valeur de sortie" sera "oui" ou "non". 

![](E:\lycee\NSI\Algorithme\schéma_algo_tri2.jpg)

Voici l'algorithme permettant de répondre au problème suivant :

Soit t un tableau d'entiers et x un nombre entier, x est-il présent dans le tableau t ? 

```
VARIABLE
t: tableau d'entiers
x: nombre entier
tr: booléen
i: nombre entier
DEBUT
tr <- FAUX
i <- 0
Tant que i<longueur(t) et que tr==FAUX:
	si t[i]==x:
		tr <- VRAI
	fin si
	i<-i+1
fin tant que
renvoyer la valeur de tr
FIN
```

Remarques : 

- ​	Quand on écrit un algorithme, on utilise un langage dit "langage naturel" ("tant que", "si"...), ce langage naturel permet de passer facilement à un langage de programmation (Python, Java...), on dit alors que l'on implémente l'algorithme.  
- ​	Traditionnellement (sauf erreur de ma part, ce n'est pas une obligation), lorsque l'on écrit un algorithme le premier élément d'un tableau a pour indice 1 (alors que dans la plupart des langages de programmation le premier élément d'un tableau a pour indice 0). Il faut donc faire attention à cela lorsque l'on veut implémenter un algorithme.  
- ​	Dans l'algorithme ci-dessus, on part du principe qu'il existe une fonction "longueur" qui prend en paramètre un tableau et qui renvoie le nombre d'éléments présents dans ce tableau. Vous noterez que déterminer le nombre d'éléments présents dans un tableau n'est pas vraiment une "opération élémentaire", pourtant ici, on considère l'utilisation de "longueur" comme une opération élémentaire ! Il arrive relativement souvent que l'on s'autorise ce genre de liberté quand on écrit un algorithme.  

La première chose à faire quand on étudie un algorithme, c'est de le "faire tourner à la main" : on "exécute" l'algorithme en utilisant uniquement une feuille et un crayon. 

Exemple 1: t=[5,8,15,23] et x = 15

|           | initialisation |      |      |      |      |
| --------- | -------------- | ---- | ---- | ---- | ---- |
| i         | 0              | 0    | 1    | 2    |      |
| t[i]      |                | 5    | 8    | 15   |      |
| tr        | FAUX           | FAUX | FAUX | VRAI |      |
| condition | VRAI           | VRAI | VRAI | FAUX |      |

L'algorithme renvoie VRAI. 

Exercice 1 :

En utilisant un tableau, faites « tourner à la main », l'algorithme « x est-il présent dans le tableau t ? » 

a. avec t=[5,8,15,53] et x=8

b. avec t = [5,8,15,53] et x=12



### IV. Complexité d'un algorithme.



La notion de complexité d'un algorithme va rendre compte de l'efficacité de cet algorithme. Pour un même problème, par exemple trier un tableau, il existe plusieurs algorithmes, certains algorithmes sont plus efficaces que d'autres (par exemple un algorithme A mettra moins de temps qu'un algorithme B pour résoudre exactement le même problème, sur la même machine). 

Il existe 2 types de complexité : une complexité en temps et une complexité en mémoire. Nous nous intéresserons ici uniquement à la complexité en temps. La complexité en temps est directement liée au nombre d'opérations élémentaires qui doivent être exécutées afin de résoudre un problème donné. L'évaluation de ce nombre d'opérations élémentaires n'est pas chose facile, on rencontre souvent des cas litigieux. Prenons tout de suite un exemple avec notre algorithme "x est-il présent dans le tableau t ?". 

Il y a 2 cas à traiter : 

- ​	L'entier recherché est bien présent dans le tableau, il se trouve à la position d'index j  
- ​	L'entier recherché n'est pas présent dans le tableau  

Commençons par le premier cas : 

```
VARIABLE
t : tableau d'entiers
x : nombre entier
tr : booléen (VRAI ou FAUX)
i : nombre entier
DEBUT
1 fois   tr ← FAUX
1 fois   i ← 1
j+1 fois tant que i<=longueur(t) et que tr==FAUX:
j fois      si t[i]==x:
1 fois       tr ← VRAI
           fin si
j fois     i ← i+1
        fin tant que
1 fois  renvoyer la valeur de tr
FIN
                        
```

Au total nous avons : 1 + 1 + j + 1 + j + 1 + j + 1 = 3j + 5 opérations élémentaires 

Dans le cas où l'entier recherché ne se trouve pas dans le tableau (et que le nombre d'éléments dans le tableau est n) : 

```
VARIABLE
t : tableau d'entiers
x : nombre entier
tr : booléen (VRAI ou FAUX)
i : nombre entier
DEBUT
1 fois   tr ← FAUX
1 fois   i ← 1
n+1 fois tant que i<=longueur(t) et que tr==FAUX:
n fois      si t[i]==x:
0 fois       tr ← VRAI
           fin si
n fois     i ← i+1
        fin tant que
1 fois  renvoyer la valeur de tr
FIN
                        
```

Au total nous avons : 1 + 1 + n + 1 + n + 0 + n + 1 = 3n + 4 opérations élémentaires 

Comme dans la plupart des cas n > j, on effectue plus d'opérations élémentaires quand le nombre recherché n'est pas dans le tableau (sauf dans le cas précis où l'entier recherché est en dernière position, mais nous ne tiendrons pas compte de ce cas). On parle de "complexité dans le pire des cas" quand on s'intéresse uniquement au cas où le nombre d'opérations élémentaires est le plus grand. Dans la suite nous nous intéresserons uniquement à cette complexité dans le pire des cas (dans la suite "complexité" = "complexité en temps dans le pire des cas"). Pour notre exemple, nous considérerons uniquement le cas où le nombre total d'opérations élémentaires est de 3n + 4. 

Nous venons de voir que la complexité dépend de la taille du tableau, plus le tableau est grand et plus le nombre d'opérations élémentaires à effectuer est important. Pour effectuer des comparaisons entre plusieurs algorithmes, nous allons raisonner sur des tableaux de grande taille, car plus les tableaux sont grands et plus les différences entre les algorithmes seront flagrantes. Pour comparer des algorithmes, nous allons donc uniquement nous intéresser à ce que l'on appelle "l'ordre de grandeur asymptotique". La définition précise de cet "ordre de grandeur asymptotique" est trop complexe pour être abordé ici. Vous devez juste savoir que cet "ordre de grandeur asymptotique" concerne les cas où l'on prend n très très grand. On note cet "ordre de grandeur asymptotique" avec un O majuscule. Pour le cas qui nous intéresse, nous aurons : 

3n+4 = O(n) 

La relation ci-dessus signifie que "3n+4 est dominée asymptotiquement par n", autrement dit "si n est suffisamment grand, il existe une constante c qui permettra d'avoir c.n ⩾ 3n+4", vous n'avez pas tout compris ? Cela n'a pas vraiment d'importance, ce qu'il faut retenir c'est que nous utiliserons systématiquement cette notation O pour exprimer la complexité des algorithmes : au final on dira donc que la complexité de notre algorithme "x est-il présent dans le tableau t ?" est O(n). 

Comment obtient-on cette notation O à partir du nombre d'opérations élémentaires ? 

Ici nous avons simplement supprimé la constante (4) et le coefficient devant le n (c'est-à-dire 3), il reste donc uniquement n d'où le 3n+4 = O(n). Dans le cas où nous avons un polynôme de degrés quelconque, par exemple pour 6n2+3n+10, il suffit de : 

- ​	supprimer la constante  
- ​	garder uniquement le n qui possède l'exposant le plus grand  
- ​	supprimer le coefficient devant le n  

On aura donc  = $O( n^2 )$ : "$6n^2+3n+10$ est dominée asymptotiquement par $n^2$" 

Exercice 2: Écrivez un algorithme permettant de trouver le plus grand entier présent dans un tableau. Vous ferez "tourner à la main" votre algorithme en utilisant le tableau t = [3,5,1,8,4,2]. Vous déterminerez ensuite la complexité de votre algorithme. 

####  

Exercice 3: Écrivez un algorithme permettant de calculer la moyenne de tous les entiers présents dans un tableau. Vous ferez "tourner à la main" votre algorithme en utilisant le tableau t = [3,5,1,8,4,2]. Vous déterminerez ensuite la complexité de votre algorithme. 