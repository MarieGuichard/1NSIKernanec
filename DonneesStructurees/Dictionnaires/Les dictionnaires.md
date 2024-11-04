# Les dictionnaires. 



## I. Définition (ou presque).



Un dictionnaire ressemble à un tableau. La principale différence est que les indices ne sont pas 	obligatoirement des nombres entiers et peuvent être du type `str`, `float`, `tuple`. Ces indices ne sont pas ordonnés et s'appellent des clés. A chaque clé correspond une valeur. 

En Python, c'est un objet de type `dic`

Pour créer un dictionnaire, nous utiliserons la syntaxe suivante :

```python
Harry = {"Nom":"Potter", "Prenom":"Harry","Age":17,"Animal":"Hedwige"}
```

Un dictionnaire est donc un ensemble de couples clé-valeur. Pour créer un dictionnaire, on écrit entre des accolades les couples séparés par des virgules, chaque couple étant composé d'une clé et de la valeur correspondante séparées par deux points. 

Pour créer un dictionnaire vide, on utilise la syntaxe suivante : 

```python
mondictionnaire_vide={}
```



## II. Utilisation.

#### 1. Accéder à un élément. 	

Pour accéder à un élément, on utilise la clé. De même que pour un tableau, on peut modifier la valeur d'un élément du dictionnaire.  

```python
>>> Harry = {"Nom":"Potter", "Prenom":"Harry","Age":17,"Animal":"Hedwige"}
>>> Harry["Nom"]
'¨Potter'
>>> Harry["Age"]=15
>>> Harry
{"Nom":"Potter", "Prenom":"Harry","Age":15,"Animal":"Hedwige"}
```

​	

Attention, si la clé n'est pas dans le dictionnaire, on obtient alors un message d'erreur. 

​	

De plus, deux méthodes donnent accés soit au clés ou aux valeurs, ce sont les méthodes keys et 	values.

```python
>>> Harry = {"Nom":"Potter", "Prenom":"Harry","Age":17,"Animal":"Hedwige"}
>>> Harry.keys()
dict_keys(['Nom','Prenom','Age','Animal'])
>>> Harry.values()
dict_values(['Potter','Harry',17,'Hedwige'])
```

​	  

Exercice 1 : 

a. Créer le dictionnaire suivant :` LOSC = {'Sport':'Football','Propriétaire':'Merlyn Partners','Stade':'Stade Pierre Mauroy','Classement L1':5}`

b. changer le classement du LOSC. 

c. Afficher la liste de clés du dictionnaire LOSC

d. Afficher la liste de valeur du dictionnaire LOSC.



​	

​	

#### 2. Supprimer un élément. 

On peut supprimer un élément d'un dictionnaire en utilisant la commande del

```python
>>> Harry = {"Nom":"Potter", "Prenom":"Harry","Age":17,"Animal":"Hedwige"}
>>> del Harry["Age"]
>>> Harry
{"Nom":"Potter", "Prenom":"Harry","Animal":"Hedwige"}
```

​	

Exercice 1 : Suite.

e. Supprimer le propriétaire dans le dictionnaire LOSC



#### 3. Ajouter un élément.

Pour ajouter un élément, il suffit  d'affecter un valeur à la variable `dict[clé]`

```python
>>> Harry = {"Nom":"Potter", "Prenom":"Harry","Age":17,"Animal":"Hedwige"}
>>> Harry["Langue"] = "Fourchelangue"
>>> Harry
{"Nom":"Potter", "Prenom":"Harry","Age":17,"Animal":"Hedwige","Langue":"Fourchelangue"}
```

Exercice 1 (suite encore): 

f. Ajouter le nom de l’entraîneur dans le dictionnaire LOSC.



#### 4. Longueur d'un tableau.

Comme pour une chaîne de caractères,un tuple ou un tableau, la fonction **len(dictionnaire)** permet 	d'obtenir la longueur de votre dictionnaire. 



#### 5. La méthode items(). 

La méthode items() renvoie la liste de couple de clés-valeurs d'un dictionnaire. 

```python
 >>> Harry = {"Nom":"Potter", "Prenom":"Harry","Age":17,"Animal":"Hedwige"}
 >>> Harry.items()
 dict_items([('Nom','Harry'),('Prenom','Harry'),('Age',17),('Animal','Hedwige')])
```

