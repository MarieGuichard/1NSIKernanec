# Les variables. 

### I. Notion de variable. 

Une **variable** est une zone de la mémoire de l'ordinateur dans laquelle une **valeur** est stockée. Aux yeux du programmeur, cette variable est définie par un **nom**, alors que pour l'ordinateur, il s'agit en fait d'une adresse, c'est-à-dire d'une zone particulière de la mémoire.

​	

En Python, la **déclaration** d'une variable et son **initialisation** (c'est-à-dire la première valeur que l'on va stocker dedans) se font en même temps. 

Pour vous en convaincre, testez les instructions suivantes dans le Shell après avoir lancé Thonny:

```python
>>> x = 2
>>> x
```

Ligne 1. Dans cet exemple, nous avons déclaré, puis initialisé la variable `x` avec la valeur 2. Notez bien qu'en réalité, il s'est passé plusieurs choses :

- Python a « deviné » que la variable était un entier. On dit que Python est un langage au **typage dynamique**.  
- Python a alloué (réservé) l'espace en mémoire pour y accueillir un entier. Chaque type de variable prend plus ou moins d'espace en mémoire. Python a aussi fait en sorte qu'on puisse retrouver la variable sous le nom `x`.  
- Enfin, Python a assigné la valeur 2 à la variable `x`.

Lignes 2 et 3. L'interpréteur nous a permis de connaître le contenu de la variable juste en tapant son nom. Retenez ceci car c'est une **spécificité de l'interpréteur Python**, très pratique pour chasser (*debugger*) les erreurs dans un programme. 

Sachez par ailleurs que l'opérateur d'affectation `=` s'utilise dans un certain sens. Par exemple, 	l'instruction `x = 2` signifie qu'on attribue la valeur située à droite de l'opérateur `=` (ici, `2`) à la variable située à gauche (ici, `x`).

Enfin, dans l'instruction `x = y - 3`, l'opération `y - 3` est d'abord évaluée et ensuite le résultat 	de cette opération est affecté à la variable `x`.

​	

En Python, le nom d'une variable doit respecter quelques règles :

- il ne peut être constitué que de lettres, de chiffres et de l'underscore _.
- il ne peut pas commencer par un chiffre.  	

De plus, Python distingue les minuscules et les majuscules. 

Question 1: 

1. Quelle instruction devez vous écrire pour affecter la valeur 5 à une variable que vous appelerez `ma_variable`? 
2. Comment pouvez vous afficher la valeur de `ma_variable`? 
3. Saisissez l'instruction `ma_variable = ma_variable + 1`. Quelle valeur est alors enregistrée dans `ma_variable` ? 



#### II. Type de variables. 

Le **type** d'une variable correspond à la nature de celle-ci.	

Python distingue différents types de variables parmi lesquels les trois principaux: les nombres entiers, les nombres décimaux et les chaines de caractères.  Ils ont des opérateurs qui leur sont dédiés. 

Python possède une fonction qui permet de déterminer la nature d'une variable. 

Question 2: Dans le Shell, exécuter les instructions suivantes:

```python
>>> x = 3
>>> type(x)
>>> y = 2.4
>>> type(y)
>>> z = "Chouchou"
>>> type(z)
```



#### a. Les nombres. 

Nous en distinguerons deux catégories: 

- Les nombres entiers : on les note **int**
- les nombres décimaux : on les note **float**. On utilise le `.` pour les noter et pas la virgule.

On peut effectuer toutes les opérations usuelles avec les nombres entiers et les nombres décimaux, comme l'addition (opérateur `+`), la soustraction (opérateur `-`), la multiplication (opérateur `x`) et la division (opérateur `/`). 

De plus, l'opérateur `//` permet d'obtenir la partie entière d'une division et `%` le reste d'une division lorsque l'on travaille avec les nombres entiers.  

Pour mettre un nombre à une puissance souhaitée, on utilise **. 

Question 3: 

1. Affecter à x la valeur 13 et à y la valeur 4

2. Quel résultat obtenez vous en entrant les calculs suivants :

   - x+y

   - x*y

   - x//y

   - x%y

   - x/y

   - y**3

3. Quel calcul pouvez vous entrer de manière à obtenir le résultat de 11 ?

#### b. Les chaines de caractères. 

On les note **str**. 

