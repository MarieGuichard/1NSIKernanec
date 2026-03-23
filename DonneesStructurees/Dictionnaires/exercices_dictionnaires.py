magasin_A={"Pomme":10,"Poire":15,"Fraise":3,"Banane":7,"Cerise":10}
magasin_B={"Pomme":3,"Poire":15,"Fraise":10,"Banane":15,"Cerise":4}

def legrandmagasin(mag_A,mag_B):
    grand_mag = {}
    for cle_A in mag_A.keys():
        if mag_A[cle_A]<mag_B[cle_A]:
            grand_mag[cle_A] = "Magasin_B"
        elif mag_A[cle_A]>mag_B[cle_A]:
            grand_mag[cle_A] = "Magasin_A"
        else:
            grand_mag[cle_A] =("Magasin_A", "Magasin_B")
    return grand_mag

eleve={"Nom":"Dupont","Prenom":"Jules","Age":17,"Classe":"1G4"}
stagiaire={"Nom":"Dupont","Prenom":"Jules","Fonction":"Developpeur","Salaire":2500}           
        
def fusion(dico1,dico2):
    reponse = dico1
    for cle in dico2.keys():
        if cle not in reponse.keys():
            reponse[cle] = dico2[cle]
    return reponse

def occurences(texte):
    resultat = {}
    for i in range(len(texte)):
        if ord(texte[i])>=65 and ord(texte[i])<=90:
            if texte[i] in resultat.keys():
                resultat[texte[i]] = resultat[texte[i]]+1 # resultat[texte[i]]+=1
            else:
                resultat[texte[i]] = 1
    return resultat

