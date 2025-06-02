import doctest

def tri_insertions(tab):
    '''renvoie un tableau de nombres entiers trié
    tab => tableau d'entiers.
    >>> tri_insertions([6,5,4,8,2,1])
    [1, 2, 4, 5, 6, 8]
    >>> tri_insertions([0,5,4,8,2,1])
    [0, 1, 2, 4, 5, 8]
    '''
    j=1
    while j<=len(tab)-1:
        i=j-1
        k=tab[j]
        while i>=0 and tab[i]>k:
            tab[i+1]=tab[i]
            i = i-1
        tab[i+1] = k
        j += 1
    return tab

def tri_selection(tab):
    '''renvoie un tableau de nombres entiers trié
    tab => tableau d'entiers.
    >>> tri_selection([6,5,4,8,2,1])
    [1, 2, 4, 5, 6, 8]
    >>> tri_selection([0,5,4,8,2,1])
    [0, 1, 2, 4, 5, 8]
    '''
    i=0
    while i< len(tab)-1:
        j = i+1
        mini = i
        while j<len(tab):
            if tab[j]<tab[mini]:
                mini =j
            j = j+1
        if mini != i:
            a = tab[i]
            tab[i]=tab[mini]
            tab[mini]= a
        i=i+1
    return tab

    

if __name__=="__main__":
    doctest.testmod(verbose=True)
