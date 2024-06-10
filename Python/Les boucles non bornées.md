# Les boucles non bornées.

### I. Les instructions.

Pour écrire certains programmes, il est parfois nécessaire de répéter une ou plusieurs instructions un nombre inconnu de fois. Lorsque le nombre de répétitions n'est pas connu à l'avance, on utilise une boucle non bornée qui est parcourue jusqu'à ce qu'une certaine condition ne soit plus vérifiée. Tant que cette condition est vérifiée, la boucle continue. 

Dans un algorithme, on utilise :

​	**Tant que** condition **faire**

​		instruction(s)

La traduction en langage python est la suivante :

​	**while** condition :

​		instruction(s)



Question 1 : 

1. Recopier le programme ci-dessous.

   ```python
   s=10000
   i=0
   while s>5000:
   	i = i + 1
   	s = s*0.95
   print(i)
   ```

   

2. Exécuter ce programme, qu'affiche-t-il ?
3. Quelle condition doit être vérifiée afin que la boucle s’exécute 
4. Combien de fois la boucle a-t-elle été éxécutée ?  
5. Remplacer la condition par s>3000 ? Qu'affiche alors le programme une fois exécuté ?
6. Remplacer la condition par s<5000 ? Qu'affiche alors le programme une fois exécuté ?Comment pouvez vous expliquez ce résultat ?
7. Remplacer la condition par s<15000 ? Que se passe-t-il ? Comment pouvez vous expliquer ce phénomène ? 
8. A quoi doit-on être vigilant lorsque l'on écrit un programme qui utilise une boucle while ?



#### II. Les exercices.

**Exercice 1 : **

```python
n=1
s=0
while s<1000:
	n= n+1
	s = s + n**2
print("le plus petit entier naturel n tel que la somme des carrés soit inférieure à 1000 est ",n)
```

1. Que fait le programme ci-dessus ?
2. Expliquer l'utilité de la variable n.  
3. Que se passe-t-il si on inverse les deux exécutions de la boucle ?
4. Modifier le script de manière à obtenir le plus petit entier n tel que la somme des cubes soit inférieur à 3000. Afficher la somme ainsi que l'entier n.  



**Exercice 2 :** Dans une petite ville, on constate depuis quelques années une hausse annuelle de 5% du prix des loyers. Cette année, le prix moyen de location du mètre carré est 8€. 

1. Quel sera le prix de location du mètre carré dans un an ?

2. On souhaite déterminer dans combien d'années le prix moyen de location du mètre carré dépassera 12€.  

   Écrire un programme  permettant de répondre à cette question.  



**Exercice 3:** On place un grain de blé sur la 1ere case d'un échiquier, deux grains de blés sur la deuxième case, quatre sur la troisième, et ainsi de suite en doublant la quantité de grains à chaque case. 

Sachant que je possède Q grains de blé, combien de cases vais-je pouvoir remplir ? 

1. Écrire un programme  pour répondre à cette question.
2. Exécuter le programme pour compléter le tableau ci-dessous.

| Q               | 20   | 100  | $10^3$ | $10^6$ |
| --------------- | ---- | ---- | ------ | ------ |
| Nombre de cases |      |      |        |        |



**Exercice 4 :** 

Écrire un programme qui demande un entier, et qui affiche ‘premier’ si le nombre est premier, ‘non premier’ sinon. 

Rappel: un nombre est un nombre premier s'il n'est divisible que 1 et par lui même. 