# Représentation approximative des nombres réels :exercices.



**Exercice 1 :** représenter en binaire les nombres décimaux suivants, indiquer si cela est une représentation exacte ou non. 

a. $\frac{1}{3}$		b. 3,625	c. $\frac{75}{16}$		d. $\frac{101}{8}$ 		e. 12,65625





**Exercice 2 :** Le microcontrôleur de l'antimissile Patriot stocke la valeur  $\frac{1}{10}$ en ne conservant que 23 bits pour la partie décimale. 

1. Écrire $\frac{1}{10}$ en binaire, en conservant au moins 30 chiffres après la virgule.  
2. Sachant que les registres du Patriot ne conservent que 23 bits après la virgule, quelle est, en base 10, la valeur codée effectivement à la place de $\frac{1}{10}$ ?  
3. Quelle est l'erreur approximative commise sur la représentation de  $\frac{1}{10}$?
4. Combien de signaux d'horloge le Patriot reçoit-il en 100h de fonctionnement ?
5. En tenant compte de l'erreur calculée à la question 3, quel est le décalage de l'horloge du Patriot par rapport à l'heure réelle au bout de 100 heures.  
6. Sachant qu'un missile se déplace à une vitesse d'environ 1676 m/s, à quelle erreur de position en mètres correspond le décalage d'horloge d'un Patriot ayant fonctionné 100 heures sans interruption ?
7. Conclure, sachant que, pour atteindre sa cible, un Patriot doit l'approcher à moins de 500 m.  



**Exercice 3:** Codage d'un flottant.

Écrire une fonction qui détermine et renvoie le codage d'un flottant en base dix. L'entrée en paramètre est de typle float et la sortie de type str. On utilise le codage sur 32 bits. 

Voici les différentes étapes :

1. le paramètre de la fonction, de type float, représente un nombre$x$ .

2. Le signe de $x$  est déterminé et stocké dans s='0' ou s='1' puis  est changé en .  

3. Calcul de l'exposant et de la mantisse. Vous utiliserez l'algorithme suivant. 

    si $x>=2$ ,

   ​	 effectuer des divisions par 2 successive, 

   si $x<1$ ,

   ​	 effectuer des multiplications par 2 successives, en remplaçant à chaque fois la valeur de  par le résultat obtenu, et dans les deux cas jusqu'à obtenir un nombre $x$ tel que $1<=x<2$. 

   L'exposant est alors le nombre de divisions ou de multiplications effectuées et la mantisse est le nombre  final.  

4. Calcul de l'exposant décalé qui est codé en binaire sur 8 bits. Le résultat est stocké dans une chaîne e.  

5. Calcul de la mantisse tronquée $x=x-1$ qui doit être écrite en binaire sur 23 bits et stockée dans une chaîne m. Pour cela, multiplier$x$  par 2 ; si $x>=1$ , ajouter '1' à m et retrancher 1 à , sinon, ajouter '0' à m ; reproduire ce schéma 23 fois.  

6. La chaine s+e+m est renvoyée.  
