# Les N-uplets ou tuples. 



Jusqu'à présent, nous avons étudié différents types de valeurs que l'on peut qualifier de simple comme les entiers (int), les flottants (float), les chaînes de caractères (str). Avec ces types, nous pouvons définir des variables qui représentent chacun une donnée dont la valeur est un nombre ou une chaîne de caractères. 

Il peut être intéressant de regrouper des données, comme pour les coordonnées d'un point par exemple. Nous avons alors besoin de définir des variables dont les valeurs sont des ensembles de valeurs : c'est ce que nous appellerons des types construits. Nous en étudierons trois cette année : les tuples (ou n-uplets), les tableaux (ou listes) et les dictionnaires. 

#### I. Définition.

Un **n-uplet** ou **tuple** est une suite ordonnée d’éléments. Ces éléments peuvent être de n'importe quel type. 

Pour créer un tuple, nous utilisons la syntaxe suivante :

```python
>>> meteo=("soleil","pluie","orage","neige","vent")

```



Les virgules sont indispensables, contrairement aux parenthèses. Mais celle-ci permettent une plus 	grande lisibilité du code. 

Pour créer un tuple vide, on utilise la syntaxe suivante :

```python
>>> mon_tuple_vide = ()
```



#### II. Utilisation.



##### 1. Accéder aux éléments.

Pour accéder à un élément d'un tuple, on utilise le nom de la variable qui contient le tuple et on lui accole, entre deux crochets, l'index numérique qui correspond à la position de élément dans le tuple. 

Attention,comme pour les chaînes de caractères, la numérotation des index commence à zéro. Ainsi, le premier caractère de la chaîne a pour index 0. 

```python
>>> meteo=("soleil","pluie","orage","neige","vent")
>>> meteo[0]
"soleil"
>>> meteo[1]
"pluie"
```

Il est également possible d'accéder à une partie du tuple en faisant une slice (tranche en anglais). 

```python
>>> meteo=("soleil","pluie","orage","neige","vent")
>>> meteo[2:4]
("orage","neige")
```

​		

Question 1 : 

1. Créer une variable `age `contenant la  valeur 81.
2. Créer un tuple nommé `personne`contenant les valeurs `Dupont`, `Jules`, `age`, `59700`rangées dans cet ordre.  				
3. Quelle instruction entre-t-on pour accéder à la première valeur du tuple `personne` ? 
4. Exécuter  l'instruction `personne[2]`. Qu'observez vous ?  				
5. Modifier la valeur de la variable `age`et exécuter  à nouveau l'instruction `personne[2]`. Que se passe-t-il? 
6. Exécuter l'instruction `personne[4]`. Qu'observez vous ? Comment pouvez vous l'expliquer? 		

​	

Attention, il n'est pas possible de modifier la valeur d'un tuple en utilisant l'instruction 				mon_tuple[i]= « blabla ». 

Question 2: Reprendre la question 1 et exécuter l'instruction `personne[0] = "Dupond"`. Qu'observez vous ? 

##### 2. Longueur d'un tuple.

Comme pour une chaîne de caractères, la fonction `len(mon_tuple)` permet d'obtenir la 				longueur de votre tuple. 

Question 3: Quelle est l'instruction vous permettant d'obenir la longueur du tuple `personne`. 



##### 3. Opérations.

L' opérateur `+`  s'utilise comme avec les chaînes de caractères. C'est un opérateur de concaténation. 

```python
>>> personne=("Dupont","Maurice")
>>> adresse=(54,"Bd de la Liberté","Lille")
>>> personne_adresse= personne+adresse
>>> personne_adresse
("Dupont","Maurice",54,"Bd de la Liberté","Lille")
```

L'opérateur `*`permet de multiplier un tuple et un entier. On obtient alors un nouveau tuple. 

