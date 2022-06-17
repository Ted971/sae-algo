def del_char(chaine, i):
    ''' Supprime le charactère d'indice i dans une chaine de charactère
        Entrée :
            chaine, type str : la chaine de charcatère traitée
            i, type int : l'indice du charactère à supprimer
        Sortie :
            type,str : renvoie la chaine de charactère sans le charactère à l'indice i
    '''
    # La nouvelle chaine est composée de la partie avant et celle apres le charactère d'indice i
    #on utilise la methode join, plus rapide que la concatenation
    return "".join([chaine[:i] ,  chaine[i+1:]])

def nb_espace(chaine,i):
    '''Compte le nombre d'espace a partir de l'indice i (compris) avec un  indice décroissant
        Entrée :
            chaine, type str : la chaine de charcatère traitée
            i, type int : l'indice a partir duquel on compte les espaces
        Sortie :
            compte, int : nombre d'espaces a partir de l'indice i
    '''
    #On pose un cas pour i = 0 ce qui permet de traiter les cas ou il y a un espaces au debut texte
    if i == 0 :
        return 1

    compte = 0
    while chaine[i] == " ":
        compte += 1
        i -= 1

    return compte

def erase(chaine):
    ''' Permet d'enlever les espaces isolés d'une chaine de charactères
        Entrée : 
            chaine, type str : la chaine de charcatère traitée
        Sortie :
            chaine, type str : renvoie la chaine de départ sans les espaces isolés
    '''
    # on part de la fin pour arriver au debut de la chaine
    i = len(chaine)-1

    while i >= 0 : #on utilise une boucle while et non une boucle for pour pourvoir changer d'indice plus librement, ceci permet de sauter plusiseurs indices si nécessaire
        if chaine[i] == " ":
            # lorsque l'on a un espace, on compte le nombre d'espace qui s'enchaine pour pouvoir traiter un indice qui ne correspond pas à un espace, ce qui reduit le nombre de comparaisons
            espaces = nb_espace(chaine ,i)
            if espaces == 1 : # si il n'y a qu'un espace, on le supprime et passe au charcatère se situant 2 indices apres, car on sait deja que le charactère d'apres n'est pas un espace
                chaine,i = del_char(chaine, i), i-1
             
            else :
                i -= espaces

        else : #si pas d'espace, on passe directement a l'indice d'après
            i-=1
    return chaine