Python reconnaît de manière automatique les entiers ou les flottants, mais cela n'est pas le cas pour les chaînes de caractères.	

 Il faut donc entourer de guillemets ou d'apostrophe les chaînes de caractères afin de les distinguer des variables. 

```python
>>> bonjour="Coucou"
>>> bonjour
"Coucou"
>>> bonjour="Salut"
>>> bonjour
"Salut"
```

On peut par exemple trouver la longueur de la chaîne de caractères en utilisant l'instruction **len**(s) ou concaténer (c'est à dire écrire les mots les uns à la suite des autres) en utilisant l'opérateur `+`.

```python
>>> bonjour = "Coucou"
>>> len(bonjour)
6
>>> prenom = " Clément"
>>> bonjour + prenom
Coucou Clément
```

Question 4 :

1. Affecter à la variable` classe` la chaîne de caractères « première »
2. Affecter à la variable `presentation` la chaîne de caractères « Ma classe actuelle est la« 
3. Donner le nombre de caractères de la variable` presentation`. 
4. Afficher la phrase « Ma classe actuelle est la première » en utilisant les variables `classe` et `presentation`.  		

### III. Saisir une valeur. 

Dans un algorithme, il faut donner des valeurs aux variables. Il existe deux façons de le faire.



- lorsque c'est le programmeur qui donne la valeur à la variable : on utilise le  `= `. 

  `X= 2`

  La variable nommée X prend alors la valeur 2.  	

  

- lorsque c'est l’utilisateur qui donne la valeur à la variable : on utilise la fonction **input()**

  `a=input(" votre nom est :")`

  A l'écran, apparaît le message  `votre nom est `. 	

  L'utilisateur entre alors ce qu'il souhaite en utilisant le clavier,Toto par exemple.   	

  Par défaut, la valeur donnée par l'utilisateur est une chaîne de caractères.

  ```python
  >>> a = input("votre nom est:")
  votre nom estToto
  >>> a
  "Toto"
  ```

  Il est possible de convertir la chaine de caractéres en entier (par exemple) e, utilisant l'instruction `int()`

  ```python
  >>> age = int(input("quel âge as tu? "))
  15
  >>> age 
  15
  >>> age = age + 1
  >>> print("dans un an, tu auras",age, "ans" )
  dans un an, tu auras 16 ans
  ```

  Question 5: 

  1. Demander à l'utilisateur son année de naissance, la mettre dans une variable annee.
  2. Dans la variable age, calculer l'age de l'utilisateur.  		
  3. Afficher l'age de l'utilisateur.  

  #### IV. Afficher un message à l'écran. 

  La fonction **print()** permet l'affichage du contenu entre parenthèses dans la console Python.

  ​		

  | Instructions                                       | Signification                                                | Affichage  |
  | :------------------------------------------------- | :----------------------------------------------------------- | :--------- |
  | nombre=7 		print(nombre)                     | Affiche la valeur de la variable nombre                      | 7          |
  | nombre = 7 		           print(« nombre »)    | Affiche le texte entre guillemets. Les guillemets peuvent être simples ou doubles | nombre     |
  | nombre = 7  		 	print(« nombre= »,nombre) | Affiche à la suite le texte entre 		guillemets puis la valeur de la variable nombre | nombre = 7 |

   	

  ​	Question 4 : 

  1. Demander à l'utilisateur le nom de son animal préféré.
  2. Afficher une phrase du type « j'adore les chats » (si l'utilisateur préfère les chats).

   		

  #### V. Exercices. 

  Pour les exercices, vous écrirez le code de votre programme dans la partie supérieure de Thonny, puis vous l'exécuterez dans le Shell. 

  **Exercice 1**: 

  1. Écrire un programme qui demande l'année de naissance de l'utilisateur puis affiche "Tu es né en …"
  2. Écrire un programme qui demande l'année de naissance de l'utilisateur puis affiche l'âge qu'aura l'utilisateur en 2050.  	

  **Exercice 2:**

  Écrire un programme qui demande le prénom d'un utilisateur puis qui lui dit combien il y a de lettres dans son prénom.

​	**Exercice 3:** 

​	Écrire un programme qui demande 2 entiers A et B, puis renvoie le quotient et le reste de la 		   	division euclidienne de A par B en faisant une phrase. 

​	**Exercice 4:**

​	Écrire un programme qui demande un nombre entier `x`à l'utilisateur et qui lui affiche la valeur de 	   	3x²-4x+1. 



​	