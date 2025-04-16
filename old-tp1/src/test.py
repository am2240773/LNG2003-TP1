import re

texte = open('IApourTP1.txt',encoding='utf8').read()
mots = re.split(r'[^\w|-|\.]+',texte)

prep_avant = ["en", "au", "aux", "à"]

# Regarder si l'un des trois mots précédent est dans la préposition

for (idx, mot) in enumerate (mots) :
    if (len(mot) > 0 and mot[0].isupper()) :
        #print (mots[idx-1][-1])
        if ((mots[idx-1].lower() in prep_avant  and mots[idx-1][-1] != "." ) 
            or (mots[idx-2].lower() in prep_avant and mots[idx-1][-1] != "." )
            or (mots[idx-3].lower() in prep_avant and mots[idx-1][-1] != ".")) :
            if (not mot.isupper()) :
                print(mots[idx-1:idx+3])
            else :
                for letter in mot :
                    if not (letter in "IVXLCDM") :
                        print(mots[idx-3:idx+3])
                        break

# Inclure "de" + Nom + Nom
