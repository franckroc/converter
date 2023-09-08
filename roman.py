def romainArabe(rep):
    # fonction conversion romain arabe

    count = index = 0  #count totalise le resultat en chiffre arabe. index itère sur rep user
    #si rep contient plus d'une lettre: conversion longue
    if len(rep) > 1:
        while index < len(rep)-1:
            if dico1.get(rep[index]) >= dico1.get(rep[index+1]):
                count=count+(dico1.get(rep[index])+dico1.get(rep[index+1]))
            if dico1.get(rep[index]) < dico1.get(rep[index+1]):
                count=count+(dico1.get(rep[index+1])-dico1.get(rep[index]))
            index+=2
            if index == len(rep)-1:
                count=count+dico1.get(rep[index])
    #si une seule lettre: conversion directe. recherche dans dico1 la valeur
    else:
        count = dico1.get(rep[0])
    return count

def arabeRomain(rep):
    # fonction conversion arabe romain
    
    # si chiffre romain simple , recherche dans dico1 la lettre correspondante
    if rep in dico1.values():
        for key,valeur in dico1.items():
            if valeur == rep:
                table = valeur #le résultat table est renseigné

    # sinon chiffre romain complexe à décomposer
    else:
        fact = 1   #fact = degré puissance 0 1 2 3 ...
        index = 0  #index itère sur rep user
        tab = []  #liste de décomposition du chiffre arabe

        #part 1
        #création d'une liste tab de décomposition qté,valeur positionnelle
        # de type ['3','1000','5',100','5','10','6','1'] pour 3556
        while index < len(rep):
            tab.append(rep[index])
            tab.append(pow(10,len(rep)-fact))
            fact+=1
            index+=1
        
        #part 2
        #creation d'une liste tabL à partir de tab. conversion qté arabe en qté lettre romaine
        # de type ['MMM','CCCCC','XXXXX','IIIIII'] pour 3556
        tabL = []
        index = 1
        while index < len(tab):
            for key, valeur in dico1.items():
                if valeur == tab[index]:
                    tabL.append(key*int(tab[index-1]))
            index+=2
        a = 0   

        #part 3
        #modification de tabL pour respecter convention chiffre romain 3 fois max C X et I
        for i in tabL:     
            if len(i) > 3:
                if i[0] == "C":
                    #900 sécrit CM et pas CCCCCCCCC
                    if len(i) == 9:
                        tabL[a] = "CM"
                    #800 s'écrit DCCC ...
                    if len(i) == 8:
                        tabL[a] = "DCCC"
                    if len(i) == 7:
                        tabL[a] = "DCC"
                    if len(i) == 6:
                        tabL[a] = "DC"
                    if len(i) == 5:
                        tabL[a] = "D"
                    if len(i) == 4:
                        tabL[a] = "CD"
                if i[0] == "X":
                    #90 s'écrit XC et pas XXXXXXXXX
                    if len(i) == 9:
                        tabL[a] = "XC"
                    if len(i) == 8:
                        tabL[a] = "LXXX"
                    if len(i) == 7:
                        tabL[a] = "LXX"
                    if len(i) == 6:
                        tabL[a] = "LX"
                    if len(i) == 5:
                        tabL[a] = "L"
                    if len(i) == 4:
                        tabL[a] = "XL"
                if i[0] == "I":
                    #9 s'écrit IX et pas IIIIIIIII
                    if len(i) == 9:
                        tabL[a] = "IX"
                    if len(i) == 8:
                        tabL[a] = "VIII"
                    if len(i) == 7:
                        tabL[a] = "VII"
                    if len(i) == 6:
                        tabL[a] = "VI"
                    if len(i) == 5:
                        tabL[a] = "V"
                    if len(i) == 4:
                        tabL[a] = "IV"
            a+=1
        #jointure tabL dans table - affiche resultat final table
        table = " ".join(tabL)
    return table


def convert(val):
    rep = str(val)
    if rep != " " and rep != "":
        if rep[0] in dico1.keys(): #si 1er char de rep est un chiffre romain dans dico1 ind=0...
            ret = romainArabe(rep)
            return ret
        else:
            ret = arabeRomain(rep)
            return ret


dico1 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

