# La façade de votre maison. 



L'objectif de ce projet est de dessiner la façade d'une maison. 

L'utilisateur doit pouvoir choisir la couleur, la forme du toit, la taille , la couleur de la porte (avec remplissage), le nombre de fenêtres, …..

Vous devez également être capable d'en calculer le  coût et de préciser à l'utilisateur si cela rentre dans son budget. 

Vous devrez me rendre le cahier des charges que vous vous fixerez, la répartition du travail, ainsi que le programme python répondant au projet. 

Ce projet sera noté. Bien évidemment, il ne suffira pas que le programme fonctionne, il faudra aussi qu'il respecte les règles de bonne conduite, que le cahier des charges soit bien rédigé et que la répartition du travail se passe bien. 

Vous commenterez votre code de manière à ce qu'une personne extérieure puisse comprendre ce que chaque fonction fait. 

```python
def ma_fonction(prenom): # permet de saluer la personne en utilisant le prenom passé en paramétre
    print("bonjour",prenom)
```

Barême:

| Barême   | Tache                                             |
| -------- | ------------------------------------------------- |
| 3 points | Cahier des charges avec avancée par séance        |
| 2 points | Répartition équilibrée du travail                 |
| 6 points | Tracé de la maison (utilisation du module turtle) |
| 4 points | Interaction avec le "client"                      |
| 2 points | structure du code                                 |
| 1 point  | propreté du code                                  |
| 1 point  | commentaires                                      |
| 1 point  | toute proposition innovante                       |

Il vous faudra également prévoir une rapide présentation que vous ferez devant vos camarades afin d'expliquer vos choix. 

Pour réaliser ce programme, vous allez utiliser le module turtle de Python. 



### 1. Les modules : généralités. 

Lorsque vous lancez python, il ne charge que le minimum. Pour ajouter des fonctionnalités à Python, on importe des modules. Python contient de nombreux modules dans sa bibliothèque standard, c'est à dire des modules qui sont disponibles juste en les appelant et sans les télécharger sur le web.

Parfois les bibliothèques standard ne nous suffisent pas et on espère que quelqu'un aura créé une bibliothèque contenant des fonctions qui vont nous faciliter la vie! Par exemple:  de la 	reconnaissance de visage sur une image, piloter la capture d'une webcam simplement,...

L'installation des bibliothèques tierces se fait avec la commande pip en ligne de commande. 



Les modules sont importés en tout début de programme avec la commande import. On peut choisir d'importer toute la bibliothèque ou juste les commandes dont on va se servir. 	Forcément la deuxième méthode consomme moins de ressources et est préférable si l'on n'utilise que peu de commandes. 



Exemples d'utilisation : 

- Importation d'une seule fonction.

  ​	

  ```python
  from math import sqrt
  def racine(a):
  	if a>=0:
  		return sqrt(a)
  	else:
  		return "la racine carrée d'un nombre négatif n'existe pas"
  ```

  ​	Cette méthode permet de n'importer qu'une seule fonction du module math (la fonction sqrt() qui permet de calculer les racines carrées).  

  ​	Elle est pertinente lorsque l'on a besoin de peu de fonctions d'un module.  

- Importation de l'ensemble des fonctions  

  ​	Il y a deux manière de faire :

  ​	

  ```python
  from math import *
  
  def racine(a):
      if a>=0:
  		return sqrt(a)
  	else:
  		return "la racine carrée d'un nombre négatif n'existe pas"
  ```

  ​	De cette manière, toutes les fonctions du module math sont importées. On peut alors 	les utiliser.  

  ​	

  ```python
  import math
  def racine(a):
      if a>=0:
  		return math.sqrt(a)
  	else:
  		return "la racine carrée d'un nombre négatif n'existe pas"
  	
  ```

  

​		En utilisant import math, on doit préciser alors que la fonction sqrt() vient du module 		math. C'est plus lourd à écrire mais cela permet de ne pas avoir de confusion si on 		utilise deux fonctions ayant le même nom mais venant de deux modules différents. 



​	

### 2. Le module turtle.



​	Afin de dessiner notre maison, nous allons utiliser un module qui s'appelle turtle. 

​	Turtle est l'adaptation python de la tortue LOGO crée dans les années 60 au 			Massachusetts Institute of Technology (MIT). La tortue logo est en fait un stylo. On peut relever ou baisser le stylo, faire des portions de cercle, etc....bref, la tortue logo sert à dessiner.



​	Comme pour toutes les bibliothèques, elle propose de nombreuses fonctions. Pour les 	découvrir, vous allez devoir devoir lire tout seul la doc en anglais (you will practice your english, it will be nice ;-))

​	Le lien officiel est : https://docs.python.org/3.3/library/turtle.html?highlight=turtle

​	Compléter le tableau suivant et n'hésiter pas à ajouter d'autres fonctions si vous en avez besoin/envie. 



| Nom de la fonction | Utilisation                  |
| ------------------ | ---------------------------- |
| reset() ou clear() | efface le dessin             |
| forward(n)         | avance le crayon de n pixels |
| backward(n)        |                              |
| left(a)            |                              |
| right(a)           |                              |
| dot(d)             |                              |
| up()               |                              |
| down()             |                              |
| color()            |                              |
| goto(x,y)          |                              |
| setx(x)            |                              |
| sety(y)            |                              |





​		