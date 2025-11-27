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
    pair = ()
    impair = ()
    for i in range(len(nombres)):
        if nombres[i]%2 == 0:
            pair = pair + (nombres[i],)
        else:
            impair = impair + (nombres[i],)
    return pair,impair

def melange(tuple1,tuple2):
    pass
