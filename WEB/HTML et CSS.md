# HTML et CSS

Nous allons nous intéresser à un acteur fondamental du développement web, le couple HTML+CSS (Hyper Text Markup Langage et Cascading Style Sheets). 

### I. HTML. 

Dans un premier temps, nous allons exclusivement nous intéresser au HTML. Qu'est-ce que le HTML, voici la définition que nous en donne Wikipedia : 

*L’Hypertext Markup Language, généralement abrégé HTML, est le format de données conçu pour représenter les pages web. C’est un langage de balisage permettant d’écrire de l’hypertexte, d’où son nom. HTML permet également de structurer sémantiquement et de mettre en forme le contenu des pages, d’inclure des ressources multimédias, dont des images, des formulaires de saisie, et des programmes informatiques. Il permet de créer des documents interopérables avec des équipements très variés de manière conforme aux exigences de l’accessibilité du web. Il est souvent utilisé conjointement avec des langages de programmation (JavaScript) et des formats de présentation (feuilles de style en cascade).* 

Pour l'instant, nous allons retenir deux éléments de cette définition «conçu pour représenter les pages web» et «un langage de balisage». 

Grâce au HTML vous allez pouvoir, dans votre navigateur (Firefox, Chrome, Opera,....), afficher du texte, afficher des images, proposer des hyperliens (liens vers d'autres pages web), afficher des formulaires et même maintenant afficher des vidéos (grâce à la dernière version du HTML, l'HTML5). 

HTML n'est pas un langage de programmation (comme le Python par exemple), ici, pas question de conditions, de boucles....c'est un langage de description. 

Nous utiliserons Geany. 

#### 1. Balises. 

 

Exercice 1: 

```html
<!DOCTYPE html>
<html>
	<head>
		<title>Ma première page</title>
		<meta charset="utf-8">
		<link href="style.css" rel="stylesheet" />
	</head>

	<body>
		<h1>Ada Lovelace</h1>
		<p>	Ada Lovelace, de son nom complet Augusta Ada King, comtesse de Lovelace, née Ada Byron le 10 décembre 1815 à Londres et morte le 27 novembre 1852 à Marylebone. C'est une pionnière de <b> la science informatique </b>.
		</p>

		<h1> Activités</h1>
			<ul>
				<li>Mathématicienne</li>
				<li>inventrice</li>
				<li> écrivaine</li>
				<li>informaticienne</li>
				<li> programmeuse</li>
				<li> poétesse</li>
				<li> ingénieure</li>
				</ul>

		<div>
		À 17 ans, Ada rencontra le mathématicien et inventeur Charles Babbage lors d'une soirée mondaine. Elle était fascinée par sa machine à calculer destinée au calcul et à l'impression de tables mathématiques, appelée machine à différences. Il devint rapidement son mentor.

		En 1835, Ada épousa William King, qui devint le comte de Lovelace trois ans plus tard, faisant d'elle la comtesse de Lovelace. Ils eurent trois enfants. À l'époque, le rôle des épouses et mères de la haute société était tourné vers l'éducation des enfants et la tenue de leur foyer. Ada Lovelace, elle, continua de travailler avec Charles Babbage.

		En 1843, Babbage développa la machine analytique, une version plus complexe de la machine à différences. Il demanda à Lovelace de traduire le texte français de son ingénieur en anglais. Elle passa neuf mois, entre 1842 et 1843, sur cette traduction. Ada Lovelace traduisit non seulement les notes, mais ajouta les siennes, les signant « AAL ».

Ces notes sont le fruit d'un travail frénétique, en collaboration étroite avec Charles Babbage qui annote les brouillons. Elle ajouta à l'article original sept notes, labellisées de A à G, représentant près de trois fois le volume du texte d'origine. La note G s'appuie sur un algorithme très détaillé pour calculer les nombres de Bernoulli avec la machine à différences. Le programme qui en résulte est considéré comme le premier véritable programme informatique au monde, dans un langage véritablement destiné à être exécuté sur une machine. 

Certaines de ces notes comparent la conception de la machine analytique au fonctionnement des machines à tisser. Les machines à tisser suivent des modèles pour créer un dessin complet et pour Ada Lovelace, la machine analytique pouvait également suivre des modèles - ou des codes - non seulement pour faire des calculs, mais aussi pour former des lettres. C'est une explication très basique de la programmation informatique.

Charles Babbage ne reçut jamais assez de financement pour terminer sa machine analytique et les notes d'Ada Lovelace tombèrent dans l'oubli. Mais en 1953, ses notes ont été republiées dans un livre sur l'informatique numérique qui montrait comment les ordinateurs fonctionnent en suivant des modèles. Bien avant l'invention du premier ordinateur, Ada Lovelace avait eu l'idée d'un langage informatique.

Elle mourut le 10 novembre 1852, plus de cent ans avant que ses notes ne soient redécouvertes. Mais pour ses travaux visionnaires, elle est souvent considérée comme la première programmeuse informatique. 

En 1979, le département américain de la Défense a même nommé un nouveau langage informatique « Ada » en son honneur, que de nombreux développeurs connaissent aujourd'hui.
		</div>
				
		<p> Si vous voulez en savoir plus, n'hésitez pas à consulter le lien suivant: <a href="https://www.nationalgeographic.fr/histoire/portrait-ada-lovelace-premiere-programmeuse-de-lhistoire"> Ada Lovelace </a>
			
		
	</body>
</html>

```

Copier et coller le code ci-dessus dans Geany. Enregistrer le au format html, puis, dans l'explorateur de fichier, double cliquez sur le fichier, celui-ci doit s'ouvrir dans votre navigateur. 



