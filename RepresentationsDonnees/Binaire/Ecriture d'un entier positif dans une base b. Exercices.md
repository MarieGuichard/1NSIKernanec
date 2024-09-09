## Ecriture d'un entier positif dans une base b.: Exercices. 

**Exercice 1:** Convertir en binaire les nombres suivants donnés en base 10.

a. $17_{10}$	b. $254_{10}$	c. $47_{10}$	d. $1024_{10}$	e. $1025_{10}$



**Exercice 2 : ** Convertir en décimal les nombres suivants donnés en binaire.

a. $1011_2$	b. $100000_2$	c. $111111_2$	d. $1011001_2$



**Exercice 3:** Convertir en hexadécimal les nombres suivants donnés en binaire.

a. $10001010_2$		b. $111001_2$	c. $111010010001_2$	d. $01011_2$

**Exercice 4:**  Convertir en binaire les nombres suivants écrits en hexadécimal.

a. $A320_{16}$		b. $FABE51_{16}$		c. $59A7_{16}$		d. $101010_{16}$

**Exercice 5 :** Écrire un algorithme permettant se saisir un nombre décimal et de le convertir en binaire.

**Exercice 7 :** Un nombre entier représente par plusieurs octets est stocké en mémoire ou dans un fichier suivant un ordre qui s'appelle « l'endianness ». Par exemple, le nombre qui s'écrit B35F en hexadécimal peut être stocké sous la forme B35F ou sous la forme 5FB3. 

Dans le premier cas, on parle d''orientation big endian ou dans le deuxième cas d’orientation little endian. Avec l'orientation big endian, 08 00 correspond à $8\times16^{2}=2048$ en décimal, alors qu'avec l'orientation little indian 0800 correspond à 8 en décimal. 

Écrire une fonction qui prend en paramètres 2 octets, représentés par deux entier compris entre 0 et 255, et une chaîne de caractères « BE » ou « LE » et renvoie la valeur décimale du nombre représenté suivant l'encodage big endian (pour « BE ») ou little endian (pour « LE »).