​	

#### 6. Appartenance. 

L 'appartenance d'une clé  à un dictionnaire se teste avec l'opérateur in comme pour les dictionnaires. 

```python
>>> Harry = {"Nom":"Potter", "Prenom":"Harry","Age":17,"Animal":"Hedwige"}
>>> "Nom" in Harry
True
>>> "Clan" in Harry
False
```

Il est alors possible d'obtenir la valeur associée à la clé en utilisant la méthode get. 

```python
>>> Harry.get("Nom")
Potter
```

Exercice 1 (encore) :

g. Tester les méthodes items() et get() sur votre dictionnaire. 

#### 7. Parcours. 

Il est possible de parcourir un dictionnaire en utlisant la boucle for. On peut alors itérer soit sur la liste de clé, soit sur la liste de valeurs, soit sur la liste de couple clé-valeur. 

```python
>>> Harry = {"Nom":"Potter", "Prenom":"Harry","Age":17,"Animal":"Hedwige"}
>>> for cle in Harry.keys():
    	print(Harry[Cle])
Potter
Harry
17
Hedwige
```

​	

Exercice 1 (encore et toujours). 

h. Afficher la liste de couple clé-valeur de votre dictionnaire LOSC. 



## III. Construire un dictionnaire.

 #### 1. A partir d'une liste de tuples.

On utilise pour cela la fonction `dict()`

```
>>> liste=[('été','soleil'),('automne','pluie'),('hiver','neige'),('printemps','brouillard')]
>>> meteo = dict(liste)
>>> meteo
('été','soleil'),('automne','pluie'),('hiver','neige'),('printemps','brouillard')
```



#### 2. Construction par compréhension.



On utilise une syntaxe proche de celle utilisée pour les tableaux ; il est juste nécessaire d'indiquer la clé au début. 

```python
>>> dict_carre = { x : x*x for x in range(5)}
>>> dict_carre
{0:0 , 1:1 , 2:4, 3:9 , 4:16}
```



## IV. Exercices.



Exercice 1 : A faire dans le shell. 

Soit le dictionnaire suivant : 	

```python
personne_1 = {'Nom':'Dupont','Prénom':'Sopie','Age': 16}
```



1. Corriger l'erreur dans le prénom Sophie sans toucher au code du dictionnaire. 

2. Afficher la liste de clés de ce dictionnaire.  		

3. Afficher la liste de valeurs de ce dictionnaire.  		

4. Afficher la liste de couple clés-valeurs de ce dictionnaire.  		

5. Ecrire une ligne de commande permettant d'afficher la phrase :  		

   Sophie Dupont est âgée de 15 ans.  		



Exercice 2 : Soit les dictionnaires suivants :

```python
magasin_A={"Pomme":10,"Poire":15,"Fraise":3,"Banane":7}
magasin_B={"Pomme":3,"Poire":5,"Fraise":10,"Banane":15}
```

Écrire une fonction qui prend en paramètres ces deux dictionnaires et qui retourne un dictionnaire ayant les mêmes clés que celles du magasin_A et du magasin_B et qui a pour valeur le nom du magasin pour lequel la valeur est la plus grande. 



Exercice 3 : Soit les dictionnaires suivants :

```python
eleve={"Nom":"Dupont","Prenom":"Jules","Age":17,"Classe":"1G4"}
stagiaire={"Nom":Dupont,"Prenom":"Jules","Fonction":"Developpeur","Salaire":2500}
```



Écrire une fonction qui prend en paramètres ces deux dictionnaires et qui retourne un unique dictionnaire, fusion des deux dictionnaires précédents.  

```python
>>>fusion(eleve,stagiaire:
{"Nom":"Dupont","Prenom":"Jules","Age":17,"Classe":"1G4","Fonction":"Developpeur","Salaire":2500}
```



Exercice 4 : Écrire une fonction stat qui prend en paramètres un texte (type str) et qui renvoie un dictionnaire dont les clés sont les différentes lettres du texte et les valeurs le nombre d’occurrences de chaque lettre. On suppose le texte écrit en lettres capitales non accentuées. 

Attention, le texte contient des caractères de ponctuation et des espaces qu'il ne faut pas comptabiliser. 









​		