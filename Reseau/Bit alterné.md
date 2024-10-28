# Bit alterné

Nous avons vu que le protocole TCP propose un mécanisme d'accusé de réception afin de s'assurer qu'un paquet est bien arrivé à destination. On parle plus généralement de processus d'acquittement. Ces processus d'acquittement permettent de détecter les pertes de paquets au sein d'un réseau, l'idée étant qu'en cas de perte, l'émetteur du paquet renvoie le paquet perdu au destinataire. Nous allons ici étudier un protocole simple de récupération de perte de paquet : le protocole de bit alterné. 

Le protocole du bit alterné est implémenté au niveau de la couche accès réseau. Il permet de détecter des pertes de paquets comme le fait TCP au niveau transport.

Lorsque A envoie une trame à B, il ajoute un drapeau qui vaut soit 0 soit 1. Lorsque B reçoit une trame de A il renvoie un accusé de réception avec le complément du drapeau pour indiquer qu’il a bien reçu la trame. Ainsi lorsque A reçoit l’accusé de réception il peut envoyer la trame suivante en changeant la valeur du drapeau :

![](D:\DISQUE ESSB\lycee\NSI\reseau\bit_alterné_1.jpg)



Maintenant regardons les cas où un dysfonctionnement se produit. Le dysfonctionnement pourra être détecté par l’ordinateur A lorsqu’il ne reçoit pas un accusé de réception. Comme il attend cet accusé de réception il doit définir un temps au-delà duquel il considère la trame perdue. Il la renverra alors. On dit qu’il y a un « timeout ». Un timeout peut se produire lorsqu’une trame est perdue :

![](D:\DISQUE ESSB\lycee\NSI\reseau\bit_alterné_2.jpg)



Cela peut aussi arriver sur l’accusé de réception est perdu :

![](D:\DISQUE ESSB\lycee\NSI\reseau\bit_alterné_3.jpg)

Dans ce cas l’ordinateur B reçoit deux trames avec le même drapeau. Il en déduit donc que son 1er accusé de réception s’est perdu et ignorera la trame reçue. Il enverra tout de même un nouvel accusé de réception pour que l’ordinateur A puisse continuer.



Le protocole du bit alterné n’est pas parfait, c’est pourquoi il est remplacé actuellement pas des protocoles plus complexes.



Existe-t-il  une situation où le bit alterné est inefficace ? 