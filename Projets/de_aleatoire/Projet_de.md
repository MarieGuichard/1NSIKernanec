## Projet dé. 



L'objectif de ce projet est de créer un programme qui affiche aléatoirement la face d'un dé cubique, en changeant aléatoirement les couleurs des points.
<div align='center'>
![](/Projets/de_aleatoire/img/image_de.jpg)
</div>



Vous apporterez un soin particulier à votre code en respectant les règles de bonne conduite suivantes :

**Un programme**

1. **doit être lisible et clair**  
2. **doit être découpé en petits composants faisant peu de choses, mais les faisant bien**  
3. **doit séparer calculs et interface homme/machine**  
4. **doit être documenté : spécification**  
5. **doit être testé.**  

 Vous serez vigilant à bien découper votre travail. 



Afin de dessiner , vous pouvez utiliser le module turtle de Python dont voici quelques instructions qui pourront vous être utiles. 

- **reset()** : On efface tout et on recommence  
- **goto(x,y)** :Aller à l'endroit de coordonnées x et y
- **forward(distance)** Avancer d'une distance donnée  
- **backward(distance)** Reculer  
- **up()** Relever le crayon (pour pouvoir avancer sans dessiner)  
- **down()** Abaisser le crayon (pour pouvoir recommencer à dessiner)  
- **color(couleur)** Couleur peut être une chaîne prédéfinie ('red', 'blue', 'green', etc.)

- **left(angle)** Tourner à gauche d'un angle donné (exprimé en degré)  
- **right(angle)** Tourner à droite  
- **width(épaisseur)** Choisir l'épaisseur du tracé  
- **circle(rayon)**Tracer un cercle de rayon donné.
-  **begin_fill()** Remplir un contour fermé à l'aide de la couleur sélectionnée (on termine la construction par end_fill())  
-  **write(texte)** texte doit être une chaîne de caractères délimitée avec des " ou des '   



Afin de vous familiariser avec ce module, vous pouvez faire les exercices suivants :

 Exercice 1 : Taper le programme suivant et exécuter le.

```python
from turtle import *
forward(120)
left(90)
color('red')
forward(80)
```



Exercice 2 : Taper le programme suivant et exécuter le. 

```python
from turtle import *
a=0
while a<12:
	a += 1
	forward(150)
	left(150)

```


Exercice 3 : Écrire un programme permettant de tracer un triangle équilatéral. 






