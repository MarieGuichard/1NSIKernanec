# Les booléens.



 A partir de 1847, le britannique George Boole propose un mode de calcul permettant de traduire des raisonnement logiques par des opérations algébriques. Il crée ainsi une branche des mathématiques qui définit des opérations dans un ensemble qui ne contient que deux éléments notés 0 et 1, ou bien False et True (pour faire le lien avec la logique), ou bien Ouvert et Fermé (lien avec l'électronique).  Celle-ci s'appelle **l’algèbre de Boole**.

En 1938, l'Américain Claude Shannon prouve que des circuits électriques peuvent résoudre tous les problèmes que l’algèbre de Boole peut résoudre. Avec les travaux d'Alan Turing de 1936, cela constitue les fondements de ce que deviendra l'informatique. 

**Définition : Un booléen est un type de variable à deux états, généralement nommés vrai et faux, et représentés respectivement par 1 et 0.**

En Python, on peut déclarer un booléen directement par sa valeur : « True » (pour vrai) et « False » (pour faux). 

Par exemple : 

```python
>>> operateur = True
>>> test = False
```

#### I. Les opérations fondamentales.



Soit A et B deux booléens. 	



##### 1. L'opérateur **Not** (ou la négation).  		

 L'opérateur **not** retourne le booléen opposé.  		

Nous avons la table de vérité suivante :

| A     | not A |
| ----- | ----- |
| True  |       |
| False |       |



Une table de vérité récapitule dans un tableau les valeurs de vérité de la sortie en fonction des valeurs de vérité des entrées. 

Exemple : 

```python
>>> test = False
>>> not test
True
```



##### 2. L'opérateur and (ou la conjonction).

L'opérateur **and** permet de tester si deux booléens sont vrais.  



Nous avons la table de vérité suivante :

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  |         |
| True  | False |         |
| False | True  |         |
| False | False |         |



Question 1: Qu'affiche le code suivant ? 

```python
note = 13
mention_AB = (note>=12)and(note<14)
print(mention_AB)
```

​		

#### 3. L'opérateur or (ou la disjonction).  		

L'opérateur **or** permet de tester si l'un des deux booléens au moins est vrai.  		

Nous avons la table de vérité suivante :

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  |        |
| True  | False |        |
| False | True  |        |
| False | False |        |

Question 2: Qu'affiche le code suivant ?  

```python
note = 18
note_extreme = note<15 or note>15
print(not_extreme)
```

#### II. Les lois de l'algèbre de Boole. 

##### 1. Priorité. 

Le and est prioritaire sur le or. Il est également possible d'utiliser des parenthèses. 

Question 3: Ecrire les tables de vérité des expressions suivantes:

a. not(A and not(B))

| A     | B     | not B | A and not B | not (A and not(B)) |
| ----- | ----- | ----- | ----------- | ------------------ |
| True  | True  |       |             |                    |
| True  | False |       |             |                    |
| False | True  |       |             |                    |
| False | False |       |             |                    |

b. A or (B and not C)

| A    | B    | C    | not C | B and not C | A or (B and not C) |
| ---- | ---- | ---- | ----- | ----------- | ------------------ |
|      |      |      |       |             |                    |
|      |      |      |       |             |                    |
|      |      |      |       |             |                    |
|      |      |      |       |             |                    |
|      |      |      |       |             |                    |
|      |      |      |       |             |                    |
|      |      |      |       |             |                    |
|      |      |      |       |             |                    |

##### 2. Quelques propriétés.  



​	La **commutativité** : l'ordre n'a pas d'importance. 

​	A and B = B and A

​	A or B = B or A

​		

​	La **distributivité** : comme dans les opération mathématiques, il est possible de distribuer :

​	A or (B and C) = (A or B) and (A or C)

​	A and (B or C) = (A and B) or (A and C)

​	**Idempotence :**

​	Compléter les tables de vérités suivantes, puis en déduire une égalité logique :

​	

| A     | A     | A and B | A or B |
| ----- | ----- | ------- | ------ |
| True  | True  |         |        |
| False | False |         |        |

​	A and A = 

​	A or A = 



​	**Règle de Morgan:**

​	 Compléter les tables de vérités suivantes, puis en déduire une égalité logique :

​	

| A     | B     | A and B | not (A and B) |
| ----- | ----- | ------- | ------------- |
| True  | True  |         |               |
| True  | False |         |               |
| False | True  |         |               |
| False | False |         |               |

| A     | B     | not A | not B | not A or not B |
| ----- | ----- | ----- | ----- | -------------- |
| True  | True  |       |       |                |
| True  | False |       |       |                |
| False | True  |       |       |                |
| False | False |       |       |                |

Conclusion:
 


#### III.  les fonctions composées.

Toutes les opérations booléennes peuvent s'écrire en n'utilisant que les trois opérateurs and, or et not. Mais en pratique, on utilise aussi d'autres fonctions logiques, qui s'obtiennent à partir des opérations fondamentales.  



##### 1. la fonction xor (ou exclusif).

A xor B = (A and not B) and (not A and B)

Compléter la table de vérité suivante de manière à obtenir A xor B dans 		la dernière colonne.  		

Que fait la fonction xor ?  		

| A     | B     |      |      |      |      |      |
| ----- | ----- | ---- | ---- | ---- | ---- | ---- |
| True  | True  |      |      |      |      |      |
| True  | False |      |      |      |      |      |
| False | True  |      |      |      |      |      |
| False | False |      |      |      |      |      |

​	

##### 2. La fonction nand (non et ).

A nand B = not (A and B)

##### 3. La fonction nor (non ou). 

A nor B = not (A or B)		



#### IV. Circuits logiques.

On appelle circuit logique (ou circuit combinatoire) un ensemble de portes logiques reliées entre elles pour répondre à une expression algébrique.

On utilise des symboles pour représenter les différents opérateurs :

![](/RepresentationsDonnees/IMG/ciricuit_logique2.jpg)

​	![](/RepresentationsDonnees/IMG/circuitlogique1.jpg)



​	Exemple :

![](/RepresentationsDonnees/IMG/circuitlogiqueex.JPG)

1. compléter avec les expressions manquantes.
2. Quelle expression représente le schéma complet ?  



#### V. Application : l'addition binaire.



Nous allons construire le circuit logique qui correspond à l'addition en binaire. 

1. Compléter la table de vérité suivante :

   S correspond à la somme de A et B et R à la retenue.

   0 correspond à False et 1 à True.   		

​	

| A    | B    | S    | R    |
| ---- | ---- | ---- | ---- |
| 0    | 0    |      |      |
| 0    | 1    |      |      |
| 1    | 0    |      |      |
| 1    | 1    |      |      |



2. A quelle opérateur correspond R et S.

​	R =

​	S =  	

3. Construire le circuit logique permettant d'obtenir R et S.





