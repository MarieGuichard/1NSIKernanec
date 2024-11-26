def melange(mot,car):
    reponse =""
    for i in range(len(mot)):
        reponse = reponse + mot[i]+car
    return reponse

def inverse(mot):
    reponse=""
    for i in range(len(mot)):
        #reponse =  reponse+mot[len(mot)-1-i]
        reponse = mot[i]+reponse
        #print(reponse)
    return reponse

def palindrome(mot):
    nvmot=inverse(mot)
    if nvmot==mot:
        return True
    else:
        return False
    