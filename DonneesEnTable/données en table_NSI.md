#  Manipulation de tables.

Une des utilisations principales de l'informatique de nos jours est le traitement de quantités
importantes de données dans des domaines très variés. : un site de commerce en ligne peut avoir à
gérer des bases de données pour des dizaines de milliers d'articles en vente, de clients, de
commandes , un hôpital doit pouvoir accéder efficacement à tous les détails de traitements de ses
patients.....
Il existe des logiciels de traitements de données , et l'étude des bases de données est une matière
importante en informatique. Cela est d'ailleurs au programme de terminale.
Pour cette année, nous allons apprendre les opérations de base sur les tables de données en utilisant
Python.

## I. Le format CSV.

Le format CSV (pour comma separated values, soit en français valeurs séparées par des virgules)
est un format très pratique pour représenter des données structurées.
Dans ce format, chaque ligne représente un enregistrement et sur, une même ligne, les différents
champs de l'enregistrement sont séparés par une virgule (d'où le nom). En pratique, on peut
spécifier le caractère utilisé pour séparer les différents champs et on utilisé fréquemment un pointvirgule,
une tabulation ou deux points pour cela.
De plus, la première ligne d'un tel fichier est en général utilisée pour indiquer le nom des différents
champs. Dans ce cas, le premier enregistrement apparaît en deuxième ligne du fichier.
Nous utiliserons dans ce chapitre le fichier musee_france_2025.csv se trouvant sur le git.
Les données sont issues du site https://data.gouv.fr et les données ont été légèrement modifiées.

Question 1 :

1. Ouvrir le document musee_france_2025 avec le bloc note.
2. Quel est le séparateur de champs utilisés ?
3. Lister le nom des différents champs.
4. Ouvrir le document musee_france_2025 avec le tableur d'openoffice (ou de libreoffice).
  Veillez à sélectionner convenablement de séparateur. Que constatez vous ?



Pour construire un fichier csv, il suffit de copier du texte en utilisant le bloc note et de le sauvegarder dans le format csv. 

Question 2:

1. Dans le bloc note, copier le texte suivant, sauvegardez le au format csv

```csv
Nom;Prenom;Age;Ville_destination;Region_destination;interet
Dupont;Lucien;25;Tours;37;Château
Fergus;Sophie;35;Marseille;13;Ecomusée
Henocque;Rabah;56;Libourne;33;Chapelle
Masquette;Juliette;27;Lille;59;Exposition
```

2. Ouvrir le fichier que vous avez enregistré en utilisant le tableur d'openoffice. Que constatez vous ? 

Il s'agit des clients d'une agence de voyage. Leur ville et leur destination de voyage est
indiquée et l'agence souhaite, en utilisant le document musees_france_2021 leur fournir une
liste de musée qui pourrait les intéresser et à proximité de leur lieu de vacances.
Nous allons apprendre comment répondre à cette question sans faire les choses à la main.

## II. Importation des données.

Nous allons utiliser la bibliothéque csv en python. 

## 1. Une première solution. 

```python
import csv
musee=[]
documents = open("musee_france_2025.csv",newline="")
lecture = csv.reader(documents,delimiter=",")
for ligne in lecture:
	musee.append(ligne)
documents.close()
```

Question 2 :
1. Copier et exécuter le code ci-dessus.
2. Afficher musee[0] et musee[1]
3. Quel le type de la variable musee ?
4. Que se passe-t-il pour les descriptions des champs ?
5. A quoi sert la fonction reader ?
6. Pourquoi cette méthode ne semble-t-elle pas pertinente ?

## 2. Une meilleure méthode. 

```python
import csv
musee=[]
documents = open("musee_france_2025.csv",newline="")
lecture = csv.DictReader(documents,delimiter=",")
for ligne in lecture:
	musee.append(dict(ligne))
documents.close()
```

