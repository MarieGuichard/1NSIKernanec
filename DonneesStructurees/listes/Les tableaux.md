# Les tableaux. 

#### I. Définition.

​	Un tableau est, comme un tuple, un ensemble ordonnée d’éléments. 

​	En python , c'est un objet de type `list`. 

​	Pour créer une liste, nous utiliserons la syntaxe suivante : 

​	

```python
>>> tableau = ["haricots verts","courgettes","carottes","aubergines","tomates"]
```

​	Un tableau peut contenir des objets de type différents, mais cela n'est pas souhaitable.

​	Les crochets, ainsi que les virgules, sont indispensables. 

​	Pour créer une liste vide, on utilise la syntaxe suivante :

```python
>>> montableau_vide = []
```

​	Contrairement aux tuples et aux chaines de caractères, les tableaux sont mutables, c'est à dire  		modifiables.

#### II. Utilisation.

##### 1. Accéder à un élément. 	

Pour accéder à un élément du tableau, on procède de la même manière que pour accéder à un élément d'un tuple.  Il est également possible d'écrire des tableaux de tableaux.

La différence fondamentale entre un tuple et un tableau est qu'il est possible de modifier la valeur d'un élément du tableau. 

Pour cela, il suffit d'utiliser la syntaxe, `tableau[i]= "blabla"`

```python
>>> legumes = ["haricots verts","courgettes","carottes","aubergines","tomates"]
>>> legumes[1]
"courgettes"
>>> legumes[2:4]
["carottes","aubergines"]
>>> legumes[0]="avocat"
>>> legumes
 ["avocat","courgettes","carottes","aubergines","tomates"]
```



 Question 1 : 

1. Créer le tableau suivant :

   ville = ["Paris","Marseille","Lille","Lens","Arras","Valenciennes"]

2. Afficher les villes du Nord-Pas de Calais (n'utiliser qu'une seule instruction).  		

3. Remplacer « Arras » par « Béthune ».  		

4. Modifier le tableau de sorte qu'il contienne un tableau de tableaux où seront indiqués le nom de la ville, ainsi que le département dans lequel il est .

5. Écrire l'instruction permettant d'accéder au département de Béthune.  		

   

##### 2. Longueur d'un tableau.

Comme pour une chaîne de caractères ou un tuple, la fonction `len(tableau)` permet d'obtenir la longueur de votre tableau. 

```python
>>> legumes = ["haricots verts","courgettes","carottes","aubergines","tomates"]
>>> len(legumes)
5
```

##### 3. Appartenance. 

L'appartenance à un tableau se teste avec l'opérateur `in` comme pour les tuple. 

```python
>>> legumes = ["haricots verts","courgettes","carottes","aubergines","tomates"]
>>> "courgettes" in legumes
True
>>> "salsifi" in legumes
False
```



##### 4. Parcours. 

On peut parcourir un tableau avec la boucle for. Il y a deux méthodes. 

```python
for elt in legumes:
	print(elt)
```

```python
for i in range (len(legumes)):
	print(legumes[i])
```

Question 2: En reprenant l'exemple précédent, parcourir le tableau ville. 

##### 4. Opérations. 

Les opérateurs + et * s'utilisent comme avec les tuples. Ce sont des opérateurs de concaténation. 

#### III. Les méthodes relatives aux tableaux. 

Il existe, en python, des méthodes associées à des objets particuliers. C'est le cas pour les 	objets de type list. Une méthode ne s'emploit pas tout à fait comme une fonction. En effet, 	elle respecte la syntaxe suivante : objet.methode(paramètre). 

 ##### 1. Supprimer un élément.

Il existe deux manières de supprimer un élément :

- soit en avec la commande `del` avec l'index de l’élément :

  ```python
  >>> legumes = ["haricots verts","courgettes","carottes","aubergines","tomates"]
  >>> del legumes[1]
  >>> legumes
  ["haricots verts","carottes","aubergines","tomates"]
  
  ```

