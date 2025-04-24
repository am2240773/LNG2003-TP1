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