Question 3 :
1. Copier et exécuter le code ci-dessus.
2. Afficher musee[0] et musee[1]
3. Quel le type de la variable musee ?
4. Que se passe-t-il pour les descriptions des champs ?
5. A quoi sert la fonction DictReader ?
6. Pourquoi cette méthode ne semble-t-elle pas pertinente ?

Bilan : Afin d'exploiter un fichier csv, il faut importer le module csv, ouvrir le document en veillant
à spécifier newline= » » et utiliser la fonction DictReader de manière à ce que chaque entrée soit
liée à un champ.

## III. Rechercher une donnée. 

En utilisant la construction d'une liste par compréhension avec une condition, il est possible,
d'obtenir des données précises.

Question 4 :
1. Prenons l'exemple de Juliette qui souhaite avoir le nom et la ville de tous les musées dans le département du 59.
   a. Entrer dans le script la ligne de code suivante.
   `musee_59=[(m['Nom_Musee'],m['Ville']) for m in musee if m['Departement']=='Nord']`
   b. A l'aide d'une boucle, afficher le contenu de la variable musee_59.
   c. Cela repond-il à la question ?
2. Déterminer la liste des noms et des numéros de téléphone des musées de la ville de
  Marseille.
3. a. Déterminer la liste des musées dans le département de l'Indre et Loire et dont le domaine thématique est l'archéologie. 
4. Déterminer la liste des écomusées dont le domaine thématique est l'archéologie. 

## IV. Tri. 

Pour exploiter des données, il peut être intéressant de les trier.
Toutefois, si nous reprenons notre exemple, cela ne veut pas dire grand chose de trier le
tableau musee. Il faut indiquer selon quels critères on veut effectuer ce tri. Pour cela, on
peut soit utiliser la fonction sorted soit la méthode sort avec l'argument supplémentaire qui
est une fonction renvoyant la valeur utilisée pour le tri.
Question 5 :
1. a. Entrer dans le script le code suivant.

   ```python
   def ville(l):
   	return l['Ville']
   musee.sort(key=ville)
   ```

   b. Afficher les trente premiers noms des musées ainsi que leurs villes de la table musee. 

2. Trier la table musee par ordre alphabétique des départements.  



## V. Fusion. 

Il est fréquent lorsqu'on travaille avec des données, et plus particulièrement des données en table, de se retrouver avec plusieurs jeux de données. Une des actions que l'on peut avoir à faire est de combiner les différentes tables pour n'en faire qu'une seule. Cela s'appelle la fusion des tables. 

Nous travaillerons, dans cette partie avec deux fichiers:

- le fichier fichier_client qui liste les numéros de référence des clients ainsi que leurs noms. 

![](F:\lycee\NSI\Les tables de données\donnees_table_1.jpg)

- le fichier fiches_com.csv qui liste les numéros de commande passées en leur associant la date ainsi que la référence du client qui a passé la commande. 

![](F:\lycee\NSI\Les tables de données\donnees_table_2.jpg)

L'objectif est de trouver une méthode permettant de fusionner ces deux tables afin que le numéro de la commande passée soit associé au client. 

Pour cela, nous allons utiliser une opération de jointure avec une clé commune qui sera le numéro de client. Il nous faudra également apprendre à écrire dans un fichier csv afin de créer une nouvelle table regroupant toutes ces informations. 

Question 7: 

1. Télécharger les fichiers fichier_client.csv, fiches_com.csv et jointure.py dans le même fichier. 

2. Ouvrir le fichier jointure.py et exécuter la ligne de commande

   ```python
   jointures("fiches_client.csv","fiches_com.csv","n_client")
   ```

   Qu'effectue cette ligne de commande? 

3. Commenter la fonction `jointures`. 

4. Exécuter les lignes de commandes suivantes:

   ```python
   nvtab=jointures("fiches_client.csv","fiches_com.csv","n_client")
   vers_csv(nvtab,"clients_commandes")
   ```

5. Ouvrir le ficher dans lequel vous avez téléchargé les documents précédents. Que constatez vous? 

6. Commenter la fonction `vers_csv`. 



