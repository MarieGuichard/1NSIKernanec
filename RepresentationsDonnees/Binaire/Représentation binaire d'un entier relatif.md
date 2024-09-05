# Représentation binaire d'un entier relatif. 

#### I. Ajouter deux nombres entiers en représentation binaire.

Dans une machine, on utilise l'écriture binaire pour représenter un entier naturel. Ils sont en 	général codé soit sur 4 octets (soit 32 bits) soit sur 8 octets (soit 64 bits). 

La taille d'un nombre entier est donc limité.

Question 1 : Si l'on décide de coder les entiers sur 4 octets, quel est le plus grand entier que 	l'on peut coder ?



Un ordinateur ne connaissant principalement qu'une opération qui est l'addition, nous allons donc apprendre à additionner deux entiers en binaire. 



Pour des simplifications d'écriture, nous allons utiliser des entiers codés sur 4 bits. 

L'addition se fait comme en base 10 en utilisant un système de retenue	

Exemple :

​		    1  0 0 1             neuf

​	       +   0  1 0 1             cinq

​                =  1  1 1 0	quatorze

​	

Question  2 : En considérant que les entiers sont codés sur 4 bits, effectuer les additions suivantes :

​	a. 0110 + 0111

​	b. 1111 + 0001

​	

Remarque : dans l'exemple précédent, nous remarquons que comme les entiers sont codés sur 4 bits, alors le bit de gauche du résultat de l'addition est perdu. La machine nous dit donc que 15 + 1 vaut zéro !



### II. Une première méthode....que nous ne garderons pas.

Une idée pour représenter les entiers relatifs  en utilisant une représentation binaire  serait  sur un nombre comportant n bits, d'utiliser 1 bit pour représenter le signe et n-1 bit pour représenter la valeur absolue du nombre à représenter. Le bit de signe étant le bit dit "de poids fort" (c'est à dire le bit le plus à gauche), ce bit de poids fort serait à 0 dans le cas d'un nombre positif et à 1 dans le cas d'un nombre négatif. 

Exemple : on représente l'entier 5 sur 8 bits par 00000101, -5 serait donc représenté par 10000101

Question 3 : En utilisant la méthode décrite ci-dessus,

​	a. représenter -15 ( sur 8 bits). 

​	b. représenter 15 ( sur 8 bits). 

​	c. Effectuer  la somme de 15 et de -15 en représentation binaire sur 8 bits. 

​	Quelle remarque pouvez vous faire ? 



Cette méthode de représentation pose donc des problèmes pour effectuer des additions. Nous ne la garderons donc pas.

### III. Le complément à deux. 

Tout d'abord, avant de représenter un entier relatif, il est nécessaire de définir le nombre de bits qui seront utilisés pour cette représentation (souvent 8, 16 , 32 ou 64 bits)

Travaillons avec un exemple : déterminons la représentation de -12 sur 8 bits

- Commençons par représenter 12 sur 8 bits (sachant que pour représenter 12 en binaire seuls 4 bits sont nécessaire, les 4 bits les plus à gauche seront à 0) : 00001100

- Inversons tous les bits (les bits à 1 passent à 0 et vice versa) : 11110011

- Ajoutons 1 au nombre obtenu à l'étape précédente : les retenues sont notées en rouge

  ![](/RepresentationsDonnees/IMG/complement_a_2.jpg)

-  La représentation de -12 sur 8 bits est donc : 11110100

Comment peut-on être sûr que 11110100 est bien la représentation de -12 ?

Nous pouvons affirmer sans trop de risque de nous tromper que 12 + (-12) = 0, vérifions que cela est vrai pour notre représentation sur 8 bits.

​	![](/RepresentationsDonnees/IMG/somme_12.jpg)





Dans l'opération ci-dessus, nous avons un 1 pour le 9e bit, mais comme notre représentation se limite à 8 bits, il nous reste bien 00000000.

Question  4 : En utilisant le complément à 2, représenter -15 (représentation sur 8 bits). 



Il faut noter qu'il est facile de déterminer si une représentation correspond à un entier positif ou un entier négatif : si le bit de poids fort est à 1, nous avons affaire à un entier négatif, si le bit de poids fort est à 0, nous avons affaire à un entier positif.

Question  5: Représentez sur 8 bits l'entier 4 puis représentez, toujours sur 8 bits, l'entier -5. 	Additionnez ces 2 nombres (en utilisant les représentations binaires bien évidemment), 	vérifiez que vous obtenez bien -1.

Question  6 :Quel est le plus petit entier négatif que l'on peut représenter sur 8 bits ?

Question  7 : Quel est le plus grand entier positif que l'on peut représenter sur 8 bits ?



Plus généralement, nous pouvons dire que pour une représentation sur n bits, il sera possible de coder des valeurs comprises entre  $-2^{n-1}$ et $2^{n-1}-1$



####   



​	
