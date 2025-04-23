class occurence_classe:
  def __init__(self, defini_len, definition_depart, definition_len):
    self.defini_len = defini_len
    self.definition_depart = definition_depart
    self.definition_len = definition_len

dict_occurence = []

import re
T = open('TALpourTP2.txt',encoding='utf8')
texte = T.read()

# 1. Pré-traitrement pour éviter couper les abréviations
texte = re.sub(r'\(abr. ([A-Z]+)\)', '(abr_ \\1)', texte)

# 2. Divisier le texte en phrase
phrase = re.findall(r'([A-Z].+?[^.].\.[ \n]|\n\n)', texte, re.S)

# 3. Post-traitement pour restaurer les abréviations
for ph in phrase:
    ph = re.sub('abr_', 'abr.', ph[0])

# 4. Sortir les éléments définis et définitoires à l'aide de regex

# Sortir les mots suivants le patron 1
for ph in phrase:
    #res_regex = re.findall(r'([A-Z]+?[\sA-Z]*?), ([\w ]*)', ph, re.S)
    res_regex = re.findall(r'(\b[A-Z]+[\sA-Z]+), ([\w ]*)', ph, re.S)
    print(res_regex)
    

# 5. Impression des résultats sur la console avec contexte
#for r in re.finditer(r'.{,75} est un .{,75}',texte,re.S):



#### Liste des patrons ####

#https://regex101.com/r/vltxNk/1
#du nom de doit précéder patron 1

# PATRON 1 : ... NOM_DEFINI, definition sur plusieurs mots jusqu'à frontière

