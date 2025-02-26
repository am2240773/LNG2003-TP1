import re

texte = open('IApourTP1.txt',encoding='utf8').read()

mots = re.split('\W+',texte)    
