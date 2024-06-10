# Introduction à Python

Nous allons apprendre à programmer dans le langage Python. Vous avez, normalement, déjà rencontré ce langage, que cela soit en SNT, en mathématiques ou en physique. 

Python est l'un des multiples langages de programmation existant. 



### I. Qu'est ce qu'un langage de programmation ? 

Un langage de programmation est une notation conventionnelle destinée à formuler des algorithmes et produire des programmes informatiques qui les appliquent. D'une manière similaire à une langue naturelle, un langage de programmation est composé d'un alphabet, d'un vocabulaire, de règles de grammaire et de signification. 

​	Les langages de programmation permettent de décrire d'une part les structures des données qui seront manipulées par l'appareil informatique, et d'autre part d'indiquer comment sont effectuées les manipulations, selon quels algorithmes. Ils servent de moyens de communication par lesquels le programmeur communique avec l'ordinateur, mais aussi avec d'autres programmeurs ; les programmes étant d'ordinaire écrits, lus, compris et modifiés par une équipe de programmeurs.  

​	Un langage de programmation est mis en œuvre par un traducteur automatique : compilateur ou interpréteur.  Un compilateur est un programme informatique qui transforme dans un premier temps un code source écrit dans un langage de programmation donné en un code cible qui pourra être directement exécuté par un ordinateur, à savoir un programme en langage machine ou encode intermédiaire, tandis que l’interprète réalise cette traduction « à la volée ».

### II. Quelles sont les particularités de Python ? 

Python est un langage de programmation, multi-paradigme et multiplateforme. Il favorise la favorise la programmation impérative, fonctionnelle et orientée objet. Il est doté d'un typage dynamique fort, d'une gestion automatique de la mémoire et d'un systéme de gestion d'exceptions. 

Le langage Python est placé sous une licence libre et fonctionne sur la plupart des plates-formes informatiques, des smartphones aux ordinateurs, de Windows à Unix avec notamment GNU/Linux en passant par macOs, ou encore Android. Il est conçu pour optimiser la productivité des programmeurs en offrant des outils de haut niveau et une syntaxe simple à utiliser. 

Il est également apprécié par certains pédagogues qui y trouvent un langage où la syntaxe, clairement séparée des mécanismes de bas niveau, permet une initiation aisée aux concepts de base de la programmation. 



Sources : https://fr.wikipedia.org/wiki/Langage_de_programmation

​	   https://fr.wikipedia.org/wiki/Python_(langage)



Question 1 :

a. Résumer en deux lignes ce qu'est un langage de programmation. 





b. Pourquoi Python est-il un langage intéressant à étudier au lycée ?











#### III. Environnement de travail. 



Nous utiliserons Thonny.  

Thonny est un environnement de développement intégré pour Python conçu pour les débutants. Il prend en charge différentes façons de parcourir le code. 



Allez ouvrir Thonny. 

![](/Python/IMG/thonny.jpg)

Vous avez, normalement, cette fenêtre qui apparaitra devant vous. 

Si cela n'est pas le cas, allez dans le menu View, décocher tout ce qui est coché, sauf le Shell (et éventuellement cocher le Shell), et si cela n'est toujours pas le cas, appelez (gentiment) votre enseignante. 

Nous ne parlerons pas de la fenêtre de droite mais uniquement des deux fenêtres horizontales sur la gauche. 

##### a. Le shell. 

La fenêtre du bas est ce qu'on appelle le shell ou la console (in french dans le texte). 

Les instructions entrées dans cette zone sont exécutées immédiatement. 

Question 2: Dans le Shell, tapez les instructions suivantes, appuyer sur entrée entre chacune 	et indiquez le résultat :

a. `3+2`

b. `3*4`

c. `print("coucou")`



#### b. Zone de script. 

La fenêtre du haut permet d'entrer un programme et de le sauvegarder. Il faut ensuite l'exécuter dans le Shell. 

Question 3: 

a. Copier le programme suivant dans la zone de script. 

```python
for i in range(5):
    print("j'ai ", i ,"euros sur mon compte")
```

b. Sauvegarder ce programme (en cliquant sur la petite disquette ou en faisant ctrl + S). 

Vous veillerez à ranger votre travail de manière ordonnée. Cela vous permettra de le retrouver plus aisément. 

c. Exécuter ce programme (en cliquant sur la flèche verte ou en appuyant sur F5). Que se passe-t-il? 

Il est également possible d'écrire des fonctions et de les exécuter. 

Question 4: 

a. Copier la fonction suivante dans la zone de script (en ouvrant une nouvelle page). 

```python
def message(nombre):
    for i in range(nombre):
        print("La vie trouve toujours son chemin.")
```

b. Sauvegarder ce programme. 

c. Exécuter ce programme. Que se passe-t-il? 

d. Dans le Shell, ecrire l'instruction `message(5)`puis appuyer sur entrée. Que se passe-t-il? 

e. Quelle instruction devez vous ecrire dans le shell pour que la phrase "La vie trouve toujours son chemin" soit affichée 10 fois. 

f. De quel film célébre est issue cette phrase? 