```python
>>> personne=("Dupont","Maurice")
>>> personne_triple = 3*personne
>>> personne_triple
("Dupont","Maurice","Dupont","Maurice","Dupont","Maurice")
```

##### 4. Appartenance

Il est possible de tester l'appartenance d'un élément à un tuple en utilisant l'opérateur `in`. 

```python
>>> personne = ("Dupont","Maurice")
>>> "Dupont" in personne
True
>>> "Durand" in personne
False
```

##### 5. Parcours. 

Pour parcourir un tuple, il est possible de procéder de deux manières différentes:

- soit en effectuant une boucle sur les index. 

  ```python
  meteo=("soleil","pluie","orage","neige","vent")
  for i in range(len(meteo)):
  	print(meteo[i])
  ```

  

- Soit en effectuant une boucle directement sur les élèments du tuple. 

  ```python
  meteo=("soleil","pluie","orage","neige","vent")
  for elt in meteo:
  	print(elt)
  ```

  

#### III. Tuples de tuples. 

Il est possible de faire des tuples de tuples (ou des tuples emboîtés). 

```python
>>>meteo=("soleil","pluie","orage","neige","vent")
>>>destination = ("mer","montagne","campagne","ville")
>>>annee = (2020,2021,2022,2023,2024)
>>> vacances = (destination, meteo,annee)
>>> vacances
(("mer","montagne","campagne","ville"),("soleil","pluie","orage","neige","vent"),(2020,2021,2022,2023,2024))
```

Pour accéder à ses éléments, on utilisera un double crochet `tuple[i][j]`, la valeur de `i`faisant référence à la place du tuple dans le tuple, et la valeur de `j`à la valeur de l'élément dans le tuple. 

```python
>>> vacances[1][0]
"soleil"
```

Question 3:

1. Quelle est l'instruction permettant d'accéder à la valeur "campagne"? 
2. Quelle est l'instruction permettant d'accéder à la valeur 2022? 

#### IV. Tuples nommés. 

Il est possible de créer des objets tuples. 

Question 4: 

1. Copier et exécuter le code suivant. 

```python
from collections import namedtuple
Point = namedtuple("Point",["x","y"])
p1=Point(2,3)
print(p1.x)
print(p1.y)
```

2. Créer un point p2 ayant pour coordonnées (6,10). 
3. En utilisant p1 et p2, créer un point p3, milieu des points p1 et p2. 

#### v. Exercices. 

**Exercice 1:** Ecrire une fonction `combien(liste,element)`qui prend en argument un tuple appelé `liste`et un element et qui renvoie le nombre de fois où élément est présent dans le tuple. 

```python
>>> combien(('a','b','a','c','a','b'),'a')
3
>>> combien(('a','b','a','c','a','b'),'z')
0
```

**Exercice 2 :** Écrire une fonction `produit(nombres,n)`qui prend en argument un tuple appelé  nombres composé de nombres et un entier naturel  n non nul et renvoie un nouveau tuple obtenu en multipliant chaque élément de la liste `nombres` par `n`. 

```python
>>> produit((1,4,7),2)
(2,8,14)
```



**Exercice 3 :** Écrire une fonction `tri_pair_impair(nombres)` qui prend en argument un tuple composé de nombres entiers et renvoie un tuple contenant deux tuples : le premier ne contenant que les entiers pairs du tuple de départ et le deuxième que les entiers impairs.

```
>>> tri_pair_impair((4,7,8,10,3,5,6))
((4,8,10,6),(7,3,5))
```



**Exercice 4:** Ecrire une fonction melange(tuple1,tuple2) qui prend en argument deux tuples de même longueur et renvoie un tuple avec les élèments du tuple1 et du tuple 2 en alternance. 

```
>>> melange(("il","fait","beau"),("ne","pas","aujourd'hui"))
("il","ne"","fait","pas","beau","aujourd'hui")
>>> melange((1,2,3),(4,5))
"Erreur, les deux tuples ne font pas la même longueur"
```





