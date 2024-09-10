# Les Booléens : Exercices.



**Exercice 1:** Dans chacun des cas suivants, donner la valeur du booléen rep.

1. ```python
   x = 3 
   rep = x**2 == -9
   ```

2. ```python
   x,y,z = 3,4,5
   rep = x**2+y**2=z**2
   ```

3. ```python
   a, b = 3,-7
   rep = a**3>50 and b**2<50
   ```

4. ```python
   a,b = 3,-7
   rep = (a**3>50 and b**2<50)or (a**2<10 and b**2>10)
   ```

   

**Exercice 2 :** Montrer  l'égalité suivante :

(A and B)or(not B and C) = (A or not B ) and (B or C)



**Exercice 3 :** Définir une fonction booléenne  sur deux variables A et B qui vaut 1 si et seulement si deux variables ont la même valeur, en utilisant uniquement les opérations not, and et or.  

Donner sa table de vérité.



**Exercice 4:** On considère la fonction booléenne à trois variables suivantes :

f(A,B,C) = (A and notB and not C)or (not A and B and not C)or(not A and not B and C)

1. Donner sa table de vérité.
2. Que fait cette fonction ?  
3. En utilisant le xor, donner une expression booléenne plus simple de cette fonction.  



**Exercice 5 :** Additionner des couleurs. 

Sur un écran, les couleurs sont créées en mélangeant du rouge, du vert et du bleu, c'est la synthése additive des trois couleurs. On imagine un dispositif dans lequel trois lampes de chacune de ces couleurs sont dirigées vers le même endroit et peuvent être allumées ou éteintes. 

1. Justifier que l'on ne peut pas créer plus de 8 couleurs différentes dont les noms et les codes binaires sont donnés ci-contre.

| Couleur | R    | V    | B    |
| ------- | ---- | ---- | ---- |
| Noir    | 0    | 0    | 0    |
| Bleu    | 0    | 0    | 1    |
| Vert    | 0    | 1    | 0    |
| Cyan    | 0    | 1    | 1    |
| Rouge   | 1    | 0    | 0    |
| Magenta | 1    | 0    | 1    |
| Jaune   | 1    | 1    | 0    |
| Blanc   | 1    | 1    | 1    |

1. Le complément d'une couleur est obtenu en allumant les lampes éteintes et en éteignant les lampes allumées.

   Déterminer les couleurs complémentaires des huit couleurs précédentes.  

2. Quelle est la couleur obtenue en effectuant les opérations suivantes :

   Bleu or Rouge

   Magenta  andCyan  

​	vert and  Blanc
