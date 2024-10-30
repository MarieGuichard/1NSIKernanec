# Le protocole TCP/IP



Regardons un peu plus en détail ce qui se passe lors d'un envoi :



### I. Envoi simple

Nous allons voir le fonctionnement général d’une communication simple d’un ordinateur A vers un ordinateur B.

**Application A**

La couche application de l’ordinateur A veut envoyer des données vers la couche application de l’ordinateur B. L’application fourni donc des données à la couche transport de l’ordinateur A.

![](D:\DISQUE ESSB\lycee\NSI\reseau\reseau_5.jpg)

**Transport A**

La couche transport de l’ordinateur A reçoit les données et les encapsule en ajoutant des informations (port, application…) c’est le protocole TCP ou UDP.

![](D:\DISQUE ESSB\lycee\NSI\reseau\reseau_6.jpg)



La couche transport envoie l’ensemble à la couche internet.



**Internet A**

La couche internet encapsule les informations venant de la couche transport en ajoutant entre autre les adresses IP de l’ordinateur A et de l’ordinateur B. 

![](D:\DISQUE ESSB\lycee\NSI\reseau\reseau_7.jpg)

Tout ceci est envoyé à la couche accès réseau.



**Accès réseau A**



Dans le cas d’Ethernet la couche réseau va ajouter les adresses MAC des cartes réseaux pour que la connexion avec l’ordinateur B puisse se faire.

Une adresse MAC est codée sur 6 octets. on écrit traditionnellement les adresses MAC en hexadécimal, chaque octet étant séparés par 2 points (exemple d'adresse MAC : 00:E0:4C:68:02:11) 

L'adresse MAC est liée au matériel, chaque carte réseau (Ethernet ou Wifi) possède sa propre adresse MAC, il n'existe pas dans le monde, 2 cartes réseau (Ethernet ou Wifi) qui possèdent la même adresse MAC. Les 3 premiers octets d'une adresse MAC ("00:E0:4C" dans l'exemple ci-dessus) désignent le constructeur du matériel, par exemple, "00:E0:4C" désigne le constructeur "realtek semiconductor corp". 

Au moment de l'encapsulation d'un paquet IP, l'ordinateur "émetteur" va utiliser un protocole nommé ARP (Address Resolution Protocol) qui va permettre de déterminer l'adresse MAC de l'ordinateur "destination", en effectuant une requête "broadcast" (requête destinée à tous les ordinateurs du réseau) du type : "j'aimerais connaitre l'adresse MAC de l'ordinateur ayant pour IP XXX.XXX.XXX.XXX". Une fois qu'il a obtenu une réponse à cette requête ARP, l'ordinateur "émetteur" encapsule le paquet IP dans une trame Ethernet et envoie cette trame sur le réseau. 

![](D:\DISQUE ESSB\lycee\NSI\reseau\reseau_8.jpg)

Enfin cette trame Ethernet est envoyée à l’ordinateur B par la carte réseau.



**Accès réseau B**



La carte réseau reçoit la trame Ethernet, vérifie qu’elle est bien destinataire de la trame et la dés-encapsule :

![](D:\DISQUE ESSB\lycee\NSI\reseau\reseau_9.jpg)

Elle envoie le résultat à la couche Internet

**Internet B**

La couche internet vérifie l’adresse IP de destination, dés-encapsule et envoie le résultat à la couche transport :

![](D:\DISQUE ESSB\lycee\NSI\reseau\reseau_10.jpg)

**Transport B**

La couche transport vérifie que tout est correct puis les données sont envoyées à la bonne application :

![](D:\DISQUE ESSB\lycee\NSI\reseau\reseau_11.jpg)





Dans le cas de TCP, un accusé de réception est envoyé à l’ordinateur A. UDP n’envoie pas d’accusé de réception, il est moins fiable mais plus rapide.





**Application B**



L’application B reçoit les données.



### II. Propriétés particulières des couches.

**Fragmentation**

IP peut fragmenter les données qu’il reçoit de la couche transport si elles sont trop volumineuses pour rentrer dans une trame Ethernet par exemple. En effet la trame Ethernet accepte des données de 1500 octets au maximum, il est donc indispensable de découper les données pour les envoyer par paquets. Le récepteur enregistre les paquets et les assemble pour reconstituer les données initiales.

Les paquets peuvent ne pas arriver dans le bon ordre à cause du routage, ils sont donc numérotés. Ce phénomène est illustré sur la page suivante.

![](D:\DISQUE ESSB\lycee\NSI\reseau\reseau_12.jpg)



### III. Routage.

IP s’occupe également de savoir vers quel ordinateur envoyer un paquet en premier pour atteindre un ordinateur éloigné. Par exemple, pour joindre Marseille depuis Lille on pourra passer par Paris. C’est ce qu’on appelle le **routage**. Chaque routeur tient à jour une table de routage pour savoir en permanence le meilleur chemin pour atteindre une destination.

La commande pour connaître la route utilisé par un paquet est **traceroute**. Cette commande ne fonctionnera pas correctement sur vos postes à cause du proxy utilisé par le lycée.



Nous pouvons donc observer que le fonctionnement d'un réseau utilise un modèle de couche. 

En particulier, nous avons observer le modèle des couches TCP/IP. 

En effet, à chaque phase d'encapsulation on associe ce que l'on appelle une couche : 

- ​	comme nous l'avons vu les protocoles HTTP, FTP, SMTP, DNS,... sont associés à la couche "Application"  
- ​	les protocoles TCP et UDP sont associés à la couche "Transport"  
- ​	le protocole IP est associé à la couche "Internet"  
- ​	les trames Ethernet (ou Wifi) sont associées à la couche "Accès réseau"  

On présente souvent ces différentes couches sur ce type de schéma : 

 ![](D:\DISQUE ESSB\lycee\NSI\reseau\couche_1.jpg)

La couche du "dessous" encapsule la couche située "au dessus" 

On nomme ce système de couche "modèle de couches TCP/IP" (car ce modèle repose principalement sur TCP et IP) 

#### **Le modèle des couches OSI**

Il existe un autre modèle de couche, le modèle OSI (Open Systems Interconnection), ce système est antérieur au modèle TCP/IP puisqu'il date des années 1970. Ce modèle est principalement théorique et à permis de poser les bases des communications réseau. Ce modèle est composé de 7 couches (alors que le modèle TCP/IP est composé de 4 couches). 

 ![](D:\DISQUE ESSB\lycee\NSI\reseau\couche_2.jpg)

Il existe des liens entre le modèle OSI et le modèle TCP/IP (par exemple on retrouve le protocole IP dans la couche 3 du modèle OSI et TCP dans la couche 4), mais parfois comparer les 2 modèles peut être délicat. 

















































































Ce modèle est donné ici à titre d'information (pour le cas où vous le rencontriez pendant vos recherches sur Internet), mais le principal est de retenir ce qui a été vu sur le modèle TCP/IP. 