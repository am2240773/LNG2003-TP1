import re

texte = open('IApourTP1.txt',encoding='utf8').read()

mot_ack = ["un", "au", "aux", "à", "en"]
mot_nack = ["l", "de", "le", "les"]

mot_interposé = ["université"]

mots = re.split(r'[^\w\.]+',texte)    

print(mots)

#for (idx, mot) in enumerate (mots) :

