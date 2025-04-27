import re
T = open('TALpourTP2.txt',encoding='utf8')
texte = T.read()

# Pré-traitement : découpe du texte en phrase
texte = re.sub(r'\(abr. ([A-Z]+)\)', '(abr_ \\1)', texte)
phrase = re.findall(r'([A-Z].+?[^.].\.[ \n]|\n\n)', texte, re.S)
for ph in phrase:
    ph = re.sub('abr_', 'abr.', ph[0])


# PATRON A : DEFINITION (abr. DEFINI)
for ph in phrase:
    res_regex = re.findall(r'(\b\w+\s\b\w+\s\b\w+\s\b\w+\s\b\w+\s)\(abr. ([A-Z]*)\)', ph)

    for hit in res_regex:
        if len(hit) > 0 :
            print(str(hit[1]) + " : " + str(hit[0]))


# PATRON B : DEFINI est DEFINITION
for ph in phrase:
    res_regex = re.findall(r'\(?([\w]*)\)? est un (.*) qui', ph)
    
    for hit in res_regex:
        if len(hit) > 0 :
            print(str(hit[0]) + " est un " + str(hit[1]))

# PATRON C : DEFINI : definition ,/.
for ph in phrase:
    res_regex = re.findall(r'^([A-Z][\w|\s]*) : (.*)[.|,]', ph)
    
    for hit in res_regex:
        if len(hit) > 0 :
            print(str(hit[0]) + " : " + str(hit[1]))

# PATRON D : Il s'agi... de DEFINITION
for ph in phrase:
    res_regex = re.findall(r'^Il s.agi(\w*) de (.*)[\.|,]', ph)
    
    for hit in res_regex:
        if len(hit) > 0 :
            print("Il s\'agi" + str(hit[0]) +  " de " + str(hit[1]))

# PATRON E : Defintion sur plusieurs mots (DEFINI)
for ph in phrase:
    res_regex = re.findall(r'([A-Z]\w*\s(\w*\s)*)\(([A-Z0-9]*)\)', ph)
    
    for hit in res_regex:
        if len(hit) > 0 :
            print(str(hit[2]) + " : " + str(hit[0]))
