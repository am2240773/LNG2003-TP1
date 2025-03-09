import re


texte = open('IApourTP1.txt',encoding='utf8').read()
mots = re.split(r'[^\w|\.|-]+',texte)    


mot_ack = ["un", "au", "aux", "à", "en"]
mot_nack = ["l", "de", "le", "les"]
mot_interposé = ["université", "l"]


for (idx, mot) in enumerate (mots) :
    # Cible les mots en majuscule qui ne commence pas une phrase.
    if (len(mot) > 1 and mot[0].isupper() and mots[idx - 1][-1] != "." and mot[1].islower()) :
        if (mots[idx-1].lower() in mot_ack) :
            print(mots[idx-1:idx+1])
        elif (mots[idx-3:idx] == ["à", "l", "université"]) :
            print(mots[idx-3:idx+1])
        elif (mots[idx-3:idx] == ["de", "l", "université"]) :
            print(mots[idx-3:idx+1])
        elif (mots[idx-4:idx] == ["à", "l", "université", "d"]) :
            print(mots[idx-4:idx+1])



