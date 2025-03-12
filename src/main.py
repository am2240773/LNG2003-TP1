import re

texte = open('IApourTP1.txt',encoding='utf8').read()
mots = re.split(r'[^\w|\.|-]+',texte)    

prep_avant = ["en", "au", "aux", "à"]

for (idx, mot) in enumerate (mots) :
    if (len(mot) > 0 and mot[0].isupper()) :
        if (mots[idx-1].lower() in prep_avant) :
            print(mots[idx-1:idx+1])

# Inclure "de" + Nom + Nom
