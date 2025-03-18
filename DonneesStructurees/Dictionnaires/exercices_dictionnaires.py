# magasin_A={"Pomme":10,"Poire":15,"Fraise":3,"Banane":7,"Cerise":10}
# magasin_B={"Pomme":3,"Poire":15,"Fraise":10,"Banane":15,"Cerise":4}
# 
# 
# def leplus(mag_A,mag_B):
#     magasin={}
#     #cle=mag_A.keys() # recupere toutes les clés du dictionnaire mag_A
#     for elt in cle: # boucle sur les clés du dictionnaire mag_A
#         if mag_A[elt]>mag_B[elt]:
#             magasin[elt]="mag_A"
#         elif mag_A[elt]< mag_B[elt]:
#             magasin[elt]="mag_B"
#         else:
#             magasin[elt]="mag_A et mag_B"
#     return magasin
# 
# 
# print(leplus(magasin_A,magasin_B))
# 
eleve={"Nom":"Dupont","Prenom":"Jules","Age":17,"Classe":"1G4"}
stagiaire={"Nom":"Dupont","Prenom":"Jules","Fonction":"Developpeur","Salaire":2500}

def fusion(dic1,dic2):
    reponse=dic1
    return reponse

print(fusion(eleve,stagiaire))
