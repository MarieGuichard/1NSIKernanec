# Représentation d'un texte en machine. 



Nous savons qu'un ordinateur est uniquement capable de traiter des données binaires, comment sont donc codés les textes dans un ordinateur ? Ou plus précisément, comment sont codés les caractères dans un ordinateur ?

#### I. Le codage ASCII.

Avant 1960 de nombreux systèmes de codage de caractères existaient, ils étaient souvent incompatibles entre eux. En 1960, l'organisation internationale de normalisation (ISO) décide de mettre un peu d'ordre dans ce bazar en créant la norme ASCII (American Standard Code for Information Interchange). 

À chaque caractère est associé un nombre binaire sur 8 bits (1 octet). En faite, seuls 7 bits sont utilisés pour coder un caractère, le 8e bit n'est pas utilisé pour le codage des caractères. Avec 7 bits il est possible de coder jusqu'à 128 caractères ce qui est largement suffisant pour un texte écrit en langue anglaise (pas d'accents et autres lettres particulières). 

![](D:\DISQUE ESSB\lycee\NSI\les types simples\représentation d'un texte\ascii.jpg)

Comme vous pouvez le constater dans le tableau ci-dessus, au "A" majuscule correspond le code binaire $1   0000001_2$  ou $65_{10}$ ou $41_{16}$. 

Question 1 :

1. A quel texte correspond la série d'octets suivante ?

   43 65 63 69 20 65 73 74 20 75 6E 20 74 65 78 74 65 21  

2. Donner le code, en hexadécimal, correspondant à la phrase: J'aime le Soleil.



Question 2 : ASCII et Python. 

La fonction ord de Python renvoie le code ASCII correspondant à un caractère. L'entier renvoyé est en base 10. On peut alors le convertir en hexadécimal ( avec la fonction hex) ou en binaire (avec la fonction bin). 

```python
>>> ord("A")
65
>>> hex(ord("A"))
'0x41'
>>> bin(ord("A"))
'0b10000001'
```



1. Écrire une fonction prenant en paramètre une chaîne de caractère et retournant un tableau contenant les codes ascii écrits en hexadécimal.  
2. Tester votre fonction sur les exemples de l'exercice précédent.  
3. Tester votre fonction sur l'exemple « ça a déjà été fait ». Que remarquez vous ?  



#### II. Normes ISO 8859.

​	Comme vous avez pu le constater dans l'exercice précédent, les caractères imprimables de la table ASCII se sont vite avérés insuffisants pour transmettre des textes dans des langues autres que l'anglais. En effet, rien qu'en considérant les langues reposant sur l'alphabet latin, il manque dans la table ASCII de nombreux caractères comme les lettres accentuées, les symboles de monnaies, etc...



​	Pour remédier à ce problème, l'ISO (Organisation Internationale de Normalisation) a proposé la norme ISO 8859, une extension de l'ASCII qui utilise les huit bits de chaque octet pour représenter les caractères. Au total, ce sont donc 256 caractères qui peuvent être encodés. Cependant, malgré un nombre de caractères doublé, cela reste insuffisant pour représenter tous les caractères utilisés rien que dans les langues latines. 

​	

​	Pour représenter le plus de caractères possible, la norme ISO 8859 définit plusieurs tables de correspondance notées 8859-n, où n est le numéro de la table. Bien qu'indépendantes les unes des autres, ces tables ont été conçues pour qu'elles soient compatibles entre-elles. Les premiers 128 caractères sont ceux de la norme ASCII. Les 128 suivants sont ceux spécifiques à la table n. De plus les caractères identiques ont le même code. 



La norme 8859 compte 16 tables en tout. 

| Code 		ISO           | Zone                                        |
| -------------------------- | ------------------------------------------- |
| 8859-1 		(latin-1)   | Europe 		occidentale                  |
| 8859-2 		(latin-2)   | Europe 		centrale ou de l'est         |
| 8859-3 		(latin-3)   | Europe 		du sud                       |
| 8859-4 		(latin-4)   | Europe 		du nord                      |
| 8859-5                     | Cyrillique                                  |
| 8859-6                     | Arabe                                       |
| 8859-7                     | Grec                                        |
| 8859-8                     | Hébreu                                      |
| 8859-9(latin-5)            | Turc, 		Kurde                         |
| 8859-10 		(latin-6)  | Nordique 		(réarrangement du latin-4) |
| 8859-11                    | Thaï                                        |
| 8859-12                    | Devanagri 		(projet abandonné)        |
| 8859-13                    | Balte                                       |
| 8859-14 		(latin-8)  | Celtique                                    |
| 8859-15 		(latin-9)  | Révision 		du latin-1 (avec €)        |
| 8859-16 		(latin-10) | Europe 		du sud-est                   |



Question 3 :Quelle table utilisera une personne originaire de :

1. Marcq en Baroeul ?
2. Athénes ?  
3. Tunis ?  



​	Cependant, il existe beaucoup d'autres langues dans le monde qui n'utilisent pas l'alphabet dit "latin", par exemple le chinois ou le japonais ! D'autres normes ont donc dû voir le jour, par exemple la norme "GB2312" pour le chinois simplifié ou encore la norme "JIS_X_0208" pour le japonais. 

​	Cette multiplication des normes a très rapidement posé problème. Imaginons un français qui parle le japonais. Son traitement de texte est configuré pour reconnaître les caractères de l'alphabet "latin" (norme ISO-8859-1). Un ami japonais lui envoie un fichier texte écrit en japonais. Le français devra modifier la configuration de son traitement afin que ce dernier puisse afficher correctement l'alphabet japonais. S'il n'effectue pas ce changement de configuration, il verra s'afficher des caractères ésotériques. 





#### III. Unicode.

​	Pour éviter ce genre de problème, en 1991 une nouvelle norme a vu le jour : Unicode

​	Unicode a pour ambition de rassembler tous les caractères existant afin qu'une personne utilisant Unicode puisse, sans changer la configuration de son traitement de texte, à la fois lire des textes en français ou en japonais

​	Unicode est uniquement une table qui regroupe tous les caractères existant au monde, il ne s'occupe pas de la façon dont les caractères sont codés dans la machine. 

​	Cette norme associe à chaque caractère (lettre, nombre, idéogramme, …) un nombre unique. Ce nombre est appelé le **point de code** du caractère. 

​	Il y a aujourd'hui plus de 110 000 caractères recensées dans cette norme, qui est conçue pour contenir les caractères de n'importe quelle langue. La capacité maximale de la norme a été fixée à 4 294 967 295 caractères, c'est à dire le plus grand entier non signé représentable sur 32 bits.

Par souci de compatibilité, les 256 premiers points de code sont ceux de la norme ISO-8859-1 (latin-1). 



​	Unicode accepte plusieurs systèmes de codage : UTF-8, UTF-16, UTF-32. Le plus utilisé, notamment sur le Web, est UTF-8. 

​	Pour encoder les caractères Unicode, UTF-8 utilise un nombre variable d'octets : les caractères "classiques" (les plus couramment utilisés) sont codés sur un octet, alors que des caractères "moins classiques" sont codés sur un nombre d'octets plus important (jusqu'à 4 octets). Un des avantages d'UTF-8 c'est qu'il est totalement compatible avec la norme ASCII : Les caractères Unicode codés avec UTF-8 ont exactement le même code que les mêmes caractères en ASCII. 

Le principe de l'encodage UTF-8 est le suivant : 

- ​	si le bit de poids fort d'un octet est à 0, alors il s'agit d'un caractère ASCII codé sur les 7 bits restant.

- ​	Sinon, les premiers bits de poids fort de l'octet indiquent le nombre d'octets utilisés pour encoder le caractère à l'aide d'une séquence de bits à 1 et se terminant par un bit à 0.  

  ​	Par exemple, si le premier octet commence par 110xxxxx, cela signifie que le caractère est codé sur 2 octets, puisqu'il commence par une séquence de deux bits de poids fort à 1 suivi d'un 0.  

- ​	Enfin, dans le cas d'un encodage sur k octets, les k-1 octets de poids fort doivent tous être de la forme 10xxxxxx.  

Nous pouvons résumer cela dans le tableau suivant :

![](D:\DISQUE ESSB\lycee\NSI\les types simples\représentation d'un texte\unicode.jpg)

Question 4 : En utilisant la norme UTF-8, donner le nombre binaire associé à :

1. ​	b
2. ​	à (code hexadécimal : E0)
3. ​	€ (code hexadécimal : 20AC)