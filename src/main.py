import re


texte = open('IApourTP1.txt',encoding='utf8').read()
mots = re.split(r'[^\w|\.|-]+',texte)    


sequence_ack = [["un"],
                ["au"],
                ["aux"],
                ["à"],
                ["en"],
                ["à", "l", "université"],
                ["de", "l", "université"],
                ["à", "l", "université", "d"],
                ["de", "l", "université", "d"],
                ["En"],
                ["du", "musée", "de"]]

for (idx, mot) in enumerate (mots) :
    if (len(mot) > 1 and mot[0].isupper() and mots[idx - 1][-1] != "." and mot[1].islower()) :
        for (seq_idx, mot_ack) in enumerate (sequence_ack) :
            if (mots[idx-len(mot_ack):idx] == mot_ack) :
                if (mots[idx+1] == "College") :
                    print(mots[idx-len(mot_ack):idx+2])
                elif (mots[idx+1] == "de" and mots[idx+2][0].isupper()) :
                    print(mots[idx-len(mot_ack):idx+3])
                else :
                    print(mots[idx-len(mot_ack):idx+1])
