## La Machine M999: Les exercices. 

Étudions le fonctionnement de l'assembleur au travers de la machine M999. 

Elle est caractéristique des architectures dites Von Neumann. 

M999 est constitué : 

- d'une mémoire qui contient à la fois les données et le programme,
- d'une unité arithmétique et logique en charge de réaliser les opérations telles que l'addition, comparaison.
- d'une unité de commande -ou unité de contrôle- qui pilote l'ordinateur
- de dispositifs d'entrée-sortie.

![](/ArchitectureMaterielle/IMG/M999.JPG)

#### 1. Mémoire et registres

​	La mémoire est composée de 100 mots mémoire de 3 chiffres (valeur de 000 à 999). Ces 100 mots mémoire sont adressables par des adresses codées sur 2 chiffres. Cette mémoire va contenir données et instructions. Le processeur dispose de deux registres généraux A et B, et d'un registre accumulateur/résultat R. Comme la mémoire, ces registres sont de 3 chiffres, et contiennent donc des valeurs entre 0 et 999.Le processeur dispose aussi d'un registre pointeur d'instruction PC contenant l'adresse mémoire de la prochaine instruction à exécuter. La mémoire et les registres peuvent être matérialisés par une grille de 10*10 et des cases supplémentaires pour les registres A, B, R.Le registre PC peut être matérialisé par un "pion" situé sur une des cases de la grille mémoire.

#### 2. Unité arithmétique et logique. 

L'unité arithmétique et logique est en charge d'effectuer les calculs. Les opérandes et résultats sont dans les registres, A et B pour les opérandes, R pour le résultat.

#### 3. Unité de commande. 

L'unité de commande pilote l'ordinateur.

Son cycle de fonctionnement comporte 3 étapes :

1. charger l'instruction depuis la mémoire pointée par PC. Incrémenter PC.  
2. décoder l'instruction : à partir des 3 chiffres codant l'instruction, identifier quelle est l’opération à réaliser, quelles sont les opérandes.  
3. exécuter l'instruction. 	

#### 4. Jeu d'instruction

*(pour débuter)*

| op0  | op1 op2               | mnémonique | instruction à 			réaliser                           |
| ---- | --------------------- | ---------- | ------------------------------------------------------------ |
| 0    | *addr*                | `LDA`      | copie le mot 			mémoire d’adresse *addr* 			dans le registre A |
| 1    | *addr*                | `LDB`      | copie le mot 			mémoire d’adresse *addr* 			dans le registre B |
| 2    | *addr*                | `STR`      | copie le 			contenu du registre R dans le mot mémoire d'adresse *addr* |
| 3    | - -                   | –          | **opérations 			arithmétiques et logiques**         |
| 3    | 0 0                   | `ADD`      | ajoute les valeurs 			des registres A et B, produit le résultat dans R |
| 3    | 0 1                   | `SUB`      | soustrait la valeur 			du registre B à celle du registre A, produit le résultat dans R |
| 3    | . .                   | etc        | …                                                            |
| 3    | 9 9                   | `NOP`      | ne fait rien                                                 |
| 4    | *rs* 			*rd* | `MOV`      | copie la valeur 			du registre source *rs* 			dans le registre destination *rd*. |
| 5    | *addr*                | `JMP`      | branche en *addr* 			(PC reçoit la valeur *addr*)   |
| 6    | *addr*                | `JPP`      | branche en *addr* 			si la valeur du registre R est strictement positive |

Les registres sont désignés par les valeurs suivantes :

| valeur | registre |
| ------ | -------- |
| 0      | A        |
| 1      | B        |
| 2      | R        |

#### Boot et arrêt

​	La machine démarre avec la valeur nulle comme pointeur d'instruction.

​	La machine stoppe si le pointeur d'instruction vaut 99.

​	On peut donc utiliser le mnémonique `HLT` comme synonyme de `JMP 99`.

#### Entrées/sorties

​	Les entrées/sorties sont "mappées" en mémoire.

​	Écrire le mot mémoire 99 écrit sur le terminal.

​	Les valeurs saisies sur le terminal seront lues dans le mot mémoire 99.


**Exercice 1:**

![](/ArchitectureMaterielle/IMG/M999_exple.jpg)

En utilisant le tableau vu dans le cours, établir ce que fait le programme indiqué dans la machine M999.

**Exercice 2:**

 Etablir ce que fait le programme indiqué dans la machine M999.

![](/ArchitectureMaterielle/IMG/M999_exple.jpg)

**Exercice 3 :** 

a. Écrire un programme M999 qui affiche le minimum de 2 entiers saisis au clavier. 

b. Quelle modification doit-on apporter si on désire saisir 3 entiers ? N entiers ? 



**Exercice 4 :**

 Écrire un programme M999 de calcul du produit de deux entier (on ne dispose pas de l'opération de multiplication). 
