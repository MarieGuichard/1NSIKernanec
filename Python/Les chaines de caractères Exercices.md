# Les chaines de caractères: Exercices. 

**Exercice 1**. 

Ecrire une fonction `affiche(mot)` qui prend en paramètre un mot et qui affiche ses caractères un par un. 

```python
>>>affiche('STOP')
S
T
O
P
```

**Exercice 2:**

Ecrire une fonction `contient(mot,car)`qui prend en paramètre un mot et un caractère et qui renvoie True si le caractère est dans le mot et False sinon. 

```python
>>>contient("STOP","O")
True
>>>contient("STOP","N")
False
```

**Exercice 3:**

Ecrire une fonction `melange(mot,car)`qui prend en paramètre un mot et un caractère `car`et qui renvoie le mot en intercalant le caractère `car`entre chaque caractère du mot. 

```python
>>>melange('Gaston','*')
'G*a*s*t*o*n'
>>> melange("Sophia","-")
"S-o-p-h-i-a"
```

**Exercice 4:**

1. Ecrire une fonction inverse(mot) qui prend en paramètre une chaine de caractères et qui renvoie cette chaîne de caractères en l'inversant. 

   ```python
   >>> inverse("soleil")
   "lielos"
   ```

   

2. En utilisant la fonction inverse() écrite précédemment, écrire une fonction `palindrome(mot)`qui prend en paramètre une chaine de caractères et qui renvoie True si cette chaine de caractères est un palindrome et False sinon. 

   ```python
   >>> palindrome("kayak")
   True
   >>> palindrome("soleil")
   False
   ```

   