Comme déjà évoqué ci-dessus, en HTML, tout est une histoire de **balise** que l'on ouvre et que l'on ferme. Une balise ouvrante est de la forme <nom_de_la_balise>, les balises fermantes sont de la forme </nom_de_la_balise>. 

En observant attentivement le code, vous devriez forcément remarquer que toute balise ouverte doit être refermée à un moment ou un autre. La balise ouvrante et la balise fermante peuvent être sur la même ligne ou pas, cela n'a aucune espèce d'importance, la seule question à se poser ici est : ai-je bien refermé toutes les balises que j'ai ouvertes ? 

Enfin pour terminer avec les généralités sur les balises, il est important de savoir qu'une structure du type : 

```<balise1>
<balise2>
</balise1>
</balise2>
```

est interdite, la balise2 a été ouverte après la balise1, elle devra donc être refermée avant la balise1. 

En revanche, l'enchaînement suivant est correct : 
```
<balise1>
<balise2>
</balise2>
</balise1>
```

Chaque balise a une signification qu'il faut bien respecter (on parle de la sémantique des balises). 

Par exemple le texte situé entre la balise ouvrante et fermante `<h1> </h1> `  est obligatoirement un titre important (il existe des balises `<h2>, <h3>` ......qui sont aussi des titres, mais des titres moins importants (sous-titre)).

 La balise ` <p>`  permet de définir des paragraphes, enfin, la balise ` <b>`  permet de mettre en évidence un élément important. 

Voici les principales :

```html
	<h1>, …., <h6> niveaux de titres et de sous-titres.   
    <p> paragraphe
	<b> texte en gras
	<i> texte en italique
    <div> permet de regrouper d'un coup un ensemble de titres et de paragraphes. 
	<ul> liste à puces
		<li> élement d'une liste
	<a href = « dest »> lien hypertexte ver la page d'adresse URL dest. 
	<img src = « photo.jpg »> image stockée à l'adresse URL photo.jpg.  Attention, cette balise ne se ferme pas !
```

Et pour en savoir plus, allez consulter le site: [html](https://www.ionos.fr/digitalguide/sites-internet/developpement-web/balises-htlm/)



Exercice 2: Modifier le code ci-dessus pour

1. ajouter un titre de niveau 3. 
2. Ajouter un lien. 
3. Ajouter deux images. 
4. Ajouter un paragraphe. 



#### 2. Attributs. 

Les éléments HTML ont des **attributs** ; ce sont des valeurs supplémentaires qui configurent les éléments ou ajustent leur comportement de différentes manières pour répondre aux critères souhaités par les utilisateurs.

Il est possible d'ajouter des éléments à une balise ouvrante, on parle d'attribut. Une balise peut contenir plusieurs attributs :

<ma_balise attribut_1= "valeur_1" attribut_2="valeur_2"> 

Il existe beaucoup d'attributs différents, nous allons nous contenter de 2 attributs: 

`class `: Cet attribut permet de définir la ou les classes auxquelles appartient un élément afin de le manipuler en script ou de le mettre en forme avec CSS.

`id`: Cet attribut permet d'identifier un élément d'un document de façon unique. Il est généralement utilisé pour manipuler l'élément avec des scripts ou pour le mettre en forme avec CSS.

Cela s'utilise de la manière suivante (attention, le code suivant ne modifiera en rien votre page mais aura un intérêt lorsque vous ajouterez le css). 

```html
<h1 class ="titre">Ada Lovelace</h1>
<p id="para_1">	Ada Lovelace, de son nom complet Augusta Ada King, comtesse de Lovelace, née Ada Byron le 10 décembre 1815 à Londres et morte le 27 novembre 1852 à Marylebone. C'est une pionnière de <b> la science informatique </b>.
</p>
```



## II. Le CSS. 

 

Le HTML n'a pas été conçu pour gérer la mise en page (c'est possible, mais c'est une mauvaise pratique). Le HTML s'occupe uniquement du contenu et de la sémantique, pour tout ce qui concerne la mise en page et l'aspect « décoratif » (on parle du « style » de la page), on utilisera le CSS (Cascading Style Sheets). 

Exercice 3:

```css
h1
{
        text-align: center;
        background-color: red;
}
p
{
        font-family: Verdana;        
        color: blue;
}
div{
	font-style: italic;
}
```

Copier et coller le code ci-dessus, enregistrer le à style.css dans le même dossier que la page web sur Ada Lovelace. 

Rechargez la page web. Que constatez vous ? (Si vous ne constatez rien, appelez votre enseignante !). 


Vous trouverez des propriétés utiles en css à l'adresse suivante: [css](https://www.cssdebutant.com/debuter-en-css-les-definitions-css/)

Exercice 4: Modifier le code ci-dessus:

1. Mettre le titre de niveau h3 en violet (ou toute autre couleur que vous trouverez à l'adresse suivante: [couleur](https://htmlcolorcodes.com/fr/) )
2. Mettre une image de fond. 
3. Redimensionnez vos images pour qu'elles aient une taille adaptée. 



Afin de personnaliser l'esthétique de chaque partie, il est possible d'utiliser les attributs `class`et `id`que nous avons vu précédemment de la manière suivante. 

```css
.titre
{ 
font-size = 54 px;
}

#para_1
{
        font-style: italic;
        color: green;
}

```

### III. Travail à rendre. 

Faire une page web concernant la vie et les découvertes d'une informaticienne célèbre. 

Vous utiliserez tout ce que nous avons vu dans ce cours. Ce travail sera noté. 

