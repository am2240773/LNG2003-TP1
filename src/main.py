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
    res_regex = re.findall(r'([A-Z][\w|\s]*) : (.*)[.|,]', ph)
    
    for hit in res_regex:
        if len(hit) > 0 :
            print(str(hit[0]) + " : " + str(hit[1]))

# PATRON à faire
# qui vise à                                    3
# parfois appelé | qui sera appelé              4 7
# Maj word word (ALLCAPS)                       5 49 51
# comporte                                      8
# du nom d' / du nom de                         9 11
# Name Name, word word,                         10
# << >> (name)                                  12
# Maj , ./,                                     16 17 18
# ne sont qu'                                   30
# il s'agit de                                  31 32 52
# Maj est ...                                   48
