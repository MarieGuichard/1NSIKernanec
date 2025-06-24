# Les instructions conditionnelles.

### I. La syntaxe.

Exemple : S'il fait beau,alors je vais au lycée en vélo, sinon je prends le bus. 



Nous sommes face à une instruction conditionnelle : 

Il y a une condition : « il fait beau » et deux exécutions différentes : « je vais au lycée en vélo »  et « je prends le bus » selon le fait que la condition soit vérifiée ou non.



Les mots clés sont si, alors, sinon. 

Nous utiliserons les mêmes dans un algorithme. 

En effet, pour aiguiller dans différentes directions l’exécution d'un programme, il est possible d'avoir recours à des instructions conditionnelles qui permettent de déterminer si les instructions qui suivent doivent être, ou non, exécutées. 

En Python, les mots clés à utiliser sont **if , else, elif** (c'est la contraction de else et if).

Attention, cela nécessite certaines précautions. 

Tout d'abord, il faut mettre **:** aprés le if et le else. 

Ensuite, il ne faut pas oublier d'**indenter** (c'est à dire de décaler en utilisant la touche ->| ) pour signaler les instructions à exécuter après le if et le else. 

Question 1 :

1. Copiez le code suivant dans la partie supérieure de Thonny. 

   ```python
   age = int(input("Quel age as-tu ?"))
   if age < 18 :
   	print("Tu es mineur")
   else:
   	print("Tu es majeur")
   ```

   

2. Exécutez le code avec 14. Qu'obtenez vous ?

3. Exécutez le code avec 22. Qu'obtenez vous ?



Question 2 :

1. Écrire un algorithme qui demande à l'utilisateur un nombre,lui renvoie le double de ce 		nombre si le nombre est strictement inférieur à 10 et lui renvoie le nombre divisé par deux sinon.
2. Tester votre code avec 18 et 6.  		



#### II.  Opérateurs de comparaison.

Les conditions évaluées après l’instruction *if*  peuvent être de différentes natures.

Les opérateurs de comparaison les plus courants sont :

| x ==y | #   x est égal à y              |
| ----- | ------------------------------- |
| x !=y | #   x est différent de y        |
| x>y   | #   x est plus grand que y      |
| x<y   | #   x est plus petit que y      |
| x>=y  | #   x est supérieur ou égal à y |
| x<=y  | #   x est inférieur ou égal à y |

Il est également possible de combiner les conditions en utilisant les mots **and** et **or**. 

### III. Les exercices.

**Exercice 1 :** Écrire un  programme qui demande à l'utilisateur de choisir un nombre, qui affiche gagné si ce nombre est 15 et perdu sinon.



**Exercice 2:** Écrire un programme qui demande à l'utilisateur son nom et son genre (M, F, I). En fonction de ces données, afficher "Cher Monsieur" , "Chère Madame" ou "Cher.e Ami.e" suivi du nom de l'utilisateur. 

Remarque : Attention M ou F est une chaîne de caractère.



**Exercice 3 :** Écrire un programme demande la température extérieure à l'utilisateur et qui lui conseille de mettre soit des bottes, soit des baskets, soit des sandales en fonction de la température (je vous laisse décider des seuils). 



**Exercice 4 :** Écrire un programme qui demande à l'utilisateur d'entrer les trois longueurs d'un triangle, qui  qui indique si le triangle est isocèle, équilatéral ou quelconque. 
