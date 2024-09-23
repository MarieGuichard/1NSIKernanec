# Les fonctions.



#### I. Cours.

Jusqu'à présent, nous avons écrit des programmes très courts. Or, lors de véritables projets, vous serez confrontés à des problèmes souvent complexes et les lignes de programme vont commencer à s'accumuler.  

L'approche efficace d'un problème complexe consiste souvent à le décomposer en plusieurs sous-problèmes plus simples qui seront étudiés séparément. Il est d'usage pour cela d'utiliser des **fonctions**.   

Nous en avons déjà rencontrées plusieurs qui font partie des fonctions préprogrammées de Python comme `range()`, `input()`, `print()`. 

​	

Question 1 :

1. Copier le programme suivant :

   ```python
   def pair_ou_impair(nombre):
       if nombre%2 == 0:
           return "pair"
       else:
           return "impair"
   ```

   2. Exécuter le. Que se passe-t-il ?  Entrer dans le Shell la commande suivante : `pair_ou_impair(14)`.

​	     Quel résultat obtenez vous ?  			

3. Entrer dans le Shell la commande suivante : `pair_ou_impair(17)`.

   Quel résultat obtenez vous ?  			

4. Que fait la fonction pair_ou_impair() ?



**Une fonction  est un programme qui porte un nom et utilise zéro, une ou plusieurs variables appelés paramètres. **

La syntaxe est la suivante : 

```python
def nom_de_la_fonction(parametre1,parametre2,..):
	instruction
	return resultat
```

​	



On peut utiliser une fonction soit dans la console, soit dans un autre script, en donnant des 	valeurs aux arguments (dans le bon ordre). 

Une fonction ne renvoie qu'un seul résultat. On utilise pour cela l'instruction **return** qui permet de renvoyer n'importe quelle valeur. 

On peut utiliser la valeur renvoyée par une fonction utilisant une variable. 

```python
>>>parite = pair_ou_impair(15)
>>> print("le nombre 15 est ", parite)
le nombre 15 est impair
```





​	Question 2 : Combien la fonction `pair_ou_impair` a-t-elle d'argument ? 



#### II. Les exercices. 

**Exercice 1 :** On a écrit le script de la fonction somme_carres

```python
def somme_carres(a,b):
    somme = a**2+b**2
    return somme
```

​	

1. Combien de paramètres cette fonction possède-t-elle ? Le(s)quel(s) ?

2. Que renvoie la fonction somme_carres lorsqu'on tape les instructions suivantes dans le shell:

​	a. somme_carres(5,7)

​	b. somme_carres(4)

**Exercice 2 :** Écrire une fonction solde qui renvoie le prix soldé d'un article lorsque l'utilisateur donne le prix initial et  la remise en pourcentage.

**Exercice 3 :** Le droit d'entrée journalier dans un parc aquatique est de 37€ pour un adulte et 28€ pour un enfant.  

1. Un groupe est formé de $x$ adultes et de $y$ enfants. Quel est le prix payé par le groupe ?
2. Programmer une fonction dont les arguments sont le nombre d'adultes et le nombre d'enfants d'un groupe et qui retourne le prix payé par le groupe à l'entrée de ce parc aquatique.  		

​	

**Exercice 4 :** 

1. Compléter la fonction vitesse ci-dessous pour qu'elle renvoie la vitesse en km/h lorsque l'utilisateur donne une distance en kilomètres et une durée en heure. On rappelle que $vitesse=\frac{distance}{temps}$

   ```python
   def vitesse(........):
   	v = .........
   	return ...........
   ```

   

2. On souhaite utiliser cette fonction dans un programme permettant de tester si le conducteur a dépassé, de manière certaine, la vitesse de 80 km/h.  		

   a. recopier et compléter le programme ci-dessous afin qu'il dise si le conducteur a dépassé la vitesse de 80 km/h.  

   ```python
   a = float(input("donner la distance parcourue en km"))
   b = .....
   v = vitesse(a,b)
   if .......:
       print("Le conducteur a dépassé la vitesse autorisée")
   else: 
       print(................................)
   ```

   ​		

   b. 		Compléter le tableau suivant :

| Distance en km  | 100  | 160  | 90   |
| -------------- | ---- | ---- | ---- |
| Temps en heure | 2    | 1,5  | 0,5  |
| Réponse.       |      |      |      |



​	
