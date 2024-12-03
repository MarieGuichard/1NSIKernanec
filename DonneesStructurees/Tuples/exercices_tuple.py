def combien(liste, element):
    rep = 0
    for i in range(len(liste)):
        if element == liste[i]:
            rep = rep +1
    return rep        

def produit(nombres,n):
    rep = ()
    for i in range(len(nombres)):
        rep = rep + (nombres[i]*n,)
    return rep 

def tri_pair_impair(nombres):
    nb_pair=()
    nb_impair=()
    for i in range(len(nombres)):
        if nombres[i]%2==0:
            nb_pair = nb_pair + (nombres[i],)
        else:
            nb_impair=nb_impair+(nombres[i],)
    return (nb_pair,nb_impair)

def melange(tuple1,tuple2):
    pass
