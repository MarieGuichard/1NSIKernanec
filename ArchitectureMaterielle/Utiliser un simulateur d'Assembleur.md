# Utiliser un simulateur d'Assembleur. 

Afin de mettre en pratique ce que nous avons étudié dans le cours "Modèle d'architecture de von Neumann", nous allons utiliser un simulateur développé par Peter L Higginson. Ce simulateur est basé sur une architecture de von Neumann. Nous allons trouver dans ce simulateur :

- une RAM
- un CPU

Une version en ligne de ce simulateur est disponible ici : http://www.peterhigginson.co.uk/AQA/

Voici ce que vous devriez obtenir en vous rendant à l'adresse indiquée ci-dessus :

![](/ArchitectureMaterielle/IMG/simulateur_assembleur.jpg)

Il est relativement facile de distinguer les différentes parties du simulateur :

- à droite, on trouve la mémoire vive ("main memory")
- au centre, on trouve le microprocesseur
- à gauche on trouve la zone d'édition ("Assembly Language"), c'est dans cette zone que nous allons saisir nos programmes en assembleur

**Exercice 1:**

```assembly
MOV R0,#42
STR R0,150
HALT
```

1. En utilisant les instructions vues dans le cours sur l'architecture Von Neumann (Attention, les instructions ne sont pas tout à fait identiques, mais elles ressemblent), indiquer ce que fait ce programme. 
2. Copier ce code dans la zone d'assembleur, puis appuyer sur le bouton submit. Que constatez vous ? A votre avis, à quoi cela correpond-il ? 
3. Appuyer maintenant sur le bouton RUN. Que constatez vous ? Cela correspond-il à la réponse que vous avez fourni à la question 1? 
4. Modifiez le programme afin qu'à la fin de l'exécution, on trouve le nombre 54 à l'adresse mémoire 50 et le nombre 32 à l'adresse mémoire 60. 

**Exercice 2:**

```assembly
  MOV R0, #4
   STR R0,30
   MOV R0, #8
   STR R0,75
   LDR R0,30
   CMP R0, #10
   BNE else
   MOV R0, #9
   STR R0,75
   B endif
else:
   LDR R0,30
   ADD R0, R0, #1
   STR R0,30
endif:
   MOV R0, #6
   STR R0,23
   HALT
	
```

1. Copiez le code ci-dessus et exécutez le. 
2. En observant attentivement ce qui se passe (n'hésitez pas à utiliser le mode STEP), traduire le code en pseudo-code. 

**Exercice 3:**

Voici un programme python. 

```python
x=0
while x<3:
	x = x+1
```

Traduire le programme ci-dessus en assembleur et testez le avec le simulateur. 

