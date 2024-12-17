# Le modèle de von Neumann.



### I. Les composants d'un ordinateur.  

Exercice 1:  

Visionner la vidéo suivante : [https://pixees.fr/demonter-un-ordinateur/](https://www.youtube.com/watch?v=Fk2kYo2E61A) , observer votre ordinateur et répondre aux questions suivantes. 

1. Quels sont les différents types de périphériques ? Citer des exemples ainsi que leurs utilités. 

2. citer des ports de connexion externe ainsi que leur utilité.

3. Sur quoi est branché l'écran ? 
4. Sur quoi sont branchés le clavier et la souris ?
5. Sur quoi sont reliés les périphériques internes ? 

6. Quelles sont les différents types de mémoire existant ? 

7. quel est le « cœur » de l'ordinateur ? 
8. De quoi est constitué un processeur ? 

​	

### II. La mémoire.

La mémoire peut être représentée par un tableau dans lequel seront stockés aussi bien les variables que les programmes. Chaque cellule de ce tableau possède une adresse X et la valeur de chaque cellule est notée M[X]

Nous distinguerons différents types de mémoire:

- La ROM (Read Only Memory) ou mémoire morte: elle désigne une mémoire informatique non volatile dont le contenu est fixé lors de sa programmation, qui pouvait être lue plusieurs fois par l'utilisateur, mais ne pouvait plus être modifiée. 

  Elle est utilisée, entre autres, pour stocker les informations nécessaires au démarrage d'un ordinateur (BIOS, instructions de démarrage). 

  Le temps d'accès à la mémoire morte est de l'ordre de grandeur de 150 nanosecondes

- La RAM (random-access memory) ou mémoire vive: elle se présente le plus souvent sous forme de barrettes que l'on peut retirer ou ajouter dans un ordinateur. Son rôle est notamment de stocker les données qui vont être traitées par l'unité centrale de traitement (UCT) (un microprocesseur dans la plupart des appareils modernes). On peut accéder à la mémoire vive alternativement en lecture ou en écriture.

  ![](/ArchitectureMaterielle/IMG/RAM_n.jpg)

  Le temps d'accès à la mémoire vive est de l'ordre de quelques dizaines de nanosecondes. 

- La mémoire flash: la mémoire flash est une forme de stockage de données utilisée par certains supports comme une carte mémoire ou un disque SSD. De plus en plus répandue, on la retrouve dans les clés USB, les smartphones, les appareils photo, et les ordinateurs portables. Elle est plus performante en termes d'accès par rapport à un disque dur mécanique, mais elle n'atteint pas la rapidité de la mémoire vive. Elle se distingue de cette dernière par sa capacité à conserver les données enregistrées quand l'appareil s'éteint. 

- La mémoire externe (de masse): ce sont les disques durs, clés USB, ….elle sert à stocker des 	documents, des programmes. Elle est non volatile.  

​	

### III. L'architecture de Von Neumann.



#### 1. Structure générale.



L'architecture des ordinateurs actuels repose sur le modèle de Von Neumann. 

Exercice 2: Ecrire une brève biographie de John Von Neumann. 

Si vous souhaitez avoir davantage d'information à propos de John Von Neumann, vous 	pouvez visionner la vidéo suivante : https://www.youtube.com/watch?v=c9pL_3tTW2c

​	

L'idée essentielle de Von Neumann est que la mémoire doit servir non seulement à stocker des données mais aussi les programmes. 

Une machine doit s'organiser avec une mémoire, une unité arithmétique et logique (dite UAL), une unité de contrôle, des systèmes d’entrées sorties et une horloge pour synchroniser le fonctionnement. Les différents éléments échangent des informations à l'aide de bus. 

![](/ArchitectureMaterielle/IMG/archi_VN.jpg)

L'UAL et l'unité de contrôle sont regroupés dans le processeur qui communiquent avec la 	mémoire par un bus. Ces composants constituent l'unité centrale, située sur la carte mère 	d'un ordinateur.  Le tout est rythmé par une horloge interne qui détermine la fréquence du 	processeur. 

​	

Exercice 3: Répondre aux questions suivantes

1.  Que signifie le fait que le processeur Intel Core i7-9700K soit cadencé à 4,9GHz ?
2. Que s'est-il passé pour la fréquence des processeurs jusque 2004 ? Et ensuite ? Comment pouvez vous l'expliquer ? 		 		



#### 2. Unité arithmétique et logique.



​	L'unité arithmétique et logique est le cœur de l'ordinateur. 

​	On la représente habituellement par ce schéma : 

![](/ArchitectureMaterielle/IMG/UAL.jpg)



​	

​	A et B sont les opérandes (les entrées)

​	R est le résultat

​	F est une fonction binaire (l'opération à effectuer)

​	D est un drapeau indiquant un résultat secondaire de la fonction (signe, erreur, division par 	0, ….) 



​	Les opérations que peuvent réaliser une UAL de base sont :

​	- les additions, soustractions, multiplications et divisions.

​	- Les opérations logiques (et, ou, non)

​	- les opérations de comparaison.  	



​	Un même processeur peut comporter plusieurs UAL. Dans certaines architectures, les UAL sont 	spécialisées et ne fonctionnent pas simultanément, dans d'autres les UAL fonctionnent en parallèle. On parle alors d'architectures multi cœur. Cela permet d'augmenter la puissance de calcul. 



#### 3. L'unité de contrôle. 

C'est elle qui donne les ordres à toutes les autres parties de l'ordinateur.  

Elle est principalement composée de quatre registres :

\- CO : le compteur ordinal, qui contient l'adresse de la prochaine instruction à exécuter.  

\- RI : le registre d'instructions qui contient l'instruction en cours d’exécution.  

\- AC : l'accumulateur chargé de stocker des opérandes intermédiaires

\- CC : le code condition, utilisé pour les instructions de rupture conditionnelle (saut).  



​	Son algorithme de fonctionnement est le suivant :

​	Répéter indéfiniment

​	RI ← M[CO]

​	CO ← CO +1

​	R.OP(RI.AD)

​	Fin du répéter. 



Exercice 4: qu'effectue chaque ligne de cet algorithme ? 

#### 4. Et maintenant ?



​	Plus de soixante ans aprés son invention, le modèle de l'architecture de Von Neumann régit 	toujours l'architecture des ordinateurs. 

​	

Par rapport au schéma initial, nous pouvons noter les évolutions suivantes:

- les entrées-sorties, initialement commandées par l'unité centrale, sont depuis le début des années 1930 sous le contrôle de processeurs autonomes (canaux d'entrée-sortie et mécanismes 	assimilés). Associée à la multiprogrammation (partage de la 	mémoire entre plusieurs programmes), cette organisation a notamment permis le développement des systèmes en temps partagé.

- Les ordinateurs comportent maintenant des processeurs multiples qu'il s'agisse d'unités séparées ou de « coeurs » multiples à l'intérieur d'une même puce. Cette organisation permet d'atteindre une puissance globale de calcul élevée sans augmenter la vitesse des processeurs individuels, limitée par les capacités d'évacuation de la chaleur dans des circuits de plus en plus dense.  	

​	Ces deux évolutions ont pour conséquence de mettre la mémoire, plutôt que l'unité centrale, au centre de l'ordinateur, et d'augmenter le degré de parallélisme dans le traitement et la circulation de l'information. Mais, elles ne remettent pas en cause les principes de base que sont la séparation entre traitement et commande de la notion de programme enregistré. 



### III. Assembleur.  



​	Un ordinateur exécute des programmes qui sont des suites d'instruction. Le processeur est 	incapable d'exécuter directement des programmes écrits, par exemple, en Python. En effet, comme tous les autres constituants d'un ordinateur, le processeur gère uniquement 2 états (toujours symbolisés par un « 1 » et un « 0 »), les instructions exécutées au niveau du processeur sont donc codées en binaire. L'ensemble des instructions exécutables directement par le microprocesseur constitue ce qu'on appelle le « langage machine » ou assembleur. 

Le principe de base est le suivant : une instruction est stockée dans une cellule mémoire désignée par une adresse. Elle est constituée de deux parties : 

- un code opération  qui indique quelle opération doit être effectuée ;
- une adresse désignant l'opérande de cette opération (son argument).  

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

​	




