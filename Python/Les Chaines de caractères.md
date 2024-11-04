# Python: Les Chaines de caractères. 



#### I. Définition. 

Une donnée de type string peut se définir comme une suite quelconque de caractères. 

Dans un script, on peut délimiter une telle suite de caractères, soit par des apostrophes, soit par des guillemets. 

```python
>>> phrase1="J'aime la NSI,"
>>> phrase2= ' et le chocolat aussi.'
>>> print(phrase1,phrase2)
J'aime la NSI, et le chocolat aussi.
```

#### II. Opérations élémentaires sur les chaines de caractères. 

##### 1. La concaténation. 

L'opétateur `+` permet d'assembler plusieurs chaines de caractères pour en construire de plus grandes.  Cette opération s'appelle la concaténation. 

```python
>>> phrase1="J'aime la NSI,"
>>> phrase2= ' et le chocolat aussi.'
>>> phrase3= phrase1+phrase2
>>> phrase3
"J'aime la NSI, et le chocolat aussi.""
```

#### 2. La longueur. 

La fonction `len()`permet de déterminer la longueur (c'est à dire le nombre de caractères) d'une chaîne. 

```python
>>> phrase1="J'aime la NSI,"
>>> len(phrase1)
14
```



#### 3. Conversion. 

Il est possible de convertir un int ou un float en str. Il faut pour cela utiliser la fonction `str()`. 

```python
>>> val = 123
>>> val
123
>>> nvval=str(val)
>>>nvval
'123'
```

#### III. Accès au caractères individuels. 

Une chaîne de caractères est constituée de caractères. 

Pour accéder à un caractère bien déterminé, on utilise le nom de la variable qui contient la chaîne de caractères et on lui accole , entre deux crochets, l'index numérique qui correspond à la position du caractère dans la chaîne. 

Attention, la numérotation des index commence à zéro. Ainsi, le premier caractère de la chaîne a pour index 0. 

```python
>>> phrase1="J'aime la NSI,"
>>> phrase1[0]
'J'
>>>phrase1[1]
'''
>>>phrase1[2]
'a'
```

