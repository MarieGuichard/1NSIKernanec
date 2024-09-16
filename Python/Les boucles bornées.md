# Les boucles bornées.

#### I. Les boucles.

Un des intérêts des programmes informatiques est de faire faire un ordinateur des calculs longs et répétitifs plutôt que de les faire à la main. 	

Pour cela, il faut utiliser une boucle. 

Une boucle est un ensemble d'instructions qui seront répétées autant de fois que nécessaire.

On distingue deux types de boucles :

- les boucles bornées : le nombre de fois où les instructions doivent être répétées est connu au préalable.
- Les boucles non bornées : le nombre de fois où les instructions doivent être répétées n'est pas connu et les instructions sont répétées tant qu'une condition est vérifiée.  	

​	

Dans ce chapitre, nous traiterons des boucles bornées. 



#### II. Les boucles bornées.

Lorsque le nombre de répétition d'une boucle est connu à l'avance, dans les algorithmes,  on utilise une boucle bornée avec l'instruction **pour** en précisant le nombre de répétition.  		

​	

**Pour** variable **allant de** minimum **à** maximum

​	instruction(s)



La traduction en langage python est la suivante :

​	**for** variable **in** range() :

​		instruction(s)



Tout comme pour le if, il ne faut pas oublier les : aprés la ligne for ainsi que l'indentation pour les instructions.



Question 1 :

1. Copier le programme suivant :

   ```python
   for i in range(10):
   	print("la valeur de i vaut", i)
   print("Le programme est terminé")
   ```

2. Exécuter ce programme. Qu'affiche-t-il ?

3. quoi semble servir l'instruction range(10) ? 		

#### III. La fonction range().

Avec les boucles **for,** on fait réguliérement appel à la fonction **range()**. Celle-ci permet d'énumérer le nombre de passages dans la boucle bornée. On peut l'utiliser de différentes façons :

- range(n), où n est un entier :  fait prendre à la variable toutes les valeurs entières de 0 à n-1, soit n valeurs au total.
- range(n,m), où n et m sont des entiers : fait prendre à la variable toutes les valeurs entières de n à m-1.
- range(n,m,k) où n, m et k sont des entiers : fait prendre toutes les valeurs entières de n à m-1 avec un pas de k.  		



​	Question 2 : Quelle instruction permet d'énumérer les entiers :

- de 0 à 15 :  
- de 5 à 10 :
- 0-10-20-....-90-100 : 	



#### IV. Les exercices.

**Exercice 1** : On souhaite placer une somme sur un compte bancaire. Celui-ci est  rémunéré à 2,5% chaque année. On souhaite connaître la somme disponible dix ans plus tard. 

1. Soit la somme de 100€, par combien faut-il la multiplier afin qu'elle subisse une hausse de 2,5% ?

2. Soit une somme de x €, par combien faut-il la multiplier afin qu'elle subisse une hausse de 2,5% ?

3. Compléter le programme  ci-dessous pour qu'il réponde à la question.

   ```python
   c = int(input("la soomme placée est:"))
   for i in range(....):
       c = .....
   print("Dans 10 ans, vous aurez", c, "euros")
   ```

   

4. Dans dix ans, quelle somme aurez vous si vous avez placé 5000€ ? 12000€ ?  



**Exercice 2 : **

1. Écrire un programme qui affiche la table de multiplication de cinq comme ci-dessous. 

![](/Python/IMG/table_multiplication.jpg)

2. Modifier votre programme afin que l'utilisateur puisse demander la table de multiplication qu'il souhaite.
3. Modifier votre programme pour que l'utilisateur puisse demander une amplitude différente sur la table de multiplication (par exemple, il pourrait demander la table de 7 entre 4 et 13).  



Exercice 3 : Soit  la fonction définie sur ℝ par $f(x)=3x²-5x+1$. Écrire un script permettant de compléter le tableau de valeurs ci-dessous : 

| $x$    | 5    | 10   | 15   | 20   | 25   | 30   | 35   | 40   |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| $f(x)$ |      |      |      |      |      |      |      |      |



**Exercice 4 :** La comète Tchouri est passée dans notre système solaire pour la dernière fois en 2015. Elle a une période de révolution de 7 ans, ce qui signifie qu'elle repassera dans notre système solaire en 2022, 2029, ….

La comète Encke qui est passée pour la dernière fois en 2017, a  une période de révolution de 3 ans. On cherche à déterminer en quelle année, au plus tôt, les deux comètes Tchouri et Encke traverseront simultanément notre système solaire. 

1. On appelle a le nombre de révolutions de la comète Tchouri et b le nombre de révolutions de la comète Encke. Écrire l'équation que doit vérifier a et b pour que les deux comètes traversent le système solaire la même année.
2. Copier le script ci-dessous dans votre éditeur et compléter le de sorte qu'il réponde à la question posée.
   '''
   for a in range(10):
      for b in range(10):
         if ......
  '''

4. Exécuter ce programme et en déduire la prochaine année de rencontre de ces deux comètes dans le système solaire.