- soit avec la méthode  `remove` (avec la valeur de l’élément).  	

  ```python
  >>> legumes = ["haricots verts","courgettes","carottes","aubergines","tomates"]
  >>> legumes.remove("courgettes")
  >>> legumes
  ["haricots verts","carottes","aubergines","tomates"]
  ```

  ​	

​	Question 3: En utilisant la méthode de votre choix, supprimer la ville de Paris et toutes les 		   	informations qui vont avec.  		



##### 2. Ajouter un élément au tableau.

​	Il est possible, avec la méthode `append`, d'ajouter un élément au tableau. 

```python
>>> legumes = ["haricots verts","courgettes","carottes","aubergines","tomates"]
>>> legumes.append("carottes")
>>> legumes 
["haricots verts","courgettes","carottes","aubergines","tomates","carottes"]
```

 		



​	Question 4:  Ajouter la ville de votre choix au tableau `ville`.



##### 3. Des méthodes supplémentaires.



​	Afin de voir quelles méthodes vous pouvez utiliser avec les tableaux, vous pouvez vous rendre sur la page suivante : 

​	https://docs.python.org/fr/2/tutorial/datastructures.html



#### IV. Construction d'un tableau. 

##### 1. Construire un tableau d’éléments identiques.



Pour créer un tableau ne comprenant que des éléments prenant la même valeur, on utilise la syntaxe suivante :

​		`tableau = [ valeur ] * nombre d’éléments souhaités. `

```python
>>> tableau = ["valeur"]*10
>>> tableau
["valeur","valeur","valeur","valeur","valeur","valeur","valeur","valeur","valeur","valeur"]
```



Question 5 : 

1. Créer un tableau contenant 100 zéro.
2. Créer le tableau [1,2,1,2,1,2,1,2,1,2,1,2]



##### 2. Construire un tableau par compréhension.

La notation en compréhension permet de créer un tableau sans énumérer explicitement les 	éléments.

On utilise la syntaxe suivante :

tableau = [ fonction sur élèment for élèment in liste if condition]

Prenons des exemples : 

1. Pour obtenir la liste des entiers entre 1 et 10 :

   ```python
   >>> tableau = [ i for i in range(1,11)]
   >>> tableau
   [1,2,3,4,5,6,7,8,9,10]	
   ```

2. Pour obtenir la liste des carrés entre 9 et 121 :  		

   ```python
   >>> tableau = [i**2 for i in range(2,12)]
   >>> tableau 
   [4,9,16,25,36,49,64,81,100,121]
   ```

   Question 6: 

   1. Construire, par compréhension, un tableau contenant tous les nombres impairs compris entre 1 et 299.
   2. Construire, par compréhension, un tableau contenant tous les multiples de 7 , compris entre 7 et 700, en excluant les multiples de 3.  		



#### V. Exercices :



**Exercice 1 :**

​	Soient les tableaux suivants :
```python

​		T1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

​		T2 = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"]
``` 

​	Écrire un programme qui crée un nouveau tableau T3. Celui-ci devra contenir tous les éléments des deux listes en les alternant, de telle manière que 	chaque nom de mois soit suivi du nombre de jours correspondant :
```python
​	["Janvier", 31, "Février", 28, …]
```



**Exercice 2 :**

Écrire un programme qui demande à l'utilisateur des nombres, puis qui les range dans un tableau.

(On pourra demander à l'utilisateur la taille souhaitée du tableau, ou demander à l'utilisateur d'écrire STOP lorsqu'il a donné le dernier nombre du tableau.)



**Exercice 3:** Écrire un programme qui analyse un par un tous les éléments d'un tableau 	contenant des mots pour générer deux nouveaux tableaux : l'un contenant les mots 	comportant moins de 6 caractères et l'autre les mots comportant 6 caractères ou davantage. 



**Exercice 4 :**

Écrire un programme qui retourne le plus grand élément présent dans une liste de nombres donnée (on n’utilisera ni la fonction `max()`, ni la fonction `sort()`)  et qui



**Exercice 5 :** Écrire un tableau qui crée un tableau à deux dimensions de taille 30 par 30 contenant des entiers tirés au hasard entre 1 et 9999, puis l'affiche. 
