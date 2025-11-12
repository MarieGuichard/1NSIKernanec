# Client-serveur. 



Introduction : Visionner la vidéo suivante : https://www.youtube.com/watch?v=CIhalbnBgA4



Nous venons de voir globalement  le fonctionnement en client/serveur du web avec l’envoi de requêtes au serveur par le client. Nous allons maintenant approfondir les choses.

### I . Client

Un client est un ordinateur qui envoie une requête à un serveur. Cela peut être un utilisateur par l’intermédiaire d’un navigateur ou un programme (bot) qui envoie une requête. Nous nous intéressons ici  au protocole **http** et au protocole **https.**

### II. Requête. 

Quand vous saisissez une URL dans un navigateur, il convertit cette URL en une requête et l’envoie vers le bon serveur.

Par exemple cette URL https://www.debian.org/intro/about sera transformée en cette requête :

```
GET /intro/about HTTP/1.0

Host : www.debian.org

Accept : text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

User-Agent : Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0

```



Détaillons cette requête :

\- la première ligne contient la commande (ici GET), l’URL et le protocole ;

Les lignes suivantes sont les entêtes (headers) qui contiennent différentes informations.

\- Host : précise le site web concerné par la requête ;

\- Accept : indique ce que le navigateur accepte comme type de contenu ;

\- User-Agent : donne des informations sur le client.



Il existe beaucoup d’autres entêtes.

**Exercice 1:** Allez sur la page ci-dessus avec Firefox et notez les autres entêtes (seulement les noms) de la requête avec le moniteur réseau (ctrl + shift + E).

Nous avons vu la commande GET qui est la plus utilisée car elle demande simplement la ressource.

 Il existe également une commande POST pour envoyer des données au serveur. Elle est notamment utilisée lors de l'utilisation de formulaires. 

La commande HEAD permet de ne demander que les entêtes pour faire des tests par exemple.

### III. Serveur. 

Un serveur est aussi un ordinateur.

Il n’est pas nécessairement puissant : votre téléphone peut être un serveur, un ordinateur de plus de dix ans, un Raspberry Pi. L’ordinateur que vous utilisez actuellement est un serveur (nous l’utiliserons plus tard).

Il existe des ordinateurs spécialement conçus pour être des serveurs avec beaucoup (beaucoup) de mémoire et beaucoup de processeurs. Ces serveurs sont en général situés dans des datacenters, des bâtiments spéciaux climatisés avec une très bonne connexion internet :

![](/WEB/IMG/image_serveur.jpg)



Vous pouvez regarder une vidéo sur un datacenter d’OVH : https://www.youtube.com/watch?v=Sfw0yoy6lIQ et une autre sur Google : https://www.youtube.com/watch?v=XZmGGAbHqa0

Les serveurs dans les datacenters peuvent être loués à des particuliers ou des entreprises.



**Exercice 2:** Allez sur le site d’OVH (leader européen situé à Roubaix) et relevez les caractéristiques (nombre de cœurs, RAM et disques) du plus cher serveur : https://www.ovh.com/fr/serveurs_dedies/tarifs/

Comment faire pour qu’un ordinateur devienne un serveur web ? Il suffit d’y installer un logiciel qui répond aux requêtes http ! Il existe des dizaines de tels logiciels, les plus répandus sont les logiciels libres **Apache** et **Nginx**.

### IV.  Réponse. 

Une fois que le serveur a reçu une requête il renvoie une réponse. Si on continue avec la même requête, voici un extrait de la réponse :

```
HTTP/1.1 200 OK

Date: Tue, 10 Dec 2019 22:29:58 GMT

Server: Apache

Content-Location: about.fr.html

…

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

<html lang="fr">

<head>
```

…

Détaillons cette réponse :
- la première ligne contient le protocole (HTTP/1.1) et le code de réponse (200 OK)
Les lignes suivantes sont encore des entêtes (headers) qui contiennent différentes informations.
- Date : la date et l’heure de la réponse ;
- Server : le type de serveur ;

Et beaucoup d’autres entêtes.

Enfin après une ligne vierge, il y a la ressource demandée : ici la page HTML.

**Exercice 3:**  

1. Allez sur les sites de Debian et de l’ENT et notez les serveurs utilisés en regardant les entêtes dans Firefox.
2. Trouvez le serveur utilisé par Google et chercher son nom complet.
3.  Cherchez la signification des codes de réponse suivants :

- 200
- 404
- 410
- 403
- 500

### V. le protocole https.



Le "HTTPS" est la version "sécurisée" du protocole HTTP. Par "sécurisé" en entend que les données sont chiffrées avant d'être transmises sur le réseau. 

Voici les différentes étapes d'une communication client - serveur utilisant le protocole HTTPS : 

- le client demande au serveur une connexion sécurisée (en utilisant "https" à la place de "http" dans la barre d'adresse du navigateur web)  
- le serveur répond au client qu'il est OK pour l'établissement d'une connexion sécurisée. Afin de prouver au client qu'il est bien celui qu'il prétend être, le serveur fournit au client un certificat prouvant son "identité". En effet, il existe des attaques dites "man in the middle", où un serveur "pirate" essaye de se faire passer, par exemple, pour le serveur d'une banque : le client, pensant être en communication avec le serveur de sa banque, va saisir son identifiant et son mot de passe, identifiant et mot de passe qui seront récupérés par le serveur pirate. Afin d'éviter ce genre d'attaque, des organismes délivrent donc des certificats prouvant l'identité des sites qui proposent des connexions "https".  
- à partir de ce moment-là, les échanges entre le client et le serveur seront chiffrés grâce à un système de clé de chiffrement (nous aborderons cette notion de clé de chiffrement l'année prochaine, en terminale). Même si un pirate arrivait à intercepter les données circulant entre le client et le serveur, ces dernières ne lui seraient d'aucune utilité, car totalement incompréhensible à cause du chiffrement (seuls le client et le serveur sont aptes à déchiffrer ces données)  

D'un point vu strictement pratique il est nécessaire de bien vérifier que le protocole est bien utilisé (l'adresse commence par "https") avant de transmettre des données sensibles (coordonnées bancaires...). Si ce n'est pas le cas, passez votre chemin, car toute personne qui interceptera les paquets de données sera en mesure de lire vos données sensibles. 

```

```


